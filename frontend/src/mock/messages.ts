import { Message } from '@/types/chat';

export const mockMessages: Message[] = Array.from({ length: 200 }, (_, i) => {
  const convId = `conv-${Math.floor(i / 10) + 1}`;
  const isUser = i % 2 === 0;

  const userMessages = [
    'I need help reviewing my residential lease agreement. Is there any hidden clause?',
    'What is the notice period required if I want to terminate the lease early?',
    'My landlord is refusing to return the security deposit. What are my options?',
    'How do I file a consumer complaint against an e-commerce website for a defective product?',
    'The company delivered a damaged laptop and is refusing a refund. Can I sue them?',
    'What documents do I need to attach for a consumer forum complaint?',
    'Can you help me analyze this NDA? It says the non-compete is for 3 years.',
    'Is a 3-year non-compete clause legally enforceable in India?',
    'What should be the ideal duration for a non-compete clause in a software job?',
    'How can I send a formal legal notice for unpaid salary to my employer?',
  ];

  const assistantMessages = [
    'I can help with that. Please upload the lease agreement or paste the clauses you are concerned about.',
    'Typically, lease agreements require a 30-day or 60-day notice. Let me look at your specific contract to verify.',
    'Under the Rent Control Act, you can send a formal legal notice to demand the deposit. If unpaid, you can file a civil suit.',
    'You can file a complaint online via the National Consumer Helpline (NCH) or approach the District Consumer Commission.',
    'Yes, under the Consumer Protection Act, 2019, refusing to refund for defective goods constitutes an unfair trade practice.',
    'You should attach the purchase invoice, proof of payment, communication logs, and photos of the damaged item.',
    'A 3-year non-compete is generally considered restrictive. Under Section 27 of the Contract Act, this might be void.',
    'Section 27 of the Indian Contract Act, 1872, voids any agreement in restraint of trade, profession, or business.',
    'For software engineers, standard non-compete clauses are usually 6 to 12 months and restricted to direct competitors.',
    'You can draft a formal demand notice under the Payment of Wages Act. I can generate a template for you.',
  ];

  return {
    id: `msg-${i + 1}`,
    content: isUser ? userMessages[i % userMessages.length] : assistantMessages[Math.floor(i / 2) % assistantMessages.length],
    role: isUser ? 'user' : 'assistant',
    createdAt: new Date(Date.now() - (200 - i) * 30 * 60 * 1000).toISOString(),
    metadata: !isUser ? {
      agent: i % 4 === 0 ? 'legal_analysis_agent' : 'domain_agent',
      processingTimeMs: Math.floor(800 + (i * 27) % 1500),
      confidence: parseFloat((0.85 + (i % 15) * 0.01).toFixed(2)),
    } : undefined,
  };
});
