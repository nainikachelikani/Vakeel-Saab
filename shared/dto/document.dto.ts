// Shared DTOs - Document
export interface UploadDocumentRequest {
  title: string;
  documentType?: string;
  language?: string;
}

export interface SearchDocumentRequest {
  query: string;
  documentType?: string;
  limit?: number;
  offset?: number;
}

export interface AnalyzeDocumentRequest {
  documentId: string;
}

export interface CompareDocumentsRequest {
  documentAId: string;
  documentBId: string;
}
