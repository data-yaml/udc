from io import StringIO

from udc import app

from .conftest import pytestmark  # NOQA F401
from .conftest import pytest, PKG_URI, SKIP_LONG_TESTS, BENCH_TENANT, BENCH_URI

@pytest.fixture
def buf():
    result = StringIO()
    yield result
    result.close()

@pytest.mark.skipif(SKIP_LONG_TESTS, reason="Skip long tests")
async def test_app():
    assert app
    assert PKG_URI
    assert BENCH_TENANT
    assert BENCH_URI

async def test_app_quilt_list(buf: StringIO):
    await app(["list", PKG_URI], buf)
    result = buf.getvalue()
    print(result)
    assert result
    assert PKG_URI in result

@pytest.mark.skip("not yet implemented")
async def test_app_bench_list(buf: StringIO):
    await app(["list", BENCH_URI], buf)
    assert PKG_URI in buf.getvalue()
