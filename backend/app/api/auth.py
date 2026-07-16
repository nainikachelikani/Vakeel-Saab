"""Authentication API routes with placeholder implementations."""

from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserLogin, TokenResponse, UserResponse
from datetime import datetime
from uuid import UUID

router = APIRouter()

# Mock user data
MOCK_USER = {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "rajesh@lawfirm.com",
    "full_name": "Rajesh Kumar",
    "role": "citizen",
    "avatar_url": None,
    "organization": "Kumar & Associates",
    "is_active": True,
    "is_verified": True,
    "created_at": "2024-01-15T10:30:00Z",
}


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate):
    """Register a new user account."""
    return {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.placeholder_access_token",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.placeholder_refresh_token",
        "token_type": "bearer",
        "user": {
            **MOCK_USER,
            "email": user_data.email,
            "full_name": user_data.full_name,
            "role": user_data.role,
        },
    }


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin):
    """Authenticate a user and return JWT tokens."""
    # Placeholder: accept any credentials
    return {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.placeholder_access_token",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.placeholder_refresh_token",
        "token_type": "bearer",
        "user": MOCK_USER,
    }


@router.post("/logout")
async def logout():
    """Logout user and invalidate tokens."""
    return {"message": "Successfully logged out"}


@router.post("/refresh")
async def refresh_token():
    """Refresh access token."""
    return {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.new_placeholder_access_token",
        "token_type": "bearer",
    }
