# ICF 2026 AI disclosure: built with AI assistance.
from fastapi import APIRouter, Depends, HTTPException

from backend.models.schemas import SimplifyRequest, SimplifyResponse
from backend.services.ai_client import AICallError, AIClient
from backend.services.simplify_pipeline import run_simplify_pipeline

router = APIRouter(tags=["simplify"])


def get_ai_client() -> AIClient:
    client = AIClient.from_env()
    if client is None:
        raise HTTPException(
            status_code=503,
            detail="ANTHROPIC_API_KEY is not configured. Simplification needs a live key.",
        )
    return client


@router.post("/simplify", response_model=SimplifyResponse)
def simplify(req: SimplifyRequest, client: AIClient = Depends(get_ai_client)):
    text = (req.text or "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="text must not be empty")

    try:
        result = run_simplify_pipeline(
            text=text,
            profile=req.profile,
            client=client,
            target_grade_level=req.target_grade_level,
        )
    except AICallError as exc:
        raise HTTPException(
            status_code=504,
            detail=f"Simplification timed out or failed before a rewrite was ready: {exc}",
        ) from exc
    except KeyError:
        raise HTTPException(status_code=422, detail="Unknown learner profile")

    return SimplifyResponse(**result)
