from datetime import date

from pydantic import BaseModel, Field, model_validator

from app.tools.registry import Tool, register

AUX_TRANSPORTE = 249095
TOPE_AUXILIO = 3501810
INTERES_CESANTIAS = 0.12


class LiquidacionInput(BaseModel):
    salary: float = Field(gt=0, description="Salario mensual (COP)")
    start: date = Field(description="Fecha de ingreso")
    end: date = Field(description="Fecha de retiro")

    @model_validator(mode="after")
    def end_after_start(self) -> "LiquidacionInput":
        if self.end <= self.start:
            raise ValueError("La fecha de retiro debe ser posterior a la de ingreso.")
        return self


class LiquidacionResult(BaseModel):
    days: int
    prima_days: int
    cesantias: float
    intereses: float
    prima: float
    vacaciones: float
    total: float
    aux_included: bool


def days360(start: date, end: date) -> int:
    d1, m1, y1 = start.day, start.month, start.year
    d2, m2, y2 = end.day, end.month, end.year
    if d1 == 31:
        d1 = 30
    if d2 == 31 and d1 == 30:
        d2 = 30
    return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)


def compute(data: LiquidacionInput) -> LiquidacionResult:
    days = days360(data.start, data.end)
    base_con_aux = data.salary + (AUX_TRANSPORTE if data.salary <= TOPE_AUXILIO else 0)

    sem_month = 1 if data.end.month <= 6 else 7
    sem_start = date(data.end.year, sem_month, 1)
    prima_start = data.start if data.start > sem_start else sem_start
    prima_days = max(0, days360(prima_start, data.end))

    cesantias = (base_con_aux * days) / 360
    intereses = (cesantias * days * INTERES_CESANTIAS) / 360
    prima = (base_con_aux * prima_days) / 360
    vacaciones = (data.salary * days) / 720
    total = cesantias + intereses + prima + vacaciones

    return LiquidacionResult(
        days=days,
        prima_days=prima_days,
        cesantias=cesantias,
        intereses=intereses,
        prima=prima,
        vacaciones=vacaciones,
        total=total,
        aux_included=data.salary <= TOPE_AUXILIO,
    )


liquidacion = register(
    Tool(
        slug="liquidacion",
        title="Liquidacion de contrato 2026",
        subtitle="Cesantias, intereses, prima y vacaciones al terminar un contrato.",
        input_schema=LiquidacionInput,
        output_schema=LiquidacionResult,
        compute=compute,
    )
)
