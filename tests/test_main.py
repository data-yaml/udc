import pytest
from asyncclick.testing import CliRunner

from udc import list

pytestmark = pytest.mark.anyio

@pytest.fixture
def anyio_backend():
    return 'trio'

runner = CliRunner()
TEST_URI = "quilt+s3://quilt-example"

async def test_list():
    result = await runner.invoke(list, [TEST_URI])
    print(result)
    assert result.exit_code == 0
    assert TEST_URI in result.stdout
