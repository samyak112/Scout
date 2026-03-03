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

        print(len(all_embeddings))
        
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

def loss_fn(pred_logits, target, threshold=0.2, gamma=2.0, beta=2.0, alpha=0.5, lambda_pairwise=1.5, margin_scale=1.0, epsilon=1e-6):
    B, N, _ = pred_logits.shape
    
    # User's diagonal mask
    mask = ~torch.eye(N, dtype=torch.bool, device=pred_logits.device).unsqueeze(0)
    pred = torch.sigmoid(pred_logits)
    
    # ---------------------------------------------------------
    # PART 1: POINTWISE SCORING (Absolute constraints)
    # ---------------------------------------------------------
    pred_m = pred[mask]
    target_m = target[mask]
    error = torch.abs(pred_m - target_m)

    # Extreme target emphasis & MSE stabilization
    weight = 1.0 + torch.log1p(target_m + epsilon) * beta
    scale  = 1.0 + (error / threshold) ** gamma
    extreme_loss = (error ** 3) * weight * scale
    mse_loss = (pred_m - target_m) ** 2

    # Confidence damping (The Lexical Trap killer)
    low_target_penalty = torch.clamp(pred_m - target_m, min=0.0) ** 2
    low_target_penalty = low_target_penalty * torch.exp(-target_m * 5.0) 

    pointwise_loss = alpha * mse_loss.mean() + (1.0 - alpha) * extreme_loss.mean() + low_target_penalty.mean()

    # ---------------------------------------------------------
    # PART 2: PAIRWISE RANKING FOR [B, N, N] MATRICES
    # ---------------------------------------------------------
    # pred shape is [Batch, Query, Candidate]
    # We want to compare Candidate_i vs Candidate_j FOR THE SAME Query.
    
    # Expand the candidate dimension so they cross over each other
    p_i = pred.unsqueeze(-1)  # Shape: [B, N, N, 1] -> (Batch, Query, Candidate_i, 1)
    p_j = pred.unsqueeze(-2)  # Shape: [B, N, 1, N] -> (Batch, Query, 1, Candidate_j)
    
    t_i = target.unsqueeze(-1)
    t_j = target.unsqueeze(-2)

    # DYNAMIC MASK: Only activate if ground truth says Candidate i > Candidate j.
    # If they are equal (Symmetric Patterns), this is 0. 
    # Also naturally ignores self-comparisons (diagonal) since t_i > t_i is False.
    valid_pairs = (t_i > t_j).float()

    # DYNAMIC MARGIN: Required gap based on your ground truth labels
    target_gap = t_i - t_j
    dynamic_margin = target_gap * margin_scale

    # PAIRWISE PENALTY: max(0, margin - (prediction_gap))
    pairwise_errors = torch.relu(dynamic_margin - (p_i - p_j))

    # Average the penalty only over the valid, logically asymmetric pairs
    ranking_loss = (pairwise_errors * valid_pairs).sum() / (valid_pairs.sum() + epsilon)

    # ---------------------------------------------------------
    # PART 3: COMBINED LOSS
    # ---------------------------------------------------------
    total_loss = pointwise_loss + (lambda_pairwise * ranking_loss)

    return total_loss

