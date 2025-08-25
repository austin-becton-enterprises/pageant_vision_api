from fastapi import APIRouter, Depends, Request, HTTPException, Security, status
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.services.content_service import ContentService
from app.services.auth_service import AuthService
from app.config.config import get_settings
from models import AuthRequest  # Adjust import if needed
import logging

api_key_header = APIKeyHeader(name="X-API-Key")

router = APIRouter()


@router.post("/my-videos")
def get_my_videos(auth: AuthRequest):
    if not auth.token:
        raise HTTPException(status_code=401, detail="Token missing in request")
    if not auth.email:
        raise HTTPException(status_code=401, detail="Email address missing in request")
    try:
        person = AuthService().validate_token_and_return_user(email=auth.email, token=auth.token)
    except Exception as e:
        logging.error(f"Auth failed: {e}")
        raise HTTPException(status_code=401, detail="Invalid token or authentication failed")
    return ContentService.get_my_videos(user_id=person.user_id())