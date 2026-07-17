"""Authentication service — real implementation.

Encapsulates all business logic for authentication so that the auth
router stays thin (HTTP concerns only) and this service remains usable
by future agent workflows, middleware, or other consumers that need
to authenticate users programmatically without going through HTTP.

Design decisions:
- Synchronous (no ``async``) to match the synchronous SQLAlchemy session
  pattern used throughout the existing repository layer.
- Takes ``db: Session`` as an explicit parameter (not stored on the
  instance) so a single ``AuthService()`` instance can safely be shared
  without holding a long-lived database connection.
- Token pair generation is extracted to a private helper to avoid
  duplication between ``register`` and ``login``.
- ``logout`` is a structural placeholder that returns a message string.
  When a Redis token blacklist or a ``refresh_tokens`` table is added,
  only this method needs to change — the router and tests remain stable.
"""

from typing import Dict, Any

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    get_access_token_expire_seconds,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:
    """Handles user authentication and JWT token lifecycle.

    Instantiate without arguments; pass ``db`` to each method call::

        service = AuthService()
        result = service.register(user_data, db=db_session)
    """

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(self, user_data: UserCreate, db: Session) -> Dict[str, Any]:
        """Register a new user account.

        Validates that the email is not already taken, hashes the
        supplied password with bcrypt, persists the new user row, and
        immediately returns a JWT token pair so the client is logged in
        after registration without a second round-trip.

        Args:
            user_data: Validated ``UserCreate`` payload from the request.
            db: Active SQLAlchemy session provided by ``get_db``.

        Returns:
            A dict matching the ``TokenResponse`` schema.

        Raises:
            HTTPException 409: If a user with the same email already exists.
        """
        repo = UserRepository(db)

        # Duplicate email check
        if repo.get_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An account with this email already exists.",
            )

        # Create user — never store the plain-text password
        user: User = repo.create(
            email=user_data.email,
            name=user_data.full_name,          # maps to User.name column
            password_hash=get_password_hash(user_data.password),
            role=user_data.role,
            organization=user_data.organization,
            is_active=True,
            is_verified=False,
        )

        return self._build_token_pair(user)

    # ------------------------------------------------------------------
    # Login
    # ------------------------------------------------------------------

    def login(self, email: str, password: str, db: Session) -> Dict[str, Any]:
        """Authenticate a user with email and password.

        Args:
            email: User-supplied email address.
            password: Plain-text password to verify against the stored hash.
            db: Active SQLAlchemy session.

        Returns:
            A dict matching the ``TokenResponse`` schema.

        Raises:
            HTTPException 401: If the email is not found or the password
                does not match.  A single generic error message is used
                deliberately to avoid user enumeration.
        """
        repo = UserRepository(db)
        user = repo.get_by_email(email)

        # Generic error for both "not found" and "wrong password" to
        # prevent user enumeration through different error messages.
        _invalid = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

        if user is None:
            raise _invalid

        if not verify_password(password, user.password_hash):
            raise _invalid

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account is disabled. Contact support.",
            )

        return self._build_token_pair(user)

    # ------------------------------------------------------------------
    # Token refresh
    # ------------------------------------------------------------------

    def refresh(self, refresh_token: str, db: Session) -> Dict[str, Any]:
        """Issue a new access token given a valid refresh token.

        Args:
            refresh_token: The refresh JWT previously issued on login.
            db: Active SQLAlchemy session.

        Returns:
            A dict matching the ``AccessTokenResponse`` schema.

        Raises:
            HTTPException 401: If the refresh token is invalid, expired,
                or carries the wrong token type.
        """
        from app.core.security import decode_token
        from uuid import UUID

        _invalid = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

        payload = decode_token(refresh_token, expected_type="refresh")
        if payload is None:
            raise _invalid

        subject: str | None = payload.get("sub")
        if subject is None:
            raise _invalid

        try:
            user_id = UUID(subject)
        except ValueError:
            raise _invalid

        repo = UserRepository(db)
        user = repo.get_by_id(user_id)
        if user is None or not user.is_active:
            raise _invalid

        # Issue a fresh access token
        access_token = create_access_token(
            data={"sub": str(user.id), "role": user.role}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": get_access_token_expire_seconds(),
        }

    # ------------------------------------------------------------------
    # Logout
    # ------------------------------------------------------------------

    def logout(self, refresh_token: str | None = None) -> Dict[str, str]:
        """Invalidate a user session.

        Current implementation is a structural placeholder that satisfies
        the API contract.  When a token blacklist is introduced (e.g.
        a Redis set or a ``revoked_tokens`` table) this method is the
        single insertion point — the router, schemas, and tests do not
        need to change.

        Args:
            refresh_token: The refresh token to revoke.  Accepted now so
                the signature is stable for future blacklist integration.

        Returns:
            A dict with a ``message`` key confirming logout.

        Future:
            - Redis: ``redis_client.sadd("revoked_tokens", refresh_token)``
            - DB table: ``RevokedToken(token=refresh_token, revoked_at=now)``
        """
        # TODO: Blacklist ``refresh_token`` in Redis or a revoked_tokens table.
        return {"message": "Successfully logged out."}

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _build_token_pair(self, user: User) -> Dict[str, Any]:
        """Build the standard token-pair response dict for a given user.

        Centralises token creation so register and login always produce
        identical response shapes.

        Args:
            user: Authenticated / newly-created ``User`` ORM object.

        Returns:
            A dict ready to be returned as a ``TokenResponse``.
        """
        payload = {"sub": str(user.id), "role": user.role}

        access_token = create_access_token(data=payload)
        refresh_token = create_refresh_token(data=payload)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": get_access_token_expire_seconds(),
            "user": user,
        }
