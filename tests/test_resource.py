from asyncclick.testing import CliRunner

from udc import (Getable, Listable, Putable, QuiltPackage, QuiltResource,
                 QuiltRegistry)

from .conftest import PKG_URI, REG_URI, pytest, pytestmark


runner = CliRunner()


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


async def test_res_reg_list():
    qreg = QuiltResource(REG_URI)
    result = await qreg.list()
    assert len(result) > 0
