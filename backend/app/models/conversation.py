"""Conversation database model."""

import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Conversation(Base, TimestampMixin):
    """Chat conversation model."""

    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(500), nullable=False)

    # Backward compatibility fields
    status = Column(
        SAEnum("active", "completed", "archived", name="conversation_status"),
        default="active",
        nullable=False,
    )
    category = Column(String(100), nullable=True)  # civil, criminal, family, property

    # Relationships
    user = relationship("User", back_populates="conversations")
    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Message.created_at",
    )

    def __repr__(self) -> str:
        return f"<Conversation {self.title}>"
