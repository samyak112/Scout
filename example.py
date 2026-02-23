from inference import ScoutInference

scout = ScoutInference()

result = scout.rank(
    query="My bread dough didn't rise at all after sitting for two hours.",
    candidates=[
        "Bread dough usually needs to sit for at least two hours to properly rise.", # Semantic Echo / Trivia
        "If your bread dough doesn't rise after two hours, it will bake into a dense, hard brick.", # Implication (Not a cause)
        "The water you poured in was boiling and killed the active culture.", # ✅ THE CAUSE (Zero lexical overlap)
        "You should cover the bread dough with a damp towel while it is sitting and rising.", # Tangential Advice
        "Sometimes bread dough simply won't rise even if you let it sit for over two hours.", # Pure Echo
        "Flour contains gluten proteins that form a network to trap gas bubbles." # Unrelated Fact
    ]
)

print("=" * 60)
print("RETRIEVAL")
print("=" * 60)
print(f"Query: {result.query}\n")
print(f"{'Rank':<6} {'Score':<8} Candidate")
print("-" * 60)
for rank, idx in enumerate(result.ranking):
    print(f"{rank + 1:<6} {result.scores[idx]:<8.4f} {result.candidates[idx]}")

print(f"\n⏱  Encoding: {result.encoding_ms:.1f}ms | "
      f"Scoring: {result.scoring_ms:.1f}ms | "
      f"Total: {result.encoding_ms + result.scoring_ms:.1f}ms")


result = scout.matrix([
    "The faucet in the kitchen is leaking.",
    "A worn-out washer is causing the leak.",
    "Replace the washer to fix the drip.",
    "The kitchen was renovated last year.",
])

print("\n\n" + "=" * 60)
print("MATRIX — Directional Relevance")
print("matrix[i][j] = how much sentence j adds value to sentence i")
print("=" * 60)

n = len(result.sentences)
print("\n" + " " * 6 + "  ".join(f"S{j}".ljust(6) for j in range(n)))
for i in range(n):
    row = f"S{i}    " + "  ".join(f"{result.matrix[i][j]:.3f}".ljust(6) for j in range(n))
    print(row)

print("\nSentences:")
for i, s in enumerate(result.sentences):
    print(f"  S{i}: {s}")

print(f"\n⏱  Encoding: {result.encoding_ms:.1f}ms | "
      f"Scoring: {result.scoring_ms:.1f}ms | "
      f"Total: {result.encoding_ms + result.scoring_ms:.1f}ms")