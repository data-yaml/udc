import importlib.resources as pkg
from yaml import safe_load
class UnYaml:

    @staticmethod
    def load_yaml(filename: str):
        yaml_file = pkg.files('udc') / 'un' / filename
        yaml_string = yaml_file.read_text()
        yaml_data = safe_load(yaml_string)
        return yaml_data

