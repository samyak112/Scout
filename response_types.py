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