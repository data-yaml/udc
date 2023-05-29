import importlib
import logging
import os
import re
from datetime import datetime
from pathlib import Path

import yaml

__version__ = importlib.metadata.version(__package__)


class UnConf:
    CATALOG_FILE = "CATALOG.webloc"
    CONFIG_FOLDER = ".quilt"
    CONFIG_YAML = "config.yaml"
    K_ACT = "action"
    K_DEP = "depend"
    K_NAM = "name"
    K_QC = "quiltconfig"
    K_REV = "revise"
    K_STG = "stage"
    K_URI = "uri"
    K_VER = "version"
    K_CAT = "view"
    REVISEME_FILE = "REVISEME.webloc"

    @staticmethod
    def AsShortcut(uri):
        return f"[InternetShortcut]\nURL={uri}"

    @staticmethod
    def AsWebloc(uri):
        return f'{{ URL = "{uri}"; }}'

    @staticmethod
    def BaseConfig():
        return {UnConf.K_VER: __version__}

    @staticmethod
    def ForRoot(root: Path):
        return UnConf(str(root / UnConf.CONFIG_FOLDER))

    @staticmethod
    def Now():
        return datetime.now().astimezone().replace(microsecond=0).isoformat()

    def __init__(self, config_location: str):
        # determine if folder or file, then set both
        loc = Path(config_location)
        is_file = loc.is_file() if loc.exists() else re.match(r"y?ml", loc.suffix)
        self.file = loc if is_file else loc / UnConf.CONFIG_YAML
        self.path = loc.parents[0] if is_file else loc
        self.path.mkdir(parents=True, exist_ok=True)

    def __repr__(self):
        return f"UnConf['{self.path}')"

    def __str__(self):
        return self.__repr__()

    def list_config(self):
        return [
            os.path.relpath(os.path.join(dir, file), self.path)
            for (dir, dirs, files) in os.walk(self.path)
            for file in files
        ]

    def get_config(self):
        if not self.file.exists():
            return UnConf.BaseConfig()

        cfg_yaml = self.file.read_text()
        logging.debug(f"UnConf.GetURI.cfg_yaml: {cfg_yaml}")
        cfg = yaml.safe_load(cfg_yaml)
        logging.debug(f"UnConf.GetURI.cfg: {cfg}")
        config = cfg.get(UnConf.K_QC)
        if not config:
            logging.error(f"{self.file}: needs yaml key '{UnConf.K_QC}'")
            return {}
        return config

    def write_file(self, file: str, text: str):
        p = self.path / file
        p.write_text(text)
        return p

    def update_config(self, options: dict, reset_stage: bool = False):
        config = self.get_config()
        for key in [UnConf.K_URI, UnConf.K_CAT, UnConf.K_REV]:
            if key in options:
                config[key] = options[key]

        if UnConf.K_DEP in options:
            depend = options[UnConf.K_DEP]
            deps = self.get_depend()
            if depend[0] == "+":
                deps.add(depend[1:])
            else:
                deps.remove(depend[1:])
            config[UnConf.K_DEP] = list(deps)

        if UnConf.K_STG in options:
            stage = options[UnConf.K_STG]
            stg = self.get_stage()
            name = stage[UnConf.K_NAM]
            stg[name] = stage
            config[UnConf.K_STG] = stg
        elif reset_stage:
            config[UnConf.K_STG] = {}

        self.save_config(config)
        return config

    def save_config(self, config):
        root = {UnConf.K_QC: config}
        yaml_str = yaml.safe_dump(root)
        self.file.write_text(yaml_str)

    def save_webloc(self, file: str, uri: str):
        shortcut_file = file.replace("webloc", "URL")
        path = self.write_file(shortcut_file, UnConf.AsShortcut(uri))
        path = self.write_file(file, UnConf.AsWebloc(uri))
        return path

    def save_uri(self, id):
        pkg_uri = id.quilt_uri()
        cat_uri = id.catalog_uri()
        rev_uri = f"{cat_uri}?action=revisePackage"
        self.save_webloc(UnConf.CATALOG_FILE, cat_uri)
        self.save_webloc(UnConf.REVISEME_FILE, rev_uri)
        options = {
            UnConf.K_URI: pkg_uri,
            UnConf.K_CAT: cat_uri,
            UnConf.K_REV: rev_uri,
        }
        self.update_config(options)
        return [
            UnConf.CATALOG_FILE,
            UnConf.REVISEME_FILE,
            UnConf.CONFIG_YAML,
        ]

    def get_uri(self, key=None):
        if not key:
            key = UnConf.K_URI
        return self.get_config().get(key)

    def get_stage(self, adds=None):
        stg = self.get_config().get(UnConf.K_STG, {})
        print(f"get_stage.stg: {stg}")
        if adds:
            return {k: v for (k, v) in stg.items() if v[UnConf.K_ACT] == "add"}
        elif adds is False:
            return {k: v for (k, v) in stg.items() if v[UnConf.K_ACT] != "add"}
        return stg

    def stage(self, file: str, is_add: bool = True):
        p = Path(file)
        if not p.exists():
            logging.error(f"MISSING_FILE: cannot stage file '{p}' that does not exist")
            return None
        stats = p.stat()
        attrs = {
            UnConf.K_NAM: file,
            UnConf.K_ACT: "add" if is_add else "remove",
            "size": stats.st_size,
            "created": stats.st_ctime,
            "updated": stats.st_mtime,
            "accessed": stats.st_atime,
        }
        self.update_config({UnConf.K_STG: attrs})
        return attrs

    def get_depend(self):
        deps = self.get_config().get(UnConf.K_DEP, [])
        return set(deps)

    def depend(self, uri: str, is_add: bool = True):
        key = f"+{uri}" if is_add else f"-{uri}"
        return self.update_config({UnConf.K_DEP: key})
