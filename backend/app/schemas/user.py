"""User Pydantic schemas.

All original schemas are preserved exactly for backward compatibility.
New schemas required by the auth module are appended below the existing
definitions.
"""

from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID


# ---------------------------------------------------------------------------
# Existing schemas (preserved, no modifications)
# ---------------------------------------------------------------------------

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str = "citizen"
    organization: Optional[str] = None

    @field_validator("role")
    @classmethod
    def validate_role(cls, v: str) -> str:
        allowed = {"citizen", "professional", "admin"}
        if v not in allowed:
            raise ValueError(f"role must be one of {allowed}")
        return v

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("password must be at least 8 characters")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str
    role: str
    avatar_url: Optional[str] = None
    organization: Optional[str] = None
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    organization: Optional[str] = None


class TokenResponse(BaseModel):
    """Full token response returned on registration and login."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int  # access token lifetime in seconds
    user: UserResponse


# ---------------------------------------------------------------------------
# New schemas added for authentication module
# ---------------------------------------------------------------------------

class RefreshRequest(BaseModel):
    """Request body for the token refresh endpoint."""
    refresh_token: str


class AccessTokenResponse(BaseModel):
    """Slim token response returned by the refresh endpoint."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int  # seconds until the new access token expires


class MessageResponse(BaseModel):
    """Generic single-message response (used by logout and similar endpoints)."""
    message: str
