import { Document, UploadDocumentRequest, SearchDocumentRequest, RiskAnalysis } from '@/types/document';
import { API_ROUTES } from '@/constants/ui';
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
});

export const documentService = {
  async listDocuments(): Promise<Document[]> {
    const response = await api.get(API_ROUTES.DOCUMENTS.LIST);
    return response.data;
  },

  async uploadDocument(file: File, docInfo?: UploadDocumentRequest): Promise<Document> {
    const formData = new FormData();
    formData.append('file', file);
    if (docInfo) {
      formData.append('title', docInfo.title);
      if (docInfo.documentType) formData.append('document_type', docInfo.documentType);
    }
    const response = await api.post(API_ROUTES.DOCUMENTS.UPLOAD, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  },

  async searchDocuments(query: SearchDocumentRequest): Promise<any> {
    const response = await api.post(API_ROUTES.DOCUMENTS.SEARCH, query);
    return response.data;
  },

  async getRiskAnalysis(documentId: string): Promise<RiskAnalysis> {
    const response = await api.post(API_ROUTES.DOCUMENTS.RISK, { document_id: documentId });
    return response.data;
  },
};
