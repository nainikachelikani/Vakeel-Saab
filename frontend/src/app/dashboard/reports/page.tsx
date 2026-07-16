'use client';

import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { FileText, Download, Share2 } from 'lucide-react';

export default function ReportsPage() {
  const reports = [
    { type: 'Risk Report', title: 'Commercial Lease Risk Analysis', date: 'Oct 24, 2026', status: 'Generated' },
    { type: 'Complaint Letter', title: 'Consumer Forum Draft', date: 'Oct 22, 2026', status: 'Generated' },
    { type: 'Compliance', title: 'Quarterly HR Audit', date: 'Oct 15, 2026', status: 'Generated' },
  ];

  return (
    <div className="flex-1 min-h-screen flex flex-col bg-[#F8FAFC]">
      <header className="bg-white border-b border-gray-100 px-8 py-6 shrink-0 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold font-serif text-[#1E293B]">Reports & Exports</h1>
          <p className="text-sm text-gray-500 mt-1">Generated documents, risk reports, and AI summaries.</p>
        </div>
        <Button className="bg-[#1E293B] text-white">Generate New Report</Button>
      </header>
      
      <main className="flex-1 p-8 overflow-y-auto">
        <div className="max-w-5xl mx-auto">
          <div className="grid gap-4">
            {reports.map((report, idx) => (
              <Card key={idx} className="p-5 flex items-center justify-between bg-white border border-gray-100 rounded-xl hover:shadow-sm transition-all">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-lg bg-gray-50 text-gray-400 flex items-center justify-center">
                    <FileText className="w-6 h-6" />
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-[10px] uppercase font-bold text-[#D97706] bg-[#D97706]/10 px-2 py-0.5 rounded">{report.type}</span>
                      <span className="text-xs text-gray-400">{report.date}</span>
                    </div>
                    <h3 className="font-bold text-[#1E293B] text-base mt-1">{report.title}</h3>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <Button variant="outline" size="sm" className="gap-2 text-gray-600">
                    <Share2 className="w-4 h-4" /> Share
                  </Button>
                  <Button variant="outline" size="sm" className="gap-2 text-gray-600">
                    <Download className="w-4 h-4" /> PDF
                  </Button>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
