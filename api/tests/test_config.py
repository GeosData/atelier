import pytest
from pydantic import ValidationError
from pydantic_settings import SettingsError

from app.config import Settings, get_settings


def test_defaults():
    settings = Settings()
    assert settings.gemini_api_key == ""
    assert settings.vision_model == "gemini-flash-latest"
    assert settings.allowed_origins == ["*"]
    assert settings.max_upload_bytes == 8 * 1024 * 1024
    assert settings.rate_limit_per_minute == 20


def test_env_overrides(monkeypatch):
    monkeypatch.setenv("MAX_UPLOAD_BYTES", "123")
    monkeypatch.setenv("RATE_LIMIT_PER_MINUTE", "5")
    monkeypatch.setenv("ALLOWED_ORIGINS", '["https://a.example"]')
    settings = Settings()
    assert settings.max_upload_bytes == 123
    assert settings.rate_limit_per_minute == 5
    assert settings.allowed_origins == ["https://a.example"]


@pytest.mark.parametrize("name,value", [("MAX_UPLOAD_BYTES", "abc"), ("RATE_LIMIT_PER_MINUTE", "x")])
def test_invalid_numeric_env_rejected(monkeypatch, name, value):
    monkeypatch.setenv(name, value)
    with pytest.raises(ValidationError):
        Settings()


def test_non_json_allowed_origins_rejected(monkeypatch):
    monkeypatch.setenv("ALLOWED_ORIGINS", "https://a.example")
    with pytest.raises(SettingsError):
        Settings()


def test_get_settings_is_cached(monkeypatch):
    first = get_settings()
    monkeypatch.setenv("MAX_UPLOAD_BYTES", "1")
    assert get_settings() is first
