'use client';

import { useState } from 'react';
import { Card } from '@/components/common/cards/Card';
import { Input } from '@/components/common/forms/Input';
import { Button } from '@/components/common/buttons/Button';
import { Sparkles, Search, FileText, UploadCloud, FileEdit, Scale, Users, MessageSquare, ShieldAlert } from 'lucide-react';
import Link from 'next/link';
import { APP_ROUTES } from '@/constants/ui';

export default function UnifiedDashboard() {
  const [query, setQuery] = useState('');

  return (
    <div className="flex-1 flex flex-col min-h-screen bg-[#F8FAFC]">
      <main className="flex-1 p-8 overflow-y-auto">
        <div className="max-w-5xl mx-auto space-y-12">
          
          {/* AI Input Section */}
          <section className="text-center space-y-6 mt-8">
            <h2 className="text-3xl font-serif font-bold text-[#1E293B]">How can Vakeel Saab help you today?</h2>
            <div className="relative max-w-2xl mx-auto">
              <textarea 
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Ask Vakeel Saab anything..."
                className="w-full h-32 rounded-2xl bg-white border border-gray-200 p-6 pr-16 text-lg shadow-sm resize-none focus:outline-none focus:ring-2 focus:ring-[#1E293B]/20 transition-all placeholder:text-gray-400"
              />
              <div className="absolute bottom-4 right-4">
                <Button size="sm" className="w-10 h-10 rounded-full shadow-md p-0 flex items-center justify-center">
                  <Sparkles className="w-5 h-5" />
                </Button>
              </div>
            </div>
          </section>

          {/* Quick Actions */}
          <section>
            <h3 className="text-sm font-bold text-gray-400 uppercase tracking-wider mb-4">Quick Actions</h3>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              <Link href={APP_ROUTES.ASSISTANT}>
                <Card hoverable className="p-4 flex flex-col items-center justify-center text-center gap-3 h-32 bg-white rounded-xl border border-gray-100">
                  <div className="w-10 h-10 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center">
                    <MessageSquare className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-gray-700">Ask Legal Question</span>
                </Card>
              </Link>
              <Link href={APP_ROUTES.DOCUMENTS}>
                <Card hoverable className="p-4 flex flex-col items-center justify-center text-center gap-3 h-32 bg-white rounded-xl border border-gray-100">
                  <div className="w-10 h-10 rounded-lg bg-[#D97706]/10 text-[#D97706] flex items-center justify-center">
                    <UploadCloud className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-gray-700">Upload Legal Document</span>
                </Card>
              </Link>
              <Link href={APP_ROUTES.REPORTS}>
                <Card hoverable className="p-4 flex flex-col items-center justify-center text-center gap-3 h-32 bg-white rounded-xl border border-gray-100">
                  <div className="w-10 h-10 rounded-lg bg-[#059669]/10 text-[#059669] flex items-center justify-center">
                    <FileEdit className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-gray-700">Generate Complaint</span>
                </Card>
              </Link>
              <Link href={APP_ROUTES.RESEARCH}>
                <Card hoverable className="p-4 flex flex-col items-center justify-center text-center gap-3 h-32 bg-white rounded-xl border border-gray-100">
                  <div className="w-10 h-10 rounded-lg bg-[#1E293B]/10 text-[#1E293B] flex items-center justify-center">
                    <Scale className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-gray-700">Research Laws</span>
                </Card>
              </Link>
              <Link href={APP_ROUTES.DASHBOARD}>
                <Card hoverable className="p-4 flex flex-col items-center justify-center text-center gap-3 h-32 bg-white rounded-xl border border-gray-100">
                  <div className="w-10 h-10 rounded-lg bg-rose-50 text-rose-600 flex items-center justify-center">
                    <Users className="w-5 h-5" />
                  </div>
                  <span className="text-xs font-semibold text-gray-700">Find Legal Aid</span>
                </Card>
              </Link>
            </div>
          </section>

          {/* Recent Sections Grid */}
          <div className="grid md:grid-cols-2 gap-8">
            
            {/* Recent Conversations */}
            <section>
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-sm font-bold text-gray-400 uppercase tracking-wider">Recent Conversations</h3>
                <Link href={APP_ROUTES.HISTORY} className="text-xs font-bold text-[#1E293B] hover:underline">View All</Link>
              </div>
              <div className="space-y-3">
                {[1, 2, 3].map((i) => (
                  <Card key={i} className="p-4 bg-white border border-gray-100 rounded-xl flex items-center justify-between group cursor-pointer hover:border-[#1E293B]/20">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-gray-50 flex items-center justify-center text-gray-400">
                        <MessageSquare className="w-4 h-4" />
                      </div>
                      <div>
                        <p className="text-sm font-semibold text-gray-900">Tenant Rights Query</p>
                        <p className="text-xs text-gray-500">2 hours ago</p>
                      </div>
                    </div>
                  </Card>
                ))}
              </div>
            </section>

            {/* Recent Documents */}
            <section>
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-sm font-bold text-gray-400 uppercase tracking-wider">Recent Documents</h3>
                <Link href={APP_ROUTES.DOCUMENTS} className="text-xs font-bold text-[#1E293B] hover:underline">View All</Link>
              </div>
              <div className="space-y-3">
                {[1, 2, 3].map((i) => (
                  <Card key={i} className="p-4 bg-white border border-gray-100 rounded-xl flex items-center justify-between group cursor-pointer hover:border-[#1E293B]/20">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded bg-red-50 flex items-center justify-center text-red-500">
                        <FileText className="w-4 h-4" />
                      </div>
                      <div>
                        <p className="text-sm font-semibold text-gray-900">Commercial_Lease_Agreement.pdf</p>
                        <p className="text-xs text-gray-500">Yesterday &middot; High Risk</p>
                      </div>
                    </div>
                  </Card>
                ))}
              </div>
            </section>
            
          </div>
        </div>
      </main>
    </div>
  );
}
