from typing import Protocol, runtime_checkable

ResultList = list[str]


@runtime_checkable
class Listable(Protocol):
    async def list(self, argv: dict = {}) -> ResultList:
        """List contents of URI."""
        return []


@runtime_checkable
class Getable(Protocol):
    async def get(self, argv: dict = {}) -> ResultList:
        """Get contents of URI into path"""
        return []


@runtime_checkable
class Patchable(Protocol):
    async def patch(self, argv: dict = {}) -> ResultList:
        """Patch (merge/update) contents of path into URI."""
        return []


@runtime_checkable
class Putable(Protocol):
    async def put(self, argv: dict = {}) -> ResultList:
        """Put (replace) contents of path into URI."""
        return []
