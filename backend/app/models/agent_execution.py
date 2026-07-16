"""Agent execution database model."""

import uuid
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, JSON, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import synonym

from app.db.base import Base, TimestampMixin


class AgentExecution(Base, TimestampMixin):
    """Agent execution log model."""

    __tablename__ = "agent_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_id = Column(UUID(as_uuid=True), nullable=True, index=True)
    agent_name = Column(String(255), nullable=False)
    status = Column(
        SAEnum("pending", "running", "completed", "failed", name="execution_status"),
        default="pending",
        nullable=False,
    )
    execution_time = Column(Float, nullable=True)  # execution duration
    confidence = Column(Float, nullable=True)

    # Synonyms for backward compatibility
    agent_type = synonym("agent_name")
    duration_ms = synonym("execution_time")

    # Backward compatibility columns
    input_data = Column(JSON, nullable=True)
    output_data = Column(JSON, nullable=True)
    error_message = Column(Text, nullable=True)
    tokens_used = Column(Integer, nullable=True)
    cost = Column(Float, nullable=True)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    def __repr__(self) -> str:
        return f"<AgentExecution {self.agent_name} ({self.status})>"
