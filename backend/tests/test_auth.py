"""Pytest test suite for the JWT Authentication module.

Test strategy
-------------
- Uses an **in-memory SQLite** database (same pattern as ``test_db.py``)
  so tests run offline without a real PostgreSQL instance.
- The production ``get_db`` dependency is replaced via
  ``app.dependency_overrides`` so every request hits the test database.
- The ``oauth2_scheme`` dependency (Bearer token extraction) is also
  overridable so protected-route tests can inject pre-built tokens
  without going through the login flow.
- No monkey-patching of internal modules — tests exercise the real
  service and repository layers end-to-end.
- Enum types (``user_role``) are handled by SQLite by using
  ``render_as_batch=False`` and native SQLAlchemy Enum rendering which
  falls back to VARCHAR for SQLite.

Coverage
--------
11 test cases:

1.  test_register_success             — 201 + tokens returned
2.  test_register_duplicate_email     — 409 conflict
3.  test_register_invalid_email       — 422 validation
4.  test_register_weak_password       — 422 validation
5.  test_login_success                — 200 + tokens returned
6.  test_login_wrong_password         — 401 unauthorized
7.  test_login_nonexistent_user       — 401 unauthorized
8.  test_refresh_token_valid          — 200 + new access token
9.  test_refresh_token_invalid        — 401 unauthorized
10. test_logout                       — 200 + message
11. test_protected_me_with_token      — 200 + user profile
12. test_protected_me_without_token   — 401 unauthorized
13. test_jwt_payload_structure        — validates sub, type, exp claims
"""

import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

from app.main import app as fastapi_app
from app.database.base import Base
from app.database.session import get_db
import app.models  # noqa: F401 — registers all ORM models on Base.metadata before create_all
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_access_token_expire_seconds,
)

# ---------------------------------------------------------------------------
# In-memory SQLite test database
# ---------------------------------------------------------------------------

# StaticPool forces every SQLAlchemy connection (including those in
# TestClient worker threads) to reuse the exact same in-memory SQLite
# connection, so tables created with create_all() remain visible across
# all threads for the lifetime of the test.
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(name="db_engine", scope="function")
def fixture_db_engine():
    """Create a single-connection in-memory SQLite engine for each test."""
    _engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,  # all calls to connect() return the same connection
    )
    Base.metadata.create_all(bind=_engine)
    yield _engine
    Base.metadata.drop_all(bind=_engine)
    _engine.dispose()


@pytest.fixture(name="client", scope="function")
def fixture_client(db_engine):
    """TestClient whose every request goes through the shared SQLite engine.

    Uses ``dependency_overrides`` to replace the production ``get_db``
    dependency with a session bound to the StaticPool SQLite engine.
    """
    TestSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=db_engine
    )

    def _override_get_db():
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()

    fastapi_app.dependency_overrides[get_db] = _override_get_db
    with TestClient(fastapi_app) as test_client:
        yield test_client
    fastapi_app.dependency_overrides.pop(get_db, None)


# ---------------------------------------------------------------------------
# Shared test data
# ---------------------------------------------------------------------------

VALID_USER = {
    "email": "advocate.sharma@vakeelsaab.com",
    "password": "SecurePass123",
    "full_name": "Advocate Sharma",
    "role": "professional",
    "organization": "Sharma & Associates",
}


def _register(client: TestClient, payload: dict | None = None) -> dict:
    """Helper — register a user and return the parsed JSON response."""
    data = payload or VALID_USER
    response = client.post("/api/v1/auth/register", json=data)
    return response


# ---------------------------------------------------------------------------
# 1. Registration — success
# ---------------------------------------------------------------------------

def test_register_success(client: TestClient):
    """POST /register with valid data should return 201 and a token pair."""
    response = _register(client)

    assert response.status_code == 201, response.text

    body = response.json()
    assert "access_token" in body
    assert "refresh_token" in body
    assert body["token_type"] == "bearer"
    assert body["expires_in"] == get_access_token_expire_seconds()

    user = body["user"]
    assert user["email"] == VALID_USER["email"]
    assert user["full_name"] == VALID_USER["full_name"]
    assert user["role"] == VALID_USER["role"]
    assert user["is_active"] is True
    # Plaintext password must never appear in the response
    assert "password" not in body
    assert "password_hash" not in str(body)


# ---------------------------------------------------------------------------
# 2. Registration — duplicate email
# ---------------------------------------------------------------------------

def test_register_duplicate_email(client: TestClient):
    """Registering the same email twice should return 409 Conflict."""
    _register(client)  # first registration
    response = _register(client)  # second — same email

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"].lower()


# ---------------------------------------------------------------------------
# 3. Registration — invalid email
# ---------------------------------------------------------------------------

def test_register_invalid_email(client: TestClient):
    """Malformed email should be rejected at the schema layer (422)."""
    payload = {**VALID_USER, "email": "not-an-email"}
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# 4. Registration — weak password
# ---------------------------------------------------------------------------

