from functools import lru_cache

from pydantic import BaseModel

from app.products.registry import Product
from app.services.providers.gemini import GeminiVisionProvider


class UnsupportedMimeError(ValueError):
    pass


@lru_cache
def _provider() -> GeminiVisionProvider:
    return GeminiVisionProvider()


def run(product: Product, content: bytes, mime: str) -> BaseModel:
    if mime not in product.accepted_mime:
        raise UnsupportedMimeError(mime)
    prompt = product.prompt
    if product.context:
        prompt = f"{prompt}\n\nReference knowledge:\n{product.context}"
    return _provider().extract(content, mime, prompt, product.output_schema)
