import { LoginRequest, RegisterRequest, AuthResponse } from '@/types/notification';
import { User } from '@/types/user';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

function mapUserResponse(backendUser: any): User {
  return {
    id: backendUser.id,
    email: backendUser.email,
    fullName: backendUser.full_name,
    role: backendUser.role,
    avatarUrl: backendUser.avatar_url,
    organization: backendUser.organization,
    isActive: backendUser.is_active,
    isVerified: backendUser.is_verified,
    createdAt: backendUser.created_at,
  };
}

function mapAuthResponse(backendResponse: any): AuthResponse {
  return {
    accessToken: backendResponse.access_token,
    refreshToken: backendResponse.refresh_token,
    tokenType: backendResponse.token_type,
    user: mapUserResponse(backendResponse.user),
  };
}

export const authService = {
  async login(data: LoginRequest): Promise<AuthResponse> {
    const response = await api.post(API_ROUTES.AUTH.LOGIN, data);
    return mapAuthResponse(response.data);
  },

  async register(data: RegisterRequest): Promise<AuthResponse> {
    const backendData = {
      email: data.email,
      password: data.password,
      full_name: data.fullName,
      role: data.role,
      organization: data.organization,
    };
    const response = await api.post(API_ROUTES.AUTH.REGISTER, backendData);
    return mapAuthResponse(response.data);
  },

  async logout(): Promise<void> {
    await api.post(API_ROUTES.AUTH.LOGOUT);
  },
};
