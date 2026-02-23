from inference import ScoutInference

scout = ScoutInference()

# ──────────────────────────────────────────────
# Demo 1: Retrieval
# ──────────────────────────────────────────────

result = scout.rank(
    query="My bread dough didn't rise at all after sitting for two hours.",
    candidates=[
        "Bread dough usually needs to sit for at least two hours to properly rise.", # Semantic Echo / Trivia
        "If your bread dough doesn't rise after two hours, it will bake into a dense, hard brick.", # Implication (Not a cause)
        "The water you poured in was boiling and killed the active culture.", # ✅ THE CAUSE (Zero lexical overlap)
        "You should cover the bread dough with a damp towel while it is sitting and rising.", # Tangential Advice
        "Sometimes bread dough simply won't rise even if you let it sit for over two hours.", # Pure Echo
        "Flour contains gluten proteins that form a network to trap gas bubbles." # Unrelated Fact
    ],
    compete=True
)

print("=" * 60)
print("RETRIEVAL")
print("=" * 60)
print(result)


# ──────────────────────────────────────────────
# Demo 2: Matrix
# ──────────────────────────────────────────────

result = scout.matrix([
    "The faucet in the kitchen is leaking.",
    "A worn-out washer is causing the leak.",
    "Replace the washer to fix the drip.",
    "The kitchen was renovated last year.",
])

print("\n\n" + "=" * 60)
print("MATRIX")
print("=" * 60)
print(result)


# ──────────────────────────────────────────────
# Demo 3: Compete — Scout vs SBERT vs Cross-Encoder
# ──────────────────────────────────────────────

result = scout.rank(
    query="My faucet is leaking heavily under the sink.",
    candidates=[
        "Tighten the main valve nut using a wrench.",
        "Turn off the main water supply immediately.",
        "Buy the best faucet here on amazon.",
        "Sinks are usually made of porcelain or stainless steel.",
    ],
    compete=True,
)

print("\n\n" + "=" * 60)
print("COMPETE — Scout vs SBERT vs Cross-Encoder")
print("=" * 60)
print(result)