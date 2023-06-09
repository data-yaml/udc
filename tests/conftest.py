import logging
import os

import pytest
from quiltplus.uri import QuiltUri

logging.basicConfig(level=logging.DEBUG)
pytestmark = pytest.mark.anyio

BENCH_TENANT = os.environ.get("BENCHLING_TENANT_DNS") or False
BENCH_ENTRY = os.environ.get("BENCHLING_ENTRY_ID") or False
BENCH_AUTHOR = os.environ.get("BENCHLING_AUTHOR_ID") or ""
BENCH_KEY = os.environ.get("BENCHLING_API_KEY")
BENCH_BASE = f"benchling+https://{BENCH_TENANT}"
BENCH_URI = f"{BENCH_BASE}#type=entries.authors&id={BENCH_ENTRY}&authors={BENCH_AUTHOR}"

TEST_BKT = "quilt-example"
TEST_PKG = "examples/wellplates"
CATALOG_URL = f"https://open.quiltdata.com/b/{TEST_BKT}/packages/{TEST_PKG}"

REG_URI = f"quilt+s3://{TEST_BKT}"
VER_URI = f"{REG_URI}#{QuiltUri.K_PKG}={TEST_PKG}"
PKG_URI = f"{VER_URI}@e1f83ce3dc7b"
PKG2_URI = f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}=examples/echarts:latest"
PTH_URI = f"{PKG_URI}&{QuiltUri.K_PTH}=README.md"
PRP_URI = f"{PTH_URI}&{QuiltUri.K_PRP}=*"
TEST_URI = f"{PTH_URI}&{QuiltUri.K_CAT}=open.quiltdata.com"

TEST_URIS = [TEST_URI, REG_URI, PKG_URI, PKG2_URI, PTH_URI, PRP_URI, VER_URI]
