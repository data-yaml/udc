import re

from udc.benchling import (RESOURCE_MAP, BenchlingEntry, BenchlingEntryList,
                             BenchlingRoot, BenchlingSchema,
                             BenchlingSchemaList, BenchlingSequence,
                             BenchlingSequenceList)
from udc import Listable, UnUri, K_URI

from .conftest import (BENCH_AUTHOR, BENCH_BASE, BENCH_ENTRY, BENCH_URI,
                       pytest, pytestmark)

TEST_URI = re.sub("&authors=.*", "", BENCH_URI).replace('entries.authors', 'entries')


@pytest.fixture
def attrs():
    uri = UnUri(TEST_URI)
    return uri.attrs

def attrs_type(type: str):
    uri = UnUri(BenchlingRoot.DEFAULT_URI)
    attrs = uri.attrs
    attrs["type"] = type
    attrs[K_URI] = attrs[K_URI].replace("type=entries", f"type={type}")
    return attrs

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_root(attrs: dict):
    root = BenchlingRoot(attrs)
    assert root
    assert root.type == "entries"
    assert root.id == BENCH_ENTRY
    assert root.pages() == []
    assert root.base_uri() == TEST_URI

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_root_uri(attrs: dict):
    root = BenchlingRoot(attrs)
    entry_dict = {"authors": BENCH_AUTHOR}
    entry = type("entries", (object,), entry_dict)
    result = root.item_uri(entry, "authors")
    assert result == f"{BENCH_BASE}#type=entries.authors&id={BENCH_ENTRY}&authors={BENCH_AUTHOR}"

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_pages(attrs: dict):
    plist = BenchlingEntryList(attrs).items()
    assert len(plist) > 1
    
    plist = BenchlingSchemaList(attrs).items()
    assert len(plist) > 0

    plist = BenchlingSequenceList(attrs).items()
    assert len(plist) > 1

async def check_list(klass, type: str):
    attrs = attrs_type(type)
    bench: Listable = klass(attrs)
    plist = await bench.list()
    assert len(plist) > 0
    uri = attrs.get(K_URI)
    print(plist[0])
    print(uri)
    assert plist[0].startswith(uri)
    
@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_list(attrs: dict):
    for type, klasses in RESOURCE_MAP.items():
        list_klass = klasses[0]
        await check_list(list_klass, type)

    result = await BenchlingEntryList(attrs).list()
    assert "id=etr" in result[0]

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_entry_fetch(attrs: dict):
    entry = BenchlingEntry(attrs)
    entry.fetch()
    assert entry.entry
    assert entry.schema
    assert entry.children

    authors = entry.children["authors"]
    assert len(authors) > 0
    author = authors[0]
    assert author == BENCH_AUTHOR
    item_uri = entry.wrap(author, "authors")
    assert BENCH_AUTHOR in item_uri
    assert "entries.authors" in item_uri

    fields = entry.children["fields"]
    assert len(fields) > 0
    field = fields[0]
    assert "Quilt+" in field



