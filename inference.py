"""
NSP Continuation Test — Scout vs SBERT vs Cross-Encoder
=========================================================
Tests whether Scout can distinguish genuine sentence continuations
from plausible impostors — sentences that sound like they could follow
but functionally don't.

This is the core capability NSP in BERT tried and failed to learn.

Candidate types:
  GENUINE    — actually continues the context, logically or causally
  IMPOSTOR   — plausible sounding, same topic, but doesn't follow
  UNRELATED  — clearly wrong domain

The hard part is IMPOSTOR. SBERT will score it high because it shares
vocabulary and topic. A model with real continuation understanding
should suppress it.
"""

import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, CrossEncoder
from main import Scout

import time
import torch
import numpy as np
from datasets import load_dataset
from sentence_transformers import SentenceTransformer, CrossEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Hardware: {device.type.upper()}")

# ==========================================
# 1. Load Models
# ==========================================
print("Loading Models...")
sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=device)
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", device=device)

def load_scout(checkpoint_path):
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    cfg = checkpoint.get("config", {'d_model': 384, 'nhead': 8, 'num_layers': 3})
    model = Scout(d_model=cfg["d_model"], nhead=cfg["nhead"], num_layers=cfg["num_layers"])
    model.load_state_dict(checkpoint["model_state_dict"], strict=False)
    model.to(device)
    model.eval()
    return model

scout_model = load_scout("checkpoints/scout_best.pt")


import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.cross_encoder import CrossEncoder

# Initialize devices and baseline models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=device)
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", device=device)

import time
import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.cross_encoder import CrossEncoder

# Initialize devices and baseline models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=device)
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", device=device)

def run_agentic_rag_test(scout_model):
    print("🤖 THE AGENTIC RAG TEST: EXECUTION TIME PROFILING")
    print("=" * 110)

    query = "My bread dough didn't rise at all after sitting for two hours."

    corpus = [
        "Bread dough usually needs to sit for at least two hours to properly rise.", # Semantic Echo / Trivia
        "If your bread dough doesn't rise after two hours, it will bake into a dense, hard brick.", # Implication (Not a cause)
        "The water you poured in was boiling and killed the active culture.", # ✅ THE CAUSE (Zero lexical overlap)
        "You should cover the bread dough with a damp towel while it is sitting and rising.", # Tangential Advice
        "Sometimes bread dough simply won't rise even if you let it sit for over two hours.", # Pure Echo
        "Flour contains gluten proteins that form a network to trap gas bubbles." # Unrelated Fact
    ]

    # Helper function to ensure GPU operations finish before timing
    def sync():
        if device.type == "cuda":
            torch.cuda.synchronize()

    # --- SBERT (Bi-Encoder Baseline) ---
    sync()
    t0_sbert = time.perf_counter()
    with torch.no_grad():
        q_emb = sbert.encode([query], convert_to_tensor=True, device=device)
        c_emb = sbert.encode(corpus, convert_to_tensor=True, device=device)
        sync()
        t1_sbert = time.perf_counter()
        
        # SBERT pure retrieval logic (Dot Product/Cosine Sim)
        sbert_scores = util.cos_sim(q_emb, c_emb)[0].cpu().numpy()
        sync()
        t2_sbert = time.perf_counter()
        
    sbert_total_time = t2_sbert - t0_sbert
    sbert_no_enc_time = t2_sbert - t1_sbert

    # --- Cross-Encoder (Industry Standard Reranker) ---
    ce_pairs = [[query, doc] for doc in corpus]
    sync()
    t0_ce = time.perf_counter()
    # Cross-Encoders cannot separate encoding from scoring
    ce_scores = torch.tensor(cross_encoder.predict(ce_pairs)).numpy()
    sync()
    t1_ce = time.perf_counter()
    ce_total_time = t1_ce - t0_ce

    # --- Scout (The Action Filter) ---
    sync()
    t0_scout = time.perf_counter()
    with torch.no_grad():
        # Encoding step (Can be skipped in production if fetching cached embeddings)
        q_emb_s = sbert.encode([query], convert_to_tensor=True, device=device)
        c_emb_s = sbert.encode(corpus, convert_to_tensor=True, device=device)
        
        sync()
        t1_scout = time.perf_counter()
        
        # Scout pure retrieval logic (The N x N Matrix)
        all_emb = torch.cat([q_emb_s, c_emb_s], dim=0).unsqueeze(0)
        out = torch.sigmoid(scout_model(all_emb) / 0.5).squeeze(0)
        scout_scores = out[0, 1:].cpu().numpy()
        
        sync()
        t2_scout = time.perf_counter()

    scout_total_time = t2_scout - t0_scout
    scout_no_enc_time = t2_scout - t1_scout

    print(f"AGENT STATE: {query}\n")
    
    def print_top_3(name, scores, total_time, no_enc_time=None):
        print(f"--- Top 3 according to {name} ---")
        if no_enc_time is not None:
            print(f"⏱️  Time (Total): {total_time * 1000:.2f} ms | Time (Without Encoding): {no_enc_time * 1000:.2f} ms")
        else:
            print(f"⏱️  Time (Total): {total_time * 1000:.2f} ms | Time (Without Encoding): N/A (Joint architecture)")
            
        top_3_idx = np.argsort(scores)[::-1][:3]
        for rank, idx in enumerate(top_3_idx):
            print(f"{rank+1}. [{scores[idx]:.4f}] {corpus[idx]}")
        print()

    print_top_3("SBERT", sbert_scores, sbert_total_time, sbert_no_enc_time)
    print_top_3("Cross-Encoder", ce_scores, ce_total_time, None)
    print_top_3("Scout", scout_scores, scout_total_time, scout_no_enc_time)

run_agentic_rag_test(scout_model)