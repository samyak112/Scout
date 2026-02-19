import torch
import json
from sentence_transformers import SentenceTransformer

# -------- import your model definitions --------
from main import Scout  # or wherever Scout is defined


# -----------------------------
# Device
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")


# -----------------------------
# Load model
# -----------------------------
def load_scout_model(checkpoint_path: str, device):
    checkpoint = torch.load(checkpoint_path, map_location=device)

    # Try to find config, or fall back to your known defaults
    if "model_config" in checkpoint:
        cfg = checkpoint["model_config"]
    elif "config" in checkpoint:  # specific check for older versions
        cfg = checkpoint["config"]
    else:
        print("⚠ Config not found in checkpoint. Using default 768/12/6 architecture.")
        cfg = {'d_model': 768, 'nhead': 12, 'num_layers': 6}

    model = Scout(
        d_model=cfg["d_model"],
        nhead=cfg["nhead"],
        num_layers=cfg["num_layers"]
    )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    print(f"✓ Loaded model from {checkpoint_path}")
    return model


# -----------------------------
# Encode sentences
# -----------------------------
def encode_sentences(sentences, device):
    sbert = SentenceTransformer(
        "sentence-transformers/all-mpnet-base-v2",
        device=device
    )

    with torch.no_grad():
        embeddings = sbert.encode(
            sentences,
            convert_to_tensor=True,
            device=device
        )

    # [N, 768] → [1, N, 768]
    return embeddings.unsqueeze(0)


# -----------------------------
# Run inference
# -----------------------------
@torch.no_grad()
def run_inference(model, sentence_embeddings):
    """
    Input:
        sentence_embeddings: [1, N, 768]

    Output:
        score_matrix: [N, N]
    """
    output = model(sentence_embeddings)  # [1, N, N]
    scores = torch.sigmoid(output/0.5)  # ← add this
    return scores.squeeze(0)              # [N, N]


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":

    # Example sentences
    sentences = [
    "the tap is leaking",
    "call a plumber",
    "water is dripping from the faucet handle",
    "tighten the valve nut under the sink",
    "plumbers charge by the hour",
]



    # Load model
    model = load_scout_model(
        "checkpoints/scout_best.pt",  # or scout.pt
        device
    )

    # Encode
    embeddings = encode_sentences(sentences, device)

    # Infer
    score_matrix = run_inference(model, embeddings)

    print("\nScore Matrix:")
    print(score_matrix.cpu().numpy())
