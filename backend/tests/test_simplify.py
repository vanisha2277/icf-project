# ICF 2026 AI disclosure: built with AI assistance.
"""Mocked pipeline tests — no live Anthropic key required."""
from fastapi.testclient import TestClient

from backend.main import app
from backend.routers.simplify import get_ai_client
from backend.services.ai_client import AICallError
from backend.services.simplify_pipeline import needs_refinement, parse_fidelity_payload

HARD = (
    "Photosynthetic phosphorylation in photoautotrophic eukaryotes necessitates "
    "the coordinated translocation of protons across thylakoid membranes, thereby "
    "establishing an electrochemical gradient whose dissipation is obligatorily "
    "coupled to ATP synthase activity under physiologically constrained conditions."
)

EASY = (
    "Plants use sunlight to make energy. They move tiny charged particles across "
    "a membrane in the leaf. That movement helps the plant make ATP, which is "
    "a fuel molecule. This happens under normal living conditions."
)


class ScriptedClient:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    def complete(self, system: str, user: str, max_tokens: int = 1024) -> str:
        self.calls.append({"system": system, "user": user, "max_tokens": max_tokens})
        if not self.replies:
            raise AICallError("no scripted reply left")
        item = self.replies.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


def test_needs_refinement_target_and_drop():
    assert needs_refinement(10.0, 9.8, None) is True
    assert needs_refinement(10.0, 8.0, None) is False
    assert needs_refinement(10.0, 7.0, 6.0) is True
    assert needs_refinement(10.0, 5.5, 6.0) is False
    assert needs_refinement(5.0, 5.0, 6.0) is False


def test_parse_fidelity_payload_from_fenced_json():
    raw = '```json\n{"facts_preserved": false, "dropped_information": ["ATP"]}\n```'
    parsed = parse_fidelity_payload(raw)
    assert parsed["facts_preserved"] is False
    assert parsed["dropped_information"] == ["ATP"]


def test_simplify_generate_measure_verify_fidelity(monkeypatch):
    client = ScriptedClient(
        [
            HARD,  # generate: still hard, should trigger refinement
            EASY,  # refinement
            '{"facts_preserved": true, "dropped_information": []}',
        ]
    )
    app.dependency_overrides[get_ai_client] = lambda: client
    try:
        response = TestClient(app).post(
            "/simplify",
            json={"text": HARD, "profile": "dyslexia", "target_grade_level": 8.0},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["simplified"] == EASY
    assert data["refinement_passes"] == 1
    assert data["verification_skipped"] is False
    assert data["fidelity_check"]["facts_preserved"] is True
    assert data["strategies_applied"]
    assert all("rationale" in item for item in data["strategies_applied"])
    assert "dyslexia" in client.calls[0]["system"].lower() or "Retrieved strategies" in client.calls[0]["system"]
    assert data["original_metrics"]["flesch_kincaid_grade"] > data["simplified_metrics"]["flesch_kincaid_grade"]


def test_simplify_skips_refinement_on_timeout_but_returns_generate():
    client = ScriptedClient(
        [
            EASY,
            AICallError("AI call timed out"),
        ]
    )
    app.dependency_overrides[get_ai_client] = lambda: client
    try:
        # Easy generate still may or may not need refinement depending on scores.
        # Force a miss by returning HARD first then timeout on refine... use HARD.
        client.replies = [HARD, AICallError("AI call timed out")]
        response = TestClient(app).post(
            "/simplify",
            json={"text": HARD, "profile": "adhd", "target_grade_level": 6.0},
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["simplified"] == HARD
    assert data["refinement_passes"] == 0
    assert data["verification_skipped"] is True
    assert "refinement skipped" in data["verification_notes"]
    assert data["fidelity_check"]["facts_preserved"] is None


def test_simplify_requires_text():
    app.dependency_overrides[get_ai_client] = lambda: ScriptedClient([])
    try:
        response = TestClient(app).post(
            "/simplify",
            json={"text": "  ", "profile": "esl"},
        )
    finally:
        app.dependency_overrides.clear()
    assert response.status_code == 400


def test_simplify_unknown_profile_rejected():
    app.dependency_overrides[get_ai_client] = lambda: ScriptedClient([])
    try:
        response = TestClient(app).post(
            "/simplify",
            json={"text": "Hello there.", "profile": "telepathy"},
        )
    finally:
        app.dependency_overrides.clear()
    assert response.status_code == 422
