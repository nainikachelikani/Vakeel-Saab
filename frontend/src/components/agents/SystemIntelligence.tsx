'use client';

import { Activity, ShieldAlert, Cpu, Terminal, CheckCircle2, Loader2, ArrowDown } from 'lucide-react';
import { useState, useEffect } from 'react';

export function SystemIntelligence() {
  const [activeStep, setActiveStep] = useState(0);

  const pipeline = [
    { name: 'Router Agent', tool: 'IntentClassifier', resource: 'N/A', conf: '99%', time: '12ms' },
    { name: 'Domain Classification', tool: 'LegalTaxonomy', resource: 'N/A', conf: '94%', time: '45ms' },
    { name: 'Retrieval', tool: 'SemanticSearch', resource: 'VectorDB', conf: '88%', time: '312ms' },
    { name: 'Legal Analysis', tool: 'ReasoningEngine', resource: 'LLM-Core', conf: '92%', time: '1.2s' },
    { name: 'Citation', tool: 'PrecedentMatcher', resource: 'CaseLaw API', conf: '97%', time: '230ms' },
    { name: 'Planner', tool: 'TaskOrchestrator', resource: 'N/A', conf: '95%', time: '50ms' },
    { name: 'Reviewer', tool: 'ComplianceChecker', resource: 'RulesEngine', conf: '98%', time: '890ms' }
  ];

  // Simulate pipeline execution
  useEffect(() => {
    const timer = setInterval(() => {
      setActiveStep((prev) => (prev < pipeline.length ? prev + 1 : 0));
    }, 2000);
    return () => clearInterval(timer);
  }, [pipeline.length]);

  return (
    <div className="flex flex-col gap-4 w-full bg-white border border-gray-100 rounded-2xl p-6 shadow-sm">
      <div className="flex items-center gap-2 mb-2 pb-3 border-b border-gray-50">
        <Cpu className="w-5 h-5 text-[#1E293B]" />
        <h3 className="text-sm font-bold text-[#1E293B]">Agent Execution Pipeline</h3>
      </div>

      <div className="flex flex-col gap-2">
        {pipeline.map((node, index) => {
          const isComplete = index < activeStep;
          const isActive = index === activeStep;
          const isPending = index > activeStep;

          return (
            <div key={node.name} className="flex flex-col">
              <div className={`p-3 rounded-xl border transition-all duration-500 ${isActive ? 'bg-[#1E293B]/5 border-[#1E293B]/20 shadow-sm transform scale-[1.02]' : isComplete ? 'bg-white border-gray-100' : 'bg-gray-50/50 border-gray-50 opacity-50'}`}>
                <div className="flex justify-between items-center mb-2">
                  <span className={`font-bold text-sm ${isActive ? 'text-[#1E293B]' : 'text-gray-600'}`}>
                    {node.name}
                  </span>
                  <div className="flex items-center gap-1.5">
                    {isComplete && <CheckCircle2 className="w-4 h-4 text-[#059669]" />}
                    {isActive && <Loader2 className="w-4 h-4 text-[#D97706] animate-spin" />}
                    <span className={`text-[10px] font-bold uppercase px-2 py-0.5 rounded ${isComplete ? 'bg-[#059669]/10 text-[#059669]' : isActive ? 'bg-[#D97706]/10 text-[#D97706]' : 'bg-gray-100 text-gray-400'}`}>
                      {isComplete ? 'Success' : isActive ? 'Processing' : 'Pending'}
                    </span>
                  </div>
                </div>
                
                <div className="grid grid-cols-2 gap-x-2 gap-y-1 text-[10px] text-gray-500">
                  <div className="flex justify-between"><span>Tool:</span> <span className="font-mono text-[#1E293B]">{node.tool}</span></div>
                  <div className="flex justify-between"><span>Resource:</span> <span className="font-mono text-[#1E293B]">{node.resource}</span></div>
                  <div className="flex justify-between"><span>Confidence:</span> <span className="font-mono text-[#059669]">{isComplete || isActive ? node.conf : '-'}</span></div>
                  <div className="flex justify-between"><span>Exec Time:</span> <span className="font-mono text-gray-700">{isComplete || isActive ? node.time : '-'}</span></div>
                </div>
              </div>
              
              {index < pipeline.length - 1 && (
                <div className="flex justify-center my-1">
                  <ArrowDown className={`w-3 h-3 ${isComplete ? 'text-[#1E293B]' : 'text-gray-200'}`} />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
