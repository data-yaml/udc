import re

from tools.benchling.resource import BenchlingResource
from tools.benchling.root import BenchlingRoot
from udc import UdcUri

from .conftest import BENCH_ENTRY, BENCH_URI, pytest

TEST_URI = re.sub('&author=.*', '', BENCH_URI)


@pytest.fixture
def root():
    uri = UdcUri(TEST_URI)
    return BenchlingRoot(uri)


def test_benchling_root(root: BenchlingRoot):
    assert root
    assert root.type == "entry"
    assert root.id == BENCH_ENTRY
    assert root.pages() == []

    assert root.base_uri() == TEST_URI


    entry_dict = {'name': 'my_name', 'entry_id': 'my_id', 'author': 'my_author'}
    entry = type('entry', (object,), entry_dict)
    assert root.entry_uri(entry) == f"{TEST_URI}&name=my_name&author=my_author"


@pytest.mark.skip("not implemented")
def test_bench_sequences():
  example_entities = BENCH_ROOT.dna_sequences.list()
  for page in example_entities:
    for sequence in page:
      print(f"name: {sequence.name}\nid:{sequence.id}\n")