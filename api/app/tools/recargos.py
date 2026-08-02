from typing import Literal

from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

NIGHT_RATE = 0.35
EXTRA_DAY_RATE = 0.25
EXTRA_NIGHT_RATE = 0.75
HOURLY_DIVISOR = 240
WEEKLY_EXTRA_LIMIT = 12


class RecargosInput(BaseModel):
    monthly_salary: float = Field(gt=0, description="Salario mensual del empleado (COP)")
    period: Literal["until_jun_2026", "from_jul_2026"] = Field(default="from_jul_2026")
    night_hours: float = Field(default=0, ge=0)
    sunday_day_hours: float = Field(default=0, ge=0)
    sunday_night_hours: float = Field(default=0, ge=0)
    extra_day: float = Field(default=0, ge=0)
    extra_night: float = Field(default=0, ge=0)
    extra_sunday_day: float = Field(default=0, ge=0)
    extra_sunday_night: float = Field(default=0, ge=0)


class RecargosResult(BaseModel):
    hourly_rate: float
    sunday_rate: float
    night: float
    sunday_day: float
    sunday_night: float
    extra_day: float
    extra_night: float
    extra_sunday_day: float
    extra_sunday_night: float
    total: float
    extra_hours: float
    weekly_limit_exceeded: bool


def compute(data: RecargosInput) -> RecargosResult:
    hourly_rate = data.monthly_salary / HOURLY_DIVISOR
    sunday_rate = 0.9 if data.period == "from_jul_2026" else 0.8

    night = data.night_hours * hourly_rate * NIGHT_RATE
    sunday_day = data.sunday_day_hours * hourly_rate * sunday_rate
    sunday_night = data.sunday_night_hours * hourly_rate * (sunday_rate + NIGHT_RATE)

    extra_day = data.extra_day * hourly_rate * (1 + EXTRA_DAY_RATE)
    extra_night = data.extra_night * hourly_rate * (1 + EXTRA_NIGHT_RATE)
    extra_sunday_day = data.extra_sunday_day * hourly_rate * (1 + sunday_rate + EXTRA_DAY_RATE)
    extra_sunday_night = data.extra_sunday_night * hourly_rate * (1 + sunday_rate + EXTRA_NIGHT_RATE)

    surcharge_total = night + sunday_day + sunday_night
    overtime_total = extra_day + extra_night + extra_sunday_day + extra_sunday_night
    extra_hours = data.extra_day + data.extra_night + data.extra_sunday_day + data.extra_sunday_night

    return RecargosResult(
        hourly_rate=hourly_rate,
        sunday_rate=sunday_rate,
        night=night,
        sunday_day=sunday_day,
        sunday_night=sunday_night,
        extra_day=extra_day,
        extra_night=extra_night,
        extra_sunday_day=extra_sunday_day,
        extra_sunday_night=extra_sunday_night,
        total=surcharge_total + overtime_total,
        extra_hours=extra_hours,
        weekly_limit_exceeded=extra_hours > WEEKLY_EXTRA_LIMIT,
    )


recargos = register(
    Tool(
        slug="recargos",
        title="Recargos nocturnos, dominicales y festivos 2026",
        subtitle="Cuanto se paga por turnos nocturnos, dominicales y festivos con la reforma laboral.",
        input_schema=RecargosInput,
        output_schema=RecargosResult,
        compute=compute,
    )
)
