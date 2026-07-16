"""Planner Agent - creates multi-step execution plans.

PLACEHOLDER: Interface only. Do not implement AI/LLM logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class PlannerAgent(ABC):
    """Creates multi-step execution plans for complex legal tasks."""

    @abstractmethod
    async def create_plan(self, task: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create a multi-step execution plan."""
        ...

    @abstractmethod
    async def execute_step(self, step: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single step of the plan."""
        ...
