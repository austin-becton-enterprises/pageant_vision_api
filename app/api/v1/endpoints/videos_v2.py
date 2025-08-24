from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.services.content_service import ContentService
from app.services.auth_service import AuthService

router = APIRouter()

def get_current_user(request: Request, db: Session = Depends(get_db)) -> models.User:
    # Extract token from Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header")
    token = auth_header.split(" ", 1)[1]
    try:
        user_email = AuthService.validate_token(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = db.query(models.User).filter(models.User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

@router.get("/my-videos")
def get_my_videos(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return ContentService.get_my_videos(current_user.id, db)