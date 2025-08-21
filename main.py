from fastapi import FastAPI, Request, Depends
from app.config.config import get_settings
from app.api.v1.api import api_router
from app.api.dependencies import get_api_key
import logging
import time
import os
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
settings = get_settings()

if not settings.DEBUG:
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)


def create_application() -> FastAPI:
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
    
    log_info = {
        "message": f"Request to {request.url.path} processed",
        "processing_time_seconds": f"{process_time:.4f}",
        "request_url": str(request.url),
        "request_method": request.method,
        "client_host": request.client.host,
    }
    if hasattr(response, 'status_code'):
        log_info["status_code"] = response.status_code

    logger.info(log_info)
    return response

if __name__ == "__main__":
    import uvicorn
    # The --reload flag should be used for development only.
    # It's better to run uvicorn programmatically for clarity.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)