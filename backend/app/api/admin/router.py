"""Admin API router with mock implementations."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
@router.get("/api/admin/ping")
async def ping():
    """Dummy health checks for admin service."""
    return {"message": "Admin API working"}
