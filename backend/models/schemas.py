from pydantic import BaseModel
from typing import List, Optional


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
