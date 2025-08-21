from pydantic import BaseModel

class MuxVideoResponse(BaseModel):
    playback_id: str
    playback_token: str
    playback_url: str
