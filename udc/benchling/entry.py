from .root import BenchlingById, BenchlingRoot
from ..types import ResultList

class BenchlingEntryList(BenchlingById):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)

    def pages(self):
        return BenchlingRoot.CLIENT.entries.list_entries()


class BenchlingEntry(BenchlingRoot):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)

    def fetch(self):
        self.entry = BenchlingRoot.CLIENT.entries.get_entry_by_id(self.id)
        self.schema = self.entry.schema.id if self.entry.schema else None
        self.children = {
            "authors": [author.id for author in self.entry.authors],
            "custom_fields": [
                self.quote(key) for key in self.entry.custom_fields.additional_keys
            ],
            "days": [day.date for day in self.entry.days],
            "fields": [self.quote(key) for key in self.entry.fields.additional_keys],
        }

    def wrap(self, id, sub_type):
        item_dict = {"id": id, sub_type: id}
        item = type(f"wrap_{sub_type}", (object,), item_dict)
        return self.item_uri(item, sub_type)

    async def list(self, argv: dict = {})-> ResultList:
        self.fetch()
        kids = self.children
        return [self.wrap(id, sub_type) for sub_type in kids for id in kids[sub_type]]

    async def get(self, argv: dict = {}) -> ResultList:
        return ['N/A']

