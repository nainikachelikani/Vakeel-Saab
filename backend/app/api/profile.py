"""Profile API routes with placeholder implementations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_profile():
    """Get current user profile."""
    return {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "email": "rajesh@lawfirm.com",
        "full_name": "Rajesh Kumar",
        "role": "citizen",
        "avatar_url": None,
        "organization": "Kumar & Associates",
        "is_active": True,
        "is_verified": True,
        "stats": {
            "total_documents": 14,
            "total_conversations": 23,
            "total_reports": 8,
            "documents_analyzed": 11,
            "active_cases": 3,
        },
        "preferences": {
            "language": "en",
            "theme": "light",
            "notifications_enabled": True,
            "email_notifications": True,
        },
        "created_at": "2024-01-15T10:30:00Z",
    }


@router.patch("")
async def update_profile(data: dict):
    """Update user profile."""
    return {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "email": "rajesh@lawfirm.com",
        "full_name": data.get("full_name", "Rajesh Kumar"),
        "role": "citizen",
        "message": "Profile updated successfully",
    }
