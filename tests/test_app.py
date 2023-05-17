from udc import app
from io import StringIO

from .conftest import pytestmark  # NOQA F401
from .conftest import PKG_URI, SKIP_LONG_TESTS, pytest


# @pytest.mark.skipif(SKIP_LONG_TESTS, reason="Skip long tests")
async def test_app():
    result = StringIO()
    await app(["list", PKG_URI], result)
    assert PKG_URI in result.getvalue()
    result.close()

