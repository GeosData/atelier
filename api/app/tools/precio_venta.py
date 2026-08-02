from typing import Literal

from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

IVA = 0.19


class PrecioVentaInput(BaseModel):
    cost: float = Field(gt=0, description="Costo del producto (COP)")
    mode: Literal["markup", "margin"] = Field(default="markup")
    pct: float = Field(ge=0, description="Porcentaje de ganancia")
    add_iva: bool = Field(default=False)


class PrecioVentaResult(BaseModel):
    price: float | None = None
    profit: float | None = None
    margin_real: float | None = None
    markup_real: float | None = None
    iva_amount: float | None = None
    price_with_iva: float | None = None
    note: str | None = None


def compute(data: PrecioVentaInput) -> PrecioVentaResult:
    if data.mode == "margin":
        if data.pct >= 100:
            return PrecioVentaResult(
                note="Un margen sobre el precio no puede ser 100% o mas. Usa un valor menor.",
            )
        price = data.cost / (1 - data.pct / 100)
    else:
        price = data.cost * (1 + data.pct / 100)

    profit = price - data.cost
    markup_real = (profit / data.cost) * 100
    margin_real = (profit / price) * 100

    iva_amount = price * IVA if data.add_iva else None
    price_with_iva = price * (1 + IVA) if data.add_iva else None

    return PrecioVentaResult(
        price=price,
        profit=profit,
        margin_real=margin_real,
        markup_real=markup_real,
        iva_amount=iva_amount,
        price_with_iva=price_with_iva,
    )


precio_venta = register(
    Tool(
        slug="precio-venta",
        title="Precio de venta y margen de ganancia",
        subtitle="A como vender: precio, ganancia y margen real, con opcion de IVA.",
        input_schema=PrecioVentaInput,
        output_schema=PrecioVentaResult,
        compute=compute,
    )
)
