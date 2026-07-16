"""Backward compatibility shim for logging services."""

from app.config.logging import logger, setup_logging

__all__ = ["logger", "setup_logging"]
