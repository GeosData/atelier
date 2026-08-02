import time

from google import genai
from google.genai import errors, types
from pydantic import BaseModel

from app.config import get_settings

_RETRYABLE = (429, 500, 503)


class GeminiVisionProvider:
    def __init__(self) -> None:
        settings = get_settings()
        self._client = genai.Client(api_key=settings.gemini_api_key)
        self._model = settings.vision_model
        self._max_attempts = 4

    def extract(self, content: bytes, mime: str, prompt: str, schema: type[BaseModel]) -> BaseModel:
        for attempt in range(self._max_attempts):
            try:
                response = self._client.models.generate_content(
                    model=self._model,
                    contents=[
                        types.Part.from_bytes(data=content, mime_type=mime),
                        prompt,
                    ],
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=schema,
                    ),
                )
                if not response.text:
                    raise ValueError("empty model response")
                return schema.model_validate_json(response.text)
            except errors.APIError as error:
                last = attempt == self._max_attempts - 1
                if last or error.code not in _RETRYABLE:
                    raise
                time.sleep(2 ** attempt)
        raise RuntimeError("unreachable")
