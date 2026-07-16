"""Chat API routes with placeholder implementations."""

from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse, ConversationResponse
from typing import List
from uuid import UUID

router = APIRouter()


@router.post("", response_model=ChatResponse)
async def send_message(request: ChatRequest):
    """Send a chat message and receive an AI response."""
    return {
        "message": {
            "id": "msg-001-resp-uuid-placeholder",
            "content": "Based on your query, I can help you understand your legal rights. Under the Indian Contract Act, 1872, Section 25-A, you are protected against unfair termination without notice. The employer must provide a mandatory 30-day notice period or pay in lieu of notice. Furthermore, under the Payment of Wages Act, withholding salary constitutes a breach of contract.\n\nI recommend the following steps:\n1. Send a formal written notice to your employer citing these provisions\n2. File a complaint with the Labour Commissioner\n3. If unresolved, approach the Labour Court under the Industrial Disputes Act, 1947\n\nWould you like me to help draft a formal complaint letter?",
            "role": "assistant",
            "metadata": {
                "agent": "domain_agent",
                "domain": "labor_law",
                "confidence": 0.94,
                "processing_time_ms": 2340,
            },
            "created_at": "2024-10-24T14:35:00Z",
        },
        "conversation_id": request.conversation_id or "conv-001-uuid-placeholder",
        "agent_executions": [
            {
                "agent": "router_agent",
                "status": "completed",
                "duration_ms": 120,
                "intent": "Civil Dispute > Labor",
            },
            {
                "agent": "retrieval_agent",
                "status": "completed",
                "duration_ms": 890,
                "documents_fetched": 3,
            },
            {
                "agent": "domain_agent",
                "status": "completed",
                "duration_ms": 1330,
                "domain": "labor_law",
            },
        ],
        "citations": [
            {
                "title": "Indian Contract Act, 1872",
                "section": "Section 25-A",
                "relevance": 95,
            },
            {
                "title": "Industrial Disputes Act, 1947",
                "section": "Section 2(s)",
                "relevance": 88,
            },
            {
                "title": "Payment of Wages Act, 1936",
                "section": "Section 5",
                "relevance": 82,
            },
        ],
        "suggested_questions": [
            "How do I file a consumer complaint for a faulty product?",
            "What are my rights as a tenant?",
            "Check if my NDA is legally binding.",
            "Process for registering a small business.",
        ],
    }


@router.get("/conversations", response_model=List[ConversationResponse])
async def get_conversations():
    """Get all conversations for the current user."""
    return [
        {
            "id": "conv-001-uuid-placeholder",
            "title": "Property Lease Agreement Review",
            "status": "completed",
            "category": "property",
            "last_message": "AI reviewed clause 4.2 regarding security deposits...",
            "message_count": 12,
            "created_at": "2024-10-22T09:15:00Z",
            "updated_at": "2024-10-22T11:30:00Z",
        },
        {
            "id": "conv-002-uuid-placeholder",
            "title": "Consumer Complaint Draft",
            "status": "active",
            "category": "civil",
            "last_message": "Waiting for purchase receipt upload to finalize...",
            "message_count": 8,
            "created_at": "2024-10-23T14:00:00Z",
            "updated_at": "2024-10-23T16:45:00Z",
        },
        {
            "id": "conv-003-uuid-placeholder",
            "title": "Employment Contract Analysis",
            "status": "active",
            "category": "civil",
            "last_message": "The non-compete clause in section 7.3 appears overly broad...",
            "message_count": 15,
            "created_at": "2024-10-20T10:00:00Z",
            "updated_at": "2024-10-24T09:00:00Z",
        },
        {
            "id": "conv-004-uuid-placeholder",
            "title": "Tenant Rights Inquiry",
            "status": "completed",
            "category": "property",
            "last_message": "Under the Rent Control Act, your landlord cannot...",
            "message_count": 6,
            "created_at": "2024-10-18T08:30:00Z",
            "updated_at": "2024-10-18T10:15:00Z",
        },
    ]


@router.get("/conversations/{conversation_id}/messages")
async def get_messages(conversation_id: str):
    """Get all messages for a specific conversation."""
    return [
        {
            "id": "msg-001-uuid",
            "content": "I need help understanding my rights regarding an unfair termination from my employer.",
            "role": "user",
            "created_at": "2024-10-24T14:30:00Z",
        },
        {
            "id": "msg-002-uuid",
            "content": "I understand your concern about unfair termination. Let me analyze your situation under Indian employment law.\n\nBased on the Industrial Relations Act, Section 25-A, employers must provide valid grounds for termination...",
            "role": "assistant",
            "metadata": {"agent": "domain_agent", "domain": "labor_law"},
            "created_at": "2024-10-24T14:30:15Z",
        },
        {
            "id": "msg-003-uuid",
            "content": "They also haven't paid my last two months' salary. What can I do?",
            "role": "user",
            "created_at": "2024-10-24T14:32:00Z",
        },
        {
            "id": "msg-004-uuid",
            "content": "The withholding of salary is a serious violation under the Payment of Wages Act, 1936. Here's what you can do:\n\n1. **File a complaint with the Labour Commissioner** under Section 15 of the Payment of Wages Act\n2. **Send a legal notice** to your employer demanding payment within 15 days\n3. **Approach the Labour Court** if the employer fails to respond\n\nWould you like me to draft a legal notice for you?",
            "role": "assistant",
            "metadata": {"agent": "domain_agent", "domain": "labor_law", "confidence": 0.96},
            "created_at": "2024-10-24T14:32:20Z",
        },
    ]
