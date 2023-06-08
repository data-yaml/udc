from quiltplus import QuiltPackage, QuiltRegistry, QuiltResourceURI

from udc import Getable, Listable, Patchable, Putable
from udc.benchling import BenchlingEntry, BenchlingResourceURI, BenchlingRoot

from .conftest import pytestmark  # NOQA F401
from .conftest import BENCH_ENTRY, BENCH_URI, PKG_URI, REG_URI, pytest


async def test_res_types():
    pkg: QuiltPackage = QuiltResourceURI(PKG_URI)
    assert isinstance(pkg, QuiltPackage)
    assert isinstance(pkg, Listable)
    assert isinstance(pkg, Getable)
    assert isinstance(pkg, Putable)
    assert not isinstance(PKG_URI, Putable)


async def test_res_pkg():
    qpkg = QuiltResourceURI(PKG_URI)
    assert isinstance(qpkg, QuiltPackage)


async def test_res_reg():
    qreg = QuiltResourceURI(REG_URI)
    assert isinstance(qreg, QuiltRegistry)
    assert isinstance(qreg, Listable)
    assert not isinstance(qreg, Getable)


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_res_bench():
    bench = BenchlingResourceURI(BENCH_URI or "")
    assert isinstance(bench, BenchlingRoot)
    assert isinstance(bench, BenchlingEntry)
    assert isinstance(bench, Listable)
    assert isinstance(bench, Getable)
    assert isinstance(bench, Patchable)
    assert not isinstance(bench, Putable)
