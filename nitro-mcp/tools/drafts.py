import httpx
import os
from mcp import tool

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000/api/v1")

@tool()
async def explain_section(section: str) -> str:
    """Pass section context inside the message wrapper for explanation."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/chat",
            json={"message": f"Explain this section: {section}"}
        )
        return response.text

@tool()
async def retrieve_case_history(conversation_id: str) -> str:
    """Retrieve chat logs matching active session ID."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BACKEND_URL}/chat/conversations" # mock endpoint for now
        )
        return response.text

@tool()
async def generate_notice(template_params: str) -> str:
    """Generate a legal notice report."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/reports",
            json={"type": "notice", "params": template_params}
        )
        return response.text

@tool()
async def generate_petition(template_params: str) -> str:
    """Trigger report generator with legal petition type."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/reports",
            json={"type": "petition", "params": template_params}
        )
        return response.text

@tool()
async def legal_advice(message: str) -> str:
    """Send user message history; set agent focus to domain_agent."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/chat",
            json={"message": message, "category": "domain"}
        )
        return response.text

@tool()
async def legal_rag(message: str) -> str:
    """Trigger context-augmented chat execution."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/chat",
            json={"message": message}
        )
        return response.text
