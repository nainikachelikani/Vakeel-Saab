"""Reviewer Agent - validates and reviews AI outputs.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class ReviewerAgent(ABC):
    """Reviews and validates outputs from other agents."""

    @abstractmethod
    async def review(self, output: Dict[str, Any], criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Review an agent's output against quality criteria."""
        ...

    @abstractmethod
    async def validate_legal_accuracy(self, content: str) -> Dict[str, Any]:
        """Validate the legal accuracy of generated content."""
        ...
