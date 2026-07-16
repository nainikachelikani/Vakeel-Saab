"""Notification service - placeholder implementation."""

from typing import Dict, Any, List
from uuid import UUID


class NotificationService:
    """Handles user notifications."""

    async def get_notifications(self, user_id: UUID) -> List[Dict[str, Any]]:
        """Get all notifications for a user. Placeholder."""
        raise NotImplementedError("Get notifications not yet implemented")

    async def mark_read(self, notification_id: UUID) -> Dict[str, Any]:
        """Mark a notification as read. Placeholder."""
        raise NotImplementedError("Mark notification read not yet implemented")

    async def create_notification(self, user_id: UUID, title: str, message: str, notification_type: str) -> Dict[str, Any]:
        """Create a new notification. Placeholder."""
        raise NotImplementedError("Create notification not yet implemented")
