"""Chat Pydantic schemas."""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[UUID] = None
    category: Optional[str] = None  # civil, criminal, family, property


class MessageResponse(BaseModel):
    id: UUID
    content: str
    role: str
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ChatResponse(BaseModel):
    message: MessageResponse
    conversation_id: UUID
    agent_executions: List[Dict[str, Any]] = []
    citations: List[Dict[str, Any]] = []
    suggested_questions: List[str] = []


class ConversationResponse(BaseModel):
    id: UUID
    title: str
    status: str
    category: Optional[str] = None
    last_message: Optional[str] = None
    message_count: int = 0
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
