import os

from benchling_sdk.auth.api_key_auth import ApiKeyAuth
from benchling_sdk.benchling import Benchling
from udc import UdcUri

BENCH_ID = "id"
BENCH_TYPE = "type"
BENCH_TYPE_DEFAULT = "entry"


class BenchlingRoot:
    BENCH_TENANT = os.environ.get("BENCHLING_TENANT_DNS")
    BENCH_ENTRY = os.environ.get("BENCHLING_ENTRY_ID")
    BENCH_AUTHOR = os.environ.get("BENCHLING_AUTHOR_ID")
    BENCH_KEY = os.environ.get("BENCHLING_API_KEY")
    CLIENT = Benchling(url=f"https://{BENCH_TENANT}", auth_method=ApiKeyAuth(BENCH_KEY))

    def __init__(self, uri: UdcUri):
        self.uri = uri
        self.type = uri.get(BENCH_TYPE) or BENCH_TYPE_DEFAULT
        self.id = uri.get(BENCH_ID)

    def __repr__(self):
        return f"<{self.__class__}({self.uri})>"

    def pages(self):
        return []

    def base_uri(self):
        base = f"benchling+https://{BenchlingRoot.BENCH_TENANT}#type={self.type}"
        base += f"&id={self.id}" if hasattr(self, "id") else ""
        return base

    def entry_uri(self, entry):
        base = self.base_uri()
        base += f"&id={entry.id}" if hasattr(entry, "id") else ""
        base += f"&name={entry.name}" if hasattr(entry, "name") else ""
        base += f"&author={entry.author}" if hasattr(entry, "author") else ""
        return base

    async def list(self) -> list:
        return [self.entry_uri(entry) for page in self.pages() for entry in page]
