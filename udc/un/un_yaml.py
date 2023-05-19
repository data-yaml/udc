import importlib.resources as pkg
from yaml import safe_load
class UnYaml:

    KEY = '_yaml'
    SEP = '.'

    @staticmethod
    def load_yaml(filename: str):
        yaml_file = pkg.files('udc') / 'un' / filename
        yaml_string = yaml_file.read_text()
        yaml_data = safe_load(yaml_string)
        return yaml_data

    def __init__(self, file) -> None:
        self.cfg = UnYaml.load_yaml(file)
        self._info = self.cfg[UnYaml.KEY]
        
    def info(self, key: str) -> str:
        return self._info.get(key)
    
    def expand(self, item):
        return item
    
    def _get(self, result, key: str):
        if not result:
            return False
        if isinstance(result, list):
            return result[int(key)]
        return result.get(key)

    def get(self, keys: str) -> object:
        result = self.cfg
        for key in keys.split(UnYaml.SEP):
            item = self._get(result, key)
            result = self.expand(item)

        return result
