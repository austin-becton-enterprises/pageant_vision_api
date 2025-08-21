from fastapi import APIRouter, Depends
from app.config.config import get_settings, Settings

router = APIRouter()

@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Welcome to Pageant Vision API",
        "environment": settings.APP_ENV
    }

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
