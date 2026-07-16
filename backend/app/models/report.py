"""Report database model."""

import uuid
from sqlalchemy import Column, String, Text, ForeignKey, JSON
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base, TimestampMixin


class Report(Base, TimestampMixin):
    """Generated report model."""

    __tablename__ = "reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    report_type = Column(
        SAEnum("risk_analysis", "compliance_audit", "contract_summary", "legal_brief", "case_analysis",
               name="report_type"),
        nullable=False,
    )
    content = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    status = Column(
        SAEnum("generating", "completed", "failed", name="report_status"),
        default="generating",
        nullable=False,
    )
    metadata_ = Column("metadata", JSON, nullable=True)

    # Foreign keys
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="reports")

    def __repr__(self) -> str:
        return f"<Report {self.title}>"
