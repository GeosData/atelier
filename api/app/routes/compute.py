from fastapi import APIRouter, Body

from app.controllers import compute_controller

router = APIRouter()


@router.get("/tools")
def tools() -> list[dict]:
    return compute_controller.catalog()


@router.post("/compute/{slug}")
def compute(slug: str, payload: dict = Body(...)) -> dict:
    return compute_controller.handle(slug, payload)
