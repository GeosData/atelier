from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

UVT = 52374
TABLE = [
    {"desde": 0, "hasta": 95, "tarifa": 0.0, "menos": 0, "mas": 0},
    {"desde": 95, "hasta": 150, "tarifa": 0.19, "menos": 95, "mas": 0},
    {"desde": 150, "hasta": 360, "tarifa": 0.28, "menos": 150, "mas": 10},
    {"desde": 360, "hasta": 640, "tarifa": 0.33, "menos": 360, "mas": 69},
    {"desde": 640, "hasta": 945, "tarifa": 0.35, "menos": 640, "mas": 162},
    {"desde": 945, "hasta": 2300, "tarifa": 0.37, "menos": 945, "mas": 268},
    {"desde": 2300, "hasta": float("inf"), "tarifa": 0.39, "menos": 2300, "mas": 770},
]


class RetencionSalariosInput(BaseModel):
    income: float = Field(gt=0, description="Ingreso laboral gravable del mes (COP)")
    has_dependents: bool = Field(default=False)
    housing: float = Field(default=0, ge=0, description="Intereses de vivienda al mes")
    health: float = Field(default=0, ge=0, description="Medicina prepagada al mes")


class RetencionSalariosResult(BaseModel):
    aportes: float
    deducciones: float
    renta_exenta: float
    base: float
    base_uvt: float
    retencion: float


def retention_uvt(base_uvt: float) -> float:
    row = next((r for r in TABLE if base_uvt > r["desde"] and base_uvt <= r["hasta"]), TABLE[0])
    if row["tarifa"] == 0:
        return 0
    return (base_uvt - row["menos"]) * row["tarifa"] + row["mas"]


def compute(data: RetencionSalariosInput) -> RetencionSalariosResult:
    aportes = data.income * 0.08
    sub1 = data.income - aportes

    dep_ded = min(data.income * 0.1, 32 * UVT) if data.has_dependents else 0
    viv_ded = min(data.housing, 100 * UVT)
    health_ded = min(data.health, 16 * UVT)
    deducciones = dep_ded + viv_ded + health_ded

    exento = min((sub1 - deducciones) * 0.25, 240 * UVT)

    beneficios = deducciones + exento
    limite40 = sub1 * 0.4
    if beneficios > limite40:
        beneficios = limite40

    base = max(0, sub1 - beneficios)
    base_uvt = base / UVT
    retencion = retention_uvt(base_uvt) * UVT

    return RetencionSalariosResult(
        aportes=aportes,
        deducciones=deducciones,
        renta_exenta=beneficios - deducciones,
        base=base,
        base_uvt=base_uvt,
        retencion=retencion,
    )


retencion_salarios = register(
    Tool(
        slug="retencion-salarios",
        title="Retencion en la fuente por salarios 2026",
        subtitle="Depuracion y retencion del mes con la tabla del Art. 383 ET y UVT 2026.",
        input_schema=RetencionSalariosInput,
        output_schema=RetencionSalariosResult,
        compute=compute,
    )
)
