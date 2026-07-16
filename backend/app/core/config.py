"""Backward compatibility shim for application settings."""

from app.config.settings import Settings, settings

__all__ = ["Settings", "settings"]
