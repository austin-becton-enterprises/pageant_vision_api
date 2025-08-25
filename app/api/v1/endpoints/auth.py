from fastapi import APIRouter
from models import AuthResponse, AuthRequest
from app.services.auth_service import AuthService
from app.services.error_service import NetworkingExceptions as error

router = APIRouter()

@router.post("/authenticate", response_model=AuthResponse)
async def authenticate(auth_request: AuthRequest):
    service = AuthService()
    auth_response = await service.authenticate_user(auth_request=auth_request)
    if auth_response.access_token is None:
        raise error.bad_credentials()
    return auth_response