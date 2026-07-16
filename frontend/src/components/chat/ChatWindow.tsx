'use client';

import { useState } from 'react';
import { Send, Sparkles, Shield, AlertTriangle } from 'lucide-react';
import { useChat } from '@/hooks/useChat';
import { useChatStore } from '@/store/chat.store';
import { Card } from '../common/cards/Card';
import { Button } from '../common/buttons/Button';

export function ChatWindow() {
  const { currentMessages, sendMessage, sending, loadMockMessages } = useChat();
  const [inputText, setInputText] = useState('');
  const { activeConversation } = useChatStore();

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim()) return;
    await sendMessage(inputText);
    setInputText('');
  };

  const handleMockClick = () => {
    if (activeConversation) {
      loadMockMessages(activeConversation.id);
    }
  };

  return (
    <div className="flex flex-col h-[600px] bg-white border border-gray-100 rounded-2xl overflow-hidden shadow-sm">
      {/* Header */}
      <div className="p-5 border-b border-gray-50 flex justify-between items-center bg-[#0F1B2D]/5">
        <div className="flex flex-col text-left">
          <h3 className="text-sm font-bold text-gray-900 leading-tight">
            {activeConversation?.title || 'Legal Assistant'}
          </h3>
          <p className="text-[10px] text-gray-500 mt-1 uppercase font-bold tracking-wide">
            Platform Workflow Agent
          </p>
        </div>
        <Button variant="ghost" size="sm" onClick={handleMockClick}>
          Simulate Dialogue
        </Button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-4">
        {currentMessages.length === 0 ? (
          <div className="flex-1 flex flex-col items-center justify-center text-center">
            <div className="w-12 h-12 rounded-2xl bg-sky-50 text-sky-500 flex items-center justify-center mb-4">
              <Sparkles className="w-6 h-6" />
            </div>
            <h4 className="text-sm font-bold text-gray-900">Start a new legal dialogue</h4>
            <p className="text-xs text-gray-500 max-w-xs mt-1">
              Ask questions regarding labor, lease, consumer protection, or rights.
            </p>
          </div>
        ) : (
          currentMessages.map((msg) => (
            <div
              key={msg.id}
              className={`flex flex-col max-w-[80%] ${
                msg.role === 'user' ? 'self-end items-end' : 'self-start items-start'
              }`}
            >
              <div
                className={`p-4 rounded-2xl text-sm leading-relaxed ${
                  msg.role === 'user'
                    ? 'bg-[#0F1B2D] text-white rounded-tr-none'
                    : 'bg-gray-100 text-gray-900 rounded-tl-none border border-gray-50'
                }`}
              >
                {msg.content}
              </div>
              {msg.metadata?.agent && (
                <div className="flex items-center gap-1.5 mt-1.5 text-[9px] text-gray-400 font-bold uppercase tracking-wider">
                  <Shield className="w-3 h-3 text-[#10B981]" />
                  Verified by {msg.metadata.agent} • {msg.metadata.confidence * 100}% Confidence
                </div>
              )}
            </div>
          ))
        )}
      </div>

      {/* Input Form */}
      <form onSubmit={handleSend} className="p-4 border-t border-gray-50 flex gap-2 items-center bg-gray-50">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Ask a follow-up question or request draft options..."
          className="flex-1 px-4 py-3 bg-white border border-gray-200 rounded-xl text-sm outline-none focus:border-gray-300 text-gray-900"
          disabled={sending}
        />
        <Button type="submit" disabled={sending} className="rounded-xl shrink-0 p-3">
          <Send className="w-4 h-4" />
        </Button>
      </form>
    </div>
  );
}
