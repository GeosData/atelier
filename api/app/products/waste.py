from pydantic import BaseModel, Field

from app.products.registry import InputKind, Product, register


class WasteClassification(BaseModel):
    item: str | None = Field(default=None, description="What the object appears to be")
    category: str = Field(description="One of: reciclable, organico, no_aprovechable, peligroso")
    bin_color: str | None = Field(default=None, description="Blanco, verde or negro per Colombian standard")
    instructions: str | None = Field(default=None, description="How to prepare it before disposal")
    confidence: float = Field(ge=0, le=1)
    notes: str | None = Field(default=None, description="Set when the image is unclear")


waste = register(
    Product(
        slug="waste",
        title="Clasificador de residuos por foto",
        input_kind=InputKind.image,
        prompt=(
            "You classify a household or business waste item from a photo, following the Colombian "
            "three-bin standard: blanco = aprovechable/reciclable, verde = organico, negro = no aprovechable; "
            "peligroso for hazardous items. Return the category, the bin color, and short preparation "
            "instructions. If the object is ambiguous lower the confidence and explain in notes."
        ),
        output_schema=WasteClassification,
        accepted_mime=("image/jpeg", "image/png", "image/webp"),
        subtitle="Foto de un residuo y te dice en que caneca va y como separarlo.",
    )
)
