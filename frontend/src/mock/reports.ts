import { Report } from '@/types/report';

export const mockReports: Report[] = Array.from({ length: 50 }, (_, i) => {
  const types: Array<'risk_analysis' | 'compliance_audit' | 'contract_summary' | 'legal_brief' | 'case_analysis'> = [
    'risk_analysis',
    'compliance_audit',
    'contract_summary',
    'legal_brief',
    'case_analysis',
  ];

  const reportType = types[i % 5];
  const titles = [
    `Risk_Analysis_Report_MSA_v${(i % 3) + 1}.pdf`,
    `Compliance_Audit_GDPR_Assessment_2024.pdf`,
    `Contract_Executive_Summary_NDA_Final.pdf`,
    `Legal_Brief_Unfair_Termination_Case.pdf`,
    `Case_Analysis_Supreme_Court_Precedents.pdf`,
  ];

  const statuses: Array<'generating' | 'completed' | 'failed'> = ['completed', 'completed', 'completed', 'generating', 'failed'];
  const status = statuses[i % 5];

  return {
    id: `report-${i + 1}`,
    title: titles[i % 5],
    reportType,
    summary: status === 'completed' ? `Automated ${reportType.replace('_', ' ')} generated for uploaded files, summarizing key legal risks, liabilities, and checklist validation findings.` : undefined,
    status,
    createdAt: new Date(Date.now() - i * 3 * 24 * 60 * 60 * 1000).toISOString(),
    updatedAt: new Date(Date.now() - i * 3 * 24 * 60 * 60 * 1000 + 10 * 60 * 1000).toISOString(),
  };
});
