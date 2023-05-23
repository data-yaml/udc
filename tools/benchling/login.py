import os

from benchling_sdk.auth.api_key_auth import ApiKeyAuth
from benchling_sdk.benchling import Benchling

BENCH_TENANT = os.environ.get("BENCHLING_TENANT_DNS")
BENCH_ENTRY = os.environ.get("BENCHLING_ENTRY_ID")
BENCH_AUTHOR = os.environ.get("BENCHLING_AUTHOR_ID")
BENCH_KEY = os.environ.get("BENCHLING_API_KEY")
BENCH = Benchling(url=f"https://{BENCH_TENANT}", auth_method=ApiKeyAuth(BENCH_KEY))

def test_bench_sequences():
  example_entities = BENCH.dna_sequences.list()
  for page in example_entities:
    for sequence in page:
      print(f"name: {sequence.name}\nid:{sequence.id}\n")