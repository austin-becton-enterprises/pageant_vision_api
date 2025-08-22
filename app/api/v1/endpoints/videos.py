import logging
from fastapi import APIRouter, Depends, Query
from app.config.config import get_settings, Settings
from app.models.mux_models import MuxVideoResponse
from app.services.jwt_service import JWTService
from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper
from dummy_videos import get_dummy_media_list

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/playback", response_model=MuxVideoResponse)
async def get_video_playback(
    video_id: str = Query(None),
    settings: Settings = Depends(get_settings)
):
    jwt_service = JWTService()
    playback_id = video_id 
    playback_token = await jwt_service.create_mux_playback_token(playback_id)
    
    # Construct the complete playback URL
    playback_url = f"https://stream.mux.com/{playback_id}.m3u8?token={playback_token}"
    
    logger.debug(f"Playback URL: {playback_url}")
    print("final")
    print(playback_id, playback_token, playback_url)
    return MuxVideoResponse(
        playback_id=playback_id,
        playback_token=playback_token,
        playback_url=playback_url
    )

@router.get("/dotComContent")
async def get_dot_com_content():
    """
    Returns a list of video objects for the website.
    Currently returns dummy data.
    """
    dummy_data = get_dummy_media_list()
    return dummy_data.data

