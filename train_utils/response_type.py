from pydantic import BaseModel, Field
from typing import List, Optional

from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class ChainInternalScores(BaseModel):  # for 3-sentence chains
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_two: float = Field(description="Score from sentence 1 to 2")
    one_to_zero: float = Field(description="Score from sentence 1 to 0")
    two_to_one: float = Field(description="Score from sentence 2 to 1")
    zero_to_two: float = Field(description="Score from sentence 0 to 2")
    two_to_zero: float = Field(description="Score from sentence 2 to 0")

class PairInternalScores(BaseModel):  # for 2-sentence bidirectional pairs
    zero_to_one: float = Field(description="Score from sentence 0 to 1")
    one_to_zero: float = Field(description="Score from sentence 1 to 0")

class CrossThreadAvgScores(BaseModel):
    thread1_to_thread2: Optional[float] = Field(default=0.0)
    thread2_to_thread1: Optional[float] = Field(default=0.0)
    thread1_to_thread3: Optional[float] = Field(default=0.0)
    thread3_to_thread1: Optional[float] = Field(default=0.0)
    thread1_to_thread4: Optional[float] = Field(default=0.0)
    thread4_to_thread1: Optional[float] = Field(default=0.0)
    thread2_to_thread3: Optional[float] = Field(default=0.0)
    thread3_to_thread2: Optional[float] = Field(default=0.0)
    thread2_to_thread4: Optional[float] = Field(default=0.0)
    thread4_to_thread2: Optional[float] = Field(default=0.0)
    thread3_to_thread4: Optional[float] = Field(default=0.0)
    thread4_to_thread3: Optional[float] = Field(default=0.0)

class Scores(BaseModel):
    thread1_internal: ChainInternalScores           # always present — at least one chain
    thread2_internal: Optional[ChainInternalScores] = None  # second chain if exists
    thread3_internal: Optional[PairInternalScores] = None   # first pair if exists
    thread4_internal: Optional[PairInternalScores] = None   # second pair if exists
    cross_thread_avg: CrossThreadAvgScores

class SentenceChain(BaseModel):
    sentences: Dict[str, List[str]] = Field(
        description="Keys: thread1, thread2 (chains), thread3, thread4 (pairs), hard_negatives"
    )
    scores: Scores