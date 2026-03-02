import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoTokenizer


# =========================
# Multi Layer Aggregator
# =========================
class MultiLayerAggregator(nn.Module):
    def __init__(self, num_layers=6, nhead=12):
        super().__init__()

        self.layer_aggregators = nn.ModuleList([
            nn.Sequential(
                nn.Conv2d(nhead, nhead // 2, kernel_size=1),
                nn.GELU(),
                nn.Conv2d(nhead // 2, 1, kernel_size=1)
            )
            for _ in range(num_layers)
        ])

        self.layer_weights = nn.Parameter(torch.randn(num_layers) * 0.1)

    def forward(self, all_layer_scores):
        layer_outputs = []

        for i, layer_scores in enumerate(all_layer_scores):
            processed = self.layer_aggregators[i](layer_scores)
            layer_outputs.append(processed)

        stacked = torch.cat(layer_outputs, dim=1)

        weights = F.softmax(self.layer_weights, dim=0)
        weights = weights.view(1, -1, 1, 1)

        final = (stacked * weights).sum(dim=1)
        return final


# =========================
# Sigmoid Attention Layer
# =========================
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

        # Pre-LN
        normed = self.norm1(x)

        q = self.q_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)
        k = self.k_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)
        v = self.v_proj(normed).view(batch_size, n, self.nhead, self.head_dim).transpose(1, 2)

        scaled_scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)

        attn_weights = torch.sigmoid(scaled_scores)

        row_sums = attn_weights.sum(dim=-1, keepdim=True) + 1e-6
        attn_output = (attn_weights @ v) / row_sums

        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, n, self.d_model)

        x = x + self.dropout(self.out_proj(attn_output))

        normed = self.norm2(x)
        ff = self.linear2(self.dropout(F.gelu(self.linear1(normed))))
        x = x + self.dropout(ff)

        return x, scaled_scores


# =========================
# Scout (unchanged logic)
# =========================
class Scout(nn.Module):
    def __init__(self, d_model, nhead, num_layers, input_dim=768):
        super().__init__()

        self.input_proj = nn.Linear(input_dim, d_model)

        self.layers = nn.ModuleList([
            SigmoidAttentionLayer(d_model, nhead)
            for _ in range(num_layers)
        ])

        self.aggregator = MultiLayerAggregator(num_layers, nhead)

    def forward(self, sentence_embeddings):
        x = self.input_proj(sentence_embeddings)
        all_raw_scores = []

        B, N, _ = x.shape
        diag_mask = torch.eye(N, dtype=torch.bool, device=x.device).unsqueeze(0)

        for layer in self.layers:
            x, raw_scores = layer(x)

            raw_scores = raw_scores.masked_fill(
                diag_mask.unsqueeze(1), 0.0
            )

            all_raw_scores.append(raw_scores)

        output = self.aggregator(all_raw_scores)
        return output


# =========================
# Full Model with SBERT
# =========================


class FullModel(nn.Module):
    def __init__(self, d_model, nhead, num_layers):
        super().__init__()

        self.tokenizer = AutoTokenizer.from_pretrained(
            "sentence-transformers/all-mpnet-base-v2"
        )

        self.encoder = AutoModel.from_pretrained(
            "sentence-transformers/all-mpnet-base-v2"
        )

        self.scout = Scout(
            d_model=d_model,
            nhead=nhead,
            num_layers=num_layers,
            input_dim=768
        )

        self._freeze_encoder()
        self._unfreeze_last_layers(n_last_layers=2)

    def _freeze_encoder(self):
        for param in self.encoder.parameters():
            param.requires_grad = False

    def _unfreeze_last_layers(self, n_last_layers=2):
        total_layers = len(self.encoder.encoder.layer)

        for i in range(total_layers - n_last_layers, total_layers):
            for param in self.encoder.encoder.layer[i].parameters():
                param.requires_grad = True

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output.last_hidden_state
        mask = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return (token_embeddings * mask).sum(1) / mask.sum(1).clamp(min=1e-9)

    def forward(self, batch_sentences):
        """
        batch_sentences: List[List[str]]
        """

        batch_embeddings = []

        for sentence_list in batch_sentences:
            encoded = self.tokenizer(
                sentence_list,
                padding=True,
                truncation=True,
                return_tensors="pt"
            )

            encoded = {k: v.to(next(self.parameters()).device) for k, v in encoded.items()}

            model_output = self.encoder(**encoded)
            embeddings = self.mean_pooling(model_output, encoded["attention_mask"])

            batch_embeddings.append(embeddings)

        embeddings = torch.stack(batch_embeddings, dim=0)
        return self.scout(embeddings)