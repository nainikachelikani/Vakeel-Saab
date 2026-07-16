"""Router Agent - routes user queries to appropriate domain agents.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class RoutingDecision:
    """Result of routing a user query."""
    intent: str  # e.g., "Civil Dispute > Labor"
    domain: str  # e.g., "labor_law", "property_law", "criminal_law"
    confidence: float  # 0.0 - 1.0
    target_agent: str  # e.g., "domain_agent", "retrieval_agent"
    metadata: Optional[Dict[str, Any]] = None


class RouterAgent(ABC):
    """Routes incoming queries to the appropriate domain-specific agent.

    The router agent analyzes user intent and determines which
    specialized agent should handle the query.
    """

    @abstractmethod
    async def route(self, query: str, context: Optional[Dict[str, Any]] = None) -> RoutingDecision:
        """Analyze a user query and determine the appropriate agent to handle it.

        Args:
            query: The user's input message.
            context: Optional conversation context.

        Returns:
            RoutingDecision with the target agent and metadata.
        """
        ...

    @abstractmethod
    async def classify_intent(self, query: str) -> Dict[str, Any]:
        """Classify the intent of a user query.

        Args:
            query: The user's input message.

        Returns:
            Dict with intent classification results.
        """
        ...
