import pytest
from asyncclick.testing import CliRunner
from udc import QuiltWrapper, QuiltResource
from .conftest import PKG_URI

pytestmark = pytest.mark.anyio

@pytest.fixture
def anyio_backend():
    return 'trio'

runner = CliRunner()

async def test_wrapper():
    wrapper = QuiltWrapper(PKG_URI)
    assert wrapper


async def test_resource():
    qr = QuiltResource(PKG_URI)
    assert qr
