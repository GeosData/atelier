from pydantic import BaseModel, Field

from app.tools.registry import Tool, register


class BreakevenInput(BaseModel):
    fixed_costs: float = Field(gt=0, description="Costos fijos del periodo")
    unit_price: float = Field(gt=0, description="Precio de venta unitario")
    unit_variable_cost: float = Field(ge=0, description="Costo variable por unidad")


class BreakevenResult(BaseModel):
    contribution_margin: float
    breakeven_units: float | None = None
    breakeven_revenue: float | None = None
    note: str | None = None


def compute(data: BreakevenInput) -> BreakevenResult:
    margin = data.unit_price - data.unit_variable_cost
    if margin <= 0:
        return BreakevenResult(
            contribution_margin=margin,
            note="El precio no cubre el costo variable: no hay punto de equilibrio.",
        )
    units = data.fixed_costs / margin
    return BreakevenResult(
        contribution_margin=margin,
        breakeven_units=units,
        breakeven_revenue=units * data.unit_price,
    )


breakeven = register(
    Tool(
        slug="punto-equilibrio",
        title="Punto de equilibrio",
        subtitle="Cuantas unidades tenes que vender para no perder plata.",
        input_schema=BreakevenInput,
        output_schema=BreakevenResult,
        compute=compute,
    )
)
