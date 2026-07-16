"""Citation database model."""

import uuid
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Citation(Base, TimestampMixin):
    """Legal citation model."""

    __tablename__ = "citations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id = Column(UUID(as_uuid=True), nullable=True, index=True)
    document_name = Column(String(500), nullable=True)
    page = Column(Integer, nullable=True)
    clause = Column(String(255), nullable=True)
    excerpt = Column(Text, nullable=True)
    confidence = Column(Float, nullable=True)

    # Backward compatibility fields
    title = Column(String(500), nullable=True)
    source = Column(String(500), nullable=True)  # e.g., "Supreme Court of India"
    reference = Column(String(255), nullable=True)  # e.g., "AIR 2023 SC 456"
    relevance_score = Column(Integer, nullable=True)  # 0-100
    year = Column(Integer, nullable=True)
    jurisdiction = Column(String(100), nullable=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("uploaded_documents.id"), nullable=True)

    # Relationships
    document = relationship("UploadedDocument", back_populates="citations")

    def __repr__(self) -> str:
        return f"<Citation {self.id} (Doc: {self.document_name})>"
