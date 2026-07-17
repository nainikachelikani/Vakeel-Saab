import httpx
import os
from mcp import tool

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000/api/v1")

@tool()
async def search_case(query: str) -> str:
    """Searches for legal cases in the database."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/search",
            json={"query": query, "document_type": "case"}
        )
        return response.text

@tool()
async def search_law(query: str) -> str:
    """Searches for specific laws or statutes in the database."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/search",
            json={"query": query, "document_type": "statute"}
        )
        return response.text

@tool()
async def vector_search(query: str) -> str:
    """Execute pure vector similarity matching query across all documents."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/documents/search",
            json={"query": query}
        )
        return response.text
