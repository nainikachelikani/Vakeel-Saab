'use client';

import { Input } from '@/components/common/forms/Input';
import { Card } from '@/components/common/cards/Card';
import { Button } from '@/components/common/buttons/Button';
import { Search, Filter, Book, FileText, Bookmark } from 'lucide-react';
import { useState } from 'react';

export default function LegalResearchPage() {
  const [activeTab, setActiveTab] = useState<'statutes' | 'judgments' | 'templates'>('statutes');

  return (
    <div className="flex-1 min-h-screen flex flex-col bg-[#F8FAFC]">
      <header className="bg-white border-b border-gray-100 px-8 py-6 shrink-0">
        <h1 className="text-2xl font-bold font-serif text-[#1E293B] mb-4">Legal Research Database</h1>
        <div className="flex gap-4 max-w-4xl">
          <div className="flex-1">
            <Input 
              icon={<Search className="w-4 h-4 text-gray-400" />}
              placeholder="Semantic search across case laws, statutes, and templates..."
              className="bg-gray-50 border-gray-200"
            />
          </div>
          <Button variant="outline" className="gap-2 shrink-0">
            <Filter className="w-4 h-4" /> Advanced Filters
          </Button>
          <Button className="bg-[#1E293B] text-white shrink-0">Search</Button>
        </div>
      </header>
      
      <main className="flex-1 p-8 overflow-y-auto">
        <div className="max-w-5xl mx-auto">
          {/* Tabs */}
          <div className="flex gap-2 border-b border-gray-200 mb-6">
            <button onClick={() => setActiveTab('statutes')} className={`px-4 py-2 text-sm font-medium border-b-2 transition-colors ${activeTab === 'statutes' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Statutes & Acts</button>
            <button onClick={() => setActiveTab('judgments')} className={`px-4 py-2 text-sm font-medium border-b-2 transition-colors ${activeTab === 'judgments' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Court Judgments</button>
            <button onClick={() => setActiveTab('templates')} className={`px-4 py-2 text-sm font-medium border-b-2 transition-colors ${activeTab === 'templates' ? 'border-[#1E293B] text-[#1E293B]' : 'border-transparent text-gray-500 hover:text-gray-900'}`}>Legal Templates</button>
          </div>

          {/* Results Area */}
          <div className="space-y-4">
            <Card className="p-6 bg-white border border-gray-100 rounded-xl hover:border-[#1E293B]/20 transition-all group">
              <div className="flex justify-between items-start">
                <div className="flex gap-3">
                  <div className="mt-1 text-[#1E293B]">
                    {activeTab === 'judgments' ? <Book className="w-5 h-5" /> : <FileText className="w-5 h-5" />}
                  </div>
                  <div>
                    <h3 className="font-bold text-[#1E293B] text-lg mb-1 group-hover:text-[#D97706] transition-colors">
                      {activeTab === 'statutes' ? 'The Indian Contract Act, 1872' : 'Sample Results'}
                    </h3>
                    <p className="text-sm text-gray-600 line-clamp-2">This is a mockup result for the semantic search. In the real application, the RAG agent will populate these results based on vector embeddings.</p>
                    <div className="mt-3 flex gap-2">
                      <span className="text-[10px] uppercase font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded">Relevance: 98%</span>
                    </div>
                  </div>
                </div>
                <Button variant="ghost" size="sm" className="text-gray-400 hover:text-[#1E293B] p-0 w-8 h-8 flex items-center justify-center">
                  <Bookmark className="w-4 h-4" />
                </Button>
              </div>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}
