import os
import time
import numpy as np
import torch
from typing import Optional
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.cross_encoder import CrossEncoder
from huggingface_hub import hf_hub_download
from main import Scout
from response_types import MatrixResult, RankResult, CompeteResult, SegmentResult


class ScoutInference:
    """
    Directional relevance scorer.

    Args:
        checkpoint_path: Path to a local .pt checkpoint. If None, downloads
                         automatically from Hugging Face.
        encoder:         Sentence encoder model name (must match what Scout was trained with).
        device:          'cuda', 'cpu', or None for auto-detect.
        temperature:     Softens or sharpens output scores. Default 0.5.
    """

    HF_REPO_ID            = "SpiderHomie/scout"
    HF_FILENAME           = "scout_best.pt"
    DEFAULT_CHECKPOINT    = "checkpoints/scout_best.pt"
    DEFAULT_ENCODER       = "sentence-transformers/all-mpnet-base-v2"
    DEFAULT_CROSS_ENCODER = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    def __init__(
        self,
        checkpoint_path: Optional[str] = None,
        encoder: str = DEFAULT_ENCODER,
        device: Optional[str] = None,
        temperature: float = 0.5,
    ):
        self.temperature = temperature
        self.device = torch.device(
            device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        )

        print(f"[Scout] Loading encoder   : {encoder}")
        self._encoder = SentenceTransformer(encoder, device=self.device)

        resolved = self._resolve_checkpoint(checkpoint_path)
        print(f"[Scout] Loading checkpoint: {resolved}")
        self._model = self._load_checkpoint(resolved)

        self._cross_encoder = None  # lazy loaded only if compete=True

        print(f"[Scout] Ready on {self.device}")

    # ──────────────────────────────────────────────
    # Public API
    # ──────────────────────────────────────────────

    def rank(
        self,
        query: str,
        candidates: list[str],
        compete: bool = False,
    ) -> RankResult | CompeteResult:
        """
        Given a query and a list of candidates, score and rank how much
        each candidate resolves or answers the query.

        Args:
            query:      The question or problem statement.
            candidates: List of candidate sentences to rank.
            compete:    If True, also runs SBERT and Cross-Encoder and returns
                        all three sets of scores side by side.

        Returns:
            RankResult normally. CompeteResult when compete=True.
        """
        if compete:
            return self._compete(query, candidates)

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

    def segment(
        self,
        sentences: list[str],
        block_size: int = 2,
        smoothing: int = 0,
        sensitivity: float = 0.5,
    ) -> SegmentResult:
        """
        Detect paragraph boundaries in a list of sentences using Scout's
        directional relevance matrix and TextTiling-style valley detection.

        How it works:
            For each gap between sentence i and i+1, a block similarity score
            is computed as the average mutual score between the k sentences
            before and after the gap. mutual(i,j) = min(score(i→j), score(j→i)).
            Valleys in this signal — where similarity drops — indicate topic or
            conceptual shifts. Boundaries are placed where the depth score
            exceeds mean + sensitivity * std.

        Args:
            sentences:   List of sentences to segment.
            block_size:  Number of sentences on each side of a gap to compare.
            smoothing:   Moving average window for the similarity signal (0 = off).
            sensitivity: Controls how aggressively boundaries are placed.
                         Lower = more boundaries. Higher = fewer. Default 0.5.

        Returns:
            SegmentResult with matrix, TextTiling signal, and detected chunks.
        """
        matrix_result = self.matrix(sentences)
        mat = np.array(matrix_result.matrix)
        n = len(sentences)

        def mutual(i, j):
            return min(mat[i][j], mat[j][i])

        def block_sim(gap, k):
            left  = list(range(max(0, gap - k + 1), gap + 1))
            right = list(range(gap + 1, min(n, gap + 1 + k)))
            if not left or not right:
                return 0.0
            return float(np.mean([mutual(i, j) for i in left for j in right]))

        # Similarity signal
        sim = np.array([block_sim(g, block_size) for g in range(n - 1)])

        # Smoothing
        def smooth(signal, window):
            out = signal.copy()
            for i in range(len(signal)):
                lo = max(0, i - window)
                hi = min(len(signal), i + window + 1)
                out[i] = np.mean(signal[lo:hi])
            return out

        sim_smooth = smooth(sim, smoothing) if smoothing > 0 else sim.copy()

        # Depth scores
        depths = np.zeros(len(sim_smooth))
        for i in range(1, len(sim_smooth) - 1):
            depths[i] = (sim_smooth[i-1] - sim_smooth[i]) + (sim_smooth[i+1] - sim_smooth[i])

        threshold = depths.mean() + sensitivity * depths.std()
        boundaries = [i for i, d in enumerate(depths) if d > threshold]

        # Build chunks
        chunks, start = [], 0
        for b in sorted(boundaries):
            chunks.append(list(range(start, b + 1)))
            start = b + 1
        chunks.append(list(range(start, n)))

        return SegmentResult(
            sentences=sentences,
            chunks=chunks,
            boundaries=boundaries,
            matrix=matrix_result.matrix,
            sim_signal=sim.tolist(),
            depth_signal=depths.tolist(),
            boundary_threshold=float(threshold),
            encoding_ms=matrix_result.encoding_ms,
            scoring_ms=matrix_result.scoring_ms,
        )

    # ──────────────────────────────────────────────
    # Compete
    # ──────────────────────────────────────────────

    def _compete(self, query: str, candidates: list[str]) -> CompeteResult:
        sbert_scores, sbert_enc_ms, sbert_score_ms = self._run_sbert(query, candidates)
        ce_scores, ce_ms                            = self._run_cross_encoder(query, candidates)
        sentences                                   = [query] + candidates
        scout_matrix, scout_enc_ms, scout_score_ms  = self._score_matrix(sentences)
        scout_scores                                = scout_matrix[0][1:]

        return CompeteResult(
            query=query,
            candidates=candidates,
            scout_scores=scout_scores,
            sbert_scores=sbert_scores,
            cross_encoder_scores=ce_scores,
            scout_encoding_ms=scout_enc_ms,
            scout_scoring_ms=scout_score_ms,
            sbert_encoding_ms=sbert_enc_ms,
            sbert_scoring_ms=sbert_score_ms,
            cross_encoder_ms=ce_ms,
        )

    def _run_sbert(
        self, query: str, candidates: list[str]
    ) -> tuple[list[float], float, float]:
        self._sync()
        t0 = time.perf_counter()

        with torch.no_grad():
            q_emb = self._encoder.encode([query],    convert_to_tensor=True, device=self.device)
            c_emb = self._encoder.encode(candidates, convert_to_tensor=True, device=self.device)

        self._sync()
        t1 = time.perf_counter()

        scores = util.cos_sim(q_emb, c_emb)[0].cpu().tolist()

        self._sync()
        t2 = time.perf_counter()

        return scores, (t1 - t0) * 1000, (t2 - t1) * 1000

    def _run_cross_encoder(
        self, query: str, candidates: list[str]
    ) -> tuple[list[float], float]:
        if self._cross_encoder is None:
            print(f"[Scout] Loading cross-encoder: {self.DEFAULT_CROSS_ENCODER}")
            self._cross_encoder = CrossEncoder(self.DEFAULT_CROSS_ENCODER, device=self.device)

        pairs = [[query, c] for c in candidates]

        self._sync()
        t0 = time.perf_counter()

        raw    = self._cross_encoder.predict(pairs)
        scores = torch.sigmoid(torch.tensor(raw)).tolist()

        self._sync()
        t1 = time.perf_counter()

        return scores, (t1 - t0) * 1000

    # ──────────────────────────────────────────────
    # Internal
    # ──────────────────────────────────────────────

    def _resolve_checkpoint(self, checkpoint_path: Optional[str]) -> str:
        # 1. Explicit path provided and exists — use it
        if checkpoint_path and os.path.exists(checkpoint_path):
            return checkpoint_path

        # 2. Default local path exists — use it
        if os.path.exists(self.DEFAULT_CHECKPOINT):
            return self.DEFAULT_CHECKPOINT

        # 3. Download from Hugging Face
        print(f"[Scout] Checkpoint not found locally, downloading from HuggingFace ({self.HF_REPO_ID})...")
        os.makedirs("checkpoints", exist_ok=True)
        path = hf_hub_download(
            repo_id=self.HF_REPO_ID,
            filename=self.HF_FILENAME,
            local_dir="checkpoints",
        )
        print(f"[Scout] Saved to {path}")
        return path

    def _sync(self):
        if self.device.type == "cuda":
            torch.cuda.synchronize()

    def _score_matrix(
        self, sentences: list[str]
    ) -> tuple[list[list[float]], float, float]:
        with torch.no_grad():
            self._sync()
            t0 = time.perf_counter()

            embeddings = self._encoder.encode(
                sentences,
                convert_to_tensor=True,
                device=self.device,
            ).unsqueeze(0)  # [1, N, 768]

            self._sync()
            t1 = time.perf_counter()

            # 1. Model now returns probabilities [1, N, N]
            probs = self._model(embeddings) 

            # 2. Handle Temperature (Optional)
            # Since Squared ReLU is already sharp, we usually just use the raw output.
            # But if you want a custom temperature, apply it to the probabilities:
            # if self.temperature != 1.0:
            #     # We use a small epsilon to avoid log(0)
            #     # This essentially "re-hyping" the already hyped signal
            #     probs = torch.pow(probs, 1.0 / self.temperature)
            #     # Re-normalize to keep it a valid distribution if needed
            #     probs = probs / (probs.sum(dim=-1, keepdim=True) + 1e-6)

            scores = probs.squeeze(0).cpu().tolist() # [N, N]

            self._sync()
            t2 = time.perf_counter()

        return scores, (t1 - t0) * 1000, (t2 - t1) * 1000

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