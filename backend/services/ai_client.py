"""Provider-agnostic AI client wrapper.

This small wrapper reads configuration from environment variables and exposes
one method used by the service: generate_word_timings(text). Implementations
for real providers can be added later. For the hackathon MVP this file simply
provides a structured place to add provider calls later.
"""
import os
import typing
from typing import Optional, List, Dict


class AIClient:
    """Minimal provider-agnostic client.

    For now this class is a thin stub. Use AIClient.from_env() to construct a
    client if provider and API key are present. The concrete generate_word_timings
    should call the configured provider and return a list of {word, start_ms, end_ms}.
    """

    def __init__(self, provider: str, api_key: str):
        self.provider = provider
        self.api_key = api_key

    @classmethod
    def from_env(cls) -> Optional["AIClient"]:
        provider = os.getenv("AI_PROVIDER")
        key = os.getenv("AI_API_KEY")
        if provider and key:
            return cls(provider.strip(), key.strip())
        return None

    def generate_word_timings(self, text: str) -> List[Dict[str, int]]:
        """Attempt to generate word timings using the configured provider.

        Raises an exception if the provider call fails. For the MVP this method
        is intentionally left as a NotImplementedError to avoid accidental
        network calls in tests. Implementations for specific providers should
        live behind this interface.
        """
        raise NotImplementedError("AI provider integration not implemented in MVP")
