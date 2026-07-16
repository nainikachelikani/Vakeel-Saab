'use client';

import { useState } from 'react';
import { DashboardLayout } from '@/components/layout/DashboardLayout';
import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { Input } from '@/components/common/forms/Input';

export default function Settings() {
  const [notify, setNotify] = useState(true);

  return (
    <DashboardLayout>
      <div className="flex flex-col gap-6 text-left max-w-2xl">
        <div>
          <h1 className="text-xl font-black text-gray-900">Application Settings</h1>
          <p className="text-xs text-gray-500 mt-1">Manage configuration preferences and system defaults.</p>
        </div>

        <Card title="User Preferences" className="p-6 flex flex-col gap-5">
          <div className="flex flex-col gap-2">
            <span className="text-[10px] font-bold text-gray-400 uppercase">Interface Theme</span>
            <select className="w-full bg-[#F8FAFC] border border-gray-200 rounded-lg p-2.5 text-xs text-gray-800 outline-none">
              <option>Light Theme</option>
              <option>Dark Theme</option>
              <option>System Default</option>
            </select>
          </div>

          <div className="flex flex-col gap-2">
            <span className="text-[10px] font-bold text-gray-400 uppercase">Default Language</span>
            <select className="w-full bg-[#F8FAFC] border border-gray-200 rounded-lg p-2.5 text-xs text-gray-800 outline-none">
              <option>English</option>
              <option>Hindi</option>
              <option>Tamil</option>
            </select>
          </div>

          <div className="flex items-center justify-between text-xs border-t border-gray-50 pt-4 mt-2">
            <span className="text-gray-600 font-semibold">Enable Real-time Email Notifications</span>
            <input
              type="checkbox"
              checked={notify}
              onChange={() => setNotify(!notify)}
              className="rounded border-gray-300 text-[#0F1B2D] focus:ring-sky-500 w-4 h-4 cursor-pointer"
            />
          </div>

          <Button className="w-full mt-4 py-2.5">Save Settings</Button>
        </Card>
      </div>
    </DashboardLayout>
  );
}
