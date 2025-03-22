from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for bot"""

    APP_MODE: str
    TELEGRAM_API_TOKEN: SecretStr

    SYNC_TOKEN: SecretStr
    API_URL: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore", env_prefix="BOT_")


@lru_cache
def get_settings() -> Settings:
    """Cached settings function"""
    return Settings()  # type: ignore
