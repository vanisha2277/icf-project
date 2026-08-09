from backend.services.chunking import split_into_sentences, chunk_paragraph


def test_split_sentences_basic():
    p = "Hello world. This is a test! Is it working? Yes"
    s = split_into_sentences(p)
    assert len(s) >= 4


def test_chunk_paragraph_default():
    p = "First sentence. Second sentence. Third sentence. Fourth."
    chunks = chunk_paragraph(p, max_sentences=2)
    assert len(chunks) == 2
    assert chunks[0].startswith("First sentence")


def test_chunk_paragraph_single_sentence():
    p = "Short."
    chunks = chunk_paragraph(p)
    assert chunks == ["Short."]


def test_chunk_paragraph_empty():
    assert chunk_paragraph("") == []
