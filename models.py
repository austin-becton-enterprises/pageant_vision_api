from pydantic import BaseModel
from typing import Optional

class AuthRequest(BaseModel):
    email: str
    password: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    token: Optional[str] = None

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    email: str
    