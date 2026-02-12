import torch
import torch.nn as nn
import torch.optim as optim
from sentence_transformers import SentenceTransformer
import torch.nn.functional as F
import random
import json
from main import Scout
import os
os.makedirs('checkpoints', exist_ok=True)
from collections import defaultdict

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")
if device.type == 'cuda':
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")


def load_and_encode_dataset(
    jsonl_path,
    device,
    sbert_batch_size=64
):
    sbert = SentenceTransformer(
        "sentence-transformers/all-mpnet-base-v2",
        device=device
    )

    # -------- read samples --------
    samples = []
    with open(jsonl_path, "r") as f:
        for line in f:
            samples.append(json.loads(line))

    # -------- flatten sentences --------
    all_sentences = []
    sentence_counts = []

    for obj in samples:
        sents = obj["sentences"]
        all_sentences.extend(sents)
        sentence_counts.append(len(sents))

    # -------- batch encode --------
    cache_path = "train_utils/embeddings_cache.pt"
    
    if os.path.exists(cache_path):
        print(f"Loading cached embeddings from {cache_path}...")
        all_embeddings = torch.load(cache_path, map_location=device)
    else:
        print("Computing embeddings (this happens once)...")
        with torch.no_grad():
            all_embeddings = sbert.encode(
                all_sentences,
                convert_to_tensor=True,
                batch_size=sbert_batch_size,
                device=device,
                show_progress_bar=True
            )
        
        # Save to cache for next time
        print(f"Saving embeddings to {cache_path}...")
        torch.save(all_embeddings, cache_path)

    # -------- rebuild per-sample tensors --------
    processed_samples = []
    offset = 0

    for obj, n in zip(samples, sentence_counts):
        emb = all_embeddings[offset:offset + n]   # [N, 768]
        tgt = torch.tensor(
            obj["target"],
            device=device,
            dtype=torch.float32
        )  # [N, N]

        # Keep metadata for grouping
        metadata = {
            'information_type_description': obj['information_type_description'],
            'domain_name': obj['domain_name']
        }

        processed_samples.append((emb,tgt, metadata))
        offset += n

    return processed_samples

def masked_weighted_mse_loss(pred, target, nonzero_weight=10.0):
    B, N, _ = pred.shape
    mask = ~torch.eye(N, dtype=torch.bool, device=pred.device).unsqueeze(0)
    pred_m = pred[mask]
    target_m = target[mask]
    weights = torch.where(
        target_m > 0.05,
        torch.full_like(target_m, nonzero_weight),
        torch.ones_like(target_m)
    )
    return (weights * (pred_m - target_m) ** 2).mean()

def create_balanced_batches(samples):
    """
    Create batches where each batch contains ONE sample from EACH available type.
    When types run out, create smaller batches with remaining types.
    
    Returns batches that can be shuffled each epoch.
    """
    # Group by information_type_description
    grouped = defaultdict(list)
    
    for sample in samples:
        info_type = sample[2]['information_type_description']
        grouped[info_type].append(sample)
    
    # Shuffle each group independently (initial shuffle)
    for group in grouped.values():
        random.shuffle(group)

    type_names = sorted(grouped.keys())
    
    # Create balanced batches with variable sizes
    batches = []
    indices = {t: 0 for t in type_names}
    
    while True:
        batch = []
        
        # Try to get one sample from each type
        for type_name in type_names:
            if indices[type_name] < len(grouped[type_name]):
                batch.append(grouped[type_name][indices[type_name]])
                indices[type_name] += 1
        
        # If we got no samples, we're done
        if len(batch) == 0:
            break
        
        batches.append(batch)
    
    # Don't shuffle here - will shuffle in training loop
    return batches

