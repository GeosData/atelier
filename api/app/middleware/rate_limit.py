import time
from collections import defaultdict, deque

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import get_settings

_WINDOW_SECONDS = 60
_SWEEP_THRESHOLD = 10_000


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)
        self._hits: dict[str, deque[float]] = defaultdict(deque)

    async def dispatch(self, request: Request, call_next):
        if request.method != "POST":
            return await call_next(request)

        limit = get_settings().rate_limit_per_minute
        client = request.client.host if request.client else "unknown"
        now = time.monotonic()
        if len(self._hits) > _SWEEP_THRESHOLD:
            self._sweep(now)
        window = self._hits[client]
        while window and now - window[0] > _WINDOW_SECONDS:
            window.popleft()
        if len(window) >= limit:
            return JSONResponse({"detail": "rate limit exceeded"}, status_code=429)
        window.append(now)
        return await call_next(request)

    def _sweep(self, now: float) -> None:
        stale = [key for key, hits in self._hits.items() if not hits or now - hits[-1] > _WINDOW_SECONDS]
        for key in stale:
            del self._hits[key]
