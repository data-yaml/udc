from udc import UdcUri
from quiltplus import QuiltResource as Resource

def QuiltResource(uri: UdcUri):
    uri_string = str(uri)
    return Resource(uri_string)

