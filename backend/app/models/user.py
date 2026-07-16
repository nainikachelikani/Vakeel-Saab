"""User database model."""

import uuid
from sqlalchemy import Column, String, Boolean, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, synonym

from app.db.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    """User account model."""

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(
        SAEnum("citizen", "professional", "admin", name="user_role"),
        default="citizen",
        nullable=False,
    )
    preferred_language = Column(String(50), default="en", nullable=False)

    # Backward compatibility synonyms
    full_name = synonym("name")
    hashed_password = synonym("password_hash")

    # Backward compatibility columns
    avatar_url = Column(String(500), nullable=True)
    organization = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    # Relationships
    uploaded_documents = relationship(
        "UploadedDocument",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    # Backward compatibility relationship alias
    @property
    def documents(self):
        return self.uploaded_documents

    conversations = relationship(
        "Conversation",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    reports = relationship(
        "Report",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    notifications = relationship(
        "Notification",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    def __repr__(self) -> str:
        return f"<User {self.email}>"
