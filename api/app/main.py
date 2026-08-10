from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.products  # noqa: F401
from app.config import get_settings
from app.middleware.rate_limit import RateLimitMiddleware
from app.routes.process import router
from app.services import usage


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title="Atelier")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(RateLimitMiddleware)
    application.include_router(router)

    @application.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    @application.get("/stats")
    def stats() -> dict:
        return usage.stats()

    return application


app = create_app()
