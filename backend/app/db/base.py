"""Backward compatibility shim for app.db.base."""

from app.database.base import Base, TimestampMixin

__all__ = ["Base", "TimestampMixin"]
