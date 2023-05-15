from .id import QuiltID
from .package import QuiltPackage

def QuiltResource(uri: str):
    id = QuiltID(uri)
    return QuiltPackage(id) if id.has_package else None
