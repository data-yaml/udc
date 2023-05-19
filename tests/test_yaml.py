from .conftest import pytest, CLI_YAML
from udc import UnYaml

@pytest.fixture
def un():
    return UnYaml(CLI_YAML)


def test_yaml():
    assert UnYaml
    return


def test_yaml_load():
    yaml_data = UnYaml.load_yaml(CLI_YAML)
    assert yaml_data
    assert UnYaml.KEY in yaml_data


def test_yaml_init(un: UnYaml):
    assert UnYaml.KEY in un.cfg
    assert isinstance(un, UnYaml)


def test_yaml_info(un: UnYaml):
    assert 'UnCli' == un.info('app')
