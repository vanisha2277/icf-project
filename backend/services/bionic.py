"""
Accessibility rationale:
Bionic reading bolds the leading letters of words to create visual anchors that
help guide eye movement and reduce tracking errors for readers who lose their place.
This supports readers with dyslexia and related difficulties by highlighting
where to begin decoding each word and reducing visual search time.
"""

import math
import re
from typing import Callable


_WORD_RE = re.compile(r"([A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*)")


def _bold_chunk(word: str, ratio: float) -> str:
    """Return the word with the first ceil(len*ratio) characters wrapped in <b>.

    Rules:
    - Always bold at least one character for non-empty words.
    - ratio should be between 0 and 1; values outside are clamped.
    """
    if not word:
        return word
    ratio = max(0.0, min(1.0, float(ratio)))
    cut = max(1, math.ceil(len(word) * ratio))
    return f"<b>{word[:cut]}</b>{word[cut:]}"


def bionic_html(text: str, ratio: float = 0.45, word_pattern: re.Pattern = _WORD_RE) -> str:
    """Transform plain text into HTML where the front portion of each word is bolded.

    - text: input string
    - ratio: fraction of each word to bold (default 0.45 ~ 40-45%)

    This function is deterministic and uses regex-based word detection to avoid
    calling external services. It preserves whitespace and punctuation outside
    of matched word tokens.
    """

    def _replacer(m: re.Match) -> str:
        w = m.group(0)
        return _bold_chunk(w, ratio)

    return word_pattern.sub(_replacer, text)
