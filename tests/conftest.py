import logging
import os

import pytest
from quiltplus import QuiltUri

logging.basicConfig(level=logging.DEBUG)
pytestmark = pytest.mark.anyio

BENCH_TENANT = os.environ.get("BENCHLING_TENANT_DNS")
BENCH_ENTRY = os.environ.get("BENCHLING_ENTRY_ID")
BENCH_AUTHOR = os.environ.get("BENCHLING_AUTHOR_ID") or ""
BENCH_KEY = os.environ.get("BENCHLING_API_KEY")
BENCH_BASE = f"benchling+https://{BENCH_TENANT}"
BENCH_URI = f"{BENCH_BASE}#type=entries.authors&id={BENCH_ENTRY}&authors={BENCH_AUTHOR}"

TEST_BKT = "quilt-example"
TEST_PKG = "examples/wellplates"
CATALOG_URL = f"https://open.quiltdata.com/b/{TEST_BKT}/packages/{TEST_PKG}"
TEST_URI = (
    f"quilt+s3://{TEST_BKT}#package={TEST_PKG}"
    + "@e1f83ce3dc7b9487e5732d58effabad64065d2e7401996fa5afccd0ceb92645c"
    + "&path=README.md&catalog=open.quiltdata.com"
)
REG_URI = f"quilt+s3://{TEST_BKT}"
PKG_URI = f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}={TEST_PKG}@e1f83ce3dc7b"
PKG2_URI = f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}=examples/echarts:latest"
PTH_URI = (
    f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}={TEST_PKG}&{QuiltUri.K_PTH}=README.md"
)
PRP_URI = f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}={TEST_PKG}&{QuiltUri.K_PTH}=README.md&{QuiltUri.K_PRP}=*"
VER_URI = f"quilt+s3://{TEST_BKT}#{QuiltUri.K_PKG}={TEST_PKG}"

TEST_URIS = [TEST_URI, REG_URI, PKG_URI, PKG2_URI, PTH_URI, PRP_URI, VER_URI]
