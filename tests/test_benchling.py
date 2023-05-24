import re

from tools.benchling import (RESOURCE_MAP, BenchlingEntry, BenchlingEntryList,
                             BenchlingRoot, BenchlingSchema,
                             BenchlingSchemaList, BenchlingSequence,
                             BenchlingSequenceList)
from udc import Listable, UdcUri

from .conftest import (BENCH_AUTHOR, BENCH_BASE, BENCH_ENTRY, BENCH_URI,
                       pytest, pytestmark)

TEST_URI = re.sub("&authors=.*", "", BENCH_URI)


@pytest.fixture
def uri():
    return UdcUri(TEST_URI)

def uri_type(type: str):
    uri = BenchlingRoot.DEFAULT_URI.replace("type=entries", f"type={type}")
    return UdcUri(uri)

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_root(uri: UdcUri):
    root = BenchlingRoot(uri)
    assert root
    assert root.type == "entries"
    assert root.id == BENCH_ENTRY
    assert root.pages() == []
    assert root.base_uri() == TEST_URI

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_root_uri(uri: UdcUri):
    root = BenchlingRoot(uri)
    entry_dict = {"authors": BENCH_AUTHOR}
    entry = type("entries", (object,), entry_dict)
    result = root.item_uri(entry, "authors")
    assert result == f"{BENCH_BASE}#type=entries.authors&id={BENCH_ENTRY}&authors={BENCH_AUTHOR}"

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_pages(uri: UdcUri):
    plist = BenchlingEntryList(uri).items()
    assert len(plist) > 1
    
    plist = BenchlingSchemaList(uri).items()
    assert len(plist) > 0

    plist = BenchlingSequenceList(uri).items()
    assert len(plist) > 1

async def check_list(klass, type: str):
    uri = uri_type(type)
    bench: Listable = klass(uri)
    plist = await bench.list()
    assert len(plist) > 0
    assert plist[0].startswith(str(uri))
    
@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_list():
    for type, klasses in RESOURCE_MAP.items():
        list_klass = klasses[0]
        await check_list(list_klass, type)
