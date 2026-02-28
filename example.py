import torch
from beir import util, LoggingHandler
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval
from beir.retrieval.search.dense import DenseRetrievalExactSearch as DRES
from beir.retrieval import models
from typing import List, Dict
import numpy as np
from inference import ScoutInference  # adjust import to your module

# ------------------------------------------------------------
# 1. Wrap Scout as a BEIR compatible model
# ------------------------------------------------------------
class ScoutBEIRModel:
    def __init__(self, scout_inference: ScoutInference, batch_size: int = 128):
        self.scout = scout_inference
        self.batch_size = batch_size

    def encode_queries(self, queries: List[str], **kwargs) -> np.ndarray:
        # Not needed for a cross‑encoder style re‑ranker – we'll use score() directly.
        raise NotImplementedError

    def encode_corpus(self, corpus: List[Dict[str, str]], **kwargs) -> np.ndarray:
        raise NotImplementedError

    def score(self, query: str, passages: List[str]) -> List[float]:
        """
        Return Scout scores for query → each passage.
        """
        # Use rank(compete=False) to get only Scout scores
        result = self.scout.rank(query, passages, compete=False)
        return result.scores  # already list of floats


# ------------------------------------------------------------
# 2. Wrap SBERT as a BEIR model (dense retriever style)
# ------------------------------------------------------------
class SBERTModel:
    def __init__(self, model_name: str = "sentence-transformers/all-mpnet-base-v2"):
        self.model = models.SentenceBERT(model_name)
        self.q_model = self.model
        self.doc_model = self.model

    def encode_queries(self, queries: List[str], **kwargs) -> np.ndarray:
        return self.model.encode_queries(queries)

    def encode_corpus(self, corpus: List[Dict[str, str]], **kwargs) -> np.ndarray:
        return self.model.encode_corpus(corpus)


# ------------------------------------------------------------
# 3. Wrap Cross‑Encoder (using the same one as in ScoutInference)
# ------------------------------------------------------------
from sentence_transformers import CrossEncoder

class CrossEncoderModel:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def score(self, query: str, passages: List[str]) -> List[float]:
        pairs = [[query, p] for p in passages]
        scores = self.model.predict(pairs, convert_to_tensor=True)
        return torch.sigmoid(scores).tolist()


# ------------------------------------------------------------
# 4. Main evaluation function
# ------------------------------------------------------------
def evaluate_on_msmarco(scout_inference: ScoutInference):
    import logging
    logging.basicConfig(level=logging.INFO)

    # Download and load MS MARCO passage dev set
    url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/msmarco.zip"
    data_path = util.download_and_unzip(url, "datasets")
    corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split="dev")

    # Use BM25 to get top‑1000 candidates for each query
    from beir.retrieval.search.lexical import BM25Search
    bm25 = BM25Search(index_name="msmarco", hostname="localhost", initialize=True)
    retriever = EvaluateRetrieval(bm25, k_values=[1000])
    results = retriever.retrieve(corpus, queries)

    # Prepare data structures for evaluation
    def evaluate_model(name, scorer):
        """
        scorer : callable with signature (query: str, passages: List[str]) -> List[float]
        Returns dict with metrics.
        """
        all_scores = {}
        for qid, query_text in queries.items():
            # Get candidate doc ids from BM25
            candidate_docs = list(results[qid].keys())
            if not candidate_docs:
                continue
            # Fetch passage texts
            passage_texts = [corpus[doc_id]["text"] for doc_id in candidate_docs]
            # Compute scores
            scores = scorer(query_text, passage_texts)
            # Store scores in BEIR format: {qid: {doc_id: score}}
            all_scores[qid] = {doc_id: score for doc_id, score in zip(candidate_docs, scores)}

        # Evaluate using BEIR's evaluator
        evaluator = EvaluateRetrieval()
        metrics = evaluator.evaluate(qrels, all_scores, [1, 10, 100, 1000])
        print(f"\n=== {name} ===")
        print(metrics)
        return metrics

    # Run evaluations
    # Scout
    scout_scorer = lambda q, ps: scout_inference.rank(q, ps, compete=False).scores
    evaluate_model("Scout", scout_scorer)

    # SBERT (dense retrieval) – we need to encode all corpus? Too slow for full corpus.
    # Instead we can re‑rank the BM25 candidates using SBERT cosine similarity.
    sbert_model = SBERTModel()
    def sbert_scorer(q, ps):
        # Encode query and passages in batches
        q_emb = sbert_model.encode_queries([q])[0]
        p_embs = sbert_model.encode_corpus([{"text": p} for p in ps])
        scores = np.dot(p_embs, q_emb).tolist()
        return scores
    evaluate_model("SBERT", sbert_scorer)

    # Cross‑encoder (already used in ScoutInference, but we use the same model)
    ce_model = CrossEncoderModel()
    ce_scorer = lambda q, ps: ce_model.score(q, ps)
    evaluate_model("CrossEncoder", ce_scorer)


if __name__ == "__main__":
    # Initialise ScoutInference (adjust checkpoint path as needed)
    scout = ScoutInference(
        checkpoint_path=None,          # downloads from HF if not local
        encoder="sentence-transformers/all-mpnet-base-v2",
        temperature=0.5,
    )
    evaluate_on_msmarco(scout)