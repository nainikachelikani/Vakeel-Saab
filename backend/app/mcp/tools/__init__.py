"""MCP Tools - placeholder interfaces for legal analysis tools.

PLACEHOLDER: Interface only. Do not implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTool(ABC):
    """Base interface for MCP tools."""

    name: str
    description: str

    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the tool with given parameters."""
        ...


class LegalSearchTool(BaseTool):
    name = "legal_search"
    description = "Search legal databases for statutes, case law, and regulations"


class DocumentAnalysisTool(BaseTool):
    name = "document_analysis"
    description = "Analyze legal documents for clauses, risks, and compliance"


class CitationLookupTool(BaseTool):
    name = "citation_lookup"
    description = "Look up and verify legal citations"


class ComplaintDraftTool(BaseTool):
    name = "complaint_draft"
    description = "Draft legal complaints based on user input"
