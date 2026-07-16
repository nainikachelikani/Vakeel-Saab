// Shared Constants - Status Enums
export const DOCUMENT_STATUS = {
  PENDING: 'pending',
  PROCESSING: 'processing',
  ANALYZED: 'analyzed',
  ERROR: 'error',
} as const;

export const CONVERSATION_STATUS = {
  ACTIVE: 'active',
  COMPLETED: 'completed',
  ARCHIVED: 'archived',
} as const;

export const REPORT_STATUS = {
  GENERATING: 'generating',
  COMPLETED: 'completed',
  FAILED: 'failed',
} as const;

export const RISK_LEVEL = {
  LOW: 'low',
  MEDIUM: 'medium',
  HIGH: 'high',
  CRITICAL: 'critical',
} as const;

export const USER_ROLE = {
  CITIZEN: 'citizen',
  PROFESSIONAL: 'professional',
  ADMIN: 'admin',
} as const;

export const LEGAL_CATEGORIES = ['Civil', 'Criminal', 'Family', 'Property', 'Labor', 'Consumer', 'Corporate'] as const;
