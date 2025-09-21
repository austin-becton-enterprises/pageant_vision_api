from typing import Union
from fastapi import APIRouter, Depends, Header, Request, HTTPException, Security, status
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.models.hax_models.pv_person import PVPerson
from app.services.content_service.content_service import ContentService
from app.services.auth_service import AuthService
from app.config.config import get_settings
from models import AuthRequest  # Adjust import if needed
import logging

api_key_header = APIKeyHeader(name="X-API-Key")

router = APIRouter()

def authenticate(auth: AuthRequest) -> Union[PVPerson, HTTPException]:
    if not auth.token:
        print("no auth token")
        raise HTTPException(status_code=401, detail="Token missing in request")
    if not auth.email:
        print("no email")
        raise HTTPException(status_code=401, detail="Email address missing in request")
    try:
        return AuthService().validate_token_and_return_user(email=auth.email, token=auth.token)
    except Exception as e:
        logging.error(f"Auth failed: {e}")
        raise HTTPException(status_code=401, detail="Invalid token or authentication failed")

@router.post("/my-videos")
async def get_my_videos(auth: AuthRequest):
    authenticated_person = authenticate(auth=auth)
    if authenticated_person is not None:
        return await ContentService.get_my_videos(user_id=authenticated_person.user_id())
    elif authenticated_person is HTTPException:
        raise authenticated_person

@router.get("/playback-token")
async def get_playback_token(video_id: str, Authorization: str = Header(None), authEmail: str = Header(None)):
    if not Authorization or not authEmail:
        raise HTTPException(status_code=401, detail="Authorization token or email missing in headers")
    verified = AuthService.validate_token_only(authEmail, Authorization)
    if verified:
        return await ContentService.get_playback_token(mux_playback_id=video_id)
    else:
        print("token verification failed")
        raise HTTPException(status_code=401, detail="Invalid token or authentication failed")