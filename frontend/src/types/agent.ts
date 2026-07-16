export type { Agent, AgentType, AgentStatus, AgentExecutionLog } from '@shared/types/agent';
export type { IAgent, IToolInterface, IPromptInterface, IResourceInterface, IWorkflowInterface, IWorkflowStep } from '@shared/interfaces/agent.interface';
export type { IMCPServer, IMCPRequest, IMCPResponse, IMCPTool, IMCPResource } from '@shared/interfaces/mcp.interface';
export type { IWorkflow, IWorkflowStepDef, IWorkflowExecution, IWorkflowStepResult } from '@shared/interfaces/workflow.interface';
export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
}

export interface ApiError {
  message: string;
  statusCode: number;
  details?: any;
}
