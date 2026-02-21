from fastapi import APIRouter

from automation_api.api.routes import health, meroshare

api_router = APIRouter()

api_router.include_router(health.router, prefix="", tags=["health"])
api_router.include_router(meroshare.router, prefix="/meroshare", tags=["meroshare"])
