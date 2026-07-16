"""Vakeel Saab - AI Powered Multi-Agent Legal Intelligence Platform.

FastAPI Backend Application Entrypoint.
"""

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from app.config.settings import settings
from app.config.logging import logger

# Import API Routers (subpackages)
from app.api.auth.router import router as auth_router
from app.api.chat.router import router as chat_router
from app.api.documents.router import router as documents_router
from app.api.reports.router import router as reports_router
from app.api.mcp.router import router as mcp_router
from app.api.admin.router import router as admin_router

# Existing Routers (backward compatibility)
from app.api.contracts import router as contracts_router
from app.api.notifications import router as notifications_router
from app.api.profile import router as profile_router
from app.api.search import router as search_router

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Powered Multi-Agent Legal Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=settings.APP_DEBUG,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global Exception Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle FastAPI endpoints standard HTTP exceptions."""
    logger.error(f"HTTP error: {exc.status_code} - {exc.detail} - path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: Exception):
    """Handle model data validation errors."""
    logger.error(f"Validation error - path: {request.url.path} - error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Data validation failed.",
            "errors": str(exc),
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch-all handler for unexpected runtime internal exceptions."""
    logger.error(f"Unhandled system error - path: {request.url.path} - error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred."},
    )


# Health check endpoint
@app.get("/health")
async def health_check():
    """Application level health check endpoint.

    Returns:
        JSON with operational status.
    """
    logger.debug("Health check retrieved.")
    return {"status": "healthy"}


# Register API Routers (V1 Prefix)
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(chat_router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(documents_router, prefix="/api/v1/documents", tags=["Documents"])
app.include_router(reports_router, prefix="/api/v1/reports", tags=["Reports"])
app.include_router(mcp_router, prefix="/api/v1/mcp", tags=["MCP"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])

# Existing Routers (backward compatibility)
app.include_router(contracts_router, prefix="/api/v1/contracts", tags=["Contracts"])
app.include_router(notifications_router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(profile_router, prefix="/api/v1/profile", tags=["Profile"])
app.include_router(search_router, prefix="/api/v1/search", tags=["Search"])
