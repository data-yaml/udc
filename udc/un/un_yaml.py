from importlib import import_module, resources
from typing import Any, Callable

from yaml import safe_load


class UnYaml:
    KEY = "_yaml"
    SEP = "/"
    PREFIX = "#/"
    REF = "$ref"
    REF_ERROR = f"Value for Key {REF} does not start with {PREFIX}"

    @staticmethod
    def load_yaml(filename: str, pkg: str, sub: str = "") -> dict:
        yaml_dir = resources.files(pkg)
        if len(sub) > 0:
            yaml_dir = yaml_dir / sub
        yaml_file = yaml_dir / filename
        yaml_string = yaml_file.read_text()
        yaml_data = safe_load(yaml_string)
        return yaml_data

    def __init__(self, yaml_data: dict) -> None:
        self.cfg = yaml_data
        self._info = self.cfg[UnYaml.KEY]

    def info(self, key: str) -> Any:
        return self._info.get(key)

    def expand(self, item):
        if isinstance(item, dict):
            if UnYaml.REF in item:
                return self._expand(item)
            return {k: self.expand(v) for (k, v) in item.items()}
        if isinstance(item, list):
            return [self.expand(v) for v in item]
        return item

    def _expand(self, item):
        ref = item[UnYaml.REF]
        if not ref.startswith(UnYaml.PREFIX):
            raise ValueError(f"cannot expand {ref}: {UnYaml.REF_ERROR}")
        value = self.get(ref[2:])
        for key in item:
            if key != UnYaml.REF:
                value[key] = item[key]
        return self.expand(value)

    def _get(self, result, key: str):
        if not result:
            return False
        if isinstance(result, list):
            return result[int(key)]
        return result.get(key)

    def get(self, keys: str) -> Any:
        result = self.cfg
        for key in keys.split(UnYaml.SEP):
            item = self._get(result, key)
            result = self.expand(item)

        return result

    def get_handler(self, key: str) -> Callable:
        handlers = self.info("handlers")
        handler = handlers.get(key)
        if not handler:
            raise ValueError(f"UnYaml.get_handler: no handler for {key}")

        module = import_module(handler["module"])
        return getattr(module, handler["method"])
