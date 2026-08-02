from fastapi import APIRouter, File, UploadFile

from app.controllers import process_controller

router = APIRouter()


@router.get("/products")
def products() -> list[dict]:
    return process_controller.catalog()


@router.post("/process/{slug}")
async def process(slug: str, file: UploadFile = File(...)) -> dict:
    return await process_controller.handle(slug, file)
