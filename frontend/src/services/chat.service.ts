import { ChatRequest, ChatResponse, Conversation, Message } from '@/types/chat';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
});

export const chatService = {
  async sendMessage(data: ChatRequest): Promise<ChatResponse> {
    const response = await api.post(API_ROUTES.CHAT.SEND, data);
    return response.data;
  },

  async getConversations(): Promise<Conversation[]> {
    const response = await api.get(API_ROUTES.CHAT.CONVERSATIONS);
    return response.data;
  },

  async getMessages(conversationId: string): Promise<Message[]> {
    const response = await api.get(API_ROUTES.CHAT.MESSAGES(conversationId));
    return response.data;
  },
};
