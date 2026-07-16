import { create } from 'zustand';
import { Document } from '@/types/document';
import { mockContracts } from '@/mock/contracts';

interface DocumentState {
  documents: Document[];
  selectedDocument: Document | null;
  uploadProgress: Record<string, number>; // fileName -> progress
  setDocuments: (documents: Document[]) => void;
  setSelectedDocument: (doc: Document | null) => void;
  setUploadProgress: (fileName: string, progress: number) => void;
  loadMockDocuments: () => void;
}

export const useDocumentStore = create<DocumentState>((set) => ({
  documents: [],
  selectedDocument: null,
  uploadProgress: {},
  setDocuments: (documents) => set({ documents }),
  setSelectedDocument: (doc) => set({ selectedDocument: doc }),
  setUploadProgress: (fileName, progress) => set((state) => ({
    uploadProgress: { ...state.uploadProgress, [fileName]: progress }
  })),
  loadMockDocuments: () => set({ documents: mockContracts }),
}));
