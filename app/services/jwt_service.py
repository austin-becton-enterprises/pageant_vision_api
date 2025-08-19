from datetime import datetime, timedelta
from typing import Optional
from jwt import encode  # Changed to import encode directly from jwt

class JWTService:
    @staticmethod
    async def create_auth_token(username: str, expires_delta: Optional[timedelta] = None) -> str:
        # TODO: Move these to environment variables
        SECRET_KEY = "your-secret-key"
        ALGORITHM = "HS256"
        
        expires = datetime.utcnow() + (expires_delta or timedelta(hours=24))
        to_encode = {
            "sub": username,
            "exp": expires,
            "type": "auth"
        }
        return encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Remove jwt. prefix

    @staticmethod
    async def create_mux_signature(video_id: str, expires_delta: Optional[timedelta] = None) -> str:
        # TODO: Move these to environment variables
        MUX_SIGNING_KEY = "your-mux-signing-key"
        ALGORITHM = "HS256"
        
        expires = datetime.utcnow() + (expires_delta or timedelta(minutes=5))
        to_encode = {
            "sub": video_id,
            "exp": expires,
            "type": "mux"
        }
        return encode(to_encode, MUX_SIGNING_KEY, algorithm=ALGORITHM)  # Remove jwt. prefix
