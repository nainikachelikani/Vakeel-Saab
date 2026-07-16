import { Report, ReportDetail, CreateReportRequest } from '@/types/report';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
});

export const reportService = {
  async listReports(): Promise<Report[]> {
    const response = await api.get(API_ROUTES.REPORTS.LIST);
    return response.data;
  },

  async createReport(data: CreateReportRequest): Promise<Report> {
    const response = await api.post(API_ROUTES.REPORTS.CREATE, data);
    return response.data;
  },

  async getReportDetail(id: string): Promise<ReportDetail> {
    const response = await api.get(API_ROUTES.REPORTS.DETAIL(id));
    return response.data;
  },
};
