import pytest
from asyncclick.testing import CliRunner
from udc import QuiltWrapper

pytestmark = pytest.mark.anyio

@pytest.fixture
def anyio_backend():
    return 'trio'

runner = CliRunner()
REG_URI = "quilt+s3://quilt-example"
PKG_URI = "quilt+s3://quilt-example#package=example/iris"

async def test_uri():
    wrapper = QuiltWrapper(REG_URI)
    assert wrapper
