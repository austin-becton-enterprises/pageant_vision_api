from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.db.session import get_db
from app.db import models
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

# Dummy authentication dependency (replace with your real auth)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Replace with your real user lookup
    user = db.query(models.User).first()
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user

def mux_thumbnail_url(mux_playback_id: str) -> str:
    # Stub: Replace with real JWT signing logic for Mux
    return f"https://image.mux.com/{mux_playback_id}/thumbnail.jpg?token=SIGNED_JWT"

@router.get("/my-videos")
def get_my_videos(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # 1. Query purchases for user
    purchases = db.query(models.Purchase).filter(models.Purchase.user_id == current_user.id).all()
    category_ids = set()
    video_ids = set()
    for purchase in purchases:
        if purchase.cat_id:
            category_ids.add(purchase.cat_id)
        if purchase.video_id:
            video_ids.add(purchase.video_id)

    # 2. Resolve accessible videos
    videos = []
    if category_ids:
        videos += db.query(models.LiveEvent).filter(models.LiveEvent.category.in_(category_ids)).all()
    if video_ids:
        videos += db.query(models.LiveEvent).filter(models.LiveEvent.id.in_(video_ids)).all()

    # Remove duplicates by id
    seen = set()
    unique_videos = []
    for v in videos:
        if v.id not in seen:
            unique_videos.append(v)
            seen.add(v.id)

    # 3. Fetch metadata and 4. Generate signed thumbnail URLs
    children = []
    for v in unique_videos:
        meta = {
            "displayTitle": v.name,
            "subtitle": v.location,
            "date": {
                "start": v.start,
                "end": v.end,
                "timezone": v.timezone
            },
            "thumbnailURL": mux_thumbnail_url(v.embed2) if v.embed2 else None
        }
        children.append({
            "metaTags": meta,
            "value": v.embed2 or v.id
        })

    # 5. Format response
    return {
        "children": children
    }
