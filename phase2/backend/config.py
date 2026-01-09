from pydantic import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database settings
    database_url: str

    # Authentication settings
    better_auth_secret: str
    algorithm: str
    access_token_expire_minutes: int

    # Application settings
    app_name: str
    app_version: str
    debug: bool

    # CORS settings
    better_auth_url: str
    frontend_url: str
    backend_cors_origins: str

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()

def get_settings():
    """Get the settings instance."""
    return settings