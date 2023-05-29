from importlib.metadata import version
from io import StringIO

from udc import app

from .conftest import pytestmark  # NOQA F401
from .conftest import BENCH_TENANT, BENCH_URI, PKG_URI, pytest

__version__ = version("udc")


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


async def test_app_version(buf: StringIO):
    await app(["--version"], buf)
    assert f"udc {__version__}\n" == buf.getvalue()


async def test_app_vflag(buf: StringIO):
    await app(["-v"], buf)
    assert f"udc {__version__}\n" == buf.getvalue()


async def test_app_quilt_list(buf: StringIO):
    await app(["list", PKG_URI], buf)
    result = buf.getvalue()
    assert result
    assert PKG_URI in result


@pytest.mark.skipif(not BENCH_TENANT, reason="Benchling environment variables not set")
async def test_app_bench_list(buf: StringIO):
    await app(["list", BENCH_URI], buf)
    results = buf.getvalue().split("\n")
    assert BENCH_URI in results[0]
