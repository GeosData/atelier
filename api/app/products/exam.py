from pydantic import BaseModel, Field

from app.products.registry import InputKind, Product, register


class GradedQuestion(BaseModel):
    number: int | None = None
    prompt: str | None = Field(default=None, description="Question text if legible")
    student_answer: str | None = None
    is_correct: bool | None = None
    difficulty: str = Field(description="One of: facil, media, dificil")
    score: float | None = Field(default=None, description="Points awarded")
    max_score: float | None = None
    feedback: str | None = Field(default=None, description="Short feedback in Spanish")
    mastery_flag: bool = Field(
        default=False,
        description="True when a correct or high-scoring answer likely does not reflect real understanding",
    )
    mastery_reason: str | None = Field(
        default=None,
        description="Spanish, plain language: why the answer looks inconsistent with real mastery",
    )


class ExamReview(BaseModel):
    subject: str | None = None
    student_name: str | None = None
    questions: list[GradedQuestion] = Field(default_factory=list)
    total_score: float | None = None
    max_total: float | None = None
    mastery_alerts: list[str] = Field(
        default_factory=list,
        description="Spanish, teacher-facing alerts such as 'acerto las dificiles y fallo las faciles'",
    )
    overall_mastery_confidence: float = Field(
        ge=0,
        le=1,
        description="How well the grade reflects real mastery: 0 inflated, 1 solid",
    )
    confidence: float = Field(ge=0, le=1)
    notes: str | None = Field(default=None, description="Set when the exam is unreadable")


exam = register(
    Product(
        slug="exam",
        title="Corrige examenes y detecta dominio inflado",
        input_kind=InputKind.image,
        prompt=(
            "You grade a photo of a single student's solved exam and, beyond grading, you judge "
            "whether the grade reflects real mastery. For each question: read the student's answer, "
            "decide if it is correct, rate its difficulty (facil, media, dificil), award a score, and "
            "write short feedback in Spanish. Then run a mastery check: raise mastery_flag on any "
            "answer that is correct or high-scoring but likely does NOT reflect real understanding, "
            "using simple, verifiable signals a teacher can trust: the student got hard items right "
            "while missing easy ones (aberrant pattern), a final answer is correct but the shown work "
            "is absent, wrong, or contradicts it, or the wording looks memorized or copy-pasted rather "
            "than reasoned. Do NOT accuse of AI use; describe the inconsistency. Fill mastery_alerts "
            "with plain Spanish sentences summarizing the pattern for the teacher, and set "
            "overall_mastery_confidence low when the total grade looks inflated. Keep it concrete and "
            "conservative: when in doubt, do not flag. If the exam is unreadable, lower confidence and "
            "explain in notes."
        ),
        output_schema=ExamReview,
        accepted_mime=("image/jpeg", "image/png", "image/webp", "application/pdf"),
        subtitle="Califica por pregunta y avisa cuando la nota no refleja dominio real.",
    )
)
