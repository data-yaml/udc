from io import StringIO

from udc import app

from .conftest import pytestmark  # NOQA F401
from .conftest import PKG_URI


# @pytest.mark.skipif(SKIP_LONG_TESTS, reason="Skip long tests")
async def test_app():
    result = StringIO()
    await app(["list", PKG_URI], result)
    assert PKG_URI in result.getvalue()
    result.close()
