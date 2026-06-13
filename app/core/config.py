from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Resources API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Data
    CSV_FILE_PATH: str = "data/resources.csv"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
