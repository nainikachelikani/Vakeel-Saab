import { Notification } from '@/types/notification';

export const mockNotifications: Notification[] = Array.from({ length: 100 }, (_, i) => {
  const types: Array<'info' | 'warning' | 'success' | 'error' | 'document' | 'report' | 'system'> = [
    'document',
    'report',
    'info',
    'warning',
    'success',
    'system',
    'error',
  ];

  const type = types[i % 7];
  const titles = [
    'Document uploaded successfully',
    'Legal report generation completed',
    'Upcoming hearing alert',
    'Compliance warning detected',
    'Payment successful',
    'System maintenance notice',
    'Analysis failed to process',
  ];

  const messages = [
    'Your uploaded file was received and is queued for parsing.',
    'The risk assessment report for your contract is now available in reports.',
    'A new hearing date has been posted for your active litigation.',
    'We found 2 clauses that violate standardized GDPR compliance rules.',
    'Your subscription renewal payment was processed successfully.',
    'Our legal intelligence database will undergo maintenance tonight at 2 AM.',
    'We encountered an OCR processing issue with the uploaded image scan.',
  ];

  const isRead = i > 10; // First 10 are unread

  return {
    id: `notif-${i + 1}`,
    title: titles[i % 7],
    message: messages[i % 7],
    notificationType: type,
    isRead,
    actionUrl: type === 'report' ? `/dashboard/reports` : undefined,
    createdAt: new Date(Date.now() - i * 4 * 60 * 60 * 1000).toISOString(),
  };
});
