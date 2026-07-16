"""Citation Agent - generates and verifies legal citations.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class CitationAgent(ABC):
    """Generates and verifies legal citations for responses."""

    @abstractmethod
    async def generate_citations(self, content: str, domain: str) -> List[Dict[str, Any]]:
        """Generate relevant legal citations for given content."""
        ...

    @abstractmethod
    async def verify_citation(self, citation: str) -> Dict[str, Any]:
        """Verify the accuracy of a legal citation."""
        ...
