"""
Vakeel Saab - AI Powered Multi-Agent Legal Intelligence Platform
FastAPI Backend Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, chat, documents, contracts, reports, notifications, profile, search
from app.core.config import settings

app = FastAPI(
    title="Vakeel Saab API",
    description="AI Powered Multi-Agent Legal Intelligence Platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(documents.router, prefix="/api/v1/documents", tags=["Documents"])
app.include_router(contracts.router, prefix="/api/v1/contracts", tags=["Contracts"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(profile.router, prefix="/api/v1/profile", tags=["Profile"])
app.include_router(search.router, prefix="/api/v1/search", tags=["Search"])


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "operational",
        "service": "Vakeel Saab API",
        "version": "1.0.0",
    }
