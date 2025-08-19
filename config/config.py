from pydantic import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    APP_ENV: str = "prod"
    DEBUG: bool = False
    APP_NAME: str = "Pageant Vision API"
    APP_VERSION: str = "0.1.0"
    
    # Add more configuration items as needed
    API_PREFIX: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    env = os.getenv("APP_ENV", "prod")
    return Settings(_env_file=f".env.{env}")
