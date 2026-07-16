"""MCP (Model Context Protocol) Server - placeholder interface.

PLACEHOLDER: Interface only. Do not implement MCP logic.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class MCPServer(ABC):
    """MCP Server interface for tool orchestration."""

    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the MCP server and register tools/resources."""
        ...

    @abstractmethod
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle an incoming MCP request."""
        ...

    @abstractmethod
    async def list_tools(self) -> List[Dict[str, Any]]:
        """List all available MCP tools."""
        ...

    @abstractmethod
    async def list_resources(self) -> List[Dict[str, Any]]:
        """List all available MCP resources."""
        ...
