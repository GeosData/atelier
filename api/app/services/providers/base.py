from typing import Protocol

from pydantic import BaseModel


class VisionProvider(Protocol):
    def extract(self, content: bytes, mime: str, prompt: str, schema: type[BaseModel]) -> BaseModel:
        ...
