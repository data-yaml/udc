from udc import UdcUri

from .root import BenchlingRoot, BenchlingById

class BenchlingEntryList(BenchlingById):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)

    def pages(self):
        return BenchlingRoot.CLIENT.entries.list_entries()
    
class BenchlingEntry(BenchlingRoot):

    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)

    def fetch(self):
        self.entry = BenchlingRoot.CLIENT.entries.get_entry_by_id(self.id)
        self.schema = self.entry.schema.id
        self.children = {
            "authors": [author.id for author in self.entry.authors],
            "custom_fields": [key for key in self.entry.custom_fields.additional_keys],
            "days": [day.date for day in self.entry.days],
            "fields": [key for key in self.entry.custom_fields.additional_keys],
        }

    def wrap(self, id, sub_type):
        item_dict = {'id': id, sub_type: id}
        item = type(f"wrap_{sub_type}", (object,), item_dict)
        return self.item_uri(item, sub_type)

    async def list(self) -> list[str]:
        self.fetch()
        kids = self.children
        return [self.wrap(id, sub_type) for sub_type in kids for id in kids[sub_type]]           
