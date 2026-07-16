'use client';

import { useState } from 'react';
import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { UploadCloud, FileText, AlertTriangle, BookOpen, List, ShieldCheck, Sparkles } from 'lucide-react';
import { ChatWindow } from '@/components/chat/ChatWindow';

export default function DocumentsWorkspace() {
  const [activeTab, setActiveTab] = useState<'summary' | 'risk' | 'clauses' | 'citations'>('summary');

  return (
    <div className="flex-1 h-screen flex flex-col bg-[#F8FAFC] overflow-hidden">
      
      {/* Header */}
      <header className="bg-white border-b border-gray-100 px-6 py-3 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-4">
          <div className="w-10 h-10 rounded-lg bg-indigo-50 text-indigo-600 flex items-center justify-center">
            <FileText className="w-5 h-5" />
          </div>
          <div>
            <h1 className="text-lg font-bold font-serif text-[#1E293B]">Commercial_Lease_Agreement.pdf</h1>
            <div className="flex items-center gap-2 mt-0.5">
              <span className="text-[10px] uppercase font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded">PDF Document</span>
              <span className="text-xs text-gray-400">Uploaded 2 hours ago</span>
            </div>
          </div>
        </div>
        <div className="flex items-center gap-3">
          <Button variant="outline" size="sm" className="gap-2">
            <UploadCloud className="w-4 h-4" /> Upload New
          </Button>
          <Button size="sm" className="bg-[#1E293B] text-white">Generate Report</Button>
        </div>
      </header>

      {/* Main Split Workspace */}
      <main className="flex-1 flex overflow-hidden">
        
        {/* Left Side: PDF Viewer & Analysis Panels */}
        <div className="flex-1 flex flex-col border-r border-gray-200">
          
          {/* Mock PDF Viewer Area */}
          <div className="flex-[3] bg-gray-100 flex items-center justify-center relative overflow-hidden p-6">
            <div className="w-full max-w-2xl h-full bg-white shadow-md border border-gray-200 flex flex-col items-center p-12 overflow-y-auto">
              <h2 className="font-serif font-bold text-2xl mb-8 border-b pb-4 w-full text-center">COMMERCIAL LEASE AGREEMENT</h2>
              <div className="space-y-6 text-sm text-gray-600 leading-relaxed text-justify">
                <p>THIS LEASE AGREEMENT (hereinafter referred to as the &quot;Lease&quot;) is made and entered into this day...</p>
                <p>1. PREMISES: The Landlord hereby leases to the Tenant, and the Tenant hereby leases from the Landlord...</p>
                <div className="bg-red-50 border border-red-100 p-4 rounded text-red-900 my-4 relative">
                  <div className="absolute -left-2 top-4 w-1 h-8 bg-red-500 rounded-full" />
                  <strong>8. INDEMNIFICATION:</strong> Tenant shall indemnify and hold Landlord harmless against any and all claims, demands, damages, costs, and expenses, including reasonable attorneys&apos; fees for the defense thereof, arising from the conduct or management of the business conducted by Tenant...
                </div>
                <p>9. DEFAULT: In the event Tenant fails to pay rent when due...</p>
              </div>
            </div>
          </div>

          {/* Bottom Analysis Tabs Area */}
          <div className="flex-[2] bg-white border-t border-gray-200 flex flex-col min-h-0">
            {/* Tabs */}
            <div className="flex items-center border-b border-gray-100 px-4">
              <button onClick={() => setActiveTab('summary')} className={`px-4 py-3 text-sm font-medium border-b-2 transition-colors ${activeTab === 'summary' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Summary</button>
              <button onClick={() => setActiveTab('risk')} className={`px-4 py-3 text-sm font-medium border-b-2 transition-colors ${activeTab === 'risk' ? 'border-red-500 text-red-600' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Risk Analysis <span className="ml-1 bg-red-100 text-red-600 px-1.5 py-0.5 rounded text-[10px]">2</span></button>
              <button onClick={() => setActiveTab('clauses')} className={`px-4 py-3 text-sm font-medium border-b-2 transition-colors ${activeTab === 'clauses' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Clause Navigation</button>
              <button onClick={() => setActiveTab('citations')} className={`px-4 py-3 text-sm font-medium border-b-2 transition-colors ${activeTab === 'citations' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Citations</button>
            </div>
            
            {/* Tab Content */}
            <div className="flex-1 overflow-y-auto p-4">
              {activeTab === 'summary' && (
                <div className="space-y-4">
                  <h3 className="font-bold text-sm text-gray-900">AI Document Summary</h3>
                  <p className="text-sm text-gray-600">This is a standard 5-year commercial lease agreement. The base rent is set at market rate with a 3% annual escalation. Key obligations fall heavily on the tenant regarding maintenance and indemnification.</p>
                </div>
              )}
              {activeTab === 'risk' && (
                <div className="space-y-4">
                  <Card className="p-4 border-red-100 bg-red-50/50">
                    <div className="flex items-start gap-3">
                      <AlertTriangle className="w-5 h-5 text-red-500 mt-0.5 shrink-0" />
                      <div>
                        <h4 className="font-bold text-sm text-red-900">Unilateral Indemnification</h4>
                        <p className="text-xs text-red-700 mt-1">Clause 8 holds the tenant completely liable for all claims regardless of landlord negligence. Highly unfavorable.</p>
                      </div>
                    </div>
                  </Card>
                </div>
              )}
              {activeTab === 'clauses' && (
                <div className="space-y-2">
                  <div className="p-3 bg-gray-50 border border-gray-100 rounded flex justify-between items-center text-sm">
                    <span className="font-medium">1. Premises</span>
                    <span className="text-gray-400">Page 1</span>
                  </div>
                  <div className="p-3 bg-gray-50 border border-gray-100 rounded flex justify-between items-center text-sm">
                    <span className="font-medium text-red-600">8. Indemnification</span>
                    <span className="text-gray-400">Page 3</span>
                  </div>
                </div>
              )}
              {activeTab === 'citations' && (
                <div className="space-y-4">
                  <Card className="p-4">
                    <div className="flex items-center gap-2 mb-2">
                      <BookOpen className="w-4 h-4 text-blue-600" />
                      <h4 className="font-bold text-sm">Indian Contract Act, 1872</h4>
                    </div>
                    <p className="text-xs text-gray-600">Section 73: Compensation for loss or damage caused by breach of contract.</p>
                  </Card>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Right Side: AI Assistant context-aware chat */}
        <div className="w-[400px] flex flex-col bg-white shrink-0">
          <div className="p-4 border-b border-gray-100 bg-[#F8FAFC]">
            <h2 className="font-bold text-sm text-[#1E293B] flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-[#D97706]" /> Document Assistant
            </h2>
            <p className="text-xs text-gray-500 mt-1">Ask questions specifically about this contract.</p>
          </div>
          <div className="flex-1 overflow-hidden relative">
             <ChatWindow />
          </div>
        </div>

      </main>
    </div>
  );
}
