from udc import UnUri

from .conftest import pytestmark  # NOQA F401
from .conftest import PKG_URI


async def test_uri():
    uri = UnUri(PKG_URI)
    assert uri
    assert "quilt" == uri.tool()
    assert "s3" == uri.get("_protocol")
    assert "s3://quilt-example" == uri.endpoint()
