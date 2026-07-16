"""Report database model."""

import uuid
from sqlalchemy import Column, String, Text, ForeignKey, JSON, DateTime, func
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, synonym

from app.db.base import Base, TimestampMixin


class Report(Base, TimestampMixin):
    """Generated report model."""

    __tablename__ = "reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("uploaded_documents.id"), nullable=True, index=True)
    report_type = Column(
        SAEnum("risk_analysis", "compliance_audit", "contract_summary", "legal_brief", "case_analysis",
               name="report_type"),
        nullable=False,
    )
    summary = Column(Text, nullable=True)
    generated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Synonyms for compatibility
    title = Column(String(500), nullable=True)
    content = Column(Text, nullable=True)
    status = Column(
        SAEnum("generating", "completed", "failed", name="report_status"),
        default="generating",
        nullable=False,
    )
    metadata_ = Column("metadata", JSON, nullable=True)

    # Relationships
    user = relationship("User", back_populates="reports")
    document = relationship("UploadedDocument", back_populates="reports")

    def __repr__(self) -> str:
        return f"<Report {self.report_type} id={self.id}>"
