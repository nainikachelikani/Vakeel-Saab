"""MCP Resources - placeholder interfaces.

PLACEHOLDER: Interface only. Do not implement.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseResource(ABC):
    """Base interface for MCP resources."""

    uri: str
    name: str
    description: str

    @abstractmethod
    async def read(self) -> Dict[str, Any]:
        """Read the resource content."""
        ...


class StatuteResource(BaseResource):
    uri = "statute://{jurisdiction}/{act}"
    name = "Legal Statute"
    description = "Access to legal statutes and acts"


class CaseLawResource(BaseResource):
    uri = "caselaw://{court}/{reference}"
    name = "Case Law"
    description = "Access to court judgments and case law"
