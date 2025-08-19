from fastapi import HTTPException, status
from .jwt_service import JWTService

class AuthService:
    def __init__(self):
        self.jwt_service = JWTService()

    async def authenticate_user(self, username: str, password: str) -> bool:
        # TODO: Replace with actual authentication logic
        if username == "user" and password == "password":
            return True
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    async def create_access_token(self, username: str) -> str:
        return await self.jwt_service.create_auth_token(username)
