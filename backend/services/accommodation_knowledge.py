# ICF 2026 AI disclosure: built with AI assistance.
"""Curated accommodation strategies for retrieval-grounded prompting.

This is a small lookup table, not embeddings or a vector database. The
simplify pipeline retrieves the list for a learner profile and puts those
strategy + rationale strings into the system prompt so the model is working
from named guidance rather than inventing what "helps dyslexia."
"""
from typing import Dict, List, TypedDict


class Strategy(TypedDict):
    strategy: str
    rationale: str


PROFILES = ("dyslexia", "adhd", "esl", "dyscalculia")

# Each rationale names the guidance it is drawn from so judges can check it.
ACCOMMODATION_KNOWLEDGE: Dict[str, List[Strategy]] = {
    "dyslexia": [
        {
            "strategy": "shorter_sentences",
            "rationale": (
                "Shorter sentences reduce working-memory load while decoding "
                "(International Dyslexia Association; British Dyslexia Association "
                "Style Guide: keep sentences short, one main idea)."
            ),
        },
        {
            "strategy": "common_vocabulary",
            "rationale": (
                "Low-frequency and irregular words increase decoding effort for "
                "dyslexic readers (IDA Structured Literacy guidance on word-level "
                "demand; BDA Style Guide: prefer familiar words)."
            ),
        },
        {
            "strategy": "simple_active_syntax",
            "rationale": (
                "Active voice and straightforward word order cut syntactic "
                "processing cost (BDA Style Guide: use active verbs; avoid "
                "passive and nested clauses)."
            ),
        },
        {
            "strategy": "consistent_word_choice",
            "rationale": (
                "Repeating the same term for the same idea avoids extra decoding "
                "of synonyms (CAST UDL Checkpoint 2.1: clarify vocabulary and "
                "symbols)."
            ),
        },
    ],
    "adhd": [
        {
            "strategy": "one_idea_per_sentence",
            "rationale": (
                "One idea at a time lowers working-memory and attention switching "
                "costs (CHADD classroom guidance: break information into smaller "
                "chunks; CAST UDL Checkpoint 3.3: guide information processing)."
            ),
        },
        {
            "strategy": "explicit_topic_cues",
            "rationale": (
                "Stating the point up front supports readers who miss implied "
                "structure (CAST UDL Checkpoint 3.2: highlight patterns, critical "
                "features, and big ideas)."
            ),
        },
        {
            "strategy": "short_paragraphs",
            "rationale": (
                "Shorter blocks reduce the amount that must be held in mind at "
                "once (CDC ADHD in the classroom: chunk tasks and information)."
            ),
        },
        {
            "strategy": "signal_sequence",
            "rationale": (
                "Clear sequence words (first, then, so) make order visible instead "
                "of inferred (CAST UDL Checkpoint 2.2: clarify syntax and structure)."
            ),
        },
    ],
    "esl": [
        {
            "strategy": "high_frequency_vocabulary",
            "rationale": (
                "High-frequency words are more likely to be known; rare academic "
                "words are a major barrier (Paul Nation: high-frequency vocabulary; "
                "WIDA: support academic language)."
            ),
        },
        {
            "strategy": "reduced_syntactic_complexity",
            "rationale": (
                "Shorter, canonical sentences improve comprehensible input "
                "(SIOP / Echevarria: reduce syntactic complexity; TESOL "
                "comprehensible-input practice)."
            ),
        },
        {
            "strategy": "avoid_unsupported_idioms",
            "rationale": (
                "Idioms and culturally bound phrases often fail for multilingual "
                "learners unless explained (WIDA ELD Standards: beware idiomatic "
                "language)."
            ),
        },
        {
            "strategy": "paraphrase_keep_key_terms",
            "rationale": (
                "Keep essential academic terms but pair them with a plain-language "
                "paraphrase so content knowledge is not stripped (Cummins: "
                "cognitive academic language proficiency — support CALP, do not "
                "delete the concept)."
            ),
        },
    ],
    "dyscalculia": [
        {
            "strategy": "one_operation_per_step",
            "rationale": (
                "Multi-step numeric procedures overload working memory "
                "(British Dyslexia Association dyscalculia guidance: break "
                "calculations into small steps)."
            ),
        },
        {
            "strategy": "name_operations_in_words",
            "rationale": (
                "Saying 'plus' or 'divided by' alongside symbols supports decoding "
                "of notation (CAST UDL Checkpoint 2.3: support decoding of text, "
                "mathematical notation, and symbols)."
            ),
        },
        {
            "strategy": "keep_quantities_explicit",
            "rationale": (
                "Restate numbers with their units and what they refer to so "
                "quantity meaning is not left implicit (Geary: working-memory "
                "load in arithmetic; NCTM: make mathematical ideas explicit)."
            ),
        },
        {
            "strategy": "fixed_step_order",
            "rationale": (
                "A stable sequence of steps reduces the need to plan the next "
                "move while calculating (NCTM effective teaching: explicit, "
                "systematic instruction; BDA: show the method step by step)."
            ),
        },
    ],
}


def strategies_for(profile: str) -> List[Strategy]:
    """Return the curated strategies for a profile.

    Raises KeyError if the profile is not in the lookup table.
    """
    key = (profile or "").strip().lower()
    if key not in ACCOMMODATION_KNOWLEDGE:
        raise KeyError(key)
    return list(ACCOMMODATION_KNOWLEDGE[key])
