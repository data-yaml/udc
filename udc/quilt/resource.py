from quiltplus import QuiltResource as Resource


def QuiltResource(attrs: dict[str, str]):
    uri = attrs.get("_uri")
    return Resource(uri)
