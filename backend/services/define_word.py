# ICF 2026 AI disclosure: built with AI assistance.
"""Context-aware word definitions with a small in-memory cache."""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Dict

from backend.services.accommodation_knowledge import strategies_for
from backend.services.ai_client import AIClient

_CACHE: Dict[str, Dict[str, str]] = {}
_CACHE_LIMIT = 256


def cache_key(word: str, profile: str, surrounding_sentence: str) -> str:
    sentence_hash = hashlib.sha256(
        (surrounding_sentence or "").strip().encode("utf-8")
    ).hexdigest()[:16]
    return f"{word.strip().lower()}|{profile.strip().lower()}|{sentence_hash}"


def reset_definition_cache() -> None:
    _CACHE.clear()


def is_cached(word: str, profile: str, surrounding_sentence: str) -> bool:
    return cache_key(word, profile, surrounding_sentence) in _CACHE


def _extract_json_object(raw: str) -> Dict[str, Any]:
    cleaned = raw.strip()
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", cleaned, re.DOTALL)
    if fenced:
        cleaned = fenced.group(1)
    else:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start != -1 and end != -1 and end > start:
            cleaned = cleaned[start : end + 1]
    return json.loads(cleaned)


def parse_definition_payload(raw: str) -> Dict[str, str]:
    data = _extract_json_object(raw)
    definition = str(data.get("definition") or "").strip()
    example = str(data.get("example_sentence") or "").strip()
    if not definition:
        raise ValueError("definition missing from model response")
    return {
        "definition": definition,
        "example_sentence": example,
    }


def define_word(
    word: str,
    surrounding_sentence: str,
    profile: str,
    client: AIClient,
) -> Dict[str, str]:
    strategies = strategies_for(profile)
    key = cache_key(word, profile, surrounding_sentence)
    cached = _CACHE.get(key)
    if cached is not None:
        return cached

    strategy_lines = "\n".join(
        f"- {item['strategy']}: {item['rationale']}" for item in strategies
    )
    system = (
        "You explain one word as it is used in the given sentence. Match the "
        "definition complexity to the learner profile using these retrieved "
        "strategies:\n"
        f"{strategy_lines}\n\n"
        "Keep the meaning accurate to this sentence, not a generic dictionary "
        "entry if the context is specific. Respond with JSON only: "
        '{"definition": "...", "example_sentence": "..."}.'
    )
    user = (
        f"Word: {word}\n"
        f"Profile: {profile}\n"
        f"Sentence: {surrounding_sentence}"
    )
    payload = parse_definition_payload(client.complete(system=system, user=user, max_tokens=400))

    if len(_CACHE) >= _CACHE_LIMIT:
        _CACHE.pop(next(iter(_CACHE)))
    _CACHE[key] = payload
    return payload
