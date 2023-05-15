from .parse import QuiltParse


class QuiltWrapper:
    """Converts string URI to Quilt Resource."""

    def __init__(self, uri: str):
        self.uri = uri
        self.parsed = QuiltParse(uri)

    def __repr__(self):
        return f"QuiltWrapper(uri={self.uri})"

    def __str__(self):
        return self.uri

    def __eq__(self, other):
        return self.uri == other.uri

    async def list(self):
        """List contents of URI."""
        return []

    async def get(self, path: str):
        """Get contents of URI into path"""
        return self.parsed.get(path)

    async def put(self, path: str):
        """Put contents of path into URI."""
        return self.parsed.put(path)
