from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

API_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = API_DIR.parent


class Settings(BaseSettings):
    cors_allowed_origins: list[str] = ["http://localhost:3000"]
    meroshare_headless: bool = False
    meroshare_username: str
    meroshare_password: str
    meroshare_dp: str

    model_config = SettingsConfigDict(
        env_file=(str(API_DIR / ".env"), str(PROJECT_ROOT / ".env")),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
