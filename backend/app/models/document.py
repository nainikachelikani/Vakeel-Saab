"""Document database model."""

import uuid
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, JSON
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Document(Base, TimestampMixin):
    """Legal document model."""

    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    file_name = Column(String(500), nullable=False)
    file_path = Column(String(1000), nullable=False)
    file_type = Column(String(50), nullable=False)  # pdf, docx, txt
    file_size = Column(Integer, nullable=False)  # in bytes
    document_type = Column(
        SAEnum("contract", "judgment", "complaint", "notice", "agreement", "nda", "policy", "other",
               name="document_type"),
        default="other",
        nullable=False,
    )
    status = Column(
        SAEnum("pending", "processing", "analyzed", "error", name="document_status"),
        default="pending",
        nullable=False,
    )
    summary = Column(Text, nullable=True)
    risk_score = Column(Float, nullable=True)
    metadata_ = Column("metadata", JSON, nullable=True)
    page_count = Column(Integer, nullable=True)
    language = Column(String(10), default="en", nullable=False)

    # Foreign keys
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relationships
    owner = relationship("User", back_populates="documents")
    citations = relationship("Citation", back_populates="document", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<Document {self.title}>"
