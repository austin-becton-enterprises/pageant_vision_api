from fastapi import FastAPI, Request, Depends
from app.config.config import get_settings
from app.api.v1.api import api_router
from app.api.dependencies import get_api_key
import logging
import time

logger = logging.getLogger(__name__)

def create_application() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.APP_NAME,
        description="Backend service for Pageant Vision",
        version=settings.APP_VERSION,
        debug=settings.DEBUG
    )
    app.include_router(api_router, prefix="/api/v1", dependencies=[Depends(get_api_key)])
    return app

app = create_application()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request to {request.url.path} processed in {process_time:.4f} seconds")
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
