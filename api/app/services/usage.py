import asyncio
import logging
import os

logger = logging.getLogger("atelier.usage")

_DB_URL = os.environ.get("DATABASE_URL", "").strip()


def _write(slug: str, ok: bool) -> None:
    try:
        import psycopg

        with psycopg.connect(_DB_URL, connect_timeout=5) as conn:
            conn.execute("INSERT INTO tool_usage (slug, ok) VALUES (%s, %s)", (slug, ok))
    except Exception:
        logger.warning("usage write failed for slug=%s", slug)


async def record(slug: str, ok: bool = True) -> None:
    if not _DB_URL:
        return
    try:
        asyncio.get_running_loop().run_in_executor(None, _write, slug, ok)
    except Exception:
        pass


def stats() -> dict:
    if not _DB_URL:
        return {"enabled": False, "tools": []}
    try:
        import psycopg

        with psycopg.connect(_DB_URL, connect_timeout=5) as conn:
            rows = conn.execute(
                "SELECT slug, count(*) AS total, "
                "count(*) FILTER (WHERE ok) AS ok, "
                "count(*) FILTER (WHERE ts > now() - interval '7 days') AS last7 "
                "FROM tool_usage GROUP BY slug ORDER BY total DESC"
            ).fetchall()
        return {
            "enabled": True,
            "tools": [{"slug": r[0], "total": r[1], "ok": r[2], "last7": r[3]} for r in rows],
        }
    except Exception:
        logger.warning("usage stats failed")
        return {"enabled": True, "tools": [], "error": "stats_unavailable"}
