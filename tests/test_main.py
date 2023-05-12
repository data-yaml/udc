from typer.testing import CliRunner
import pytest
pytestmark = pytest.mark.anyio


@pytest.fixture
def anyio_backend():
    return 'trio'

from udc import app

runner = CliRunner()
TEST_URI = "quilt+s3://quilt-example"

async def test_list():
    result = runner.invoke(app, [TEST_URI])
    assert result.exit_code == 0
    assert TEST_URI in result.stdout
