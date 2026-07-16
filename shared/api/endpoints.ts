// Shared API - Endpoint Definitions
export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    REGISTER: '/auth/register',
    LOGOUT: '/auth/logout',
    REFRESH: '/auth/refresh',
  },
  CHAT: {
    SEND: '/chat',
    CONVERSATIONS: '/chat/conversations',
    MESSAGES: (conversationId: string) => `/chat/conversations/${conversationId}/messages`,
  },
  DOCUMENTS: {
    LIST: '/documents',
    UPLOAD: '/documents/upload',
    SEARCH: '/documents/search',
    ANALYZE: '/documents/analyze',
    COMPARE: '/documents/compare',
    RISK: '/documents/risk',
  },
  CONTRACTS: {
    LIST: '/contracts',
    DETAIL: (id: string) => `/contracts/${id}`,
  },
  REPORTS: {
    LIST: '/reports',
    CREATE: '/reports',
    DETAIL: (id: string) => `/reports/${id}`,
  },
  NOTIFICATIONS: {
    LIST: '/notifications',
    MARK_READ: (id: string) => `/notifications/${id}/read`,
    MARK_ALL_READ: '/notifications/read-all',
  },
  PROFILE: {
    GET: '/profile',
    UPDATE: '/profile',
  },
  SEARCH: {
    QUERY: '/search',
  },
} as const;
