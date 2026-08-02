from typing import Literal

from pydantic import BaseModel, Field

from app.tools.registry import Tool, register

UVT = 52374
CONCEPTS = {
    "compra": {"label": "Compra de bienes o productos", "base_uvt": 10, "decl": 0.025, "no_decl": 0.035, "usa_decl": True},
    "servicio": {"label": "Servicios generales", "base_uvt": 2, "decl": 0.04, "no_decl": 0.06, "usa_decl": True},
    "honorarios": {"label": "Honorarios y comisiones", "base_uvt": 0, "decl": 0.11, "no_decl": 0.1, "usa_decl": True},
    "arrInmueble": {"label": "Arrendamiento de inmueble", "base_uvt": 10, "decl": 0.035, "no_decl": 0.035, "usa_decl": False},
    "arrMueble": {"label": "Arrendamiento de bien mueble", "base_uvt": 0, "decl": 0.04, "no_decl": 0.04, "usa_decl": False},
}


class RetencionPagosInput(BaseModel):
    concept: Literal["compra", "servicio", "honorarios", "arrInmueble", "arrMueble"] = Field(default="compra")
    amount: float = Field(gt=0, description="Valor del pago, antes de IVA (COP)")
    is_declarant: bool = Field(default=True)


class RetencionPagosResult(BaseModel):
    concept_label: str
    base_min: float
    base_uvt: int
    tarifa: float
    applies: bool
    retencion: float


def compute(data: RetencionPagosInput) -> RetencionPagosResult:
    concept = CONCEPTS[data.concept]
    base_min = concept["base_uvt"] * UVT
    tarifa = concept["decl"] if data.is_declarant else concept["no_decl"]
    applies = data.amount >= base_min
    retencion = data.amount * tarifa if applies else 0

    return RetencionPagosResult(
        concept_label=concept["label"],
        base_min=base_min,
        base_uvt=concept["base_uvt"],
        tarifa=tarifa,
        applies=applies,
        retencion=retencion,
    )


retencion_pagos = register(
    Tool(
        slug="retencion-pagos",
        title="Retencion en la fuente por pagos 2026",
        subtitle="Retencion en compras, servicios, honorarios y arrendamientos, con bases y tarifas vigentes.",
        input_schema=RetencionPagosInput,
        output_schema=RetencionPagosResult,
        compute=compute,
    )
)
