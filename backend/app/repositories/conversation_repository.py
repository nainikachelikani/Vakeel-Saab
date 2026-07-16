"""Conversation repository - data access layer for Conversation model."""

from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.models.conversation import Conversation


class ConversationRepository:
    """Repository for Conversation CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, conversation_id: UUID) -> Optional[Conversation]:
        return self.db.query(Conversation).filter(Conversation.id == conversation_id).first()

    def get_by_user(self, user_id: UUID, skip: int = 0, limit: int = 50) -> List[Conversation]:
        return self.db.query(Conversation).filter(Conversation.user_id == user_id).order_by(
            Conversation.updated_at.desc()
        ).offset(skip).limit(limit).all()

    def create(self, **kwargs) -> Conversation:
        conversation = Conversation(**kwargs)
        self.db.add(conversation)
        self.db.commit()
        self.db.refresh(conversation)
        return conversation

    def update(self, conversation_id: UUID, **kwargs) -> Optional[Conversation]:
        conversation = self.get_by_id(conversation_id)
        if conversation:
            for key, value in kwargs.items():
                setattr(conversation, key, value)
            self.db.commit()
            self.db.refresh(conversation)
        return conversation
