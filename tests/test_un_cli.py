from io import StringIO
from pathlib import Path

from udc import UnCli, UnUri

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
    assert "list" in commands


def test_un_cli_eval():
    assert eval("str") == str
    assert eval("Path") == Path
    assert eval("UnUri") == UnUri


def test_un_cli_arg():
    d = {"type": "Path"}
    kw = UnCli.ARG_KWS(d)
    assert kw


async def test_un_cli_parser(cli: UnCli, buf: StringIO):
    argv = ["--version"]
    parser = cli.make_parser()
    assert parser
    assert cli.parse(argv)
    await cli.run(argv, buf)
    assert "udc" in buf.getvalue()


def test_un_cli_get_quilt(cli: UnCli):
    uri = UnUri(PKG_URI)
    assert cli.get_resource(uri)


@pytest.mark.skipif(not BENCH_TENANT, reason="Benchling environment variables not set")
def test_un_cli_get_benchling(cli: UnCli):
    uri = UnUri(BENCH_URI)
    assert cli.get_resource(uri)
