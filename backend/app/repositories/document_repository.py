"""Document repository - data access layer for UploadedDocument model."""

from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.models.document import UploadedDocument


class DocumentRepository:
    """Repository for UploadedDocument CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, document_id: UUID) -> Optional[UploadedDocument]:
        return self.db.query(UploadedDocument).filter(UploadedDocument.id == document_id).first()

    def get_by_owner(self, owner_id: UUID, skip: int = 0, limit: int = 100) -> List[UploadedDocument]:
        return self.db.query(UploadedDocument).filter(UploadedDocument.user_id == owner_id).offset(skip).limit(limit).all()

    def create(self, **kwargs) -> UploadedDocument:
        document = UploadedDocument(**kwargs)
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def update(self, document_id: UUID, **kwargs) -> Optional[UploadedDocument]:
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
