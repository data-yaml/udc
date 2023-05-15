from typing import Protocol

class Listable(Protocol):    
    async def list(self):
        """List contents of URI."""
        return []
    

class Getable(Listable):
    async def get(self, path: str):
        """Get contents of URI into path"""
        return None
    

class Putable(Getable):
    async def put(self, path: str):
        """Put contents of path into URI."""
        return None
