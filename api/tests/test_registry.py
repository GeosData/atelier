import dataclasses

import pytest
from pydantic import BaseModel

from app.products import registry
from app.products.registry import InputKind, Product, get_product, list_products, register


class Schema(BaseModel):
    value: int


def build(slug="t") -> Product:
    return Product(
        slug=slug,
        title="T",
        input_kind=InputKind.text,
        prompt="p",
        output_schema=Schema,
        accepted_mime=("text/plain",),
    )


@pytest.fixture(autouse=True)
def restore_registry():
    snapshot = dict(registry._registry)
    yield
    registry._registry.clear()
    registry._registry.update(snapshot)


def test_register_and_get():
    product = register(build("custom"))
    assert get_product("custom") is product
    assert product in list_products()


def test_unknown_slug_is_none():
    assert get_product("missing") is None


def test_product_is_immutable():
    with pytest.raises(dataclasses.FrozenInstanceError):
        build().slug = "other"


def test_missing_required_field_rejected():
    with pytest.raises(TypeError):
        Product(slug="x", title="x")


def test_builtin_products_are_well_formed():
    import app.products  # noqa: F401

    for product in list_products():
        assert product.slug and product.prompt and product.accepted_mime
        assert issubclass(product.output_schema, BaseModel)
        assert isinstance(product.input_kind, InputKind)
