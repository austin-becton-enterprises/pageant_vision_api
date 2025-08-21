from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    APP_ENV: str = "prod"
    DEBUG: bool = False
    APP_NAME: str = "Pageant Vision API"
    APP_VERSION: str = "0.1.0"
    
    # Add more configuration items as needed
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = ""
    API_KEY: str = ""
    MUX_KEY_ID: str = ""
    MUX_SECRET_KEY: str = ""
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

@lru_cache()
def get_settings():
    # First, determine the environment. Pydantic-settings loads from environment variables first.
    # So, if APP_ENV is set in the shell, it will be used to find the correct .env file.
    # If not set, it will default to "prod" from the Settings class.
    env = Settings().APP_ENV
    
    # Now, load the settings from the correct environment file.
    return Settings(
        _env_file=[".env", f".env.{env}"],
        _env_file_encoding="utf-8"
    )
