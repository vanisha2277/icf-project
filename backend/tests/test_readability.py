from backend.services.readability import measure_readability

SIMPLE = "The cat sat on the mat. The sun was hot. We went to the park."

ACADEMIC = (
    "Photosynthetic phosphorylation in photoautotrophic eukaryotes necessitates "
    "the coordinated translocation of protons across thylakoid membranes, thereby "
    "establishing an electrochemical gradient whose dissipation is obligatorily "
    "coupled to ATP synthase activity under physiologically constrained conditions."
)


def test_simple_text_has_low_grade_and_high_ease():
    scores = measure_readability(SIMPLE)
    assert scores["flesch_kincaid_grade"] < 6.0
    assert scores["flesch_reading_ease"] > 70.0
    assert scores["avg_sentence_length"] > 0
    assert scores["avg_syllables_per_word"] > 0


def test_academic_text_is_harder_than_simple_text():
    simple = measure_readability(SIMPLE)
    academic = measure_readability(ACADEMIC)
    assert academic["flesch_kincaid_grade"] > simple["flesch_kincaid_grade"]
    assert academic["flesch_reading_ease"] < simple["flesch_reading_ease"]
    assert academic["dale_chall_score"] > simple["dale_chall_score"]


def test_empty_string_returns_zeros():
    scores = measure_readability("")
    assert scores == {
        "flesch_kincaid_grade": 0.0,
        "flesch_reading_ease": 0.0,
        "dale_chall_score": 0.0,
        "avg_sentence_length": 0.0,
        "avg_syllables_per_word": 0.0,
    }
    assert measure_readability("   \n") == scores
