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

    cfg = checkpoint["model_config"]
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
    return output.squeeze(0)              # [N, N]


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":

    # Example sentences
    sentences = [
    "Liam submitted his research paper to the conference.",          # 0
    "The submission deadline was extended by one week.",             # 1  (hard negative – same topic)
    "He received reviewer comments two months later.",               # 2  → depends on 0
    "The paper was accepted after revisions.",                       # 3  → depends on 0, 2
    "The conference will be held in Vienna this year.",              # 4  (hard negative – same topic)
    "The reviewers requested additional experiments.",               # 5  ↔ symmetric with 2
    "Those experiments addressed the reviewers’ concerns."           # 6  ↔ symmetric with 5
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
