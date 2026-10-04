import pytest

from backend.services.accommodation_knowledge import (
    PROFILES,
    strategies_for,
)


def test_all_profiles_have_named_sources():
    for profile in PROFILES:
        entries = strategies_for(profile)
        assert len(entries) >= 3
        for item in entries:
            assert item["strategy"]
            assert item["rationale"]
            rationale = item["rationale"].lower()
            assert any(
                marker in rationale
                for marker in (
                    "ida",
                    "international dyslexia",
                    "british dyslexia",
                    "bda",
                    "udl",
                    "cast",
                    "chadd",
                    "cdc",
                    "wida",
                    "tesol",
                    "siop",
                    "nation",
                    "cummins",
                    "nctm",
                    "geary",
                )
            )


def test_unknown_profile_raises():
    with pytest.raises(KeyError):
        strategies_for("not-a-profile")
