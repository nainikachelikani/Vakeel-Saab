"""Backward compatibility shim for app.core.database."""

from app.database.session import engine, SessionLocal, get_db

__all__ = ["engine", "SessionLocal", "get_db"]
