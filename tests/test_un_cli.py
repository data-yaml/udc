from .conftest import pytest
from udc import UnCli


@pytest.fixture
def cli():
    return UnCli()


def test_un_cli(cli: UnCli):
    assert cli
