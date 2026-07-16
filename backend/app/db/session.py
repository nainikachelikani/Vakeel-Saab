"""Backward compatibility shim for app.db.session."""

from app.database.session import SessionLocal, get_db

__all__ = ["SessionLocal", "get_db"]
