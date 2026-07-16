import { Document } from '@/types/document';

export const mockContracts: Document[] = Array.from({ length: 100 }, (_, i) => {
  const id = `contract-${i + 1}`;
  const parties = [
    ['TechCorp Solutions Ltd', 'Apex Global Industries'],
    ['Tata Consultancy Services', 'Reliance Industries Ltd'],
    ['Infosys Technologies', 'HDFC Bank Ltd'],
    ['Wipro Digital Services', 'ICICI Bank Ltd'],
    ['Adani Enterprises', 'Larsen & Toubro Ltd'],
  ][i % 5];

  const types: Array<'contract' | 'nda' | 'agreement' | 'policy'> = ['contract', 'nda', 'agreement', 'policy'];
  const docType = types[i % 4];

  const titles = [
    `Master_Services_Agreement_${parties[0].replace(/\s+/g, '_')}_v${(i % 3) + 1}.pdf`,
    `Non_Disclosure_Agreement_${parties[0].replace(/\s+/g, '_')}_Final.docx`,
    `Vendor_Service_Agreement_${parties[1].replace(/\s+/g, '_')}_Executed.pdf`,
    `Data_Processing_Addendum_${parties[0].replace(/\s+/g, '_')}_2024.pdf`,
  ];

  const statusList: Array<'analyzed' | 'processing' | 'pending' | 'error'> = ['analyzed', 'analyzed', 'processing', 'pending'];
  const status = statusList[i % 4];
  const riskScore = status === 'analyzed' ? Math.floor(20 + (i * 7) % 75) : undefined;

  return {
    id,
    title: titles[i % 4],
    fileName: titles[i % 4],
    fileType: titles[i % 4].endsWith('.pdf') ? 'application/pdf' : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    fileSize: 1024 * 102 * ((i % 10) + 1),
    documentType: docType,
    status,
    summary: status === 'analyzed' ? `This document is a formal ${docType} between ${parties[0]} and ${parties[1]} governing services, liabilities, and intellectual property terms.` : undefined,
    riskScore,
    pageCount: (i % 15) + 3,
    language: 'en',
    createdAt: new Date(Date.now() - i * 24 * 60 * 60 * 1000).toISOString(),
    updatedAt: new Date(Date.now() - i * 12 * 60 * 60 * 1000).toISOString(),
  };
});
