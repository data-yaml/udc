from .id import QuiltID
from .package import QuiltPackage
from .parse import K_BKT, K_PKG, K_PTH


def QuiltResource(uri: str):
    id = QuiltID(uri)
    t = id.type()
    if t == K_PKG:
        return QuiltPackage(id)
    elif t == K_PTH:
        return QuiltPackage(id)
    elif t == K_BKT:
        return QuiltPackage(id)
    else:
        raise ValueError(f"Unknown resource type: {t}")
