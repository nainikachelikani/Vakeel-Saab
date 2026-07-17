"""
Core package exports.

This package re-exports the application settings from the single
source of truth located in app.config.settings.
"""

from app.config.settings import Settings, settings

__all__ = ["Settings", "settings"]