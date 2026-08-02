from google import genai
from google.genai import types
from pydantic import BaseModel

from app.config import get_settings


class GeminiVisionProvider:
    def __init__(self) -> None:
        settings = get_settings()
        self._client = genai.Client(api_key=settings.gemini_api_key)
        self._model = settings.vision_model

    def extract(self, content: bytes, mime: str, prompt: str, schema: type[BaseModel]) -> BaseModel:
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
        return schema.model_validate_json(response.text)