def create_balanced_batches(samples, batch_size=9, stride=None):
    """
    Create batches where each batch contains batch_size types.
    Batches overlap smoothly across types to avoid abrupt differences.
    
    Args:
        samples: list of (emb, target, metadata) tuples
        batch_size: number of types per batch
        stride: number of types to move between batches; if None, defaults to half of batch_size

    Returns:
        List of batches (each batch is a list of samples)
    """
    from collections import defaultdict
    import random

    # --- Group samples by information type ---
    grouped = defaultdict(list)
    for sample in samples:
        info_type = sample[2]['information_type_description']
        grouped[info_type].append(sample)

    # Shuffle each type's samples independently
    for group in grouped.values():
        random.shuffle(group)

    type_names = sorted(grouped.keys())
    num_types = len(type_names)
    if stride is None:
        stride = max(1, batch_size // 2)  # default overlap = 50%

    # Track which sample index to pick next for each type
    indices = {t: 0 for t in type_names}

    batches = []
    start_idx = 0

    while True:
        batch = []

        # Select batch_size types in sequence, wrap around
        selected_types = [type_names[(start_idx + i) % num_types] for i in range(batch_size)]

        # Pick one sample from each selected type if available
        for t in selected_types:
            if indices[t] < len(grouped[t]):
                batch.append(grouped[t][indices[t]])
                indices[t] += 1

        if len(batch) == 0:
            break  # no samples left

        batches.append(batch)

        # Move start index by stride for next batch
        start_idx = (start_idx + stride) % num_types

        # If all indices have reached end, stop
        if all(indices[t] >= len(grouped[t]) for t in type_names):
            break

    return batches

def train_full_dataset():

    d_model = 384
    nhead = 8
    num_layers = 3

    model = Scout(d_model=d_model, nhead=nhead, num_layers=num_layers)
    model = model.to(device) 
    model.train()
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-4,weight_decay=0.05)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=5
    )

    processed_samples = load_and_encode_dataset("train_utils/dataset.jsonl",device=device,sbert_batch_size=128)
    random.shuffle(processed_samples)
    split_idx = int(len(processed_samples) * 0.8)
    
    train_samples = processed_samples[:split_idx]
    val_samples = processed_samples[split_idx:]
    
    print(f"Dataset Split: {len(train_samples)} Train | {len(val_samples)} Validation")

    epoch = 0
    best_val_loss = float('inf')
    patience = 20
    patience_counter = 0
    min_delta = 1e-6 

    while True:
        epoch += 1
        
        model.train()
        train_batches = create_balanced_batches(train_samples)
        random.shuffle(train_batches)
        
        total_train_loss = 0.0
        
        for batch in train_batches:
                optimizer.zero_grad()
                                
                for emb, tgt, meta in batch:
                    embeddings = emb.unsqueeze(0)
                    target = tgt.unsqueeze(0)
                    
                    N = embeddings.shape[1]
                    idx = torch.randperm(N, device=device)
                    shuffled_emb = embeddings[:, idx, :]
                    shuffled_tgt = target[:, idx][:, :, idx]
                    
                    logits = model(shuffled_emb)

                    logits = torch.clamp(logits, min=-10, max=10)
                    
                    # Calculate Loss
                    loss = loss_fn(logits, shuffled_tgt)

                    loss = loss / len(batch)
                    
                    loss.backward()
                    
                    # Track the raw loss value (float only, no graph)
                    total_train_loss += (loss.item() * len(batch))

                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()
                
        avg_train_loss = total_train_loss / len(train_samples)

        # --- VALIDATION LOOP (The "Holdout") ---
        model.eval()
        total_val_loss = 0.0
        
        with torch.no_grad():
            for emb, tgt, meta in val_samples:
                embeddings = emb.unsqueeze(0)
                target = tgt.unsqueeze(0)
                
                logits = model(embeddings)
                logits = torch.clamp(logits, min=-10, max=10) 
                loss = loss_fn(logits, target)

                total_val_loss += loss.item()
        
        avg_val_loss = total_val_loss / len(val_samples)
        scheduler.step(avg_val_loss)
        current_lr = optimizer.param_groups[0]['lr']

        # --- LOGGING & SAVING ---
        if epoch % 1 == 0: #
            print(f"Epoch {epoch:03d} | Train Loss: {avg_train_loss:.6f} | Val Loss: {avg_val_loss:.6f} | LR: {current_lr:.2e}")

        # Check Early Stopping against VALIDATION loss
        if avg_val_loss < best_val_loss - min_delta:
            best_val_loss = avg_val_loss
            patience_counter = 0
            
            checkpoint = {
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': avg_val_loss,
                'config': {'d_model': d_model, 'nhead': nhead, 'num_layers': num_layers}
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


def test_overfit_single_batch():
    d_model = 384
    nhead = 8
    num_layers = 3

    model = Scout(d_model=d_model, nhead=nhead, num_layers=num_layers)
    model = model.to(device) 
    model.train()
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.05)  # higher LR

    processed_samples = load_and_encode_dataset("train_utils/dataset.jsonl", device=device, sbert_batch_size=128)
    
    # Just take one single batch
    single_batch = create_balanced_batches(processed_samples)[0]

    print(single_batch)
    # print(single_batch)
    print(f"Overfitting on {len(single_batch)} samples")

    for epoch in range(1, 501):
        model.train()
        optimizer.zero_grad()
        total_train_loss = 0.0

        for emb, tgt, meta in single_batch:
            embeddings = emb.unsqueeze(0)
            target = tgt.unsqueeze(0)
            
            logits = model(embeddings)
            logits = torch.clamp(logits, min=-10, max=10)
            
            loss = loss_fn(logits, target)
            loss = loss / len(single_batch)
            loss.backward()

            # Add this right after loss.backward() in your overfit test
            # for name, param in model.named_parameters():
            #     if param.grad is not None:
            #         print(f"{name}: grad_norm={param.grad.norm():.6f}")
            #     else:
            #         print(f"{name}: NO GRADIENT")
            # break  # only check first iteration
            
            total_train_loss += (loss.item() * len(single_batch))

        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        
        avg_train_loss = total_train_loss / len(single_batch)

        if epoch % 50 == 0:
            print(f"Epoch {epoch:03d} | Loss: {avg_train_loss:.6f}")

        if avg_train_loss < 1e-4:
            print(f"✓ Overfit at epoch {epoch}")
            return

    print("✗ Failed to overfit")

if __name__ == "__main__":
    import numpy as np
    # test_overfit_single_batch()
    train_full_dataset()
