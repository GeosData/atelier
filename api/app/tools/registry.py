from dataclasses import dataclass
from typing import Callable

from pydantic import BaseModel


@dataclass(frozen=True)
class Tool:
    slug: str
    title: str
    subtitle: str
    input_schema: type[BaseModel]
    output_schema: type[BaseModel]
    compute: Callable[[BaseModel], BaseModel]


_registry: dict[str, Tool] = {}


def register(tool: Tool) -> Tool:
    _registry[tool.slug] = tool
    return tool


def get_tool(slug: str) -> Tool | None:
    return _registry.get(slug)


def list_tools() -> list[Tool]:
    return list(_registry.values())
