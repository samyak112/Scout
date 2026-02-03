# Scout: Directional Information Gain Between Sentences

**Status:** Experimental | [Details in Issues](https://github.com/samyak112/Scout/issues/2)

## What is this?

Scout learns **directional relevance** between sentences—not just "are these similar?" but "does sentence B add functional value after reading sentence A?"

**Example:**

- `"My faucet is leaking" → "Tighten the valve nut"` = **High** (solution adds value)
- `"Tighten the valve nut" → "My faucet is leaking"` = **Low** (problem doesn't help solution)
- BUT `"The valve nut is located under the handle at the base of the faucet"` makes sense for `"Tighten the valve nut"`

This asymmetry enables:

- **Retrieval:** Find sentences that solve/explain a query
- **Clustering:** Group sentences with mutual information gain
- **Segmentation:** Detect when topics actually shift vs. just keywords changing

## Why not use existing methods?

- **Cross-encoders:** One pair at a time, slow for N×N comparisons
- **Cosine similarity:** Symmetric, confuses "same topic" with "adds value"
- **BM25/SBERT:** Keyword/embedding overlap ≠ information gain

## How it works

Scout processes **batches of sentences** and outputs an **N×N relevance matrix** in one forward pass.

**Key architecture changes:**

1. **No positional encoding** (sentence order shouldn't affect pairwise relevance)
2. **Sigmoid attention** instead of softmax (relationships are independent, not competitive)
3. **Multi-layer aggregation** (learns which transformer layers capture relevance best)

## Current Status

Training on synthetic directional batches (problem→diagnosis→solution chains, cross-domain negatives). Validating whether attention mechanics can learn functional relevance without supervision at the token level.
