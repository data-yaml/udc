from .main import app  # NOQA F401
from .types import Getable, Listable, Putable  # NOQA F401
from .un.un_cli import UnCli  # NOQA F401
from .un.un_uri import UnUri  # NOQA F401
from .un.un_yaml import UnYaml  # NOQA F401

# Legacy vars for quiltplus
"""
SEP = "+"
K_HOST = "_hostname"
K_PROT = "_protocol"
K_QRY = "_query"
K_TOOL = "_tool"
K_URI = "_uri"
"""