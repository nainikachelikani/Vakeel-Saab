import { LoginRequest, RegisterRequest, AuthResponse } from '@/types/notification';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const authService = {
  async login(data: LoginRequest): Promise<AuthResponse> {
    const response = await api.post(API_ROUTES.AUTH.LOGIN, data);
    return response.data;
  },

  async register(data: RegisterRequest): Promise<AuthResponse> {
    const response = await api.post(API_ROUTES.AUTH.REGISTER, data);
    return response.data;
  },

  async logout(): Promise<void> {
    await api.post(API_ROUTES.AUTH.LOGOUT);
  },
};
