from .id import QuiltID
from typing_extensions import Self
from quilt3 import list_package_versions


class QuiltVersions:
    """Creates versions manager for a package."""

    def __init__(self, id: QuiltID):
        self.id = id
        self.registry = id.registry()
        self.pkg = id.pkg()

    def __repr__(self):
        return f"QuiltVersions({self.registry})"
    
    def __eq__(self, other: Self):
        return self.registry == other.registry

    async def list(self):
        """List versions in package."""
        return list(list_package_versions(self.pkg, self.registry))
