from udc import UnCli

from .conftest import BENCH_URI, PKG_URI, pytest


@pytest.fixture
def config():
    return UnCli()


def test_un_cli(config: UnCli):
    assert config
    commands = config.get(UnCli.CMD)
    assert commands


def test_un_cli_commands(config: UnCli):
    cf_list = config.cmd_opts("list")
    assert cf_list
    assert "name" in cf_list
    assert cf_list["name"] == "list"


def test_un_get_resource(config: UnCli):
    assert config.get_resource(PKG_URI)
    assert config.get_resource(BENCH_URI)
