"""Domain Agent - handles domain-specific legal reasoning.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class DomainAgent(ABC):
    """Processes queries within a specific legal domain (e.g., labor law, property law)."""

    @abstractmethod
    async def process(self, query: str, domain: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Process a query within a specific legal domain."""
        ...

    @abstractmethod
    async def get_applicable_statutes(self, domain: str, query: str) -> List[Dict[str, Any]]:
        """Retrieve applicable statutes for a given domain and query."""
        ...

    @abstractmethod
    async def generate_action_plan(self, query: str, domain: str) -> List[str]:
        """Generate an actionable plan for the user's legal situation."""
        ...
