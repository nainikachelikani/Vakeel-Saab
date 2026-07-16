import { create } from 'zustand';
import { Conversation, Message } from '@/types/chat';
import { mockMessages } from '@/mock/messages';

interface ChatState {
  conversations: Conversation[];
  activeConversation: Conversation | null;
  messages: Record<string, Message[]>; // conversationId -> messages
  setConversations: (conversations: Conversation[]) => void;
  setActiveConversation: (conversation: Conversation | null) => void;
  addMessage: (conversationId: string, message: Message) => void;
  loadMockMessages: (conversationId: string) => void;
}

export const useChatStore = create<ChatState>((set) => ({
  conversations: [],
  activeConversation: null,
  messages: {},
  setConversations: (conversations) => set({ conversations }),
  setActiveConversation: (conversation) => set({ activeConversation: conversation }),
  addMessage: (conversationId, message) => set((state) => {
    const convoMessages = state.messages[conversationId] || [];
    return {
      messages: {
        ...state.messages,
        [conversationId]: [...convoMessages, message],
      }
    };
  }),
  loadMockMessages: (conversationId) => set((state) => {
    // Return a slice of 10 messages for simplicity
    const filtered = mockMessages.slice(0, 10);
    return {
      messages: {
        ...state.messages,
        [conversationId]: filtered,
      }
    };
  }),
}));
