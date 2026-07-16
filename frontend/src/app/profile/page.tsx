'use client';

import { DashboardLayout } from '@/components/layout/DashboardLayout';
import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { Input } from '@/components/common/forms/Input';
import { useAuth } from '@/hooks/useAuth';

export default function Profile() {
  const { user } = useAuth();

  return (
    <DashboardLayout>
      <div className="flex flex-col gap-6 text-left max-w-2xl">
        <div>
          <h1 className="text-xl font-black text-gray-900">User Profile</h1>
          <p className="text-xs text-gray-500 mt-1">Manage profile information and system credentials.</p>
        </div>

        <Card title="Account Details" className="p-6 flex flex-col gap-5">
          <Input label="Full Name" defaultValue={user?.fullName || 'Rajesh Kumar'} />
          <Input label="Email Address" defaultValue={user?.email || 'rajesh@lawfirm.com'} disabled />
          <Input label="Organization" defaultValue={user?.organization || 'Kumar & Associates'} />
          <Button className="w-full py-2.5 mt-2">Update Profile</Button>
        </Card>
      </div>
    </DashboardLayout>
  );
}
