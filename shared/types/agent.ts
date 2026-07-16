// Shared Types - Agent
export type AgentType = 'router' | 'domain' | 'retrieval' | 'legal_analysis' | 'citation' | 'planner' | 'reviewer';
export type AgentStatus = 'idle' | 'running' | 'completed' | 'error';

export interface Agent {
  id: string;
  type: AgentType;
  name: string;
  description: string;
  status: AgentStatus;
  lastExecutionMs?: number;
}

export interface AgentExecutionLog {
  id: string;
  agentType: AgentType;
  status: AgentStatus;
  inputData?: Record<string, any>;
  outputData?: Record<string, any>;
  errorMessage?: string;
  durationMs?: number;
  tokensUsed?: number;
  cost?: number;
  createdAt: string;
}
