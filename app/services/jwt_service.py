from typing import Optional
from jwt import encode, decode, exceptions as jwt_exceptions
from fastapi import HTTPException, status
from app.config.config import get_settings
import os
import time

class JWTService:
    
    @staticmethod
    async def create_auth_token(user_email: str, expires_delta_seconds: Optional[int] = None) -> str:
        settings = get_settings()
        
        expires = time.time() + (expires_delta_seconds or 24 * 60 * 60)
        to_encode = {
            "sub": user_email,
            "exp": expires,
            "type": "auth"
        }
        return encode(to_encode, settings.SECRET_KEY, algorithm="HS256")

    @staticmethod
    async def create_mux_playback_token(playback_id: str) -> str:
        settings = get_settings()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        key_path = os.path.join(current_dir, 'singing_key.pem')

        with open(key_path, 'rb') as f:
            private_key = f.read()
        
        to_encode = {
            "sub": playback_id,
            "exp": time.time() + (60 * 60),
            "aud": "v"
        }
        headers = {
            "kid": settings.MUX_KEY_ID
        }
        return encode(to_encode, private_key, algorithm="RS256", headers=headers)

    @staticmethod
    def verify_auth_token(token: str, expected_username: Optional[str] = None) -> str:
        settings = get_settings()
        try:
            payload = decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            username = payload.get("sub")
            if not username:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
            if expected_username is not None and username != expected_username:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token does not match user")
            return username
        except jwt_exceptions.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
        except jwt_exceptions.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
