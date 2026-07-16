export interface LegalCase {
  id: string;
  title: string;
  caseNumber: string;
  court: string;
  parties: string;
  status: 'active' | 'pending' | 'resolved' | 'appealed';
  fillingDate: string;
  nextHearingDate?: string;
  assignedLawyer: string;
  description: string;
}

export const mockCases: LegalCase[] = Array.from({ length: 50 }, (_, i) => {
  const courts = ['Delhi District Court', 'Mumbai Civil Court', 'Bangalore High Court', 'Consumer Forum District'];
  const lawyers = ['Adv. Vikram Singh', 'Adv. Neha Sharma', 'Adv. Amit Patel', 'Adv. Priya Iyer'];
  const statuses: Array<'active' | 'pending' | 'resolved' | 'appealed'> = ['active', 'pending', 'resolved', 'appealed'];

  const titles = [
    'TechCorp vs Apex Global Services',
    'Rajesh Kumar Lease Dispute',
    'Rohan Mehta Consumer Protection Claim',
    'Sharma Family Partition Suit',
  ];

  return {
    id: `case-${i + 1}`,
    title: titles[i % 4] + ` - Part ${Math.floor(i / 4) + 1}`,
    caseNumber: `CS(OS)/${200 + i}/${2020 + (i % 5)}`,
    court: courts[i % 4],
    parties: i % 2 === 0 ? 'Appellant: Rajesh Kumar, Respondent: Landlord Association' : 'Plaintiff: TechCorp, Defendant: Apex Global Services',
    status: statuses[i % 4],
    fillingDate: new Date(Date.now() - (i * 30 + 100) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
    nextHearingDate: i % 2 === 0 ? new Date(Date.now() + (i * 5 + 3) * 24 * 60 * 60 * 1000).toISOString().split('T')[0] : undefined,
    assignedLawyer: lawyers[i % 4],
    description: 'This litigation involves complex civil claims related to breach of contractual obligations, seeking damages and specific performance reliefs.',
  };
});
