import httpx
import os
from mcp import tool

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000/api/v1")

@tool()
async def summarize_document(document_id: str) -> str:
    """Run AI analysis to summarize a document."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/analyze",
            json={"document_id": document_id}
        )
        return response.text

@tool()
async def upload_document(file_name: str, file_data: str, title: str = None, document_type: str = "other") -> str:
    """Upload a document to the server. file_data must be base64 encoded."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/upload",
            headers={"Content-Type": "application/json"},
            json={
                "file_name": file_name,
                "file_data": file_data,
                "title": title,
                "document_type": document_type
            }
        )
        return response.text

@tool()
async def document_analysis(document_id: str) -> str:
    """Returns full risks and recommendations list for a document."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/analyze",
            json={"document_id": document_id}
        )
        return response.text
