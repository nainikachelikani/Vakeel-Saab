"""Search API routes with placeholder implementations."""

from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def search(request: dict):
    """Global semantic search across all legal content."""
    query = request.get("query", "")
    return {
        "query": query,
        "results": [
            {
                "type": "document",
                "id": "doc-001-uuid",
                "title": "Tech-Corp_Master_Service_v4.pdf",
                "excerpt": "Section 4.1 - General Indemnity clause addresses liability...",
                "relevance": 0.95,
                "category": "contract",
            },
            {
                "type": "conversation",
                "id": "conv-001-uuid",
                "title": "Property Lease Agreement Review",
                "excerpt": "AI reviewed clause 4.2 regarding security deposits...",
                "relevance": 0.82,
                "category": "property",
            },
            {
                "type": "citation",
                "id": "cite-001-uuid",
                "title": "Indian Contract Act, 1872 - Section 73",
                "excerpt": "Compensation for loss or damage caused by breach of contract...",
                "relevance": 0.78,
                "category": "statute",
            },
            {
                "type": "report",
                "id": "report-001-uuid",
                "title": "Risk Analysis: MSA_TechCorp_2024.pdf",
                "excerpt": "Critical vulnerability identified in indemnification clause...",
                "relevance": 0.75,
                "category": "risk_analysis",
            },
        ],
        "total": 4,
        "processing_time_ms": 230,
    }
