from .id import QuiltID
from typing_extensions import Self
from quilt3 import list_packages


class QuiltRegistry:
    """Creates registry object from QuiltID."""

    def __init__(self, id: QuiltID):
        self.id = id
        self.registry = id.registry()

    def __repr__(self):
        return f"QuiltRegistry({self.registry})"
    
    def __eq__(self, other: Self):
        return self.registry == other.registry

    async def list(self):
        """List packages in registry."""
        return list(list_packages(self.registry))
