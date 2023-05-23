from udc import UdcUri
from tools.benchling.resource import BenchlingResource

from .conftest import pytest, BENCH_URI


@pytest.fixture
def bench():
    uri = UdcUri(BENCH_URI)
    return BenchlingResource(uri)


def test_benchling(bench: BenchlingResource):
    assert bench