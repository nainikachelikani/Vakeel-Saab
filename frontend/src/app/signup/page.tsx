'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/hooks/useAuth';
import { Input } from '@/components/common/forms/Input';
import { Button } from '@/components/common/buttons/Button';
import { Card } from '@/components/common/cards/Card';
import Link from 'next/link';

export default function SignupPage() {
  const router = useRouter();
  const { register, loading } = useAuth();
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!fullName || !email || !password) {
      setError('Please fill in all fields');
      return;
    }
    setError('');

    try {
      await register({
        fullName,
        email,
        password,
        role: 'citizen',
      });
      router.push('/dashboard');
    } catch (err) {
      setError('Registration failed. Please try again.');
    }
  };

  return (
    <div className="min-h-screen bg-[#F8FAFC] flex items-center justify-center p-6">
      <Card className="w-full max-w-md p-8 border border-gray-100 rounded-2xl bg-white shadow-sm flex flex-col text-center">
        <div className="flex justify-center mb-6">
          <div className="w-12 h-12 rounded-2xl bg-[#0F1B2D] text-white flex items-center justify-center font-extrabold text-xl">VS</div>
        </div>
        <h2 className="text-xl font-bold text-gray-900">Create your account</h2>
        <p className="text-xs text-gray-500 mt-1">Get legal protection with Vakeel Saab</p>

        <form onSubmit={handleSubmit} className="mt-8 flex flex-col gap-5 text-left">
          {error && <div className="p-3 bg-red-50 text-red-600 rounded-lg text-xs font-semibold">{error}</div>}
          <Input
            label="Full Name"
            placeholder="John Doe"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />
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
          <Button type="submit" disabled={loading} className="w-full mt-2 py-3">
            {loading ? 'Registering...' : 'Register Account'}
          </Button>
        </form>

        <p className="text-xs text-gray-500 mt-8">
          Already have an account? <Link href="/login" className="font-semibold text-sky-600 hover:underline">Sign In</Link>
        </p>
      </Card>
    </div>
  );
}
