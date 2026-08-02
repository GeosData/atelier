from pydantic import BaseModel, Field

from app.products.registry import InputKind, Product, register


class Treatment(BaseModel):
    approach: str = Field(description="organico or quimico")
    action: str
    caution: str | None = Field(default=None, description="Dosage or safety note")


class CropDiagnosis(BaseModel):
    crop: str | None = Field(default=None, description="Crop guessed from the image if any")
    diagnosis: str = Field(description="Pest or disease, or 'sano' if healthy")
    also_possible: str | None = Field(default=None, description="Second hypothesis")
    severity: str | None = Field(default=None, description="leve, moderado or severo")
    treatments: list[Treatment] = Field(default_factory=list)
    prevention: str | None = None
    confidence: float = Field(ge=0, le=1)
    notes: str | None = Field(
        default=None,
        description="Set when the leaf is unclear or a real agronomist should confirm",
    )


CARIBBEAN_CROP_GUIDE = (
    "Common issues in Cordoba/Caribbean Colombia crops:\n"
    "- Platano/banano: sigatoka negra (manchas alargadas negras en hojas), moko "
    "(marchitez bacteriana, pudricion interna), picudo negro.\n"
    "- Maiz: mancha de asfalto, roya, gusano cogollero (Spodoptera), pudricion de mazorca.\n"
    "- Name: antracnosis (manchas necroticas), pudricion del tuberculo.\n"
    "- Sandia/melon: alternariosis, mildeo, mosca blanca.\n"
    "Prefer agroinsumos available in Colombian agro shops. Always add a safety/dosage caution "
    "and recommend confirming with an agronomo when severity is high."
)


crop = register(
    Product(
        slug="crop",
        title="Diagnostico de cultivo por foto",
        input_kind=InputKind.image,
        prompt=(
            "You are an agronomic assistant for small farmers in Cordoba, Colombia. From a photo of a "
            "leaf, fruit or plant, identify the most likely pest or disease (or 'sano'), give a second "
            "hypothesis if relevant, estimate severity, and propose concrete treatments (organic and "
            "chemical) with dosage/safety cautions. If the image is unclear, lower confidence and say so."
        ),
        output_schema=CropDiagnosis,
        accepted_mime=("image/jpeg", "image/png", "image/webp"),
        context=CARIBBEAN_CROP_GUIDE,
        subtitle="Foto de la hoja o el fruto y te dice que plaga o enfermedad tiene y como tratarla.",
    )
)
