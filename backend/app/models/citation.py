"""Citation database model."""

import uuid
from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Citation(Base, TimestampMixin):
    """Legal citation model."""

    __tablename__ = "citations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    source = Column(String(500), nullable=False)  # e.g., "Supreme Court of India"
    reference = Column(String(255), nullable=False)  # e.g., "AIR 2023 SC 456"
    excerpt = Column(Text, nullable=True)
    relevance_score = Column(Integer, nullable=True)  # 0-100
    year = Column(Integer, nullable=True)
    jurisdiction = Column(String(100), nullable=True)

    # Foreign keys
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=True)

    # Relationships
    document = relationship("Document", back_populates="citations")

    def __repr__(self) -> str:
        return f"<Citation {self.reference}>"
