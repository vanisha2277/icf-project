# ICF 2026 AI disclosure: built with AI assistance.
"""Anthropic-backed text completion used by simplify and define-word.

Word-level TTS timings still use the deterministic fallback in tts_timing.py.
This client is for generation and verification calls only.
"""
from __future__ import annotations

import os
from typing import Dict, List, Optional

from anthropic import Anthropic, APITimeoutError


DEFAULT_MODEL = "claude-haiku-4-5"
DEFAULT_TIMEOUT_SECONDS = 8.0


class AICallError(Exception):
    """Provider call failed (timeout, HTTP error, or empty response)."""


class AIClient:
    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_MODEL,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        provider: str = "anthropic",
    ):
        self.provider = provider
        self.api_key = api_key
        self.model = model
        self.timeout_seconds = timeout_seconds
        self._client = Anthropic(api_key=api_key, timeout=timeout_seconds)

    @classmethod
    def from_env(cls) -> Optional["AIClient"]:
        key = (os.getenv("ANTHROPIC_API_KEY") or os.getenv("AI_API_KEY") or "").strip()
        if not key:
            return None
        model = (os.getenv("ANTHROPIC_MODEL") or DEFAULT_MODEL).strip()
        return cls(api_key=key, model=model)

    def complete(self, system: str, user: str, max_tokens: int = 1024) -> str:
        """Return the model's text. Raises AICallError on timeout or failure."""
        try:
            message = self._client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                timeout=self.timeout_seconds,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
        except APITimeoutError as exc:
            raise AICallError("AI call timed out") from exc
        except Exception as exc:
            raise AICallError(f"AI call failed: {exc}") from exc

        parts = []
        for block in message.content:
            text = getattr(block, "text", None)
            if text:
                parts.append(text)
        combined = "".join(parts).strip()
        if not combined:
            raise AICallError("AI returned an empty response")
        return combined

    def generate_word_timings(self, text: str) -> List[Dict[str, int]]:
        """Not used for TTS in this MVP; timings stay deterministic."""
        raise NotImplementedError(
            "TTS timings use the synthetic fallback; this client is for text generation"
        )
