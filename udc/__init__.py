import yaml

from .main import __version__, app  # NOQA F401
from .types import Getable, Listable, Patchable, Putable  # NOQA F401

# Legacy vars for quiltplus
"""
SEP = "+"
K_HOST = "_hostname"
K_PROT = "_protocol"
K_QRY = "_query"
K_TOOL = "_tool"
K_URI = "_uri"
"""


def default_representer(dumper, data):
    # Alternatively, use repr() instead str():
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data))


yaml.representer.SafeRepresenter.add_representer(None, default_representer)  #
