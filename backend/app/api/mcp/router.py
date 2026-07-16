"""MCP API router with mock implementations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
@router.get("/api/mcp/ping")
async def ping():
    """Dummy health checks for MCP service."""
    return {"message": "MCP API working"}
