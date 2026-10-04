# ICF 2026 AI disclosure: built with AI assistance.
"""Live Anthropic smoke test. Skipped unless ANTHROPIC_API_KEY is set."""
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from backend.main import app
from backend.services.ai_client import AIClient

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

HARD = (
    "Photosynthetic phosphorylation in photoautotrophic eukaryotes necessitates "
    "the coordinated translocation of protons across thylakoid membranes."
)


@pytest.mark.skipif(
    AIClient.from_env() is None and not os.getenv("ANTHROPIC_API_KEY"),
    reason="ANTHROPIC_API_KEY not set; skipping live pipeline check",
)
def test_live_simplify_pipeline_lowers_grade_or_reports_skip():
    client = TestClient(app)
    response = client.post(
        "/simplify",
        json={"text": HARD, "profile": "dyslexia", "target_grade_level": 8.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["simplified"].strip()
    assert "flesch_kincaid_grade" in data["original_metrics"]
    assert data["strategies_applied"]
    if not data["verification_skipped"]:
        assert data["simplified_metrics"]["flesch_kincaid_grade"] <= data["original_metrics"]["flesch_kincaid_grade"]
