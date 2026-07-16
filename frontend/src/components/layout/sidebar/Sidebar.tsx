'use client';

import { useThemeStore } from '@/store/theme.store';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, Sparkles, FolderOpen, Search, PieChart, History, Settings, HelpCircle, ShieldAlert } from 'lucide-react';
import { APP_ROUTES } from '@/constants/ui';

export function Sidebar() {
  const pathname = usePathname();
  const { sidebarCollapsed } = useThemeStore();

  const menuItems = [
    { name: 'Dashboard', href: APP_ROUTES.DASHBOARD, icon: Home },
    { name: 'AI Assistant', href: APP_ROUTES.ASSISTANT, icon: Sparkles },
    { name: 'Documents', href: APP_ROUTES.DOCUMENTS, icon: FolderOpen },
    { name: 'Legal Research', href: APP_ROUTES.RESEARCH, icon: Search },
    { name: 'Reports', href: APP_ROUTES.REPORTS, icon: PieChart },
    { name: 'History', href: APP_ROUTES.HISTORY, icon: History },
    { name: 'Agent Monitor', href: APP_ROUTES.AGENT_MONITOR, icon: ShieldAlert },
    { name: 'Settings', href: APP_ROUTES.SETTINGS, icon: Settings },
  ];

  return (
    <aside className={`h-screen bg-white border-r border-gray-100 flex flex-col justify-between transition-all duration-300 ${sidebarCollapsed ? 'w-20' : 'w-64'}`}>
      <div className="flex flex-col">
        {/* Branding header */}
        <div className="p-6 border-b border-gray-50 flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-[#1E293B] flex items-center justify-center text-white font-bold">VS</div>
          {!sidebarCollapsed && (
            <div className="flex flex-col">
              <span className="font-bold font-serif text-[#1E293B] text-sm tracking-wide">Vakeel Saab</span>
              <span className="text-[10px] text-gray-500 font-medium tracking-wider uppercase -mt-0.5">AI Legal Intel</span>
            </div>
          )}
        </div>

        {/* Sidebar items */}
        <nav className="p-4 flex flex-col gap-1.5">
          {menuItems.map((item) => {
            const isActive = pathname === item.href;
            const Icon = item.icon;
            return (
              <Link
                key={item.name}
                href={item.href}
                className={`flex items-center gap-3.5 px-4 py-3 rounded-lg transition-colors text-sm font-medium ${
                  isActive ? 'bg-[#1E293B]/5 text-[#1E293B]' : 'text-gray-500 hover:bg-gray-50 hover:text-gray-900'
                }`}
              >
                <Icon className="w-5 h-5 shrink-0" />
                {!sidebarCollapsed && <span>{item.name}</span>}
              </Link>
            );
          })}
        </nav>
      </div>

      {/* Footer controls */}
      <div className="p-4 border-t border-gray-50 flex flex-col gap-1">
        <Link href="/help" className="flex items-center gap-3.5 px-4 py-3 rounded-lg text-gray-500 hover:bg-gray-50 hover:text-gray-900 text-sm font-medium">
          <HelpCircle className="w-5 h-5 shrink-0" />
          {!sidebarCollapsed && <span>Help Center</span>}
        </Link>
      </div>
    </aside>
  );
}
