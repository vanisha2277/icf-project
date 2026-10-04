# ICF 2026 AI disclosure: built with AI assistance.
from fastapi.testclient import TestClient

from backend.main import app
from backend.routers.simplify import get_ai_client
from backend.services.define_word import reset_definition_cache
from backend.tests.test_simplify import ScriptedClient


def setup_function():
    reset_definition_cache()
    app.dependency_overrides.clear()


def teardown_function():
    app.dependency_overrides.clear()
    reset_definition_cache()


def test_define_word_uses_context_and_cache():
    client = ScriptedClient(
        [
            '{"definition": "Green pigment that catches light.", "example_sentence": "Chlorophyll in the leaf catches sunlight."}',
        ]
    )
    app.dependency_overrides[get_ai_client] = lambda: client
    http = TestClient(app)
    payload = {
        "word": "chlorophyll",
        "surrounding_sentence": "Plants absorb light using chlorophyll.",
        "profile": "esl",
    }
    first = http.post("/define-word", json=payload)
    second = http.post("/define-word", json=payload)

    assert first.status_code == 200
    assert first.json()["cached"] is False
    assert "pigment" in first.json()["definition"].lower()
    assert second.status_code == 200
    assert second.json()["cached"] is True
    assert second.json()["definition"] == first.json()["definition"]
    assert len(client.calls) == 1
    assert "chlorophyll" in client.calls[0]["user"]
    assert "esl" in client.calls[0]["user"].lower() or "esl" in client.calls[0]["system"].lower()


def test_define_word_requires_sentence():
    app.dependency_overrides[get_ai_client] = lambda: ScriptedClient([])
    response = TestClient(app).post(
        "/define-word",
        json={"word": "cell", "surrounding_sentence": "", "profile": "dyslexia"},
    )
    assert response.status_code == 400
