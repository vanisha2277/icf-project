# ICF 2026 AI disclosure: built with AI assistance.
from fastapi import APIRouter, Depends, HTTPException

from backend.models.schemas import DefineWordRequest, DefineWordResponse
from backend.services.ai_client import AICallError, AIClient
from backend.routers.simplify import get_ai_client
from backend.services.define_word import define_word, is_cached

router = APIRouter(tags=["define-word"])


@router.post("/define-word", response_model=DefineWordResponse)
def define_word_endpoint(
    req: DefineWordRequest,
    client: AIClient = Depends(get_ai_client),
):
    word = (req.word or "").strip()
    sentence = (req.surrounding_sentence or "").strip()
    if not word:
        raise HTTPException(status_code=400, detail="word must not be empty")
    if not sentence:
        raise HTTPException(status_code=400, detail="surrounding_sentence must not be empty")

    was_cached = is_cached(word, req.profile, sentence)

    try:
        payload = define_word(word, sentence, req.profile, client)
    except AICallError as exc:
        raise HTTPException(
            status_code=504,
            detail=f"Definition timed out or failed: {exc}",
        ) from exc
    except KeyError:
        raise HTTPException(status_code=422, detail="Unknown learner profile")
    except (ValueError, TypeError) as exc:
        raise HTTPException(status_code=502, detail=f"Could not parse definition: {exc}") from exc

    return DefineWordResponse(
        definition=payload["definition"],
        example_sentence=payload["example_sentence"],
        cached=was_cached,
    )
