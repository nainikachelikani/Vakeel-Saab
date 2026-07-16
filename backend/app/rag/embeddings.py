"""Embeddings - placeholder interface for text embeddings.

PLACEHOLDER: Interface only. Do not implement.
"""

from abc import ABC, abstractmethod
from typing import List


class EmbeddingProvider(ABC):
    """Interface for generating text embeddings."""

    @abstractmethod
    async def embed_text(self, text: str) -> List[float]:
        """Generate embedding for a single text."""
        ...

    @abstractmethod
    async def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a batch of texts."""
        ...

    @abstractmethod
    def get_dimension(self) -> int:
        """Return the embedding dimension."""
        ...
