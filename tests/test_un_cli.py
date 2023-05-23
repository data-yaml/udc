from udc import UnCli

from .conftest import pytest


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
