'use client';

import { SystemIntelligence } from '@/components/agents/SystemIntelligence';

export default function AgentMonitor() {
  return (
    <div className="flex-1 min-h-screen flex flex-col bg-[#F8FAFC]">
      <header className="bg-white border-b border-gray-100 px-8 py-6 shrink-0 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold font-serif text-[#1E293B]">AI Agent Orchestrator Monitor</h1>
          <p className="text-sm text-gray-500 mt-1">Supervise real-time execution of router, domain, retriever, planner, and reviewer agents.</p>
        </div>
      </header>
      
      <main className="flex-1 p-8 overflow-y-auto">
        <div className="max-w-4xl mx-auto">
          <SystemIntelligence />
        </div>
      </main>
    </div>
  );
}
