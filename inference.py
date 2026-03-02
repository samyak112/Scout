import os
import time
import torch
from typing import Optional, List
from sentence_transformers import SentenceTransformer, util
from sentence_transformers.cross_encoder import CrossEncoder
from huggingface_hub import hf_hub_download
from main import Scout
from response_types import MatrixResult, RankResult, CompeteResult, SegmentResult

class ScoutInference:
    HF_REPO_ID  = "SpiderHomie/scout"
    HF_FILENAME = "scout_best.pt"
    DEFAULT_CHECKPOINT = "checkpoints/scout_best.pt"
    DEFAULT_ENCODER    = "sentence-transformers/all-mpnet-base-v2"
    DEFAULT_CROSS_ENCODER = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    def __init__(
        self,
        checkpoint_path: Optional[str] = None,
        encoder: str = DEFAULT_ENCODER,
        device: Optional[str] = None,
        temperature: float = 0.5,
        use_cache: bool = True,
        cache_path: str = "checkpoints/sbert_cache.pt"
    ):
        self.temperature = temperature
        self.device = torch.device(
            device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        )
        self.use_cache = use_cache
        self.cache_path = cache_path
        self._emb_cache = {} if use_cache else None

        print(f"[Scout] Loading encoder: {encoder}")
        self._encoder = SentenceTransformer(encoder, device=self.device)

        resolved = self._resolve_checkpoint(checkpoint_path)
        print(f"[Scout] Loading checkpoint: {resolved}")
        self._model = self._load_checkpoint(resolved)

        self._cross_encoder = None  # lazy loaded
        print(f"[Scout] Ready on {self.device}")

    # ──────────────────────────────────────────────
    # Public API
    # ──────────────────────────────────────────────
    def rank(self, query: str, candidates: List[str], compete: bool = False):
        if compete:
            return self._compete(query, candidates)

        sentences = [query] + candidates
        matrix, enc_ms, score_ms = self._score_matrix(sentences)
        scores = matrix[0][1:]
        ranking = sorted(range(len(candidates)), key=lambda i: scores[i], reverse=True)

        return RankResult(
            query=query,
            candidates=candidates,
            scores=scores,
            ranking=ranking,
            matrix=matrix,
            encoding_ms=enc_ms,
            scoring_ms=score_ms,
        )

    # ──────────────────────────────────────────────
    # Internal helpers
    # ──────────────────────────────────────────────
    def _resolve_checkpoint(self, checkpoint_path: Optional[str]) -> str:
        if checkpoint_path and os.path.exists(checkpoint_path):
            return checkpoint_path
        if os.path.exists(self.DEFAULT_CHECKPOINT):
            return self.DEFAULT_CHECKPOINT
        print(f"[Scout] Checkpoint not found locally, downloading from HuggingFace ({self.HF_REPO_ID})...")
        os.makedirs("checkpoints", exist_ok=True)
        path = hf_hub_download(
            repo_id=self.HF_REPO_ID,
            filename=self.HF_FILENAME,
            local_dir="checkpoints",
        )
        print(f"[Scout] Saved to {path}")
        return path

    def _load_checkpoint(self, path: str) -> Scout:
        checkpoint = torch.load(path, map_location=self.device)
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

    def _sync(self):
        if self.device.type == "cuda":
            torch.cuda.synchronize()

    def _score_matrix(self, sentences: List[str]):
        with torch.no_grad():
            self._sync()
            t0 = time.perf_counter()

            embeddings_list = []
            for s in sentences:
                if self.use_cache and s in self._emb_cache:
                    embeddings_list.append(self._emb_cache[s])
                else:
                    emb = self._encoder.encode([s], convert_to_tensor=True, device=self.device)
                    embeddings_list.append(emb[0])
                    if self.use_cache:
                        self._emb_cache[s] = emb[0]

            embeddings = torch.stack(embeddings_list, dim=0).unsqueeze(0)  # [1, N, 768]
            self._sync()
            t1 = time.perf_counter()

            logits = self._model(embeddings)
            scores = torch.sigmoid(logits / self.temperature)
            scores = scores.squeeze(0).cpu().tolist()
            self._sync()
            t2 = time.perf_counter()

        # Save cache if needed
        if self.use_cache and not os.path.exists(self.cache_path):
            torch.save(self._emb_cache, self.cache_path)

        return scores, (t1 - t0) * 1000, (t2 - t1) * 1000

    # ──────────────────────────────────────────────
    # Compete / cross-encoder
    # ──────────────────────────────────────────────
    def _compete(self, query: str, candidates: List[str]):
        sbert_scores, enc_ms, score_ms = self._run_sbert(query, candidates)
        ce_scores, ce_ms = self._run_cross_encoder(query, candidates)
        sentences = [query] + candidates
        scout_matrix, scout_enc_ms, scout_score_ms = self._score_matrix(sentences)
        scout_scores = scout_matrix[0][1:]

        return CompeteResult(
            query=query,
            candidates=candidates,
            scout_scores=scout_scores,
            sbert_scores=sbert_scores,
            cross_encoder_scores=ce_scores,
            scout_encoding_ms=scout_enc_ms,
            scout_scoring_ms=scout_score_ms,
            sbert_encoding_ms=enc_ms,
            sbert_scoring_ms=score_ms,
            cross_encoder_ms=ce_ms,
        )

    def _run_sbert(self, query: str, candidates: List[str]):
        self._sync()
        t0 = time.perf_counter()
        with torch.no_grad():
            q_emb = self._encoder.encode([query], convert_to_tensor=True, device=self.device)
            c_emb = self._encoder.encode(candidates, convert_to_tensor=True, device=self.device)
        self._sync()
        t1 = time.perf_counter()
        scores = util.cos_sim(q_emb, c_emb)[0].cpu().tolist()
        self._sync()
        t2 = time.perf_counter()
        return scores, (t1 - t0) * 1000, (t2 - t1) * 1000

    def _run_cross_encoder(self, query: str, candidates: List[str]):
        if self._cross_encoder is None:
            print(f"[Scout] Loading cross-encoder: {self.DEFAULT_CROSS_ENCODER}")
            self._cross_encoder = CrossEncoder(self.DEFAULT_CROSS_ENCODER, device=self.device)
        pairs = [[query, c] for c in candidates]
        self._sync()
        t0 = time.perf_counter()
        raw = self._cross_encoder.predict(pairs)
        scores = torch.sigmoid(torch.tensor(raw)).tolist()
        self._sync()
        t1 = time.perf_counter()
        return scores, (t1 - t0) * 1000