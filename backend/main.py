# ICF 2026 AI disclosure: built with AI assistance.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import transform as transform_router

app = FastAPI(title="ICF Project - Reading Mode Backend")

# Allow chrome-extension origins (match any chrome-extension://<id>), plus the
# Vite dev server origin so the frontend can be exercised in a normal browser
# tab during local development, before it's packaged as an unpacked extension.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^(chrome-extension://.*|http://localhost:5173|http://127\.0\.0\.1:5173)$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transform_router.router)


@app.get("/health")
async def health():
    """Simple health check endpoint."""
    return {"status": "ok"}
