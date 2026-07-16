'use client';

import { useState } from 'react';
import { DashboardLayout } from '@/components/layout/DashboardLayout';
import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { mockNotifications } from '@/mock/notifications';
import { Bell, ShieldCheck, Mail, CheckCircle2 } from 'lucide-react';

export default function Notifications() {
  const [notifs, setNotifs] = useState(mockNotifications.slice(0, 10));

  const handleMarkAllRead = () => {
    setNotifs(notifs.map((n) => ({ ...n, isRead: true })));
  };

  return (
    <DashboardLayout>
      <div className="flex flex-col gap-6 text-left max-w-4xl">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-xl font-black text-gray-900">Alerts &amp; Notifications</h1>
            <p className="text-xs text-gray-500 mt-1">View latest updates, hearing alarms, and document audit outcomes.</p>
          </div>
          <Button variant="outline" size="sm" onClick={handleMarkAllRead}>Mark all as read</Button>
        </div>

        <div className="grid gap-4">
          {notifs.map((n) => (
            <Card
              key={n.id}
              className={`p-5 border border-gray-100 bg-white shadow-sm flex items-center justify-between rounded-xl ${
                !n.isRead ? 'border-l-4 border-l-sky-500' : ''
              }`}
            >
              <div className="flex items-center gap-4">
                <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 bg-sky-50 text-sky-600`}>
                  <Bell className="w-5 h-5" />
                </div>
                <div className="flex flex-col text-left gap-0.5">
                  <span className="text-sm font-bold text-gray-900">{n.title}</span>
                  <span className="text-xs text-gray-500">{n.message}</span>
                  <span className="text-[9px] text-gray-400 font-medium mt-1">
                    {new Date(n.createdAt).toLocaleDateString()}
                  </span>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </DashboardLayout>
  );
}
