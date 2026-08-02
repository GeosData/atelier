from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

AUX_TRANSPORTE = 249095
TOPE_AUXILIO = 3501810
SEMESTER_DAYS = 180


class PrimaServiciosInput(BaseModel):
    salary: float = Field(gt=0, description="Salario mensual (COP)")
    days: float = Field(gt=0, description="Dias trabajados en el semestre")


class PrimaServiciosResult(BaseModel):
    base: float
    days: float
    prima: float
    aux_included: bool


def compute(data: PrimaServiciosInput) -> PrimaServiciosResult:
    days = min(data.days, SEMESTER_DAYS)
    base_con_aux = data.salary + (AUX_TRANSPORTE if data.salary <= TOPE_AUXILIO else 0)
    prima = (base_con_aux * days) / 360

    return PrimaServiciosResult(
        base=base_con_aux,
        days=days,
        prima=prima,
        aux_included=data.salary <= TOPE_AUXILIO,
    )


prima_servicios = register(
    Tool(
        slug="prima-servicios",
        title="Prima de servicios 2026",
        subtitle="30 dias de salario por ano, con auxilio de transporte incluido.",
        input_schema=PrimaServiciosInput,
        output_schema=PrimaServiciosResult,
        compute=compute,
    )
)
