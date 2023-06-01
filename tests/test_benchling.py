import re
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory

from tzlocal import get_localzone
from udc import Listable
from udc.benchling import (
    RESOURCE_MAP,
    BenchlingEntry,
    BenchlingEntryList,
    BenchlingRoot,
    BenchlingSchemaList,
    BenchlingSequenceList,
)
from un_yaml import UnUri

from .conftest import pytestmark  # noqa: F401
from .conftest import (
    BENCH_AUTHOR,
    BENCH_BASE,
    BENCH_ENTRY,
    BENCH_URI,
    CATALOG_URL,
    pytest,
)

TEST_URI = re.sub("&authors=.*", "", BENCH_URI).replace("entries.authors", "entries")


def Now() -> str:
    tz = get_localzone()
    dt = datetime.now(tz)
    dts = dt.replace(microsecond=0)
    return dts.isoformat()


def Seconds() -> int:
    tz = get_localzone()
    dt = datetime.now(tz)
    return int(dt.timestamp())


@pytest.fixture
def attrs():
    uri = UnUri(TEST_URI)
    return uri.attrs


def attrs_type(type: str):
    uri = UnUri(BenchlingRoot.DEFAULT_URI)
    attrs = uri.attrs
    attrs["type"] = type
    attrs[UnUri.K_URI] = attrs[UnUri.K_URI].replace("type=entries", f"type={type}")
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
    assert (
        result
        == f"{BENCH_BASE}#type=entries.authors&id={BENCH_ENTRY}&authors={BENCH_AUTHOR}"
    )


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
    uri = attrs.get(UnUri.K_URI)
    assert plist[0].startswith(str(uri))


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_list(attrs: dict):
    for rtype, klasses in RESOURCE_MAP.items():
        list_klass = klasses[0]
        await check_list(list_klass, rtype)

    result = await BenchlingEntryList(attrs).list()
    assert "id=etr" in result[0]


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_entry_fetch(attrs: dict):
    entry = BenchlingEntry(attrs)
    entry.fetch()
    assert entry.entry
    assert entry.schema_id
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


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_entry_get(attrs: dict):
    entry = BenchlingEntry(attrs)
    assert entry.id == BENCH_ENTRY

    filename = f"{entry.id}.json"
    with TemporaryDirectory() as tmpdir:
        dir_path = Path(tmpdir)
        file_path = dir_path / filename
        opts = {"path": dir_path}
        results = await entry.get(opts)
        assert str(file_path) in results
        assert filename in results[0]
        assert file_path.exists()


@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
async def test_benchling_entry_patch_uri(attrs: dict):
    new_name = f"test_benchling_entry_patch_uri {Now()}"
    attrs[UnUri.K_QRY] = {
        "name": new_name,
        "fields": {
            "Quilt Catalog URL": {"value": CATALOG_URL},
            "Sentinel": {"value": Seconds()},
        },
    }
    entry = BenchlingEntry(attrs)
    result = await entry.patch()
    assert result

    entry.fetch()
    assert entry.entry.name == new_name
    fields = entry.entry.fields.to_dict()
    assert fields["Quilt Catalog URL"]["value"] == CATALOG_URL
