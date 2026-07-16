"""Vector Store - placeholder interface.

PLACEHOLDER: Interface only. Do not implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class VectorStore(ABC):
    """Interface for vector storage and similarity search."""

    @abstractmethod
    async def upsert(self, documents: List[Dict[str, Any]]) -> None:
        """Insert or update documents in the vector store."""
        ...

    @abstractmethod
    async def search(self, query_embedding: List[float], top_k: int = 5, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Search for similar documents."""
        ...

    @abstractmethod
    async def delete(self, document_ids: List[str]) -> None:
        """Delete documents from the vector store."""
        ...
