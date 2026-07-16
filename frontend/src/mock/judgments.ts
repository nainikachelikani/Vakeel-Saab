export interface CourtJudgment {
  id: string;
  title: string;
  citation: string;
  court: string;
  judge: string;
  appellant: string;
  respondent: string;
  date: string;
  summary: string;
  keyTakeaways: string[];
  keywords: string[];
}

export const mockJudgments: CourtJudgment[] = Array.from({ length: 50 }, (_, i) => {
  const courts = [
    'Supreme Court of India',
    'High Court of Delhi',
    'High Court of Bombay',
    'High Court of Karnataka',
    'High Court of Madras',
  ];
  
  const subjects = [
    'Unfair labor termination and severance compensation',
    'Intellectual property rights infringement in digital media',
    'Land acquisition compensation valuation discrepancies',
    'Corporate governance and shareholder minority rights protection',
    'Arbitration award enforcement disputes under Section 34',
  ];

  const citations = [
    `AIR 202${i % 5} SC ${100 + i * 7}`,
    `202${i % 5} SCC ${200 + i * 9}`,
    `(202${i % 5}) ${i + 1} SCALE ${50 + i * 4}`,
  ];

  return {
    id: `judgment-${i + 1}`,
    title: `${subjects[i % 5]} - Case #${1000 + i}`,
    citation: citations[i % 3],
    court: courts[i % 5],
    judge: `Hon'ble Justice ${['D.Y. Chandrachud', 'S.K. Kaul', 'S.R. Bhat', 'H. Kohli', 'B.V. Nagarathna'][i % 5]}`,
    appellant: `${['Rajesh Sharma', 'TechCorp Solutions', 'Union of India', 'Karnataka Power Corp', 'Sundaram Finance'][i % 5]}`,
    respondent: `${['State of Maharashtra', 'Apex Global Industries', 'A.K. Gopalan', 'Municipal Corporation of Delhi', 'Tata Motors Ltd'][i % 5]}`,
    date: new Date(Date.now() - (i * 45 + 10) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
    summary: `A landmark ruling detailing the scope of liability and obligations under relevant legislative frameworks. The court evaluated historical precedents and clarified the interpretation of statutory provisions to determine liability.`,
    keyTakeaways: [
      'Clarified limits of liability in service agreements.',
      'Emphasized procedural fairness in administrative actions.',
      'Invalidated overly restrictive covenants.',
    ],
    keywords: ['indemnity', 'termination', 'damages', 'statute', 'precedent'],
  };
});
