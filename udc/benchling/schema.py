from udc import UdcUri

from .root import BenchlingRoot


class BenchlingSchema(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)


class BenchlingSchemaList(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)

    def pages(self):
        return BenchlingRoot.CLIENT.schemas.list_entry_schemas()