def test_register_weak_password(client: TestClient):
    """Password shorter than 8 characters should be rejected (422)."""
    payload = {**VALID_USER, "email": "new@test.com", "password": "short"}
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# 5. Login — success
# ---------------------------------------------------------------------------

def test_login_success(client: TestClient):
    """POST /login with correct credentials should return 200 and tokens."""
    _register(client)

    response = client.post(
        "/api/v1/auth/login",
        json={"email": VALID_USER["email"], "password": VALID_USER["password"]},
    )

    assert response.status_code == 200, response.text

    body = response.json()
    assert "access_token" in body
    assert "refresh_token" in body
    assert body["token_type"] == "bearer"
    assert body["expires_in"] > 0

    user = body["user"]
    assert user["email"] == VALID_USER["email"]


# ---------------------------------------------------------------------------
# 6. Login — wrong password
# ---------------------------------------------------------------------------

def test_login_wrong_password(client: TestClient):
    """POST /login with wrong password should return 401."""
    _register(client)

    response = client.post(
        "/api/v1/auth/login",
        json={"email": VALID_USER["email"], "password": "WrongPassword!"},
    )

    assert response.status_code == 401
    assert "invalid" in response.json()["detail"].lower()


# ---------------------------------------------------------------------------
# 7. Login — nonexistent user
# ---------------------------------------------------------------------------

def test_login_nonexistent_user(client: TestClient):
    """POST /login for an email that was never registered should return 401."""
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "ghost@nowhere.com", "password": "AnyPassword123"},
    )

    assert response.status_code == 401


# ---------------------------------------------------------------------------
# 8. Refresh token — valid
# ---------------------------------------------------------------------------

def test_refresh_token_valid(client: TestClient):
    """POST /refresh with a valid refresh token should return a new access token."""
    reg = _register(client)
    refresh_token = reg.json()["refresh_token"]

    response = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token},
    )

    assert response.status_code == 200, response.text

    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"
    assert body["expires_in"] > 0
    # Refresh endpoint must NOT return a new refresh token
    assert "refresh_token" not in body


# ---------------------------------------------------------------------------
# 9. Refresh token — invalid / tampered
# ---------------------------------------------------------------------------

def test_refresh_token_invalid(client: TestClient):
    """POST /refresh with a tampered token should return 401."""
    response = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.tampered.signature"},
    )
    assert response.status_code == 401


# ---------------------------------------------------------------------------
# 10. Logout
# ---------------------------------------------------------------------------

def test_logout(client: TestClient):
    """POST /logout should return 200 and a message."""
    reg = _register(client)
    refresh_token = reg.json()["refresh_token"]

    response = client.post(
        "/api/v1/auth/logout",
        json={"refresh_token": refresh_token},
    )

    assert response.status_code == 200
    assert "message" in response.json()
    assert "logged out" in response.json()["message"].lower()


# ---------------------------------------------------------------------------
# 11. Protected route — GET /me — with valid token
# ---------------------------------------------------------------------------

def test_protected_me_with_token(client: TestClient):
    """GET /me with a valid Bearer token should return the user's profile."""
    reg = _register(client)
    access_token = reg.json()["access_token"]

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200, response.text

    body = response.json()
    assert body["email"] == VALID_USER["email"]
    assert body["full_name"] == VALID_USER["full_name"]
    assert body["role"] == VALID_USER["role"]
    assert body["is_active"] is True
    # Sensitive fields must not leak
    assert "password_hash" not in body
    assert "password" not in body


# ---------------------------------------------------------------------------
# 12. Protected route — GET /me — without token
# ---------------------------------------------------------------------------

def test_protected_me_without_token(client: TestClient):
    """GET /me without an Authorization header should return 401."""
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


# ---------------------------------------------------------------------------
# 13. JWT payload structure
# ---------------------------------------------------------------------------

def test_jwt_payload_structure(client: TestClient):
    """Decoded access and refresh tokens must contain sub, type, and exp claims."""
    reg = _register(client)
    body = reg.json()

    access_token = body["access_token"]
    refresh_token = body["refresh_token"]

    # Verify access token payload
    access_payload = decode_token(access_token, expected_type="access")
    assert access_payload is not None, "Access token failed to decode"
    assert "sub" in access_payload
    assert access_payload["type"] == "access"
    assert "exp" in access_payload
    assert "role" in access_payload
    assert access_payload["role"] == VALID_USER["role"]

    # Verify refresh token payload
    refresh_payload = decode_token(refresh_token, expected_type="refresh")
    assert refresh_payload is not None, "Refresh token failed to decode"
    assert "sub" in refresh_payload
    assert refresh_payload["type"] == "refresh"
    assert "exp" in refresh_payload

    # Verify tokens are NOT interchangeable (type-confusion protection)
    assert decode_token(access_token, expected_type="refresh") is None
    assert decode_token(refresh_token, expected_type="access") is None

    # Both tokens must embed the same user ID
    assert access_payload["sub"] == refresh_payload["sub"]
