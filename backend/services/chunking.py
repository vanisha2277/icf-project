"""
Accessibility rationale:
Chunking long paragraphs into shorter blocks reduces working-memory load and
makes long passages easier to parse for readers with attention and processing
differences (ADHD, auditory processing differences). Shorter chunks improve
comprehension by allowing the reader to focus on a small number of sentences
before moving on.
"""

import re
from typing import List


_SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')


def split_into_sentences(paragraph: str) -> List[str]:
    """Split a paragraph into sentences using punctuation-based heuristics.

    This is intentionally simple (no NLP dependency) and aims for good-enough
    sentence boundaries for typical web text. It preserves trailing punctuation
    on sentences.
    """
    if not paragraph:
        return []
    sentences = [s.strip() for s in _SENTENCE_SPLIT_RE.split(paragraph) if s.strip()]
    return sentences


def chunk_paragraph(paragraph: str, max_sentences: int = 2) -> List[str]:
    """Break a paragraph into smaller chunks at natural sentence boundaries.

    - paragraph: input paragraph string
    - max_sentences: number of sentences per chunk (default 2)

    Returns a list of chunk strings. Sentences are grouped in-order; the last
    chunk may contain fewer than max_sentences.
    """
    if not paragraph:
        return []
    sentences = split_into_sentences(paragraph)
    if not sentences:
        return [paragraph.strip()]

    chunks = []
    current = []
    for s in sentences:
        current.append(s)
        if len(current) >= max_sentences:
            chunks.append(" ".join(current).strip())
            current = []

    if current:
        chunks.append(" ".join(current).strip())

    return chunks
