"""Notification database model."""

import uuid
from sqlalchemy import Column, String, Text, Boolean, ForeignKey
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Notification(Base, TimestampMixin):
    """User notification model."""

    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    notification_type = Column(
        SAEnum("info", "warning", "success", "error", "document", "report", "system",
               name="notification_type"),
        default="info",
        nullable=False,
    )
    is_read = Column(Boolean, default=False, nullable=False)
    action_url = Column(String(500), nullable=True)

    # Foreign keys
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="notifications")

    def __repr__(self) -> str:
        return f"<Notification {self.title}>"
