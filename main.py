import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class MultiLayerAggregator(nn.Module):
    def __init__(self, num_layers=6, nhead=12):
        super().__init__()
        
        # Separate processing for each layer
        self.layer_aggregators = nn.ModuleList([
            nn.Sequential(
                nn.Conv2d(nhead, nhead // 2, kernel_size=1),
                nn.GELU(),
                nn.Conv2d(nhead // 2, 1, kernel_size=1)            
            )
            for _ in range(num_layers)
        ])
        
        # Learnable weights for combining layers
        self.layer_weights = nn.Parameter(torch.randn(num_layers) * 0.1)

        
    def forward(self, all_layer_scores):
        """
        Input: List of [Batch, nhead, N, N] tensors (one per layer)
        Output: [Batch, N, N]
        """
        layer_outputs = []
        
        # Process each layer separately
        for i, layer_scores in enumerate(all_layer_scores):
            # layer_scores: [Batch, 12, N, N]
            processed = self.layer_aggregators[i](layer_scores)  # [Batch, 1, N, N]
            layer_outputs.append(processed)
        
        # Stack: [Batch, num_layers, N, N]
        stacked = torch.cat(layer_outputs, dim=1)
        
        # using softmax here so that we can weight the importance of each layer
        weights = F.softmax(self.layer_weights, dim=0)  # [6]
        weights = weights.view(1, -1, 1, 1)  # [1, 6, 1, 1]
        
        # Weighted sum
        final = (stacked * weights).sum(dim=1)  # [Batch, N, N]
        
        return final

class SigmoidAttentionLayer(nn.Module):
    def __init__(self, d_model, nhead, dropout=0.25):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.head_dim = d_model // nhead
        
        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)
        self.out_proj = nn.Linear(d_model, d_model)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.linear1 = nn.Linear(d_model, d_model * 4)
        self.linear2 = nn.Linear(d_model * 4, d_model)
        self.dropout = nn.Dropout(dropout)


    def forward(self, x):
        batch_size, n, _ = x.shape

        # PRE-LN: Normalize BEFORE attention
        normed = self.norm1(x)
        
        q = self.q_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)
        k = self.k_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)
        v = self.v_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)

        raw_scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # used Sigmoid instead of Softmax, because I didnt wanted sum = 1 for a row , Now every cell is 0.0 to 1.0 independently.
        attn_probs = torch.sigmoid(raw_scores)
        attn_output = (attn_probs @ v) / (n ** 0.5) # Soft scaling factor
                
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, n, self.d_model)
        x = x + self.dropout(self.out_proj(attn_output))
        
        normed = self.norm2(x)
        ff = self.linear2(self.dropout(F.gelu(self.linear1(normed))))
        x = x + self.dropout(ff)

        return x, attn_probs

class Scout(nn.Module):
    def __init__(self, d_model, nhead, num_layers,input_dim=768):
        super().__init__()
        self.input_proj = nn.Linear(input_dim, d_model) 
        self.layers = nn.ModuleList([
            SigmoidAttentionLayer(d_model, nhead) for _ in range(num_layers)
        ])
        
        self.aggregator = MultiLayerAggregator(num_layers, nhead)

    def forward(self, sentence_embeddings):
        x = self.input_proj(sentence_embeddings)
        all_raw_scores = []
        B, N, _ = x.shape
        
        # Create diagonal mask once
        diag_mask = torch.eye(N, dtype=torch.bool, device=x.device).unsqueeze(0)
        
        for layer in self.layers:
            x, raw_score_matrix = layer(x)
            # Zero out diagonal before aggregation
            raw_score_matrix = raw_score_matrix.masked_fill(
                diag_mask.unsqueeze(1), 0.0
            )
            all_raw_scores.append(raw_score_matrix)

        output = self.aggregator(all_raw_scores)
        return output