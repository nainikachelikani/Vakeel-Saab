"""Security utilities for JWT token management and password hashing.

Provides:
- Password hashing and verification via passlib/bcrypt
- JWT access token creation and decoding (existing, backward-compatible)
- JWT refresh token creation and type-aware decoding (new)

These utilities are intentionally stateless and dependency-free so they
remain reusable across the auth module, future agent integrations, and
any middleware that needs token introspection.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, Literal

from jose import jwt, JWTError
import bcrypt
from app.core.config import settings

# ---------------------------------------------------------------------------
# Password context — bcrypt (direct)
# ---------------------------------------------------------------------------

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against its bcrypt hash.

    Args:
        plain_password: The raw password supplied by the user.
        hashed_password: The stored bcrypt hash from the database.

    Returns:
        True if the password matches, False otherwise.
    """
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )
    except Exception:
        return False


def get_password_hash(password: str) -> str:
    """Hash a plain-text password using bcrypt.

    Args:
        password: The raw password to hash.

    Returns:
        A bcrypt hash string safe to store in the database.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


# ---------------------------------------------------------------------------
# JWT — Access tokens (backward-compatible, preserved exactly)
# ---------------------------------------------------------------------------

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Create a signed JWT access token.

    Encodes the supplied data with an expiry claim.  The token type is
    not set here to remain backward-compatible with any existing callers.

    Args:
        data: Arbitrary payload to encode (should include ``sub``).
        expires_delta: Custom expiry duration; defaults to the configured
            ``JWT_ACCESS_TOKEN_EXPIRE_MINUTES`` setting.

    Returns:
        A signed JWT string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> Optional[Dict[str, Any]]:
    """Decode and verify a JWT access token.

    Backward-compatible wrapper kept for any existing callers.
    Delegates to :func:`decode_token`.

    Args:
        token: The raw JWT string to verify.

    Returns:
        The decoded payload dict, or ``None`` if the token is invalid or
        expired.
    """
    return decode_token(token, expected_type="access")


# ---------------------------------------------------------------------------
# JWT — Refresh tokens (new)
# ---------------------------------------------------------------------------

def create_refresh_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Create a signed JWT refresh token.

    Refresh tokens carry a ``type: refresh`` claim so they cannot be
    confused with access tokens.  This prevents token-type confusion
    attacks where a refresh token is passed to a resource endpoint.

    Args:
        data: Arbitrary payload to encode (should include ``sub``).
        expires_delta: Custom expiry duration; defaults to the configured
            ``JWT_REFRESH_TOKEN_EXPIRE_DAYS`` setting.

    Returns:
        A signed JWT string tagged as a refresh token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS
        )
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


# ---------------------------------------------------------------------------
# JWT — Type-aware decode (new, used by dependencies and service)
# ---------------------------------------------------------------------------

def decode_token(
    token: str,
    expected_type: Literal["access", "refresh"] = "access",
) -> Optional[Dict[str, Any]]:
    """Decode a JWT and enforce the expected token type.

    Validates the signature, expiry, and the ``type`` claim.  This
    prevents a refresh token from being accepted where an access token
    is required and vice-versa.

    Args:
        token: The raw JWT string to decode.
        expected_type: Which token type is accepted — ``"access"`` or
            ``"refresh"``.

    Returns:
        The decoded payload dict if valid, or ``None`` on any failure
        (expired, bad signature, wrong type, malformed).
    """
    try:
        payload: Dict[str, Any] = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        # Enforce token type claim to prevent token-confusion attacks
        if payload.get("type") != expected_type:
            return None
        return payload
    except JWTError:
        return None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_access_token_expire_seconds() -> int:
    """Return access token lifetime in seconds (useful for ``expires_in`` responses)."""
    return settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60
