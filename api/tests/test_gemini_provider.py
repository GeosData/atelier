import pytest
from google.genai import errors
from pydantic import BaseModel, ValidationError

from app.services.providers import gemini


class Answer(BaseModel):
    value: int


class FakeResponse:
    def __init__(self, text):
        self.text = text


class FakeModels:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return FakeResponse(outcome)


@pytest.fixture
def build_provider(monkeypatch):
    sleeps = []
    monkeypatch.setattr(gemini.time, "sleep", sleeps.append)

    def build(outcomes):
        models = FakeModels(outcomes)

        class FakeClient:
            def __init__(self, api_key):
                self.models = models

        monkeypatch.setattr(gemini.genai, "Client", FakeClient)
        return gemini.GeminiVisionProvider(), models, sleeps

    return build


def api_error(code):
    return errors.APIError(code, {"error": {"message": "x", "status": "X"}})


def test_valid_json_is_parsed_into_schema(build_provider):
    provider, models, _ = build_provider(['{"value": 3}'])
    assert provider.extract(b"img", "image/png", "prompt", Answer) == Answer(value=3)
    config = models.calls[0]["config"]
    assert config.response_mime_type == "application/json"
    assert config.response_schema is Answer


def test_empty_response_raises(build_provider):
    provider, _, _ = build_provider([""])
    with pytest.raises(ValueError):
        provider.extract(b"img", "image/png", "prompt", Answer)


def test_none_response_raises(build_provider):
    provider, _, _ = build_provider([None])
    with pytest.raises(ValueError):
        provider.extract(b"img", "image/png", "prompt", Answer)


@pytest.mark.parametrize("text", ["not json", '{"value": "x"}', "{}", "[]"])
def test_malformed_or_schema_violating_output_raises_validation_error(build_provider, text):
    provider, _, _ = build_provider([text])
    with pytest.raises(ValidationError):
        provider.extract(b"img", "image/png", "prompt", Answer)


def test_retries_retryable_codes_with_backoff(build_provider):
    provider, models, sleeps = build_provider([api_error(429), api_error(503), '{"value": 1}'])
    assert provider.extract(b"i", "image/png", "p", Answer) == Answer(value=1)
    assert len(models.calls) == 3
    assert sleeps == [1, 2]


def test_gives_up_after_max_attempts(build_provider):
    provider, models, sleeps = build_provider([api_error(500)] * 4)
    with pytest.raises(errors.APIError):
        provider.extract(b"i", "image/png", "p", Answer)
    assert len(models.calls) == 4
    assert sleeps == [1, 2, 4]


@pytest.mark.parametrize("code", [400, 401, 403, 404])
def test_non_retryable_code_fails_immediately(build_provider, code):
    provider, models, sleeps = build_provider([api_error(code)])
    with pytest.raises(errors.APIError):
        provider.extract(b"i", "image/png", "p", Answer)
    assert len(models.calls) == 1
    assert sleeps == []
