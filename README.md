# Scout: Directional Information Gain Between Sentences

**Status:** Experimental | [Details in Issues](https://github.com/samyak112/Scout/issues/2)

## What is this?

Scout is an experimental attention model that modifies the standard Transformer attention architecture designed to learn **directional relevance** between sentences. 

Instead of measuring symmetric topical similarity ("are these similar?"), it calculates functional value ("does sentence B provide a logical next step after reading sentence A?").

**The Core Concept:**
- `"My faucet is leaking"` $\rightarrow$ `"Tighten the valve nut"` = **High Gain** (Actionable solution)
- `"Tighten the valve nut"` $\rightarrow$ `"My faucet is leaking"` = **Low Gain** (Reverse causality)
- `"My faucet is leaking"` $\rightarrow$ `"Buy the best faucet on Amazon"` = **Low Gain** (Topical match, but lacks immediate utility)
- BUT `"The valve nut is located under the handle at the base of the faucet"` makes sense for `"Tighten the valve nut"`

This asymmetry is primarily useful for:
- **Retrieval (RAG):** Filtering out "semantic echoes" to find executable actions.
- **Clustering:** Grouping sentences by mutual information gain.
- **Segmentation:** Detecting when a procedural chain logically shifts.

## Why not use existing methods?

Existing methods are industry standards for search and QA, but they optimize for different mathematical goals:
- **Bi-Encoders (e.g., SBERT):** Highly efficient for symmetric topic matching, but keyword overlap can occasionally retrieve "semantic echoes" when directional causality is needed.
- **Cross-Encoders (e.g., MS-MARCO):** Excellent for deep Question/Answer relevance, but evaluating one pair at a time can be computationally heavy for $N \times N$ discourse graphing. 

## Benchmark: Agentic Troubleshooting

To test how Scout handles directional logic compared to standard retrieval, we ran a troubleshooting benchmark specifically designed to trap models with topical noise.

**Query (Agent State):** *"My faucet is leaking heavily under the sink."*

| Rank | SBERT (Bi-Encoder) | Cross-Encoder (MS-MARCO) (After Sigmoid) | **Scout (Directional Gain)** |
| :--- | :--- | :--- | :--- |
| **1.** | `[0.4821]` Buy the best faucet here on amazon | `[0.0022]` Buy the best faucet here on amazon | `[0.9585]` **Tighten the main valve nut using a wrench.** |
| **2.** | `[0.4532]` Turn off the main water supply immediately. | `[0.0010]` Sinks are usually made of porcelain... | `[0.9388]` **Turn off the main water supply immediately.** |
| **3.** | `[0.3802]` Tighten the main valve nut using a wrench. | `[0.0001]` Turn off the main water supply... | `[0.5356]` Buy the best faucet here on amazon |
| **Time** | 119.84 ms *(0.14 ms without encoding)* | 22.39 ms *(Joint architecture)* | 73.91 ms *(2.33 ms without encoding)* |

### Interpretation
In this scenario, SBERT correctly identifies that "Buy the best faucet" is highly relevant to the topic of a leaking faucet, ranking it #1. However, if this context is passed to an autonomous agent, it introduces topical noise rather than a solution. 

By applying an asymmetric $N \times N$ pass, Scout actively lowered the score of the Amazon link to `0.5356`, prioritizing the imperative physical actions ("Tighten", "Turn off") at `0.95+`. It acts as a routing filter to ensure agents retrieve the mechanical next step rather than conversational or commercial noise. Scout ignores simple keyword overlap to evaluate the logical utility between sentences. It identifies when Sentence B provides a functional next step, cause, or resolution for Sentence A, even if they share no common vocabulary.

## How it works

Scout processes **batches of sentences** and outputs an **N×N relevance matrix** in a single forward pass over pre-computed embeddings.

**Key architecture differences:**
1. **No positional encoding:** Sentence order shouldn't affect pairwise relevance in a retrieval setting.
2. **Asymmetric Projections:** Uses separate $W_Q$ (Need) and $W_K$ (Resolution) matrices to map directional logic.
3. **Sigmoid attention:** Output is calculated via Sigmoid instead of Softmax, allowing relationships to be independent rather than competitive.

## Installation

Requires Python 3.9+
```bash
uv sync
```

## Download the Model

Download the checkpoint from [Hugging Face](https://huggingface.co/your-model-link) and place it at:
```
scout/
└── checkpoints/
    └── scout_best.pt
```

## Usage

See [`example.py`](example.py) for a full working demo.

## A Note on What This Actually Is

This is an architecture experiment, not a production retrieval system.

The benchmark here is one hand-crafted test case designed to illustrate 
the concept — not a rigorous evaluation. The model is trained on ~4,500 
synthetic sentence pairs, which is small. I don't yet know how well it 
generalises to arbitrary domains and text styles.

The real question I'm exploring is: can attention mechanics be trained to 
encode functional utility between sentences rather than just contextual 
compatibility? Early results suggest yes, but this is still an open 
question with limited evidence.

Treat it as an interesting primitive worth experimenting with — not a 
drop-in replacement for established retrieval methods. If you find cases 
where it works well or breaks badly, I want to know.

## Applications
These are some applications where I think scout would be helpful

- Search: Given query A's row, the highest-scoring B is my answer
- Clustering: Find groups where sentences mutually attend to each other
- Topic detection: Track when attention patterns shift across a document
- Asymmetry analysis: Measure whether A→B ≠ B→A

## Current Status

The model is currently in active testing. 
* **Training Data:** Trained on diverse synthetic directional datasets (e.g., troubleshooting chains, conversational adjacency pairs, and epistemic scaffolding), alongside cross-domain negatives.
* **Validation Goal:** Testing whether sequence-level attention mechanics can reliably learn functional relevance without token-level supervision.
* **Application:** Early RAG benchmarks indicate the model functions well as an $O(1)$ semantic filter to suppress topical noise and isolate actionable steps in agentic workflows.
