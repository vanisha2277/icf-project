from fastapi import APIRouter, HTTPException
from fastapi import Depends
from backend.models.schemas import TransformRequest, TransformResponse, ChunkResponse
from backend.services import bionic, chunking, tts_timing

router = APIRouter(prefix="", tags=["transform"])


@router.post("/transform", response_model=TransformResponse)
async def transform(req: TransformRequest):
    """Process text per requested options and return chunks with optional bionic HTML and TTS timings.

    Workflow:
    - Split into paragraphs (blank-line separated). If chunking enabled, further split paragraphs into shorter chunks.
    - For each chunk: optionally generate bionic HTML and optionally generate word timings (AI-assisted when available).
    """
    text = (req.text or "").strip()
    if text == "":
        return TransformResponse(chunks=[])

    # Split into paragraphs by blank lines
    paragraphs = [p.strip() for p in __import__("re").split(r"\n\s*\n", text) if p.strip()]

    all_chunks = []
    for para in paragraphs:
        if req.options.chunking:
            para_chunks = chunking.chunk_paragraph(para)
        else:
            para_chunks = [para]

        for ch in para_chunks:
            bionic_html = None
            word_timings = None
            if req.options.bionic:
                bionic_html = bionic.bionic_html(ch)
            if req.options.tts_sync:
                # Attempt to get AI-assisted timings, falls back to synthetic timings
                word_timings = tts_timing.generate_word_timings(ch)

            all_chunks.append(ChunkResponse(text=ch, bionic_html=bionic_html, word_timings=word_timings))

    return TransformResponse(chunks=all_chunks)
