import pytest
from asyncclick.testing import CliRunner
from udc import QuiltResource

pytestmark = pytest.mark.anyio

@pytest.fixture
def anyio_backend():
    return 'trio'

runner = CliRunner()
TEST_URI = "quilt+s3://quilt-example"

async def test_uri():
    pass