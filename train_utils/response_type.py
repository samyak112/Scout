from pydantic import BaseModel, Field
from typing import List, Optional

class Thread1InternalScores(BaseModel):
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_two: float = Field(description="Score from sentence 1 to 2")
    one_to_zero: float = Field(description="Score from sentence 1 to 0")
    two_to_one: float = Field(description="Score from sentence 2 to 1")
    zero_to_two: float = Field(description="Score from sentence 0 to 2")
    two_to_zero: float = Field(description="Score from sentence 2 to 0")


class Thread2InternalScores(BaseModel):
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_zero: float = Field(description="Score from sentence 1 to 0")


class CrossThreadAvgScores(BaseModel):
    thread1_to_thread2: float = Field(description="Average score from any thread1 sentence to any thread2 sentence")
    thread2_to_thread1: float = Field(description="Average score from any thread2 sentence to any thread1 sentence")


class Scores(BaseModel):
    thread1_internal: Thread1InternalScores
    thread2_internal: Thread2InternalScores
    cross_thread_avg: CrossThreadAvgScores

class SentenceChain(BaseModel):
    asymmetric: List[str] = Field(description="Ordered chain of asymmetric sentences")
    symmetric: List[str] = Field(description="Symmetric sentence pairs")
    hard_negatives: List[str] = Field(description="Hard negative sentences")
    scores: Scores