// Shared Types - Report
export type ReportType = 'risk_analysis' | 'compliance_audit' | 'contract_summary' | 'legal_brief' | 'case_analysis';
export type ReportStatus = 'generating' | 'completed' | 'failed';

export interface Report {
  id: string;
  title: string;
  reportType: ReportType;
  summary?: string;
  status: ReportStatus;
  createdAt: string;
  updatedAt: string;
}

export interface ReportDetail extends Report {
  content?: string;
  metadata?: Record<string, any>;
  citations: Citation[];
  riskFindings: RiskFinding[];
}

export interface RiskFinding {
  severity: 'low' | 'medium' | 'high' | 'critical';
  title: string;
  section: string;
}

import { Citation } from './chat';
export type { Citation };
