from .parse import QuiltParse

class QuiltResource:
    """Converts string URI to Quilt Resource."""

    def __init__(self, uri: str):
        self.uri = uri
        self.parsed = QuiltParse(uri)

    def __repr__(self):
        return f"QuiltResource(uri={self.uri})"
    
    def __str__(self):
        return self.uri
    
    def __eq__(self, other):
        return self.uri == other.uri
    