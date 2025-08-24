from fastapi import Security, HTTPException, status, Depends
from fastapi.security import APIKeyHeader, HTTPBearer, HTTPAuthorizationCredentials
from app.config.config import get_settings
from jwt import decode, exceptions as jwt_exceptions
from app.services.jwt_service import JWTService

api_key_header = APIKeyHeader(name="X-API-Key")
security = HTTPBearer()

def get_api_key(api_key: str = Security(api_key_header)):
    settings = get_settings()
    if api_key == settings.API_KEY:
        return api_key
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return JWTService.verify_auth_token(token)