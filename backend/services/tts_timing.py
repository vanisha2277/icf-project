"""Generate word-level timing hints for TTS playback.

This module prefers AI-assisted timing when configured, but provides a
small deterministic fallback so the frontend can receive plausible timings
without any external calls (useful for demos/offline testing).
"""
import os
import typing
from typing import List, Dict, Optional

from . import ai_client


def _synthetic_timings(text: str) -> List[Dict[str, int]]:
    """Create simple, deterministic word timings (ms) from text.

    This fallback uses word length to proportionally assign durations and a
    short inter-word gap to approximate natural speech pacing. It is NOT
    replacement for a high-quality TTS timing model but is fine for demos.
    """
    import re

    words = re.findall(r"([A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*)|\S", text)
    # words may include None groups; normalize
    flat_words = [w for w in words if w and not w.isspace()]

    timings = []
    cursor = 0
    for w in flat_words:
        # duration base: 80ms + 40ms per character, with minimum
        duration = max(100, 40 * len(w) + 80)
        start = cursor
        end = start + duration
        timings.append({"word": w, "start_ms": start, "end_ms": end})
        cursor = end + 50  # small gap between words

    return timings


def generate_word_timings(text: str, use_ai: bool = True) -> List[Dict[str, int]]:
    """Return word timing hints for the given text.

    - If AI provider is configured and reachable, attempt AI-assisted timings via ai_client.
    - Otherwise fall back to deterministic synthetic timings.
    """
    # Attempt AI-assisted timing if available
    client = ai_client.AIClient.from_env()
    if use_ai and client is not None:
        try:
            ai_result = client.generate_word_timings(text)
            if ai_result:
                return ai_result
        except Exception:
            # Fail quietly to fallback for demo stability
            pass

    return _synthetic_timings(text)
