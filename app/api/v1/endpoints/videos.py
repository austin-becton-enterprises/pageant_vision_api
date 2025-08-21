import logging
from fastapi import APIRouter, Depends, Query
from app.config.config import get_settings, Settings
from app.models.mux_models import MuxVideoResponse
from app.services.jwt_service import JWTService
from hax_telegraph.model.database_object.wrapper import DatabaseObjectWrapper

router = APIRouter()
logger = logging.getLogger(__name__)

def get_dummy_media_list() -> DatabaseObjectWrapper:
    """Creates a dummy DatabaseObjectWrapper for testing purposes."""
    nested_object_dict = {
        "metaTags": {
            "displayTitle": "Nested Video",
            "subtitle": "A nested video example",
            "date": "July 1, 2025",
            "thumbnailURL": "dummy_thumbnail"
        },
        "value": "nested_video_id"
    }

    children = [
        {
            "metaTags": {
                "displayTitle": "Miss Michigan",
                "subtitle": "Live from Port Huron, Michigan",
                "date": "August 9, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4",
            "children": [nested_object_dict, nested_object_dict]
        },
        {
            "metaTags": {
                "displayTitle": "Miss USA",
                "subtitle": "Live from Las Vegas, Nevada",
                "date": "September 12, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss Universe",
                "subtitle": "Live from Miami, Florida",
                "date": "October 3, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss Teen",
                "subtitle": "Live from Dallas, Texas",
                "date": "July 21, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        },
        {
            "metaTags": {
                "displayTitle": "Miss World",
                "subtitle": "Live from London, England",
                "date": "November 15, 2025",
                "thumbnailURL": "dummy_miss_michigan"
            },
            "value": "tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4"
        }
    ]

    return DatabaseObjectWrapper(jsonDict={"children": children})

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

