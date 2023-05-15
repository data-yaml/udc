from asyncclick.testing import CliRunner

from udc import cli, list

from .conftest import pytestmark  # NOQA F401
from .conftest import PKG_URI, SKIP_LONG_TESTS, pytest

runner = CliRunner()


@pytest.mark.skipif(SKIP_LONG_TESTS, reason="Skip long tests")
async def test_list():
    result = await runner.invoke(list, [PKG_URI])
    print(result)
    assert result.exit_code == 0
    assert PKG_URI in result.stdout


@pytest.mark.skipif(SKIP_LONG_TESTS, reason="Skip long tests")
async def test_sub_list():
    result = await runner.invoke(cli, ["list", PKG_URI])
    print(result)
    assert result.exit_code == 0
    assert PKG_URI in result.stdout
