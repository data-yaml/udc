from .root import BenchlingRoot


class BenchlingSchema(BenchlingRoot):
    def __init__(self, attrs: dict[str, str]) -> None:
        super().__init__(attrs)


class BenchlingSchemaList(BenchlingRoot):
    def __init__(self, attrs: dict[str, str]) -> None:
        super().__init__(attrs)

    def pages(self):
        return BenchlingRoot.CLIENT.schemas.list_entry_schemas()