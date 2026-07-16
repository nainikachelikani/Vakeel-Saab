"""Notifications API routes with placeholder implementations."""

from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("")
async def list_notifications():
    """Get all notifications for the current user."""
    return [
        {
            "id": "notif-001",
            "title": "Document Analysis Complete",
            "message": "Your document 'Tech-Corp_Master_Service_v4.pdf' has been analyzed. 3 critical risk areas found.",
            "notification_type": "document",
            "is_read": False,
            "action_url": "/dashboard/professional/risk?doc=doc-001-uuid",
            "created_at": "2024-10-24T16:00:00Z",
        },
        {
            "id": "notif-002",
            "title": "Report Generated",
            "message": "Risk Analysis Report for MSA_TechCorp_2024.pdf is ready for review.",
            "notification_type": "report",
            "is_read": False,
            "action_url": "/dashboard/professional/reports/report-001-uuid",
            "created_at": "2024-10-24T15:30:00Z",
        },
        {
            "id": "notif-003",
            "title": "New Legal Update",
            "message": "The Consumer Protection Act, 2019 has been amended. Review changes affecting your active cases.",
            "notification_type": "system",
            "is_read": True,
            "action_url": None,
            "created_at": "2024-10-23T09:00:00Z",
        },
        {
            "id": "notif-004",
            "title": "Complaint Status Update",
            "message": "Your complaint 'Municipal Complaint: Water Supply' status has changed to 'Submitted'.",
            "notification_type": "info",
            "is_read": True,
            "action_url": "/dashboard/citizen/complaints/comp-002",
            "created_at": "2024-10-22T14:00:00Z",
        },
        {
            "id": "notif-005",
            "title": "AI Agent Update",
            "message": "The legal analysis agent has been updated with latest Supreme Court judgments from Q3 2024.",
            "notification_type": "system",
            "is_read": True,
            "action_url": None,
            "created_at": "2024-10-21T10:00:00Z",
        },
    ]


@router.patch("/{notification_id}/read")
async def mark_as_read(notification_id: str):
    """Mark a notification as read."""
    return {"id": notification_id, "is_read": True}


@router.patch("/read-all")
async def mark_all_as_read():
    """Mark all notifications as read."""
    return {"message": "All notifications marked as read", "count": 5}
