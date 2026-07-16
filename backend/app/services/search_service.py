"""Search service - placeholder implementation."""

from typing import Dict, Any, List


class SearchService:
    """Handles global semantic search."""

    async def search(self, query: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Perform semantic search across all content. Placeholder."""
        raise NotImplementedError("Search service not yet implemented")
