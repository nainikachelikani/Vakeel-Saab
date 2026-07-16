"""Agent execution database model."""

import uuid
from sqlalchemy import Column, String, Text, Integer, Float, ForeignKey, JSON
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base, TimestampMixin


class AgentExecution(Base, TimestampMixin):
    """Agent execution log model."""

    __tablename__ = "agent_executions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    agent_type = Column(
        SAEnum("router", "domain", "retrieval", "legal_analysis", "citation", "planner", "reviewer",
               name="agent_type"),
        nullable=False,
    )
    status = Column(
        SAEnum("pending", "running", "completed", "failed", name="execution_status"),
        default="pending",
        nullable=False,
    )
    input_data = Column(JSON, nullable=True)
    output_data = Column(JSON, nullable=True)
    error_message = Column(Text, nullable=True)
    duration_ms = Column(Integer, nullable=True)
    tokens_used = Column(Integer, nullable=True)
    cost = Column(Float, nullable=True)

    # Foreign keys
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return f"<AgentExecution {self.agent_type} ({self.status})>"
