import logging
import urllib.parse
from json import dump, loads
from pathlib import Path

from benchling_api_client.v2.stable.models.entry_day import EntryDay
from benchling_api_client.v2.stable.models.user_summary import UserSummary
from benchling_sdk.models import Entry, EntryUpdate

# , EntrySchemaDetailed, Fields, CustomFields
from un_yaml import UnUri

from ..types import ResultList
from .root import BenchlingById, BenchlingRoot


class BenchlingEntryList(BenchlingById):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)

    def pages(self):
        return BenchlingRoot.CLIENT.entries.list_entries()


class BenchlingEntry(BenchlingRoot):
    @staticmethod
    def DIR_ARG(argv: dict) -> Path:
        return argv.get("path") or Path(".")

    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)

    def fetch(self):
        self.entry: Entry = BenchlingRoot.CLIENT.entries.get_entry_by_id(self.id)
        self.last_day: EntryDay | None = (
            self.entry.days[-1] if self.entry.days else None
        )
        self.author: UserSummary | None = (
            self.entry.authors[0] if self.entry.authors else None
        )
        self.schema_id = self.entry.schema.id if self.entry.schema else None
        self.children = {
            "authors": [author.id for author in self.entry.authors],
            "custom_fields": [
                self.quote(key) for key in self.entry.custom_fields.additional_keys
            ],
            "days": [day.date for day in self.entry.days],
            "fields": [self.quote(key) for key in self.entry.fields.additional_keys],
        }

    def push(self, id, changes: dict) -> Entry:
        for key, value in changes.items():
            if isinstance(value, list): # non-parsed
                result = value[0]
                print(f"result: {result}")
                changes[key] = loads(result) if result[0] == '{' else result
        print(f"changes: {changes}")
        update = EntryUpdate.from_dict(changes)
        print(f"update: {update}")
        return BenchlingRoot.CLIENT.entries.update_entry(entry_id=id, entry=update)

    def wrap(self, id, sub_type):
        item_dict = {"id": id, sub_type: id}
        item = type(f"wrap_{sub_type}", (object,), item_dict)
        return self.item_uri(item, sub_type)

    async def list(self, argv: dict = {}) -> ResultList:
        self.fetch()
        kids = self.children
        return [self.wrap(id, sub_type) for sub_type in kids for id in kids[sub_type]]

    async def get(self, argv: dict = {}) -> ResultList:
        self.fetch()
        dir_path = BenchlingEntry.DIR_ARG(argv)
        filename = f"{self.entry.id}.json"
        file_path = dir_path / filename
        with file_path.open("w", encoding="utf-8") as json_file:
            dump(self.entry.to_dict(), json_file, indent=4, sort_keys=True)

        return [str(file_path)]

    async def patch(self, argv: dict = {}) -> ResultList:
        query = self.attrs.get(UnUri.K_QRY) or argv.get(UnUri.K_QRY)
        if not query:
            logging.error(f"patch: no query string found in {self.uri}")

        try:
            if not isinstance(query, dict):
                query = urllib.parse.parse_qs(query)
            result = self.push(self.id, query)
            print(f"patched {result.web_url}\n{query}")
        except Exception as ex:
            logging.error(f"patch query not valid for EntryUpdate: {query}\n{ex}")
            return []
        return [self.base_uri()]
