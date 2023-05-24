import os
import logging

from benchling_sdk.auth.api_key_auth import ApiKeyAuth
from benchling_sdk.benchling import Benchling
from udc import UdcUri

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

    def __init__(self, uri: UdcUri):
        self.uri = uri
        self.type = uri.get(BENCH_TYPE) or BENCH_TYPE_DEFAULT
        self.id = uri.get(BENCH_ID)

    def __repr__(self) -> str:
        return f"<{self.__class__}({self.uri})>"

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
        logging.debug(f'item_uri.base: {base}')
        if hasattr(item, 'id'):
            if "&id=" not in base:
                base += f"&id={item.id}"
        if sub_type and hasattr(item, sub_type):
            base += f"&{sub_type}={getattr(item, sub_type)}"
        logging.debug(f'item_uri.uri: {base}')
        return base

    async def list(self) -> list[str]:
        return [self.item_uri(item) for item in self.items()]

class BenchlingById(BenchlingRoot):

    @classmethod
    def ForType(cls, type: str, id: str):
        uri = f"benchling+https://{BenchlingRoot.BENCH_TENANT}#type={type}&id={id}"
        udc = UdcUri(uri)
        return cls(udc)
    

    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)
        self.id = uri.get(BENCH_ID)
