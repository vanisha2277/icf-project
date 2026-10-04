# ICF 2026 AI disclosure: built with AI assistance.
"""Deterministic readability metrics.

These scores come from established formulas (Flesch–Kincaid, Flesch Reading
Ease, Dale–Chall), not from an AI model. That keeps measurement fast, stable
for demos, and independent of the generator we are checking.
"""
from typing import Dict

import textstat


ReadabilityScores = Dict[str, float]


def measure_readability(text: str) -> ReadabilityScores:
    """Return standard readability metrics for `text`.

    Empty or whitespace-only input returns zeros so callers never have to
    special-case textstat exceptions during a live demo.
    """
    cleaned = (text or "").strip()
    if not cleaned:
        return {
            "flesch_kincaid_grade": 0.0,
            "flesch_reading_ease": 0.0,
            "dale_chall_score": 0.0,
            "avg_sentence_length": 0.0,
            "avg_syllables_per_word": 0.0,
        }

    return {
        "flesch_kincaid_grade": float(textstat.flesch_kincaid_grade(cleaned)),
        "flesch_reading_ease": float(textstat.flesch_reading_ease(cleaned)),
        "dale_chall_score": float(textstat.dale_chall_readability_score(cleaned)),
        # words_per_sentence is the current textstat name for mean sentence length.
        "avg_sentence_length": float(textstat.words_per_sentence(cleaned)),
        "avg_syllables_per_word": float(textstat.avg_syllables_per_word(cleaned)),
    }
