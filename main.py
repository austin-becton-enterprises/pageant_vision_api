from fastapi import FastAPI, Depends
from app.config.config import get_settings, Settings
from models import AuthRequest, AuthResponse
from app.services.auth_service import AuthService

def create_application() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.APP_NAME,
        description="Backend service for Pageant Vision",
        version=settings.APP_VERSION,
        debug=settings.DEBUG
    )
    return app

app = create_application()

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Welcome to Pageant Vision API",
        "environment": settings.APP_ENV
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/authenticate", response_model=AuthResponse)
async def authenticate(auth_request: AuthRequest):
    auth_service = AuthService()
    await auth_service.authenticate_user(auth_request.username, auth_request.password)
    access_token = await auth_service.create_access_token(auth_request.username)
    return AuthResponse(access_token=access_token)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
