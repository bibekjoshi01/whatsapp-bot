from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Project Imports
from automation_api.api.router import api_router
from automation_api.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="Automation API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    description="APIs for browser automation and back-office triggers.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Customer-Session-Id"],
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["meta"])
async def root() -> dict[str, str]:
    return {"service": "automation apis", "status": "ok"}
