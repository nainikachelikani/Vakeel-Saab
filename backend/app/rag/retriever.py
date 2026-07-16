"""Retriever - placeholder interface for RAG retrieval.

PLACEHOLDER: Interface only. Do not implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class Retriever(ABC):
    """Interface for RAG document retrieval."""

    @abstractmethod
    async def retrieve(self, query: str, top_k: int = 5, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Retrieve relevant documents for a query."""
        ...

    @abstractmethod
    async def rerank(self, query: str, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rerank retrieved documents for relevance."""
        ...
