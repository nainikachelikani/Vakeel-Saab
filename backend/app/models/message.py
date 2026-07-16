"""Message database model."""

import uuid
from sqlalchemy import Column, String, Text, ForeignKey, JSON
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Message(Base, TimestampMixin):
    """Chat message model."""

    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(Text, nullable=False)
    role = Column(SAEnum("user", "assistant", "system", name="message_role"), nullable=False)
    metadata_ = Column("metadata", JSON, nullable=True)  # agent info, citations, etc.

    # Foreign keys
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=False)

    # Relationships
    conversation = relationship("Conversation", back_populates="messages")

    def __repr__(self) -> str:
        return f"<Message {self.id} ({self.role})>"
