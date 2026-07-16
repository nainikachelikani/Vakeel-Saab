// Shared Types - User
export interface User {
  id: string;
  email: string;
  fullName: string;
  role: 'citizen' | 'professional' | 'admin';
  avatarUrl?: string;
  organization?: string;
  isActive: boolean;
  isVerified: boolean;
  createdAt: string;
}

export interface UserStats {
  totalDocuments: number;
  totalConversations: number;
  totalReports: number;
  documentsAnalyzed: number;
  activeCases: number;
}

export interface UserPreferences {
  language: string;
  theme: 'light' | 'dark';
  notificationsEnabled: boolean;
  emailNotifications: boolean;
}
