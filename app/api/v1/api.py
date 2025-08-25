from fastapi import APIRouter
from app.api.v1.endpoints import auth, videos_v2, system

api_router = APIRouter()

#UNSECURED ENDPOINTS
api_router.include_router(system.router, tags=["system"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

#SECURED ENDPOINTS
api_router.include_router(
    videos_v2.router,
    prefix="/video",
    tags=["video"]
)