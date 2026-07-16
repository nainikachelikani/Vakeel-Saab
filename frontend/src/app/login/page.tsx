'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/hooks/useAuth';
import { Input } from '@/components/common/forms/Input';
import { Button } from '@/components/common/buttons/Button';
import { Card } from '@/components/common/cards/Card';
import Link from 'next/link';

export default function LoginPage() {
  const router = useRouter();
  const { login, loading, error: authError } = useAuth();
  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }
    setError('');

    try {
      await login({ email, password });
      router.push('/dashboard');
    } catch (err) {
      setError('Invalid credentials, please try again.');
    }
  };

  return (
    <div className="min-h-screen bg-[#F8FAFC] flex items-center justify-center p-6">
      <Card className="w-full max-w-md p-8 border border-gray-100 rounded-2xl bg-white shadow-sm flex flex-col text-center">
        <div className="flex justify-center mb-6">
          <div className="w-12 h-12 rounded-2xl bg-[#0F1B2D] text-white flex items-center justify-center font-extrabold text-xl">VS</div>
        </div>
        <h2 className="text-xl font-bold text-gray-900">Sign In to Vakeel Saab</h2>
        <p className="text-xs text-gray-500 mt-1">AI Legal Intelligence Platform</p>

        <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5 text-left">
          {error && <div className="p-3 bg-red-50 text-red-600 rounded-lg text-xs font-semibold">{error}</div>}
          <Input
            label="Email Address"
            placeholder="name@firm.com"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Input
            label="Password"
            placeholder="••••••••"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <div className="flex items-center justify-between text-xs font-semibold">
            <label className="flex items-center gap-2 text-gray-600 cursor-pointer">
              <input type="checkbox" className="rounded border-gray-300 text-[#0F1B2D] focus:ring-sky-500" />
              Remember this device
            </label>
            <Link href="#" className="text-sky-600 hover:underline">Forgot password?</Link>
          </div>
          <Button type="submit" disabled={loading} className="w-full mt-2 py-3">
            {loading ? 'Signing In...' : 'Sign In'}
          </Button>
        </form>

        <div className="relative flex items-center justify-center my-6">
          <span className="absolute px-3 bg-white text-[10px] text-gray-400 font-bold uppercase tracking-wider">Or continue with</span>
          <div className="w-full border-t border-gray-100"></div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <Button variant="outline" size="sm" className="font-semibold text-xs py-2.5">Google</Button>
          <Button variant="outline" size="sm" className="font-semibold text-xs py-2.5">SSO</Button>
        </div>

        <p className="text-xs text-gray-500 mt-8">
          New to Vakeel Saab? <Link href="/signup" className="font-semibold text-sky-600 hover:underline">Create an account</Link>
        </p>
      </Card>
    </div>
  );
}
