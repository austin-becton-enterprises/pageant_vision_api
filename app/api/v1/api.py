from fastapi import APIRouter

from app.api.v1.endpoints import auth, videos, system

api_router = APIRouter()
api_router.include_router(system.router, tags=["system"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(videos.router, prefix="/video", tags=["video"])
