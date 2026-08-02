from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

IPC_2025 = 0.051


class IncrementoArriendoInput(BaseModel):
    canon: float = Field(gt=0, description="Canon actual (COP)")
    proposed: float = Field(default=0, ge=0, description="Valor nuevo propuesto (opcional)")


class IncrementoArriendoResult(BaseModel):
    canon: float
    increase: float
    max_canon: float
    proposed_within_law: bool | None = None
    proposed_excess: float | None = None


def compute(data: IncrementoArriendoInput) -> IncrementoArriendoResult:
    increase = data.canon * IPC_2025
    max_canon = data.canon + increase

    proposed_within_law: bool | None = None
    proposed_excess: float | None = None
    if data.proposed > 0:
        if data.proposed <= max_canon + 0.5:
            proposed_within_law = True
        else:
            proposed_within_law = False
            proposed_excess = data.proposed - max_canon

    return IncrementoArriendoResult(
        canon=data.canon,
        increase=increase,
        max_canon=max_canon,
        proposed_within_law=proposed_within_law,
        proposed_excess=proposed_excess,
    )


incremento_arriendo = register(
    Tool(
        slug="incremento-arriendo",
        title="Incremento de arriendo 2026",
        subtitle="Cuanto te pueden subir el arriendo con el IPC 2025 (5,1%).",
        input_schema=IncrementoArriendoInput,
        output_schema=IncrementoArriendoResult,
        compute=compute,
    )
)
