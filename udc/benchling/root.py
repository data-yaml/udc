import logging
import os
import urllib.parse

from benchling_sdk.auth.api_key_auth import ApiKeyAuth
from benchling_sdk.benchling import Benchling

BENCH_ID = "id"
BENCH_TYPE = "type"
BENCH_TYPE_DEFAULT = "entries"


class BenchlingRoot:
    BENCH_TENANT = os.environ.get("BENCHLING_TENANT_DNS")
    BENCH_ENTRY = os.environ.get("BENCHLING_ENTRY_ID")
    BENCH_AUTHOR = os.environ.get("BENCHLING_AUTHOR_ID")
    BENCH_KEY = os.environ.get("BENCHLING_API_KEY")
    CLIENT = Benchling(url=f"https://{BENCH_TENANT}", auth_method=ApiKeyAuth(BENCH_KEY))
    DEFAULT_URI = f"benchling+https://{BENCH_TENANT}#type=entries"

    def __init__(self, attrs: dict):
        self.attrs = attrs
        self.uri = attrs.get("_uri")
        self.id = attrs.get(BENCH_ID)
        self.set_type(attrs.get(BENCH_TYPE))

    def __repr__(self) -> str:
        return f"<{self.__class__}({self.uri})>"

    def set_type(self, btype: str):
        type = btype or BENCH_TYPE_DEFAULT
        types = type.split(".")
        self.type = types[0]
        self.sub_type = types[1] if len(types) > 1 else None

    def quote(self, value: str) -> str:
        return urllib.parse.quote_plus(value)

    def pages(self) -> list:
        return []

    def items(self) -> list:
        return [item for page in self.pages() for item in page]

    def base_uri(self, sub_type=None) -> str:
        type = f"{self.type}.{sub_type}" if sub_type else self.type
        base = f"benchling+https://{BenchlingRoot.BENCH_TENANT}#type={type}"
        base += f"&id={self.id}" if self.id else ""
        return base

    def item_uri(self, item, sub_type=None) -> str:
        base = self.base_uri(sub_type)
        logging.debug(f"item_uri.base: {base}")
        if hasattr(item, "id"):
            if "&id=" not in base:
                base += f"&id={item.id}"
        if sub_type and hasattr(item, sub_type):
            base += f"&{sub_type}={getattr(item, sub_type)}"
        logging.debug(f"item_uri.uri: {base}")
        return base

    async def list(self, argv: dict = {}) -> list[str]:
        return [self.item_uri(item) for item in self.items()]


class BenchlingById(BenchlingRoot):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)
        self.id = attrs.get(BENCH_ID)
