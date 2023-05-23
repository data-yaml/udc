from udc import UnCli

from .conftest import pytest, PKG_URI, BENCH_URI


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

def test_un_cli_resource(config: UnCli):
    qres = config.get_resource(PKG_URI)
    # qbench = config.get_resource(BENCH_URI)
   
