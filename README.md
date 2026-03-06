# Scout: Directional Information Gain Between Sentences

**Status:** Experimental | [Details in Issues](https://github.com/samyak112/Scout/issues/2)

## What is this?

Scout is an experimental attention model that slightly modifies the standard Transformer attention architecture to learn **directional relevance** between sentences. 

It treats sentences as tokens in a custom attention block and produces a full N×N matrix in a single forward pass where every cell [i][j] answers one question: "Given that I just read sentence i, does sentence j add functional value?"

**The Core Concept:**
- `"My faucet is leaking"` $\rightarrow$ `"Tighten the valve nut"` = **High Gain** (Actionable solution)
- `"Tighten the valve nut"` $\rightarrow$ `"My faucet is leaking"` = **Low Gain** (Reverse causality)
- `"My faucet is leaking"` $\rightarrow$ `"Buy the best faucet on Amazon"` = **Low Gain** (Topical match, but lacks immediate utility)
- BUT `"The valve nut is located under the handle at the base of the faucet"` makes sense for `"Tighten the valve nut"`

## The N×N Matrix

When you call `scout.matrix(sentences)` (check [example.py](https://github.com/samyak112/Scout/blob/main/example.py) for trying yourself), you get back a full N×N relevance matrix in around 2ms on cpu.

```python
sentences = [
    "This function queries the database inside a loop causing N+1 requests.", # S0
    "Move the query outside the loop and fetch all records in a single call.", # S1
    "Batching the queries reduced response time from 800ms to 12ms in testing.", # S2
    "The same N+1 pattern appears in the user profile endpoint as well.",     # S3
    "Database query optimization is a common topic in backend engineering.",  # S4 noise
    "Python was created by Guido van Rossum in 1991.",                        # S5 noise
]

matrix = scout.matrix(sentences)

# matrix[0][1] = 0.827  — problem → fix (high)
# matrix[1][2] = 0.835  — fix → result (high)
# matrix[1][0] = 0.151  — fix → problem (low, asymmetry works)
# matrix[0][3] = 0.330  — same pattern recognized across endpoints (moderate)
# matrix[4][0] = 0.000  — generic topic sentence (noise rejected)
# matrix[5][*] = 0.000  — Python history (completely irrelevant, zeroed)
```

This asymmetry can be useful for:
- **Retrieval (RAG):** Filtering out "semantic echoes" to find executable actions.
- **Clustering:** Grouping sentences by mutual information gain.
- **Segmentation:** Detecting when a procedural chain logically shifts.

## Can't I just fine-tune a standard Bi-Encoder or Cross-Encoder?

**Technically, yes, but hear me out.**

1. **Bi-Encoders (like SBERT) are stuck in "Similarity":** You can train them on all the directional data in the world, but the math is still symmetric ($A \cdot B = B \cdot A$). They can't tell the difference between "Cause $\rightarrow$ Effect" and "Effect $\rightarrow$ Cause" because they are built to measure distance, not flow.
    
2. **Cross-Encoders (like BERT) are "Slow":** They can handle the logic perfectly, but they have to evaluate pairs one-by-one. If you want to see how 50 sentences relate to each other, you have to run the model 2,500 times. That’s a massive compute tax.
   

**Scout:** The real goal with Scout was to see if we could just **rip out the attention mechanism** and use it as the scoring engine itself. By using asymmetric projections ($W_Q \neq W_K$), we get that directional "Cross-Encoder" logic but keep the speed of a Bi-Encoder.

The "power" here is that Scout gives you a full **$N \times N$ matrix** (a complete map of how every sentence relates to every other sentence) in one quick pass. It turns a "Search List" into a "Reasoning Graph" without making your CPU cry.

## Test: Agentic Troubleshooting

You can call `scout.rank` to rank a list of candidates against a query. See [`example.py`](example.py) to run it yourself.

**Query (Agent State):** *"My faucet is leaking heavily under the sink."*

| Rank | SBERT (Bi-Encoder) | Cross-Encoder (MS-MARCO) (After Sigmoid) | **Scout (Directional Gain)** |
| :--- | :--- | :--- | :--- |
| **1.** | `[0.4821]` Buy the best faucet here on amazon | `[0.0022]` Buy the best faucet here on amazon | `[0.9585]` **Tighten the main valve nut using a wrench.** |
| **2.** | `[0.4532]` Turn off the main water supply immediately. | `[0.0010]` Sinks are usually made of porcelain... | `[0.9388]` **Turn off the main water supply immediately.** |
| **3.** | `[0.3802]` Tighten the main valve nut using a wrench. | `[0.0001]` Turn off the main water supply... | `[0.5356]` Buy the best faucet here on amazon |
| **Time** | 119.84 ms *(0.14 ms without encoding)* | 22.39 ms *(Joint architecture)* | 73.91 ms *(2.33 ms without encoding)* |

In this scenario, SBERT correctly identifies that "Buy the best faucet" is highly relevant to the topic of a leaking faucet, ranking it #1. However, if this context is passed to an autonomous agent, it introduces topical noise rather than a solution. 

By applying an asymmetric $N \times N$ pass, Scout actively lowered the score of the Amazon link to `0.5356`, prioritizing the imperative physical actions ("Tighten", "Turn off") at `0.95+`. It acts as a routing filter to ensure agents retrieve the mechanical next step rather than conversational or commercial noise. Scout ignores simple keyword overlap to evaluate the logical utility between sentences. It identifies when Sentence B provides a functional next step, cause, or resolution for Sentence A, even if they share no common vocabulary.

## How it works

Scout processes **batches of sentences** and outputs an **N×N relevance matrix** in a single forward pass over pre-computed embeddings.

**Key architecture differences:**
- **No positional encoding** sentence order doesn't affect pairwise 
  relevance. Embeddings are passed directly without position signals.

- **Sigmoid attention with dynamic normalization** sigmoid is used 
  instead of softmax so each cell [i][j] is scored independently between 
  0 and 1, rather than competing with other candidates in the same row. 

- **Multi-layer score aggregation** raw attention scores from each 
  layer are processed separately through a small Conv2d network, then 
  combined using learnable softmax weights. The model learns which layers 
  capture the most useful directional signal rather than averaging across 
  all layers equally.

## Installation

Requires Python 3.9+
```bash
uv sync
python3 example.py
```

The model will be downloaded automatically from Hugging Face on first run.

## A Note on What This Actually Is

This is an architecture experiment, not a production retrieval system.

Scout currently doesn't work on every sort of functional relevance test right now, but it can be trained on those. My current assumption is that the tiny training set (8500 arrays) is the bottleneck, but I'm excited to see where the architecture itself might hit a wall. If it misses a specific kind of reasoning even with good data, that’s where the experiment gets interesting.


The real question I'm exploring is: can attention mechanics be trained to 
encode functional utility between sentences rather than just contextual 
compatibility? Early results suggest yes, but this is still an open 
question with limited evidence.

Treat it as an interesting primitive worth experimenting with not a 
drop-in replacement for established retrieval methods. If you find cases 
where it works well or breaks badly, I want to know.

One thing i have noticed is that Scout doesnt works fine when there are only 2-3 sentences because the results are coming directly from attention's qk mechanism so i suspect that when there are less sentences there is not much to attend to and thats when this happens

## Current Status

The model is currently in active testing. 
* **Training Data:** Trained on diverse synthetic directional datasets (e.g., troubleshooting chains, conversational adjacency pairs, and epistemic scaffolding), alongside cross-domain negatives.
* **Validation Goal:** Testing whether sequence-level attention mechanics can reliably learn functional relevance without token-level supervision.
* **Application:** Early RAG benchmarks indicate the model functions well as an $O(1)$ semantic filter to suppress topical noise and isolate actionable steps in agentic workflows.










