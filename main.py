import torch
import torch.nn as nn
import torch.nn.functional as F
import math


class DynamicElementAggregator(nn.Module):
    def __init__(self, d_model, num_layers=6, nhead=12):
        super().__init__()
        self.total_heads = num_layers * nhead
        
        # The Micro-Router
        self.router = nn.Sequential(
            nn.Linear(d_model, d_model // 2),
            nn.GELU(),
            nn.Linear(d_model // 2, self.total_heads)
        )
        
        # Logit Bias: Allows the network to safely center its unbounded predictions
        self.bias = nn.Parameter(torch.zeros(1))

    def forward(self, x, all_layer_scores):
        # 1. Generate UNBOUNDED dynamic weights 
        # By removing Softmax, the network can output true Logits (-inf to +inf)
        raw_weights = self.router(x) 
        
        # 2. Stack all attention maps into one tensor
        stacked_scores = torch.cat(all_layer_scores, dim=1) 
        
        # 3. The Routing Math (Einstein Summation)
        # raw_weights can now be negative or >1, allowing the router to actively 
        # subtract bad attention heads or massively amplify good ones.
        final_matrix = torch.einsum('b n h, b h n m -> b n m', raw_weights, stacked_scores)
        
        # Add bias for stable logit zero-centering
        return final_matrix + self.bias

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
        # DYNAMIC NORMALIZATION:
        # Since Sigmoid rows don't sum to 1 (unlike Softmax), a raw (attn_probs @ v) 
        # is a weighted SUM that fluctuates based on how many 'hits' the Sigmoid finds.
        # By dividing by the actual row_sum, we convert this into a weighted AVERAGE.
        # This preserves the semantic 'energy' of the signal and ensures the output 
        # scale remains constant regardless of the number of candidates (N).
        row_sums = attn_probs.sum(dim=-1, keepdim=True) + 1e-6
        attn_output = (attn_probs @ v) / row_sums
                
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
        
        self.aggregator = DynamicElementAggregator(d_model, num_layers, nhead)

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

        output = self.aggregator(x, all_raw_scores)
        return output