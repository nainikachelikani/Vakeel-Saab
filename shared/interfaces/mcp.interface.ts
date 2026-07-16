// Shared Interfaces - MCP
export interface IMCPServer {
  initialize(): Promise<void>;
  handleRequest(request: IMCPRequest): Promise<IMCPResponse>;
  listTools(): Promise<IMCPTool[]>;
  listResources(): Promise<IMCPResource[]>;
}

export interface IMCPRequest {
  method: string;
  params: Record<string, any>;
}

export interface IMCPResponse {
  result?: Record<string, any>;
  error?: { code: number; message: string };
}

export interface IMCPTool {
  name: string;
  description: string;
  inputSchema: Record<string, any>;
}

export interface IMCPResource {
  uri: string;
  name: string;
  description: string;
  mimeType?: string;
}
