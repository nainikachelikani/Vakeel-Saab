"""Document database models."""

import uuid
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, JSON, DateTime, func
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, synonym

from app.db.base import Base, TimestampMixin


class UploadedDocument(Base, TimestampMixin):
    """Uploaded legal document model."""

    __tablename__ = "uploaded_documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    filename = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)  # pdf, docx, txt
    size = Column(Integer, nullable=False)  # in bytes
    storage_path = Column(String(1000), nullable=False)
    status = Column(
        SAEnum("pending", "processing", "analyzed", "error", name="document_status"),
        default="pending",
        nullable=False,
    )

    # Synonyms for backward compatibility
    owner_id = synonym("user_id")
    file_name = synonym("filename")
    file_path = synonym("storage_path")
    file_size = synonym("size")
    uploaded_at = synonym("created_at")

    # Extra/Legacy fields for backward compatibility
    title = Column(String(500), nullable=True)
    document_type = Column(
        SAEnum("contract", "judgment", "complaint", "notice", "agreement", "nda", "policy", "other",
               name="document_type"),
        default="other",
        nullable=True,
    )
    summary = Column(Text, nullable=True)
    risk_score = Column(Float, nullable=True)
    metadata_ = Column("metadata", JSON, nullable=True)
    page_count = Column(Integer, nullable=True)
    language = Column(String(10), default="en", nullable=True)

    # Relationships
    user = relationship("User", back_populates="uploaded_documents")
    # For backward compatibility
    owner = relationship("User", back_populates="uploaded_documents", overlaps="user")
    
    chunks = relationship(
        "DocumentChunk",
        back_populates="document",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    reports = relationship(
        "Report",
        back_populates="document",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    citations = relationship(
        "Citation",
        back_populates="document",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    def __repr__(self) -> str:
        return f"<UploadedDocument {self.filename}>"


# Class alias for backward compatibility
Document = UploadedDocument


class DocumentChunk(Base, TimestampMixin):
    """Document text chunk model for RAG / retrieval."""

    __tablename__ = "document_chunks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = Column(UUID(as_uuid=True), ForeignKey("uploaded_documents.id"), nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    embedding_id = Column(String(255), nullable=True)  # Reference to vector store (optional, no DB foreign key)
    page_number = Column(Integer, nullable=True)

    # Relationships
    document = relationship("UploadedDocument", back_populates="chunks")

    def __repr__(self) -> str:
        return f"<DocumentChunk doc_id={self.document_id} index={self.chunk_index}>"
