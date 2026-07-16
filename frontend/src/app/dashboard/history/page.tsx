'use client';

import { Card } from '@/components/common/cards/Card';
import { History, MessageSquare, FileText } from 'lucide-react';

export default function HistoryPage() {
  return (
    <div className="flex-1 min-h-screen flex flex-col bg-[#F8FAFC]">
      <header className="bg-white border-b border-gray-100 px-8 py-6 shrink-0">
        <h1 className="text-2xl font-bold font-serif text-[#1E293B]">Activity History</h1>
        <p className="text-sm text-gray-500 mt-1">Past conversations, documents, and research activity.</p>
      </header>
      
      <main className="flex-1 p-8 overflow-y-auto">
        <div className="max-w-3xl mx-auto space-y-8">
          
          <div className="space-y-4">
            <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Today</h3>
            <Card className="p-4 bg-white border border-gray-100 flex items-center gap-4 hover:border-[#1E293B]/20 cursor-pointer transition-all">
              <div className="w-10 h-10 rounded bg-indigo-50 flex items-center justify-center text-indigo-600">
                <MessageSquare className="w-5 h-5" />
              </div>
              <div>
                <p className="text-sm font-semibold text-[#1E293B]">Analyzed Commercial Lease</p>
                <p className="text-xs text-gray-500">You asked the AI Assistant to find indemnity clauses.</p>
              </div>
            </Card>
          </div>

          <div className="space-y-4">
            <h3 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Yesterday</h3>
            <Card className="p-4 bg-white border border-gray-100 flex items-center gap-4 hover:border-[#1E293B]/20 cursor-pointer transition-all">
              <div className="w-10 h-10 rounded bg-[#059669]/10 flex items-center justify-center text-[#059669]">
                <FileText className="w-5 h-5" />
              </div>
              <div>
                <p className="text-sm font-semibold text-[#1E293B]">Generated Legal Notice</p>
                <p className="text-xs text-gray-500">Drafted a consumer complaint regarding defective goods.</p>
              </div>
            </Card>
          </div>

        </div>
      </main>
    </div>
  );
}
