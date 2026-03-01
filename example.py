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

print(result)