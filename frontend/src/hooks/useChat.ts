'use client';

import { useState } from 'react';
import { useChatStore } from '@/store/chat.store';
import { chatService } from '@/services/chat.service';
import { Message } from '@/types/chat';

export function useChat() {
  const { activeConversation, messages, addMessage, loadMockMessages } = useChatStore();
  const [sending, setSending] = useState(false);

  const sendMessage = async (text: string) => {
    if (!text.trim() || !activeConversation) return;

    const userMsg: Message = {
      id: `msg-temp-${Date.now()}`,
      content: text,
      role: 'user',
      createdAt: new Date().toISOString(),
    };

    addMessage(activeConversation.id, userMsg);
    setSending(true);

    try {
      const res = await chatService.sendMessage({
        message: text,
        conversationId: activeConversation.id,
        category: activeConversation.category,
      });

      addMessage(activeConversation.id, res.message);
    } catch (err) {
      console.error('Failed to send message', err);
      // Fallback: Add a mock response
      const botMsg: Message = {
        id: `msg-bot-temp-${Date.now()}`,
        content: 'This is a mock response from the platform assistant. Please ensure backend services are running to get actual response.',
        role: 'assistant',
        createdAt: new Date().toISOString(),
        metadata: {
          agent: 'domain_agent',
          confidence: 0.95,
        }
      };
      addMessage(activeConversation.id, botMsg);
    } finally {
      setSending(false);
    }
  };

  return {
    activeConversation,
    currentMessages: activeConversation ? (messages[activeConversation.id] || []) : [],
    sendMessage,
    sending,
    loadMockMessages,
  };
}
