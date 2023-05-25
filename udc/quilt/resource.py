from quiltplus import QuiltResource as Resource


def QuiltResource(attrs: dict):
    uri = attrs.get("_uri")
    return Resource(uri)
