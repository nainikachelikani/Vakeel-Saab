"""Authentication API router.

Exposes all auth endpoints under the ``/api/v1/auth`` prefix (set in
``main.py``).  This router is intentionally thin — each handler
delegates immediately to ``AuthService`` so the business logic stays
testable independently of HTTP concerns.

Endpoints
---------
GET  /ping          Health check (preserved from original implementation).
POST /register      Create a new user account; returns JWT token pair.
POST /login         Authenticate and return JWT token pair.
POST /refresh       Exchange a refresh token for a new access token.
POST /logout        Invalidate the current session (structural placeholder).
GET  /me            Protected endpoint — returns the authenticated user's profile.

Swagger documentation is fully automatic via FastAPI's OpenAPI integration:
every endpoint has a ``summary``, ``description``, and explicit
``response_model`` so the generated spec is complete and accurate.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.auth_service import AuthService
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse,
    RefreshRequest,
    AccessTokenResponse,
    MessageResponse,
)
from app.core.dependencies import get_current_active_user
from app.models.user import User

router = APIRouter()

# Module-level service instance — stateless, safe to share
_auth_service = AuthService()


# ---------------------------------------------------------------------------
# Health check (preserved from original implementation)
# ---------------------------------------------------------------------------

@router.get(
    "/ping",
    summary="Authentication health check",
    description="Returns a simple JSON payload confirming the auth router is operational.",
    tags=["Authentication"],
)
@router.get("/api/auth/ping", include_in_schema=False)  # backward-compat alias
async def ping():
    """Dummy health check for the authentication service."""
    return {"message": "Auth API working"}


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

@router.post(
    "/register",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description=(
        "Creates a new user account in PostgreSQL with a bcrypt-hashed password. "
        "Returns a JWT access token and refresh token so the client is immediately "
        "authenticated after registration.\n\n"
        "**Roles accepted:** `citizen` (default), `professional`, `admin`.\n\n"
        "**Password rules:** minimum 8 characters."
    ),
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    """Register a new user account and return JWT tokens.

    - **email**: Must be a valid, unique email address.
    - **password**: Minimum 8 characters; stored as bcrypt hash.
    - **full_name**: Display name for the user.
    - **role**: One of `citizen`, `professional`, `admin` (default: `citizen`).
    - **organization**: Optional affiliated organisation name.
    """
    return _auth_service.register(user_data, db=db)


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Login with email and password",
    description=(
        "Verifies the supplied credentials against the stored bcrypt hash. "
        "Returns a JWT access token (short-lived) and a refresh token "
        "(long-lived) on success.\n\n"
        "A generic *'Invalid email or password'* error is returned for both "
        "unrecognised emails and wrong passwords to prevent user enumeration."
    ),
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    """Authenticate with email + password and receive JWT tokens.

    - **email**: Registered email address.
    - **password**: Plain-text password (transmitted over HTTPS only).
    """
    return _auth_service.login(
        email=credentials.email,
        password=credentials.password,
        db=db,
    )


# ---------------------------------------------------------------------------
# Token refresh
# ---------------------------------------------------------------------------

@router.post(
    "/refresh",
    response_model=AccessTokenResponse,
    summary="Refresh access token",
    description=(
        "Accepts a valid refresh token and issues a new short-lived access "
        "token.  The refresh token itself is **not** rotated on this endpoint "
        "(stateless design); rotation can be layered in when a token blacklist "
        "is introduced.\n\n"
        "Returns HTTP 401 if the refresh token is expired, tampered with, or "
        "carries the wrong token type."
    ),
)
def refresh_token(
    body: RefreshRequest,
    db: Session = Depends(get_db),
):
    """Exchange a refresh token for a new access token.

    - **refresh_token**: The refresh JWT obtained from `/login` or `/register`.
    """
    return _auth_service.refresh(body.refresh_token, db=db)


# ---------------------------------------------------------------------------
# Logout
# ---------------------------------------------------------------------------

@router.post(
    "/logout",
    response_model=MessageResponse,
    summary="Logout and invalidate session",
    description=(
        "Signals the end of the user's session.  Currently a structural "
        "placeholder — the response is always HTTP 200.  When a Redis token "
        "blacklist or a `revoked_tokens` table is added, only the service "
        "layer changes; this endpoint signature remains stable.\n\n"
        "Best practice: the client should **always** discard the stored "
        "access and refresh tokens on logout regardless of this response."
    ),
)
def logout(body: RefreshRequest):
    """Logout and invalidate the refresh token.

    - **refresh_token**: The refresh JWT to revoke (stored for future blacklist use).
    """
    return _auth_service.logout(refresh_token=body.refresh_token)


# ---------------------------------------------------------------------------
# Protected route — GET /me
# ---------------------------------------------------------------------------

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current authenticated user",
    description=(
        "Returns the profile of the user identified by the Bearer access "
        "token in the `Authorization` header.\n\n"
        "Use this endpoint to verify that authentication is working correctly "
        "and to populate the client's user state after login.\n\n"
        "Returns HTTP 401 if no token is provided or the token is invalid, "
        "and HTTP 403 if the account has been disabled."
    ),
)
def get_me(
    current_user: User = Depends(get_current_active_user),
):
    """Return the authenticated user's profile.

    Requires a valid Bearer access token in the `Authorization` header.
    """
    return current_user
