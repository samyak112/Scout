import time
import torch
from typing import Optional
from sentence_transformers import SentenceTransformer
from main import Scout
from response_types import MatrixResult, RankResult


class ScoutInference:
    """
    Directional relevance scorer.

    Args:
        checkpoint_path: Path to a Scout .pt checkpoint file.
        encoder:         Sentence encoder model name (must match what Scout was trained with).
        device:          'cuda', 'cpu', or None for auto-detect.
        temperature:     Softens or sharpens output scores. Default 0.5.
    """

    DEFAULT_CHECKPOINT = "checkpoints/scout_best.pt"
    DEFAULT_ENCODER    = "sentence-transformers/all-mpnet-base-v2"

    def __init__(
        self,
        checkpoint_path: str = DEFAULT_CHECKPOINT,
        encoder: str = DEFAULT_ENCODER,
        device: Optional[str] = None,
        temperature: float = 0.5,
    ):
        self.temperature = temperature
        self.device = torch.device(
            device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        )

        print(f"[Scout] Loading encoder : {encoder}")
        self._encoder = SentenceTransformer(encoder, device=self.device)

        print(f"[Scout] Loading checkpoint: {checkpoint_path}")
        self._model = self._load_checkpoint(checkpoint_path)
        print(f"[Scout] Ready on {self.device}")

    def rank(self, query: str, candidates: list[str]) -> RankResult:
        """
        Given a query and a list of candidates, score and rank how much
        each candidate resolves or answers the query.

        Args:
            query:      The question or problem statement.
            candidates: List of candidate sentences to rank.

        Returns:
            RankResult with scores, ranking, timing, and full NxN matrix.
        """
        sentences = [query] + candidates
        matrix, encoding_ms, scoring_ms = self._score_matrix(sentences)

        scores  = matrix[0][1:]
        ranking = sorted(range(len(candidates)), key=lambda i: scores[i], reverse=True)

        return RankResult(
            query=query,
            candidates=candidates,
            scores=scores,
            ranking=ranking,
            matrix=matrix,
            encoding_ms=encoding_ms,
            scoring_ms=scoring_ms,
        )

    def matrix(self, sentences: list[str]) -> MatrixResult:
        """
        Compute the full NxN directional relevance matrix for a set of sentences.
        matrix[i][j] = how much sentence j adds value to sentence i.

        Useful for clustering, segmentation, or exploring relationships
        within a document.

        Args:
            sentences: List of sentences to compare.

        Returns:
            MatrixResult with the full NxN matrix and timing.
        """
        matrix, encoding_ms, scoring_ms = self._score_matrix(sentences)

        return MatrixResult(
            sentences=sentences,
            matrix=matrix,
            encoding_ms=encoding_ms,
            scoring_ms=scoring_ms,
        )


    def _sync(self):
        if self.device.type == "cuda":
            torch.cuda.synchronize()

    def _score_matrix(
        self, sentences: list[str]
    ) -> tuple[list[list[float]], float, float]:

        with torch.no_grad():

            # --- Encoding ---
            self._sync()
            t0 = time.perf_counter()

            embeddings = self._encoder.encode(
                sentences,
                convert_to_tensor=True,
                device=self.device,
            ).unsqueeze(0)  # [1, N, 768]

            self._sync()
            t1 = time.perf_counter()

            # --- Scoring ---
            logits = self._model(embeddings)                    # [1, N, N]
            scores = torch.sigmoid(logits / self.temperature)   # [1, N, N]
            scores = scores.squeeze(0).cpu().tolist()           # [N, N]

            self._sync()
            t2 = time.perf_counter()

        encoding_ms = (t1 - t0) * 1000
        scoring_ms  = (t2 - t1) * 1000

        return scores, encoding_ms, scoring_ms

    def _load_checkpoint(self, path: str) -> Scout:
        checkpoint = torch.load(path, map_location=self.device, weights_only=False)
        cfg = checkpoint.get("config", {"d_model": 384, "nhead": 8, "num_layers": 3})
        model = Scout(
            d_model=cfg["d_model"],
            nhead=cfg["nhead"],
            num_layers=cfg["num_layers"],
        )
        model.load_state_dict(checkpoint["model_state_dict"], strict=False)
        model.to(self.device)
        model.eval()
        return model