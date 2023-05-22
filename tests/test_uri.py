from udc import UdcUri

from .conftest import pytestmark  # NOQA F401
from .conftest import pytest, PKG_URI


async def test_uri():
    uri = UdcUri(PKG_URI)
    assert uri
    assert "quilt" == uri.tool()
    assert "s3" == uri.get("_protocol")
    assert "s3://quilt-example" == uri.endpoint()