import importlib.resources as pkg
from yaml import safe_load
class UnYaml:

    KEY = '_yaml'

    @staticmethod
    def load_yaml(filename: str):
        yaml_file = pkg.files('udc') / 'un' / filename
        yaml_string = yaml_file.read_text()
        yaml_data = safe_load(yaml_string)
        return yaml_data

    def __init__(self, file) -> None:
        self.cfg = UnYaml.load_yaml(file)
        self._info = self.cfg[UnYaml.KEY]
        
    def info(self, key: str):
        return self._info.get(key)
