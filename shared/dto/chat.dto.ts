// Shared DTOs - Chat
export interface SendMessageRequest {
  message: string;
  conversationId?: string;
  category?: string;
}
