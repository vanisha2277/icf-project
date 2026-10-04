# ICF 2026 AI disclosure: built with AI assistance.
"""Generate → Measure → Verify → Fidelity-check simplification pipeline.

Readability numbers always come from textstat. Accommodation rationales always
come from the curated lookup table, not from the model.
"""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Optional

from backend.services.accommodation_knowledge import Strategy, strategies_for
from backend.services.ai_client import AICallError, AIClient
from backend.services.readability import measure_readability

MEANINGFUL_GRADE_DROP = 0.5
MAX_REFINEMENT_PASSES = 2


def _format_strategies(strategies: List[Strategy]) -> str:
    lines = []
    for item in strategies:
        lines.append(f"- {item['strategy']}: {item['rationale']}")
    return "\n".join(lines)


def _generation_system_prompt(profile: str, strategies: List[Strategy]) -> str:
    return (
        "You rewrite educational text so it is easier to read for the named "
        "learner profile. Follow ONLY the retrieved accommodation strategies "
        "below. Do not invent extra accessibility claims.\n\n"
        f"Learner profile: {profile}\n"
        "Retrieved strategies (curated lookup, not model memory):\n"
        f"{_format_strategies(strategies)}\n\n"
        "Rules:\n"
        "- Preserve every factual claim, number, name, and causal relationship.\n"
        "- Do not add new facts.\n"
        "- Return only the rewritten passage. No preamble or bullets about your process."
    )


def _refinement_user_prompt(
    original: str,
    current: str,
    current_grade: float,
    target: Optional[float],
) -> str:
    if target is not None:
        gap = (
            f"The current rewrite is Flesch–Kincaid grade {current_grade:.1f}. "
            f"The target grade is {target:.1f}. Simplify further until it meets "
            f"that target, without dropping facts."
        )
    else:
        gap = (
            f"The current rewrite is Flesch–Kincaid grade {current_grade:.1f}. "
            "It is not meaningfully easier than the original. Simplify further "
            "with shorter sentences and more common words, without dropping facts."
        )
    return (
        f"{gap}\n\nOriginal:\n{original}\n\nCurrent rewrite:\n{current}\n\n"
        "Return only the improved rewrite."
    )


def _fidelity_system_prompt() -> str:
    return (
        "You compare an original educational passage with a simplified rewrite. "
        "Decide whether every factual claim was preserved. Respond with JSON only, "
        'no markdown, shape: {"facts_preserved": true or false, '
        '"dropped_information": ["..."]}. '
        "List concrete facts, numbers, or relationships that were lost or changed. "
        "If nothing was lost, use an empty list."
    )


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


def parse_fidelity_payload(raw: str) -> Dict[str, Any]:
    data = _extract_json_object(raw)
    preserved = bool(data.get("facts_preserved"))
    dropped = data.get("dropped_information") or []
    if not isinstance(dropped, list):
        dropped = [str(dropped)]
    return {
        "facts_preserved": preserved,
        "dropped_information": [str(item) for item in dropped],
    }


def needs_refinement(
    original_grade: float,
    simplified_grade: float,
    target_grade_level: Optional[float],
) -> bool:
    if original_grade <= 0:
        return False
    if target_grade_level is not None:
        if original_grade <= target_grade_level:
            return False
        return simplified_grade > target_grade_level
    return simplified_grade > original_grade - MEANINGFUL_GRADE_DROP


def run_simplify_pipeline(
    text: str,
    profile: str,
    client: AIClient,
    target_grade_level: Optional[float] = None,
) -> Dict[str, Any]:
    strategies = strategies_for(profile)
    original_metrics = measure_readability(text)

    simplified = client.complete(
        system=_generation_system_prompt(profile, strategies),
        user=f"Rewrite this passage:\n\n{text}",
    )
    simplified_metrics = measure_readability(simplified)

    refinement_passes = 0
    skipped_notes: List[str] = []

    while (
        refinement_passes < MAX_REFINEMENT_PASSES
        and needs_refinement(
            original_metrics["flesch_kincaid_grade"],
            simplified_metrics["flesch_kincaid_grade"],
            target_grade_level,
        )
    ):
        try:
            simplified = client.complete(
                system=_generation_system_prompt(profile, strategies),
                user=_refinement_user_prompt(
                    text,
                    simplified,
                    simplified_metrics["flesch_kincaid_grade"],
                    target_grade_level,
                ),
            )
            simplified_metrics = measure_readability(simplified)
            refinement_passes += 1
        except AICallError as exc:
            skipped_notes.append(f"refinement skipped: {exc}")
            break

    fidelity_check = {
        "facts_preserved": None,
        "dropped_information": [],
    }
    try:
        fidelity_raw = client.complete(
            system=_fidelity_system_prompt(),
            user=f"Original:\n{text}\n\nSimplified:\n{simplified}",
            max_tokens=512,
        )
        fidelity_check = parse_fidelity_payload(fidelity_raw)
    except (AICallError, json.JSONDecodeError, TypeError, ValueError) as exc:
        skipped_notes.append(f"fidelity check skipped: {exc}")

    return {
        "simplified": simplified,
        "original_metrics": original_metrics,
        "simplified_metrics": simplified_metrics,
        "refinement_passes": refinement_passes,
        "fidelity_check": fidelity_check,
        "strategies_applied": strategies,
        "verification_skipped": bool(skipped_notes),
        "verification_notes": "; ".join(skipped_notes) if skipped_notes else None,
    }
