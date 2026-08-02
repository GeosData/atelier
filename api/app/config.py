from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    gemini_api_key: str = ""
    vision_model: str = "gemini-flash-latest"
    allowed_origins: list[str] = ["*"]
    max_upload_bytes: int = 8 * 1024 * 1024
    rate_limit_per_minute: int = 20


@lru_cache
def get_settings() -> Settings:
    return Settings()
