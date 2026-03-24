from functools import lru_cache
from typing import Literal

from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment (and optional `.env` file)."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: PostgresDsn = Field(
        ...,
        description="Async SQLAlchemy URL; use postgresql+asyncpg://...",
    )
    redis_url: RedisDsn = Field(
        ...,
        description="Redis URL for cache, locks, and Celery broker/backend.",
    )

    env: Literal["development", "staging", "production"] = "development"
    debug: bool = False

    jwt_secret_key: str = Field(
        default="dev-only-change-me-not-for-production",
        min_length=16,
    )
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


@lru_cache
def get_settings() -> Settings:
    """Cached settings singleton so dependency injection does not re-parse env each call."""
    return Settings()


settings = get_settings()