def train_full_dataset():
    sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    sbert = sbert.to(device)

    model = Scout(d_model=768, nhead=12, num_layers=6)
    model = model.to(device) 
    model.train()
    
    optimizer = optim.AdamW(model.parameters(), lr=3e-5)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=2
    )

    criterion = nn.MSELoss()

    processed_samples = load_and_encode_dataset("train_utils/dataset.jsonl",device=device,sbert_batch_size=128)
    random.shuffle(processed_samples)
    split_idx = int(len(processed_samples) * 0.8)
    
    train_samples = processed_samples[:split_idx]
    val_samples = processed_samples[split_idx:]
    
    print(f"Dataset Split: {len(train_samples)} Train | {len(val_samples)} Validation")

    epoch = 0
    best_val_loss = float('inf')
    patience = 8 
    patience_counter = 0
    min_delta = 1e-6 
    while True:
        epoch += 1
        
        model.train()
        train_batches = create_balanced_batches(train_samples)
        random.shuffle(train_batches)
        
        total_train_loss = 0.0
        
        for batch in train_batches:
                # 1. Zero gradients BEFORE the batch starts
                optimizer.zero_grad()
                                
                # Process each sample in the batch
                for emb, tgt, meta in batch:
                    # ... (your existing shuffling logic is fine) ...
                    # Add batch dimension
                    embeddings = emb.unsqueeze(0)
                    target = tgt.unsqueeze(0)
                    
                    N = embeddings.shape[1]
                    idx = torch.randperm(N, device=device)
                    shuffled_emb = embeddings[:, idx, :]
                    shuffled_tgt = target[:, idx][:, :, idx]
                    
                    # Forward pass
                    # (Remember to remove sigmoid inside model if using BCEWithLogitsLoss!)
                    logits = model(shuffled_emb) 
                    
                    # Calculate Loss
                    loss = masked_weighted_mse_loss(logits, shuffled_tgt)

                    
                    # CRITICAL FIX 1: Normalize loss by batch size
                    # Since we are summing gradients, we must divide by N 
                    # so the step size doesn't explode for larger batches.
                    loss = loss / len(batch)
                    
                    # CRITICAL FIX 2: Backward pass INSIDE the loop
                    # This calculates gradients and FREES THE GRAPH immediately.
                    loss.backward()
                    
                    # Track the raw loss value (float only, no graph)
                    total_train_loss += (loss.item() * len(batch))
                
                # 2. Step the optimizer ONCE after the whole batch is processed
                # The gradients have been accumulating in model.parameters().grad
                optimizer.step()
                
        avg_train_loss = total_train_loss / len(train_samples)

        # --- VALIDATION LOOP (The "Holdout") ---
        model.eval() # Disable dropout
        total_val_loss = 0.0
        
        with torch.no_grad(): # Disable gradient calculation (saves RAM/Speed)
            for emb, tgt, meta in val_samples:
                # No shuffling needed for validation
                embeddings = emb.unsqueeze(0)
                target = tgt.unsqueeze(0)
                
                logits = model(embeddings)
                loss = masked_weighted_mse_loss(logits, shuffled_tgt)

                total_val_loss += loss.item()
        
        avg_val_loss = total_val_loss / len(val_samples)
        scheduler.step(avg_val_loss)
        current_lr = optimizer.param_groups[0]['lr']

        # --- LOGGING & SAVING ---
        if epoch % 1 == 0: # Print every epoch
            print(f"Epoch {epoch:03d} | Train Loss: {avg_train_loss:.6f} | Val Loss: {avg_val_loss:.6f} | LR: {current_lr:.2e}")

        # Check Early Stopping against VALIDATION loss
        if avg_val_loss < best_val_loss - min_delta:
            best_val_loss = avg_val_loss
            patience_counter = 0
            
            # Save Best Model
            checkpoint = {
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': avg_val_loss,
                'config': {'d_model': 768, 'nhead': 12, 'num_layers': 6}
            }
            torch.save(checkpoint, 'checkpoints/scout_best.pt')
            print(f"  ★ Saved new best model (Val Loss: {avg_val_loss:.6f})")
        else:
            patience_counter += 1
            print(f"  No improvement ({patience_counter}/{patience})")

        if patience_counter >= patience:
            print(f"\n✓ Early stopping triggered at epoch {epoch}")
            break
        
        if epoch >= 1000:
            break

if __name__ == "__main__":
    import numpy as np
    train_full_dataset()