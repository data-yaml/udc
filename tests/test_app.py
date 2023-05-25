from importlib.metadata import version
from io import StringIO

from udc import app

from .conftest import pytestmark  # NOQA F401
from .conftest import BENCH_TENANT, BENCH_URI, PKG_URI, pytest


@pytest.fixture
def buf():
    result = StringIO()
    yield result
    result.close()


@pytest.mark.skipif(not BENCH_TENANT, reason="Benchling environment variables not set")
async def test_app():
    assert app
    assert PKG_URI
    assert BENCH_TENANT
    assert BENCH_URI

@pytest.mark.skip("not yet implemented")
async def test_app_version(buf: StringIO):
    __version__ = version('udc')
    await app(["--version"], buf)
    assert __version__ in buf.getvalue()
    assert '0.2.0' in buf.getvalue()

async def test_app_quilt_list(buf: StringIO):
    await app(["list", PKG_URI], buf)
    result = buf.getvalue()
    assert result
    assert PKG_URI in result

@pytest.mark.skipif(not BENCH_TENANT, reason="Benchling environment variables not set")
async def test_app_bench_list(buf: StringIO):
    await app(["list", BENCH_URI], buf)
    results = buf.getvalue().split('\n')
    assert BENCH_URI in results[0]
