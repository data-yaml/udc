import re

from tools.benchling.root import BenchlingRoot
from udc import UdcUri

from .conftest import BENCH_ENTRY, BENCH_URI, pytest

TEST_URI = re.sub("&author=.*", "", BENCH_URI)


@pytest.fixture
def root():
    uri = UdcUri(TEST_URI)
    return BenchlingRoot(uri)

@pytest.mark.skipif(not BENCH_ENTRY, reason="Benchling environment variables not set")
def test_benchling_root(root: BenchlingRoot):
    assert root
    assert root.type == "entry"
    assert root.id == BENCH_ENTRY
    assert root.pages() == []

    assert root.base_uri() == TEST_URI

    entry_dict = {"name": "my_name", "entry_id": "my_id", "author": "my_author"}
    entry = type("entry", (object,), entry_dict)
    assert root.entry_uri(entry) == f"{TEST_URI}&name=my_name&author=my_author"
