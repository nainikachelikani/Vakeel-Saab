"""Reusable FastAPI authentication and authorization dependencies.

Every dependency in this module is a pure, injectable callable so that:
- The auth router, future agent routers, and middleware can share them.
- Tests can override them via ``app.dependency_overrides`` without
  touching the database or producing real tokens.
- Adding RBAC or claims-based auth later requires only adding a new
  dependency here, not touching individual routers.

Usage in a router::

    from app.core.dependencies import get_current_active_user, require_role

    @router.get("/admin-only")
    def admin_view(user: User = Depends(require_role("admin"))):
        ...
"""

from typing import Callable
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.database.session import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository

# ---------------------------------------------------------------------------
# OAuth2 scheme
# ---------------------------------------------------------------------------

# Points to the login endpoint so Swagger's "Authorize" button works correctly.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ---------------------------------------------------------------------------
# Core dependency: resolve token → User
# ---------------------------------------------------------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Resolve a Bearer access token to the corresponding ``User`` row.

    Raises:
        HTTPException 401: If the token is missing, expired, malformed,
            carries the wrong type, or the embedded user ID does not
            exist in the database.

    Returns:
        The authenticated ``User`` ORM object.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Decode and validate the access token
    payload = decode_token(token, expected_type="access")
    if payload is None:
        raise credentials_exception

    # Extract subject (user ID stored as string UUID)
    subject: str | None = payload.get("sub")
    if subject is None:
        raise credentials_exception

    # Resolve user from database
    try:
        user_id = UUID(subject)
    except ValueError:
        raise credentials_exception

    repo = UserRepository(db)
    user = repo.get_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user


# ---------------------------------------------------------------------------
# Derived dependency: active user gate
# ---------------------------------------------------------------------------

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """Extend :func:`get_current_user` by asserting the account is active.

    Raises:
        HTTPException 403: If ``user.is_active`` is ``False`` (account
            disabled by an administrator).

    Returns:
        The authenticated, active ``User`` ORM object.
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled. Contact support.",
        )
    return current_user


# ---------------------------------------------------------------------------
# Role-based dependency factory
# ---------------------------------------------------------------------------

def require_role(*allowed_roles: str) -> Callable[[User], User]:
    """Return a FastAPI dependency that enforces role-based access control.

    Accepts one or more role strings.  The dependency will pass if the
    authenticated user holds **any** of the listed roles, enabling
    flexible multi-role gates.

    Args:
        *allowed_roles: One or more role strings (e.g. ``"admin"``,
            ``"professional"``, ``"citizen"``).

    Returns:
        A FastAPI-compatible dependency callable.

    Example::

        @router.delete("/users/{id}")
        def delete_user(user: User = Depends(require_role("admin"))):
            ...

        @router.get("/dashboard")
        def dashboard(user: User = Depends(require_role("admin", "professional"))):
            ...
    """
    def _role_gate(current_user: User = Depends(get_current_active_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"Access denied. Required role: {' or '.join(allowed_roles)}. "
                    f"Your role: {current_user.role}."
                ),
            )
        return current_user

    return _role_gate
