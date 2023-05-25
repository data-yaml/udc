from io import StringIO

from udc import UnCli

from .conftest import pytestmark  # NOQA F401
from .conftest import BENCH_TENANT, BENCH_URI, PKG_URI, pytest


@pytest.fixture
def cli():
    return UnCli()

@pytest.fixture
def buf():
    result = StringIO()
    yield result
    result.close()

def test_un_cli(cli: UnCli):
    assert cli
    commands = cli.get(UnCli.CMD)
    assert commands


def test_un_cli_commands(cli: UnCli):
    cf_list = cli.cmd_opts("list")
    assert cf_list
    assert "name" in cf_list
    assert cf_list["name"] == "list"

async def test_un_cli_parser(cli: UnCli, buf: StringIO):
    parser = cli.make_parser()
    assert parser

@pytest.mark.skipif(not BENCH_TENANT, reason="Benchling environment variables not set")
def test_un_cli_get_resource(cli: UnCli):
    assert cli.get_resource(PKG_URI)
    assert cli.get_resource(BENCH_URI)
