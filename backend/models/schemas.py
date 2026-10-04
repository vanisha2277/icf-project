from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class TransformOptions(BaseModel):
    bionic: bool = False
    chunking: bool = False
    tts_sync: bool = False


class TransformRequest(BaseModel):
    text: str
    options: TransformOptions


class WordTiming(BaseModel):
    word: str
    start_ms: int
    end_ms: int


class ChunkResponse(BaseModel):
    text: str
    bionic_html: Optional[str] = None
    word_timings: Optional[List[WordTiming]] = None


class TransformResponse(BaseModel):
    chunks: List[ChunkResponse]


LearnerProfile = Literal["dyslexia", "adhd", "esl", "dyscalculia"]


class ReadabilityMetrics(BaseModel):
    flesch_kincaid_grade: float
    flesch_reading_ease: float
    dale_chall_score: float
    avg_sentence_length: float
    avg_syllables_per_word: float


class StrategyApplied(BaseModel):
    strategy: str
    rationale: str


class FidelityCheck(BaseModel):
    facts_preserved: Optional[bool] = None
    dropped_information: List[str] = Field(default_factory=list)


class SimplifyRequest(BaseModel):
    text: str
    profile: LearnerProfile
    target_grade_level: Optional[float] = None


class SimplifyResponse(BaseModel):
    simplified: str
    original_metrics: ReadabilityMetrics
    simplified_metrics: ReadabilityMetrics
    refinement_passes: int
    fidelity_check: FidelityCheck
    strategies_applied: List[StrategyApplied]
    verification_skipped: bool = False
    verification_notes: Optional[str] = None


class DefineWordRequest(BaseModel):
    word: str
    surrounding_sentence: str
    profile: LearnerProfile


class DefineWordResponse(BaseModel):
    definition: str
    example_sentence: str
    cached: bool = False
