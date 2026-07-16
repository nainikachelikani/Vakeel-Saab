// Shared Types - Document
export type DocumentType = 'contract' | 'judgment' | 'complaint' | 'notice' | 'agreement' | 'nda' | 'policy' | 'other';
export type DocumentStatus = 'pending' | 'processing' | 'analyzed' | 'error';

export interface Document {
  id: string;
  title: string;
  fileName: string;
  fileType: string;
  fileSize: number;
  documentType: DocumentType;
  status: DocumentStatus;
  summary?: string;
  riskScore?: number;
  pageCount?: number;
  language: string;
  createdAt: string;
  updatedAt: string;
}

export interface DocumentSearchResult {
  document: Document;
  relevanceScore: number;
  matchedExcerpt: string;
}

export interface RiskAnalysis {
  documentId: string;
  overallRiskScore: number;
  riskLevel: 'low' | 'medium' | 'high' | 'critical';
  exposureByCategory: Record<string, number>;
  highRiskClauses: RiskClause[];
  complianceChecklist: ComplianceItem[];
  aiExecutiveSummary: string;
}

export interface RiskClause {
  section: string;
  title: string;
  description: string;
  recommendation: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
}

export interface ComplianceItem {
  item: string;
  status: 'passed' | 'failed' | 'warning';
  details: string;
}

export interface Clause {
  clauseNumber: string;
  title: string;
  text: string;
  riskLevel: 'low' | 'medium' | 'high';
  category: string;
}
