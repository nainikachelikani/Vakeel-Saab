// Shared Types - Notification
export type NotificationType = 'info' | 'warning' | 'success' | 'error' | 'document' | 'report' | 'system';

export interface Notification {
  id: string;
  title: string;
  message: string;
  notificationType: NotificationType;
  isRead: boolean;
  actionUrl?: string;
  createdAt: string;
}
