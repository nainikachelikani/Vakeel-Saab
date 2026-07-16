"""User repository - data access layer for User model."""

from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """Repository for User CRUD operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def create(self, **kwargs) -> User:
        """Create a new user."""
        user = User(**kwargs)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, user_id: UUID, **kwargs) -> Optional[User]:
        """Update an existing user."""
        user = self.get_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def list_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """List all users with pagination."""
        return self.db.query(User).offset(skip).limit(limit).all()
