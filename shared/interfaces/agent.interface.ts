// Shared Interfaces - Agent
export interface IAgent {
  id: string;
  type: string;
  name: string;
  description: string;
  execute(input: Record<string, any>): Promise<Record<string, any>>;
}

export interface IToolInterface {
  name: string;
  description: string;
  parameters: Record<string, any>;
  execute(params: Record<string, any>): Promise<Record<string, any>>;
}

export interface IPromptInterface {
  name: string;
  description: string;
  template: string;
  variables: string[];
  render(values: Record<string, string>): string;
}

export interface IResourceInterface {
  uri: string;
  name: string;
  description: string;
  read(): Promise<Record<string, any>>;
}

export interface IWorkflowInterface {
  id: string;
  name: string;
  steps: IWorkflowStep[];
  execute(input: Record<string, any>): Promise<Record<string, any>>;
}

export interface IWorkflowStep {
  id: string;
  agentType: string;
  input: Record<string, any>;
  output?: Record<string, any>;
  status: 'pending' | 'running' | 'completed' | 'failed';
}
