from quiltplus import QuiltResource as Resource
from udc import UdcUri


def QuiltResource(uri: UdcUri):
    uri_string = str(uri)
    return Resource(uri_string)
