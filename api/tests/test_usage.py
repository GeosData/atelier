import asyncio

from app.services import usage


def test_record_is_noop_without_database(monkeypatch):
    monkeypatch.setattr(usage, "_DB_URL", "")
    called = []
    monkeypatch.setattr(usage, "_write", lambda *a: called.append(a))
    asyncio.run(usage.record("receipt"))
    assert called == []


def test_write_failure_is_swallowed(monkeypatch):
    monkeypatch.setattr(usage, "_DB_URL", "postgresql://invalid.invalid/db")
    usage._write("receipt", True)


def test_stats_reports_unavailable_on_database_error(monkeypatch):
    monkeypatch.setattr(usage, "_DB_URL", "postgresql://invalid.invalid/db")
    assert usage.stats() == {"enabled": True, "tools": [], "error": "stats_unavailable"}
