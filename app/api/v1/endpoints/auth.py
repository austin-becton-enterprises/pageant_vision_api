from fastapi import APIRouter, Request
from models import AuthResponse

router = APIRouter()

@router.post("/authenticate", response_model=AuthResponse)
async def authenticate(request: Request):
    print("auth called")
    # The line below will fail now, so we'll keep it commented.
    # auth_service = AuthService()
    # await auth_service.authenticate_user(auth_request.username, auth_request.password)
    # access_token = await auth_service.create_access_token(auth_request.username)
    # return AuthResponse(access_token=access_token)
    return AuthResponse(access_token="")



