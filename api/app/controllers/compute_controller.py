from fastapi import HTTPException, status
from pydantic import ValidationError

from app.tools.registry import get_tool, list_tools


def catalog() -> list[dict]:
    return [
        {
            "slug": t.slug,
            "title": t.title,
            "subtitle": t.subtitle,
            "inputs": list(t.input_schema.model_json_schema().get("properties", {}).keys()),
        }
        for t in list_tools()
    ]


def handle(slug: str, payload: dict) -> dict:
    tool = get_tool(slug)
    if tool is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"unknown tool: {slug}")
    try:
        data = tool.input_schema.model_validate(payload)
    except ValidationError as error:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, error.errors())
    result = tool.compute(data)
    return {"tool": tool.slug, "result": result.model_dump()}
