from asyncclick.testing import CliRunner

from udc import (Getable, Listable, Putable, QuiltPackage, QuiltResource,
                 QuiltWrapper)

from .conftest import PKG_URI, pytest, pytestmark


@pytest.fixture
def anyio_backend():
    return "trio"


runner = CliRunner()


async def test_wrapper():
    wrapper = QuiltWrapper(PKG_URI)
    assert wrapper


async def test_resource():
    qr = QuiltResource(PKG_URI)
    assert qr


async def test_types():
    pkg: QuiltPackage = QuiltPackage.FromURI(PKG_URI)
    assert isinstance(pkg, QuiltPackage)
    assert isinstance(pkg, Listable)
    assert isinstance(pkg, Getable)
    assert isinstance(pkg, Putable)
    assert not isinstance(PKG_URI, Putable)
