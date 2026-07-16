'use client';

import { ChatWindow } from '@/components/chat/ChatWindow';

export default function AssistantPage() {
  return (
    <div className="flex-1 h-screen flex flex-col bg-[#F8FAFC]">
      <header className="bg-white border-b border-gray-100 px-8 py-4 flex items-center justify-between shrink-0">
        <div>
          <h1 className="text-xl font-bold font-serif text-[#1E293B]">AI Legal Assistant</h1>
          <p className="text-xs text-gray-500">Ask questions, generate complaints, or review clauses.</p>
        </div>
      </header>
      
      <main className="flex-1 overflow-hidden relative">
        <div className="absolute inset-0 max-w-4xl mx-auto flex flex-col bg-white shadow-sm border-x border-gray-100">
          <ChatWindow />
        </div>
      </main>
    </div>
  );
}
