"""Document repository - data access layer for Document model."""

from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    """Repository for Document CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, document_id: UUID) -> Optional[Document]:
        return self.db.query(Document).filter(Document.id == document_id).first()

    def get_by_owner(self, owner_id: UUID, skip: int = 0, limit: int = 100) -> List[Document]:
        return self.db.query(Document).filter(Document.owner_id == owner_id).offset(skip).limit(limit).all()

    def create(self, **kwargs) -> Document:
        document = Document(**kwargs)
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def update(self, document_id: UUID, **kwargs) -> Optional[Document]:
        document = self.get_by_id(document_id)
        if document:
            for key, value in kwargs.items():
                setattr(document, key, value)
            self.db.commit()
            self.db.refresh(document)
        return document

    def delete(self, document_id: UUID) -> bool:
        document = self.get_by_id(document_id)
        if document:
            self.db.delete(document)
            self.db.commit()
            return True
        return False
