from fastapi import FastAPI, Request
from app.config.config import get_settings
from app.api.v1.api import api_router
import logging
import time
from pythonjsonlogger import jsonlogger
from app.db.session import get_db
import os

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
    # Remove global dependency on get_api_key here:
    app.include_router(api_router, prefix="/api/v1")
    return app

app = create_application()

# override get_db with dummy DB if enabled ---
if os.getenv("USE_DUMMY_DB", "0") == "1":
    from app.db.testing.dummy_db import get_dummy_db
    app.dependency_overrides[get_db] = get_dummy_db

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