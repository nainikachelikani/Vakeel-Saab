from pydantic import BaseModel, Field
from typing import Optional

class SearchRequest(BaseModel):
    query: str = Field(..., description="The semantic search query")
    document_type: Optional[str] = Field(None, description="Optional document type filter")

class DocumentUploadRequest(BaseModel):
    file_name: str = Field(..., description="Name of the file")
    file_data: str = Field(..., description="Base64 encoded file content")
    title: Optional[str] = Field(None, description="Optional document title")
    document_type: str = Field("other", description="Type of the document")
    file_type: str = Field("application/pdf", description="MIME type of the document")

class ChatRequest(BaseModel):
    message: str = Field(..., description="The user message to send to the chat agent")
    conversation_id: Optional[str] = Field(None, description="Optional conversation UUID")
    category: Optional[str] = Field(None, description="Domain category for the agent")

class AnalyzeRequest(BaseModel):
    document_id: str = Field(..., description="The UUID of the document to analyze")
