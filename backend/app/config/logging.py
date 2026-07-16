"""Logging configuration for the application."""

import logging
import sys
from app.config.settings import settings


def setup_logging(level: str = None) -> logging.Logger:
    """Configure and return the application logger."""
    if level is None:
        level = "DEBUG" if settings.APP_DEBUG else "INFO"

    logger = logging.getLogger("vakeelsaab")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Avoid duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = setup_logging()
