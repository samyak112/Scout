from dataclasses import dataclass
import numpy as np


@dataclass
class RankResult:
    query: str
    candidates: list[str]
    scores: list[float]        # score[i] = how much candidates[i] resolves the query
    ranking: list[int]         # indices sorted best → worst
    matrix: list[list[float]]  # full NxN matrix (query at row 0)
    encoding_ms: float         # time spent encoding sentences
    scoring_ms: float          # time spent running Scout

    @property
    def total_ms(self) -> float:
        return self.encoding_ms + self.scoring_ms

    def __repr__(self):
        lines = [f"Query: {self.query!r}\n"]
        for rank, idx in enumerate(self.ranking):
            lines.append(f"  {rank + 1}. [{self.scores[idx]:.4f}] {self.candidates[idx]}")
        lines.append(
            f"\n⏱  Encoding: {self.encoding_ms:.1f}ms | "
            f"Scoring: {self.scoring_ms:.1f}ms | "
            f"Total: {self.total_ms:.1f}ms"
        )
        return "\n".join(lines)


@dataclass
class MatrixResult:
    sentences: list[str]
    matrix: list[list[float]]  # matrix[i][j] = how much sentence j adds value to sentence i
    encoding_ms: float         # time spent encoding sentences
    scoring_ms: float          # time spent running Scout

    @property
    def total_ms(self) -> float:
        return self.encoding_ms + self.scoring_ms

    def __repr__(self):
        n = len(self.sentences)
        lines = ["Directional Relevance Matrix (row → col means 'col adds value to row')\n"]
        header = "".ljust(6) + "  ".join(f"S{j}".ljust(6) for j in range(n))
        lines.append(header)
        for i in range(n):
            row = f"S{i}".ljust(6) + "  ".join(f"{self.matrix[i][j]:.3f}".ljust(6) for j in range(n))
            lines.append(row)
        lines.append("\nSentences:")
        for i, s in enumerate(self.sentences):
            lines.append(f"  S{i}: {s}")
        lines.append(
            f"\n⏱  Encoding: {self.encoding_ms:.1f}ms | "
            f"Scoring: {self.scoring_ms:.1f}ms | "
            f"Total: {self.total_ms:.1f}ms"
        )
        return "\n".join(lines)


@dataclass
class SegmentResult:
    sentences: list[str]
    chunks: list[list[int]]         # each chunk is a list of sentence indices
    boundaries: list[int]           # gap indices where boundaries were placed
    matrix: list[list[float]]       # full NxN mutual score matrix
    sim_signal: list[float]         # raw TextTiling similarity at each gap
    depth_signal: list[float]       # depth score at each gap
    boundary_threshold: float       # threshold used to detect boundaries
    encoding_ms: float
    scoring_ms: float

    @property
    def total_ms(self) -> float:
        return self.encoding_ms + self.scoring_ms

    def __repr__(self):
        n = len(self.sentences)
        mat = self.matrix
        lines = []

        # ── NxN matrix ────────────────────────────────────────────────────────
        lines.append("=" * (6 + 6 * n))
        lines.append("NxN DIRECTIONAL RELEVANCE MATRIX")
        lines.append("matrix[i][j] = how much sentence j adds value to sentence i")
        lines.append("=" * (6 + 6 * n))
        lines.append("     " + "  ".join(f"S{j:02d}" for j in range(n)))
        for i in range(n):
            lines.append(f"S{i:02d}  " + "  ".join(f"{mat[i][j]:.2f}" for j in range(n)))

        # ── TextTiling signal ─────────────────────────────────────────────────
        lines.append(f"\n{'=' * 62}")
        lines.append("TEXTTILING SIGNAL  (Scout mutual scores across each gap)")
        lines.append("=" * 62)
        lines.append(f"{'Gap':<10} {'Sim':<10} {'Depth':<10} {'Boundary'}")
        lines.append("-" * 42)
        for i in range(n - 1):
            marker = "  ◄ BOUNDARY" if i in self.boundaries else ""
            lines.append(
                f"S{i:02d}→S{i+1:02d}  "
                f"{self.sim_signal[i]:<10.4f}"
                f"{self.depth_signal[i]:<10.4f}"
                f"{marker}"
            )
        lines.append(f"\nBoundary threshold: {self.boundary_threshold:.4f}")

        # ── Chunks ────────────────────────────────────────────────────────────
        lines.append(f"\n{'=' * 62}")
        lines.append(f"DETECTED CHUNKS  ({len(self.chunks)} segments)")
        lines.append("=" * 62)
        for i, chunk in enumerate(self.chunks):
            lines.append(f"\nChunk {i + 1}  ({len(chunk)} sentences)")
            lines.append("-" * 50)
            for idx in chunk:
                lines.append(f"  S{idx:02d}: {self.sentences[idx]}")

        lines.append(f"\n⏱  Encoding: {self.encoding_ms:.1f}ms | Scoring: {self.scoring_ms:.1f}ms | Total: {self.total_ms:.1f}ms")
        return "\n".join(lines)


@dataclass
class CompeteResult:
    query: str
    candidates: list[str]
    scout_scores: list[float]
    sbert_scores: list[float]
    cross_encoder_scores: list[float]
    scout_encoding_ms: float
    scout_scoring_ms: float
    sbert_encoding_ms: float
    sbert_scoring_ms: float
    cross_encoder_ms: float

    @property
    def scout_total_ms(self) -> float:
        return self.scout_encoding_ms + self.scout_scoring_ms

    @property
    def sbert_total_ms(self) -> float:
        return self.sbert_encoding_ms + self.sbert_scoring_ms

    def __repr__(self):
        n = len(self.candidates)

        scout_order = sorted(range(n), key=lambda i: self.scout_scores[i], reverse=True)
        col_w = max(len(c) for c in self.candidates) + 2

        lines = [
            f"Query: {self.query!r}\n",
            f"{'Candidate':<{col_w}} {'Scout':>8}  {'SBERT':>8}  {'CrossEnc':>8}",
            "-" * (col_w + 32),
        ]

        for idx in scout_order:
            lines.append(
                f"{self.candidates[idx]:<{col_w}} "
                f"{self.scout_scores[idx]:>8.4f}  "
                f"{self.sbert_scores[idx]:>8.4f}  "
                f"{self.cross_encoder_scores[idx]:>8.4f}"
            )

        lines.append(
            f"\n⏱  Scout : encoding {self.scout_encoding_ms:.1f}ms | "
            f"scoring {self.scout_scoring_ms:.1f}ms | "
            f"total {self.scout_total_ms:.1f}ms"
        )
        lines.append(
            f"⏱  SBERT : encoding {self.sbert_encoding_ms:.1f}ms | "
            f"scoring {self.sbert_scoring_ms:.1f}ms | "
            f"total {self.sbert_total_ms:.1f}ms"
        )
        lines.append(
            f"⏱  Cross : total {self.cross_encoder_ms:.1f}ms"
        )

        return "\n".join(lines)