"""Report Pydantic schemas."""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID


class ReportCreate(BaseModel):
    title: str
    report_type: str
    document_id: Optional[UUID] = None


class ReportResponse(BaseModel):
    id: UUID
    title: str
    report_type: str
    summary: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ReportDetailResponse(ReportResponse):
    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    citations: List[Dict[str, Any]] = []
    risk_findings: List[Dict[str, Any]] = []
