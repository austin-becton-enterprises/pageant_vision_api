from fastapi import FastAPI, Depends
from config.config import get_settings, Settings

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
