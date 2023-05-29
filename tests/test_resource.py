from quiltplus import QuiltPackage, QuiltRegistry, QuiltResource
from udc import Getable, Listable, Putable

from .conftest import pytestmark  # NOQA F401
from .conftest import BENCH_ENTRY, PKG_URI, REG_URI, pytest


async def test_res_types():
    pkg: QuiltPackage = QuiltPackage.FromURI(PKG_URI)
    assert isinstance(pkg, QuiltPackage)
    assert isinstance(pkg, Listable)
    assert isinstance(pkg, Getable)
    assert isinstance(pkg, Putable)
    assert not isinstance(PKG_URI, Putable)


async def test_res_pkg():
    qpkg = QuiltResource(PKG_URI)
    assert isinstance(qpkg, QuiltPackage)


async def test_res_reg():
    qreg = QuiltResource(REG_URI)
    assert isinstance(qreg, QuiltRegistry)
    assert isinstance(qreg, Listable)
    assert not isinstance(qreg, Getable)


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_res_bench():
    pass
