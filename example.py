from inference import ScoutInference

scout = ScoutInference()

# ──────────────────────────────────────────────
# Demo 1: Retrieval
# ──────────────────────────────────────────────

result = scout.rank(
    query="My phone is getting very hot and the battery drains in two hours.",
    candidates = [
    # ── CORRECT: actual causes and fixes ──────────────────────────────────────
    "Background apps running constantly consume CPU cycles and generate heat.",         # CORRECT - root cause
    "A degraded battery loses its ability to hold charge and overworks the processor.", # CORRECT - root cause
    "Check which apps are using the most battery in your settings and close them.",     # CORRECT - fix
    "Replacing a swollen or old battery will fix both overheating and drain issues.",   # CORRECT - fix
    "A phone running too hot throttles its processor to cool down, draining more power.", # CORRECT - mechanism

    # ── HARD NEGATIVE: causal structure, right domain, wrong problem ──────────
    # These are the real traps — structured exactly like correct answers but aren't
    "A cracked screen allows moisture inside which corrodes the charging port.",        # causal, phone, wrong problem
    "Dropping a phone damages the gyroscope sensor causing rotation glitches.",        # causal, phone, wrong problem
    "Water damage shorts the speaker circuit making audio sound distorted.",           # causal, phone, wrong problem
    "A loose SIM card causes the phone to constantly search for signal.",              # causal, phone, wrong problem

    # ── HARD NEGATIVE: mentions heat and battery but doesn't resolve the query ─
    "Lithium-ion batteries degrade faster when consistently exposed to high heat.",    # sounds relevant, doesn't fix it
    "Processors generate heat as a byproduct of computation.",                         # true, related, not a fix
    "Battery capacity is measured in milliamp hours and decreases with age.",          # related concept, not a fix
    "Heat is the biggest enemy of long-term battery health.",                          # sounds like insight, no utility
],
  
)

print("=" * 60)
print("RETRIEVAL")
print("=" * 60)
# print(result)


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


# # ──────────────────────────────────────────────
# # Demo 3: Compete — Scout vs SBERT vs Cross-Encoder
# # ──────────────────────────────────────────────

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

# # ──────────────────────────────────────────────
# # Demo 4: Paragraph boundary detection
# # ──────────────────────────────────────────────

sentences = [
    # What genes are
    "The gene is the basic unit of heredity in living organisms.",
    "Genes are made of DNA and carry the instructions for building proteins.",
    "Every cell in your body contains the same genetic information.",
    "Genes are copied and passed down from parent to offspring.",

    # Survival logic
    "Genes that help an organism survive are more likely to be passed on.",
    "Natural selection acts on genes through the bodies they build.",
    "A gene that causes harm to its host is less likely to survive across generations.",
    "Successful genes are simply those that have survived long enough to be common.",

    # Organisms as vehicles
    "Organisms are best thought of as vehicles built by genes for their own propagation.",
    "The body is a gene's way of making more genes.",
    "Individual survival matters only insofar as it serves the gene's replication.",
    "From the gene's perspective, the organism is temporary but the gene is potentially immortal.",
]

result = scout.segment(sentences)
print(result)