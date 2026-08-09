from backend.services.bionic import bionic_html


def test_bionic_basic():
    src = "This is a test"
    out = bionic_html(src, ratio=0.5)
    # Each alpha word should have a bolded front portion
    assert "<b>Th</b>is" in out or "<b>T</b>his" in out
    assert "<b>is</b>" in out or "<b>i</b>s" in out


def test_bionic_single_short_word():
    assert bionic_html("A", ratio=0.45) == "<b>A</b>"


def test_bionic_empty():
    assert bionic_html("", ratio=0.45) == ""


def test_bionic_preserves_punctuation():
    src = "Hello, world! It's great."
    out = bionic_html(src)
    # punctuation should remain after bolding
    assert "," in out and "!" in out and "'" in out
