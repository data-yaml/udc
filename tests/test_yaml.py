from udc import UnYaml


def test_yaml():
    assert UnYaml
    return


def test_yaml_load():
    yaml_data = UnYaml.load_yaml('cli.yaml')
    assert yaml_data
    assert '_yaml' in yaml_data
