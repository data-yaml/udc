from udc import UdcUri

from .root import BenchlingRoot


class BenchlingEntry(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)


class BenchlingEntryList(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)

    def pages(self):
        return BenchlingRoot.CLIENT.entries.list_entries()