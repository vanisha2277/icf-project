import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


def test_transform_bionic_only():
    payload = {"text": "Hello world.", "options": {"bionic": True, "chunking": False, "tts_sync": False}}
    r = client.post("/transform", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "chunks" in data
    assert data["chunks"][0]["bionic_html"] is not None
    assert data["chunks"][0]["word_timings"] is None


def test_transform_chunking_only():
    text = "First sentence. Second sentence. Third sentence."
    payload = {"text": text, "options": {"bionic": False, "chunking": True, "tts_sync": False}}
    r = client.post("/transform", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert len(data["chunks"]) >= 2


def test_transform_both():
    text = "One. Two. Three. Four."
    payload = {"text": text, "options": {"bionic": True, "chunking": True, "tts_sync": False}}
    r = client.post("/transform", json=payload)
    assert r.status_code == 200
    data = r.json()
    for c in data["chunks"]:
        assert c["bionic_html"] is not None
