import time
import torch
from sentence_transformers import SentenceTransformer, CrossEncoder
from main import Scout

# -----------------------------
# 1. Setup & Configuration
# -----------------------------
# Explicitly forcing CPU as requested
device = torch.device("cpu")
print(f"Running on: {device}\n")

def load_scout(checkpoint_path):
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    # Fallback to defaults if config isn't in your checkpoint
    cfg = checkpoint.get("config", {'d_model': 384, 'nhead': 8, 'num_layers': 3})
    
    model = Scout(d_model=cfg["d_model"], nhead=cfg["nhead"], num_layers=cfg["num_layers"])
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()
    return model

# Load Models
print("Loading SBERT (Scout Encoder)...")
sbert = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=device)

print("Loading Scout Model...")
scout_model = load_scout("checkpoints/scout_best.pt")

print("Loading Cross-Encoder Baseline...")
# ms-marco is specifically trained to rank answers for queries
cross_encoder = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", device=device)

# -----------------------------
# 2. The "Human Intuition" Data
# -----------------------------
query = "My faucet is leaking heavily under the sink."

# A mix of direct solutions, shared-topic useless facts, and completely random facts.
corpus = [
    "Tighten the main valve nut using a wrench.",              # The actual solution
    "Turn off the main water supply immediately.",             # Good next step
    "Sinks are usually made of porcelain or stainless steel.", # Hard Negative (Shared topic, no utility)
    "Water bills can be very expensive in the summer.",        # Hard Negative (Shared topic, no utility)
    "Python is a great programming language for AI.",          # Completely unrelated
]

# Combine query and corpus so Scout can build its N x N matrix
all_sentences = [query] + corpus

print("-" * 50)
print(f"QUERY: {query}")
print("-" * 50)

# ==========================================
# TEST A: SCOUT PIPELINE
# ==========================================
# 1. Measure SBERT Encoding Time
t0 = time.perf_counter()
with torch.no_grad():
    embeddings = sbert.encode(all_sentences, convert_to_tensor=True, device=device)
    embeddings = embeddings.unsqueeze(0) # [1, N, 768]
t_encode = time.perf_counter() - t0

# 2. Measure Scout Inference Time
t1 = time.perf_counter()
with torch.no_grad():
    raw_output = scout_model(embeddings)
    # Using your /0.5 scaling
    scout_scores = torch.sigmoid(raw_output / 0.5).squeeze(0) 
t_infer = time.perf_counter() - t1

# 3. Extract the Query -> Corpus row (Row 0, Columns 1 to N)
query_to_corpus_scores = scout_scores[0, 1:].tolist()

# Pair scores with sentences and sort descending
scout_results = list(zip(query_to_corpus_scores, corpus))
scout_results.sort(key=lambda x: x[0], reverse=True)

# ==========================================
# TEST B: CROSS-ENCODER PIPELINE
# ==========================================
# Cross encoders need data formatted as pairs: [[Query, Corpus1], [Query, Corpus2], ...]
pairs = [[query, doc] for doc in corpus]

t2 = time.perf_counter()
cross_scores = cross_encoder.predict(pairs)
t_cross = time.perf_counter() - t2

cross_results = list(zip(cross_scores, corpus))
cross_results.sort(key=lambda x: x[0], reverse=True)


# -----------------------------
# 3. Print the Showdown
# -----------------------------
print("\n🏆 SCOUT MODEL RANKING")
print(f"Encoding Time:  {t_encode:.4f} seconds")
print(f"Inference Time: {t_infer:.4f} seconds")
print(f"Total Time:     {t_encode + t_infer:.4f} seconds")
for score, text in scout_results:
    print(f"[{score:.4f}] {text}")

print("\n" + "="*50)

print("\n⚖️ CROSS-ENCODER BASELINE RANKING")
print(f"Total Time:     {t_cross:.4f} seconds")
for score, text in cross_results:
    print(f"[{score:.4f}] {text}")
print("\n")