"""Verification test suite for app main routes."""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Verify GET /health returns the correct operational status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_cors_headers():
    """Verify CORS headers are present on responses."""
    response = client.get("/health", headers={"Origin": "http://localhost:3000"})
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"


def test_auth_ping():
    """Verify authentication ping endpoint."""
    response = client.get("/api/v1/auth/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Auth API working"}


def test_chat_ping():
    """Verify chat ping endpoint."""
    response = client.get("/api/v1/chat/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Chat API working"}


def test_documents_ping():
    """Verify documents ping endpoint."""
    response = client.get("/api/v1/documents/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Documents API working"}


def test_reports_ping():
    """Verify reports ping endpoint."""
    response = client.get("/api/v1/reports/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Reports API working"}


def test_mcp_ping():
    """Verify MCP ping endpoint."""
    response = client.get("/api/v1/mcp/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "MCP API working"}


def test_admin_ping():
    """Verify admin ping endpoint."""
    response = client.get("/api/v1/admin/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Admin API working"}


def test_global_exception_handler():
    """Verify global exception handler catches 404 for nonexistent path."""
    response = client.get("/nonexistent-path-for-testing")
    assert response.status_code == 404
    assert "detail" in response.json()
