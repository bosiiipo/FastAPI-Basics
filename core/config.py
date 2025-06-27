from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "API Project"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./sql_app.db"  # Default to SQLite
    
    # Optional: Add these if you want to use environment variables
    # DATABASE_USER: Optional[str] = None
    # DATABASE_PASSWORD: Optional[str] = None
    # DATABASE_HOST: Optional[str] = "localhost"
    # DATABASE_PORT: Optional[str] = "5432"
    # DATABASE_NAME: Optional[str] = "fastapi_db"

    # class Config:
    #     env_file = ".env"

settings = Settings()