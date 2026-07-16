'use client';

import { useThemeStore } from '@/store/theme.store';
import { useAuth } from '@/hooks/useAuth';
import { Menu, Bell, Search, Sun, Moon } from 'lucide-react';
import Link from 'next/link';

export function Navbar() {
  const { toggleSidebar, theme, toggleTheme } = useThemeStore();
  const { user } = useAuth();

  return (
    <header className="h-16 border-b border-gray-100 bg-white flex items-center justify-between px-6 sticky top-0 z-10">
      <div className="flex items-center gap-4 flex-1">
        <button onClick={toggleSidebar} className="text-gray-500 hover:text-gray-900 transition-colors p-1.5 rounded-lg hover:bg-gray-50 md:hidden">
          <Menu className="w-5 h-5" />
        </button>

        {/* Global Search Bar */}
        <div className="relative max-w-md w-full hidden sm:block">
          <span className="absolute inset-y-0 left-3 flex items-center pointer-events-none text-gray-400">
            <Search className="w-4 h-4" />
          </span>
          <input
            type="text"
            placeholder="Search legal documents, cases, or templates..."
            className="w-full bg-[#F8FAFC] border border-gray-100 rounded-lg py-2 pl-9 pr-4 text-xs outline-none focus:border-gray-200 transition-all text-gray-900"
          />
        </div>
      </div>

      <div className="flex items-center gap-4">
        {/* Theme Toggle */}
        <button onClick={toggleTheme} className="text-gray-500 hover:text-gray-900 p-1.5 rounded-lg hover:bg-gray-50 transition-colors">
          {theme === 'dark' ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
        </button>

        {/* Notification Button */}
        <Link href="/notifications" className="text-gray-500 hover:text-gray-900 p-1.5 rounded-lg hover:bg-gray-50 transition-colors relative">
          <Bell className="w-5 h-5" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-[#10B981] rounded-full border border-white"></span>
        </Link>

        {/* User Account */}
        <Link href="/profile" className="flex items-center gap-3.5 pl-2 border-l border-gray-100">
          <div className="w-8 h-8 rounded-full bg-[#1E293B] text-white flex items-center justify-center font-bold text-xs">
            {user?.fullName?.charAt(0) || 'U'}
          </div>
          <div className="flex flex-col text-left hidden md:flex">
            <span className="text-xs font-semibold text-gray-900 leading-none">{user?.fullName || 'Guest User'}</span>
            <span className="text-[9px] font-medium text-gray-500 tracking-wide uppercase mt-0.5">{user?.role || 'Visitor'}</span>
          </div>
        </Link>
      </div>
    </header>
  );
}
