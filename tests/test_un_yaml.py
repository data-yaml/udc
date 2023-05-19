from .conftest import pytest
from udc import UnYaml, UnCli

@pytest.fixture
def un():
    return UnCli()


def test_un_load():
    yaml_data = UnYaml.load_yaml(UnCli.CLI_YAML, 'cli')
    assert yaml_data
    assert UnYaml.KEY in yaml_data
    un = UnYaml(yaml_data)
    assert un


def test_un_init(un: UnYaml):
    assert UnYaml.KEY in un.cfg
    assert isinstance(un, UnYaml)


def test_un_info(un: UnYaml):
    assert 'UnCli' == un.info('app')
    assert 'udc' == un.info('doc')


def test_un_expand(un: UnYaml):
    obj = {}
    assert obj == un.expand(obj)
    literal = {'key': 'value'}
    assert literal == un.expand(literal)
    ref = {UnYaml.REF: '#/variables/uri'}
    assert un.cfg['variables']['uri'] == un.expand(ref)


def test_un_get(un: UnYaml):
    assert un.get(UnYaml.KEY)
    assert not un.get('cmd/list')
    assert un.get('commands/list')
    assert un.get('commands/list/arguments')
    arg0 = un.get('commands/list/arguments/0')
    assert isinstance(arg0, dict)
    assert 'uri' == arg0.get('name')


def test_un_re_expand(un: UnYaml):
    getref = un.get('commands/get')
    assert 'help' in getref
    assert 'arguments' in getref
    args = getref['arguments']
    dir = args[0]
    assert 'name' in dir
    assert dir['format'] == 'path'
