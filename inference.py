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
    sentences = ["The living area's HVAC isn't blowing cold air, even on the moderate setting.", "The refrigerant line in the HVAC system is likely leaking due to environmental corrosion.", "A licensed HVAC technician should inspect and recharge the refrigerant line soon to prevent further damage.", "Cleaning HVAC air filters monthly prevents restricted airflow and potential overheating.", "Dirty HVAC air filters restrict airflow, causing the system to work harder and potentially overheat the living area.", "Dusting the living area furniture makes it look nicer.", "Environmental awareness involves reducing waste and conserving energy."]



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
