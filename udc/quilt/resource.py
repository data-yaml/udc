from quiltplus import QuiltResource as Resource


def QuiltResource(attrs: dict):
    resource = None
    try:
        resource = Resource(attrs)
    except Exception as e:
        pass
    if resource:
        return resource
    uri = attrs.get("_uri")
    return Resource(uri)
