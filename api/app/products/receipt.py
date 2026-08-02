from pydantic import BaseModel, Field

from app.products.registry import InputKind, Product, register


class LineItem(BaseModel):
    description: str
    quantity: float | None = None
    unit_price: float | None = None
    amount: float | None = None


class Receipt(BaseModel):
    vendor: str | None = Field(default=None)
    document_number: str | None = None
    issued_at: str | None = Field(default=None, description="ISO date if legible")
    currency: str | None = None
    subtotal: float | None = None
    tax: float | None = None
    total: float | None = None
    line_items: list[LineItem] = Field(default_factory=list)
    confidence: float = Field(ge=0, le=1)
    notes: str | None = Field(default=None, description="Set when data is missing or unreadable")


receipt = register(
    Product(
        slug="receipt",
        title="Factura o recibo a datos",
        input_kind=InputKind.image,
        prompt=(
            "You extract structured accounting data from a photo of an invoice or receipt. "
            "Read every legible field. Amounts are numbers without thousand separators. "
            "Use the currency shown on the document. If a field is unreadable leave it null and "
            "explain in notes. Set confidence to your overall certainty about the totals."
        ),
        output_schema=Receipt,
        accepted_mime=("image/jpeg", "image/png", "image/webp", "application/pdf"),
        subtitle="Foto de una factura o recibo y devuelve los datos listos para tu contabilidad.",
    )
)
