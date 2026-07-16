"""Legal Analysis Agent - performs deep legal analysis.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class LegalAnalysisAgent(ABC):
    """Performs deep legal analysis on documents and queries."""

    @abstractmethod
    async def analyze_document(self, document_id: str) -> Dict[str, Any]:
        """Perform comprehensive legal analysis on a document."""
        ...

    @abstractmethod
    async def assess_risk(self, document_id: str) -> Dict[str, Any]:
        """Assess legal risk in a document."""
        ...

    @abstractmethod
    async def compare_documents(self, doc_a_id: str, doc_b_id: str) -> Dict[str, Any]:
        """Compare two legal documents."""
        ...

    @abstractmethod
    async def extract_clauses(self, document_id: str) -> List[Dict[str, Any]]:
        """Extract and categorize clauses from a document."""
        ...
