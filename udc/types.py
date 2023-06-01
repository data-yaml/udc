from typing import Protocol, runtime_checkable


@runtime_checkable
class Listable(Protocol):
    async def list(self, argv: dict = {}):
        """List contents of URI."""
        return []


@runtime_checkable
class Getable(Protocol):
    async def get(self, argv: dict = {}):
        """Get contents of URI into path"""
        return None


@runtime_checkable
class Putable(Protocol):
    async def put(self, argv: dict = {}):
        """Put contents of path into URI."""
        return None
