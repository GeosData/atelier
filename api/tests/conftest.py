from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel

from app.config import get_settings
from app.main import create_app
from app.services import engine


class RecordingProvider:
    def __init__(self, result: BaseModel | None = None, error: Exception | None = None) -> None:
        self.result = result
        self.error = error
        self.calls: list[dict] = []

    def extract(self, content, mime, prompt, schema):
        self.calls.append({"content": content, "mime": mime, "prompt": prompt, "schema": schema})
        if self.error:
            raise self.error
        return self.result if self.result is not None else schema.model_validate(VALID_PAYLOADS[schema.__name__])


VALID_PAYLOADS = {
    "Receipt": {
        "vendor": "Tienda La Esquina",
        "total": 1500.5,
        "line_items": [{"description": "Arroz", "quantity": 2, "amount": 1500.5}],
        "confidence": 0.9,
    },
}


@pytest.fixture(autouse=True)
def isolated_settings(monkeypatch):
    for name in ("GEMINI_API_KEY", "VISION_MODEL", "ALLOWED_ORIGINS", "MAX_UPLOAD_BYTES", "RATE_LIMIT_PER_MINUTE"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.chdir(Path(__file__).parent)
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


@pytest.fixture
def provider(monkeypatch):
    stub = RecordingProvider()
    monkeypatch.setattr(engine, "_provider", lambda: stub)
    return stub


@pytest.fixture
def client(provider):
    return TestClient(create_app())


@pytest.fixture
def make_client(monkeypatch):
    def build(**env: str) -> TestClient:
        for name, value in env.items():
            monkeypatch.setenv(name, value)
        get_settings.cache_clear()
        return TestClient(create_app())

    return build
