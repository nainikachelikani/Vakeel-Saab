'use client';

import { useAuthStore } from '@/store/auth.store';
import { authService } from '@/services/auth.service';
import { LoginRequest, RegisterRequest } from '@/types/notification';
import { useState } from 'react';

export function useAuth() {
  const { user, isAuthenticated, login: storeLogin, logout: storeLogout } = useAuthStore();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const login = async (data: LoginRequest) => {
    setLoading(true);
    setError(null);
    try {
      const res = await authService.login(data);
      storeLogin(res.user, res.accessToken);
      return res.user;
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Authentication failed');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const register = async (data: RegisterRequest) => {
    setLoading(true);
    setError(null);
    try {
      const res = await authService.register(data);
      storeLogin(res.user, res.accessToken);
      return res.user;
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'Registration failed');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
    } catch (err) {
      console.error('Logout error', err);
    } finally {
      storeLogout();
    }
  };

  return {
    user,
    isAuthenticated,
    loading,
    error,
    login,
    register,
    logout,
  };
}
