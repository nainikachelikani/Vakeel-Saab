"""Database initialization utilities."""

import logging
from sqlalchemy.orm import Session

from app.database.base import Base
from app.database.session import engine

# Import all models to ensure they are registered on the Base metadata
from app.models.user import User  # noqa
from app.models.document import Document  # noqa
from app.models.conversation import Conversation  # noqa
from app.models.message import Message  # noqa
from app.models.report import Report  # noqa
from app.models.citation import Citation  # noqa
from app.models.notification import Notification  # noqa
from app.models.agent_execution import AgentExecution  # noqa

logger = logging.getLogger("vakeelsaab")


def init_db(db: Session = None) -> None:
    """Initialize the database by creating tables.

    Note: In a production environment, Alembic migrations should be used.
    This creates tables directly based on SQLAlchemy metadata.
    """
    try:
        logger.info("Creating database tables from metadata...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables initialized successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
        raise e
