ICF Project - Reading Mode Backend

This backend provides deterministic text transformations for the ICF Project Chrome
extension (reading mode MVP).

Features
- Bionic reading (bold leading letters of words)
- Paragraph chunking (split long paragraphs into short, sentence-based chunks)
- Word-level TTS timing hints (AI-assisted if configured; falls back to a deterministic generator)

Quickstart
1. Create a Python 3.11+ virtual environment and activate it:
   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Create a local .env (optional) from .env.example and add AI_PROVIDER/AI_API_KEY if you plan to enable AI features.

4. Run the app locally using uvicorn:
   uvicorn backend.main:app --reload

Tests
- Run unit tests with pytest from the repository root:
  pytest backend/tests

Environment variables
- AI_PROVIDER: optional provider name (e.g., claude, gemini)
- AI_API_KEY: optional API key for provider

Notes for judges
- Bionic reading and chunking are pure, deterministic functions (no external calls).
- The AI integration point is isolated behind services/ai_client.py and services/tts_timing.py.
- See tests in backend/tests for usage examples and edge-case coverage.
