from pydantic import BaseModel, Field
from typing import List, Optional

class AsymmetricForwardScores(BaseModel):
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_two: float = Field(description="Score from sentence 1 to 2")


class AsymmetricBackwardScores(BaseModel):
    one_to_zero: float = Field(description="Score from sentence 1 to 0")
    two_to_one: float = Field(description="Score from sentence 2 to 1")
    two_to_zero: float = Field(description="Score from sentence 2 to 0")


class SymmetricBidirectionalScores(BaseModel):
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_zero: float = Field(description="Score from sentence 1 to 0")


class Scores(BaseModel):
    asymmetric_forward: AsymmetricForwardScores
    asymmetric_backward: AsymmetricBackwardScores
    symmetric_bidirectional: SymmetricBidirectionalScores


class SentenceChain(BaseModel):
    asymmetric: List[str] = Field(description="Ordered chain of asymmetric sentences")
    symmetric: List[str] = Field(description="Symmetric sentence pairs")
    hard_negatives: List[str] = Field(description="Hard negative sentences")
    scores: Scores