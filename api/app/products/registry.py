from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel


class InputKind(str, Enum):
    image = "image"
    audio = "audio"
    text = "text"


@dataclass(frozen=True)
class Product:
    slug: str
    title: str
    input_kind: InputKind
    prompt: str
    output_schema: type[BaseModel]
    accepted_mime: tuple[str, ...]
    context: str = ""
    subtitle: str = ""


_registry: dict[str, Product] = {}


def register(product: Product) -> Product:
    _registry[product.slug] = product
    return product


def get_product(slug: str) -> Product | None:
    return _registry.get(slug)


def list_products() -> list[Product]:
    return list(_registry.values())
