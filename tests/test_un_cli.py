from .conftest import pytest
from udc import UnCli


@pytest.fixture
def config():
    return UnCli()


def test_un_cli(config: UnCli):
    assert config
    commands = config.get(UnCli.CMD)
    assert commands


def test_un_cli_commands(config: UnCli):
    cf_list = config.command('list')
    assert cf_list
    assert 'name' in cf_list
    assert cf_list['name'] == 'list'
