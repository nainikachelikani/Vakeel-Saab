// Shared Types - Chat
export type MessageRole = 'user' | 'assistant' | 'system';
export type ConversationStatus = 'active' | 'completed' | 'archived';

export interface Message {
  id: string;
  content: string;
  role: MessageRole;
  metadata?: Record<string, any>;
  createdAt: string;
}

export interface Conversation {
  id: string;
  title: string;
  status: ConversationStatus;
  category?: string;
  lastMessage?: string;
  messageCount: number;
  createdAt: string;
  updatedAt: string;
}

export interface ChatRequest {
  message: string;
  conversationId?: string;
  category?: string;
}

export interface ChatResponse {
  message: Message;
  conversationId: string;
  agentExecutions: AgentExecution[];
  citations: Citation[];
  suggestedQuestions: string[];
}

export interface AgentExecution {
  agent: string;
  status: string;
  durationMs: number;
  [key: string]: any;
}

export interface Citation {
  title: string;
  section?: string;
  reference?: string;
  relevance: number;
}
