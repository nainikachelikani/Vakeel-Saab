import { Notification } from '@/types/notification';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
});

export const notificationService = {
  async listNotifications(): Promise<Notification[]> {
    const response = await api.get(API_ROUTES.NOTIFICATIONS.LIST);
    return response.data;
  },

  async markAsRead(id: string): Promise<void> {
    await api.patch(API_ROUTES.NOTIFICATIONS.MARK_READ(id));
  },

  async markAllRead(): Promise<void> {
    await api.patch(API_ROUTES.NOTIFICATIONS.MARK_ALL_READ);
  },
};
