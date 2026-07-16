"""Document Pydantic schemas."""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID


class DocumentCreate(BaseModel):
    title: str
    document_type: str = "other"
    language: str = "en"


class DocumentResponse(BaseModel):
    id: UUID
    title: str
    file_name: str
    file_type: str
    file_size: int
    document_type: str
    status: str
    summary: Optional[str] = None
    risk_score: Optional[float] = None
    page_count: Optional[int] = None
    language: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DocumentSearchQuery(BaseModel):
    query: str
    document_type: Optional[str] = None
    limit: int = 10
    offset: int = 0


class DocumentSearchResult(BaseModel):
    document: DocumentResponse
    relevance_score: float
    matched_excerpt: str


class DocumentAnalysisResponse(BaseModel):
    document_id: UUID
    summary: str
    key_clauses: List[Dict[str, Any]]
    risk_areas: List[Dict[str, Any]]
    recommendations: List[str]
    processing_time_ms: int


class DocumentCompareResponse(BaseModel):
    document_a_id: UUID
    document_b_id: UUID
    similarities: List[Dict[str, Any]]
    differences: List[Dict[str, Any]]
    risk_comparison: Dict[str, Any]


class RiskAnalysisResponse(BaseModel):
    document_id: UUID
    overall_risk_score: float
    risk_level: str  # low, medium, high, critical
    exposure_by_category: Dict[str, float]
    high_risk_clauses: List[Dict[str, Any]]
    compliance_checklist: List[Dict[str, Any]]
    ai_executive_summary: str
