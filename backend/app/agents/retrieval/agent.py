"""Retrieval Agent - handles document retrieval using RAG.

PLACEHOLDER: Interface only. Do not implement AI/LLM/RAG logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class RetrievalAgent(ABC):
    """Retrieves relevant legal documents and passages using RAG pipeline."""

    @abstractmethod
    async def retrieve(self, query: str, top_k: int = 5, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Retrieve relevant documents for a query."""
        ...

    @abstractmethod
    async def retrieve_by_citation(self, citation: str) -> Optional[Dict[str, Any]]:
        """Retrieve a specific document by legal citation reference."""
        ...
