import torch
import torch.nn as nn
import torch.optim as optim
from sentence_transformers import SentenceTransformer
import torch.nn.functional as F


from train.training_data import training_data
from main import Scout


def analyze_multiscale_aggregator(model):
    """Analyze which layers and heads the MultiScaleAggregator trusts"""
    
    print("\n" + "="*60)
    print("MULTI-SCALE AGGREGATOR ANALYSIS")
    print("="*60)
    
    # ============================================
    # PART 1: Layer-Level Importance
    # ============================================
    print("\n--- LAYER-LEVEL WEIGHTS ---")
    
    # Get raw weights
    raw_weights = model.aggregator.layer_weights.data  # [6]
    
    # Convert to probabilities (softmax)
    layer_probs = F.softmax(raw_weights, dim=0)
    
    print(f"\nRaw Weights: {raw_weights.numpy()}")
    print(f"Probabilities (after softmax): {layer_probs.numpy()}\n")
    
    for i in range(len(layer_probs)):
        bar = "█" * int(layer_probs[i].item() * 50)  # Visual bar
        print(f"Layer {i}: {layer_probs[i].item():.4f} {bar}")
    
    # ============================================
    # PART 2: Head-Level Importance (Per Layer)
    # ============================================
    print("\n" + "="*60)
    print("HEAD-LEVEL IMPORTANCE (Within Each Layer)")
    print("="*60)
    
    for layer_idx in range(len(model.aggregator.layer_aggregators)):
        print(f"\n--- Layer {layer_idx} ---")
        
        # Get this layer's aggregator network
        layer_agg = model.aggregator.layer_aggregators[layer_idx]
        
        # Extract the first conv layer (12 → 6)
        first_conv = layer_agg[0]  # Conv2d(12, 6, kernel_size=1)
        
        # Get weights: [out_channels=6, in_channels=12, 1, 1]
        weights = first_conv.weight.data  # [6, 12, 1, 1]
        
        # Average across output channels to get per-head importance
        head_importance = weights.abs().mean(dim=0).squeeze()  # [12]
        
        # Sort heads by importance
        sorted_indices = torch.argsort(head_importance, descending=True)
        
        print(f"Top 3 heads in Layer {layer_idx}:")
        for i in range(3):
            head_idx = sorted_indices[i].item()
            importance = head_importance[head_idx].item()
            bar = "█" * int(importance * 20)
            print(f"  Head {head_idx}: {importance:.4f} {bar}")
    
    # ============================================
    # PART 3: Overall Top Heads (Combining Both)
    # ============================================
    print("\n" + "="*60)
    print("OVERALL TOP 10 HEADS (Layer Weight × Head Weight)")
    print("="*60)
    
    all_heads = []
    
    for layer_idx in range(len(model.aggregator.layer_aggregators)):
        layer_weight = layer_probs[layer_idx].item()
        layer_agg = model.aggregator.layer_aggregators[layer_idx]
        first_conv = layer_agg[0]
        weights = first_conv.weight.data
        head_importance = weights.abs().mean(dim=0).squeeze()
        
        for head_idx in range(len(head_importance)):
            # Combined score = layer importance × head importance
            combined_score = layer_weight * head_importance[head_idx].item()
            all_heads.append((layer_idx, head_idx, combined_score))
    
    # Sort by combined score
    all_heads.sort(key=lambda x: x[2], reverse=True)
    
    print("\nTop 10 Most Important Heads:")
    for rank, (layer_idx, head_idx, score) in enumerate(all_heads[:10], 1):
        print(f"Rank {rank:2d}: Layer {layer_idx}, Head {head_idx:2d} | Score: {score:.4f}")
    
    print("\n" + "="*60)


def train_full_dataset():
    sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    model = Scout(d_model=768, nhead=12, num_layers=6)
    model.train()
    
    optimizer = optim.AdamW(model.parameters(), lr=1e-4) 

    criterion = nn.MSELoss()
    processed_batches = []
    
    for batch in training_data:
        emb = sbert.encode(batch['sentences'], convert_to_tensor=True).clone()
        emb = emb.unsqueeze(0) # [1, N, 768]
        tgt = torch.tensor(batch['target']).float().unsqueeze(0) # [1, N, N]
        processed_batches.append((emb, tgt))

    epoch = 0
    while True:
        epoch += 1
        total_loss = 0
        
        for embeddings, target in processed_batches:
            # shuffling data set so that model doesnt learn positional patterns even after removing PE
            N = embeddings.shape[1] # 14 sentences
            
            # 1. Generate random permutation (e.g., [5, 0, 13, 2...])
            idx = torch.randperm(N)
            
            # 2. Shuffle Embeddings (Reorder the sequence dim)
            shuffled_emb = embeddings[:, idx, :] 
            
            # 3. Shuffle Target (Must reorder BOTH rows and columns to match)
            # Reorder Rows (dim 1)
            shuffled_tgt = target[:, idx, :]
            # Reorder Cols (dim 2)
            shuffled_tgt = shuffled_tgt[:, :, idx]
            
            # 4. Train on SHUFFLED data
            optimizer.zero_grad()
            output_matrix = model(shuffled_emb)

            loss = criterion(output_matrix, shuffled_tgt)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()
        
        avg_loss = total_loss / len(processed_batches)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:03d} | Avg Loss: {avg_loss:.6f}")
        
        # Exit condition
        # if avg_loss < 0.0005:
        #     print(f"\nSUCCESS: Reached target loss at Epoch {epoch}!")
        #     break
            
        if epoch >= 300:
            print("Stopped at 2000.")
            break

    print("\n--- FINAL ROBUSTNESS TEST ---")
    model.eval() 
    analyze_multiscale_aggregator(model)

    
    # We take the first batch and shuffle it ONE LAST TIME to prove it works
    emb, tgt = processed_batches[0]
    idx = torch.randperm(14)
    
    test_emb = emb[:, idx, :]
    test_tgt = tgt[:, idx, :][:, :, idx]
    
    print(f"Random Shuffle Order: {idx.tolist()}")
    
    with torch.no_grad():
        preds = model(test_emb)
        
    
    print("\nTarget (First 5x5 of Shuffled Matrix):")
    print((test_tgt[0, :5, :5] > 0.5).numpy())
    
    print("\nPrediction (Rounded):")
    print(preds[0, :5, :5].round().numpy())
    
    # Check if they match
    accuracy = (preds.round() == (test_tgt > 0.5)).float().mean()
    print(f"\nMatrix Accuracy: {accuracy.item() * 100:.2f}%")

if __name__ == "__main__":
    import numpy as np
    train_full_dataset()