"""FastAPI dependency injection utilities."""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token

security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    """Get the current authenticated user from JWT token.

    Placeholder: Returns a mock user for development.
    """
    # TODO: Implement actual token verification
    # For now, return a mock user
    return {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "email": "rajesh@lawfirm.com",
        "full_name": "Rajesh Kumar",
        "role": "citizen",
    }


async def require_role(required_role: str):
    """Dependency that checks if the user has the required role."""
    async def _check_role(user=Depends(get_current_user)):
        if user["role"] != required_role and user["role"] != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user
    return _check_role
