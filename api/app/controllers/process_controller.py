from fastapi import HTTPException, UploadFile, status

from app.config import get_settings
from app.products.registry import get_product, list_products
from app.services import engine
from app.services.engine import UnsupportedMimeError


async def handle(slug: str, file: UploadFile) -> dict:
    product = get_product(slug)
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"unknown product: {slug}")

    content = await file.read()
    if not content:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "empty file")
    if len(content) > get_settings().max_upload_bytes:
        raise HTTPException(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, "file too large")

    mime = file.content_type or ""
    try:
        result = engine.run(product, content, mime)
    except UnsupportedMimeError:
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"{mime} not accepted, expected {product.accepted_mime}",
        )

    return {"product": product.slug, "result": result.model_dump()}


def catalog() -> list[dict]:
    return [
        {
            "slug": p.slug,
            "title": p.title,
            "subtitle": p.subtitle,
            "input": p.input_kind.value,
            "accept": list(p.accepted_mime),
        }
        for p in list_products()
    ]
