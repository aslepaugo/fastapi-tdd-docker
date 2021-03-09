import logging
import os

from pydantic import BaseSettings, AnyUrl
from functools import lru_cache


log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMET", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.getenv("DATABASE_URL")

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
