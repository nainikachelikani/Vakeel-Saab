"""Notification database model."""

import uuid
from sqlalchemy import Column, String, Text, Boolean, ForeignKey, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, synonym

from app.db.base import Base, TimestampMixin


class Notification(Base, TimestampMixin):
    """User notification model."""

    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(
        SAEnum("unread", "read", "archived", name="notification_status"),
        default="unread",
        nullable=False,
    )

    # Synonyms for backward compatibility
    message = synonym("description")

    # Backward compatibility columns
    notification_type = Column(String(50), default="info", nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    action_url = Column(String(500), nullable=True)

    # Relationships
    user = relationship("User", back_populates="notifications")

    def __repr__(self) -> str:
        return f"<Notification {self.title}>"
