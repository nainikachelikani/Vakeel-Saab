// Shared Interfaces - Workflow
export interface IWorkflow {
  id: string;
  name: string;
  description: string;
  steps: IWorkflowStepDef[];
}

export interface IWorkflowStepDef {
  id: string;
  name: string;
  agentType: string;
  dependsOn?: string[];
  config: Record<string, any>;
}

export interface IWorkflowExecution {
  id: string;
  workflowId: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  steps: IWorkflowStepResult[];
  startedAt: string;
  completedAt?: string;
}

export interface IWorkflowStepResult {
  stepId: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  result?: Record<string, any>;
  error?: string;
  durationMs?: number;
}
