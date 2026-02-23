from dataclasses import dataclass


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