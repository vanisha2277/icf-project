from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import transform as transform_router

app = FastAPI(title="ICF Project - Reading Mode Backend")

# Allow chrome-extension origins (match any chrome-extension://<id>)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^chrome-extension://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transform_router.router)


@app.get("/health")
async def health():
    """Simple health check endpoint."""
    return {"status": "ok"}
