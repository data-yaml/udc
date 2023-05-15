import logging
import os

import pytest
from udc import (  # NOQA F401
    K_BKT,
    K_HSH,
    K_PKG,
    K_PTH,
    K_STR,
    GitIgnore,
    QuiltConfig,
    QuiltID,
    QuiltPackage,
    cli,
)

logging.basicConfig(level=logging.DEBUG)
pytestmark = pytest.mark.anyio


CATALOG_URL = (
    "https://open.quiltdata.com/b/quilt-example/" + "packages/examples/wellplates"
)
TEST_BKT = "quilt-example"
TEST_PKG = "examples/wellplates"
TEST_URI = (
    f"quilt+s3://{TEST_BKT}#package={TEST_PKG}"
    + "@e1f83ce3dc7b9487e5732d58effabad64065d2e7401996fa5afccd0ceb92645c"
    + "&path=README.md&catalog=open.quiltdata.com"
)
REG_URI = f"quilt+s3://{TEST_BKT}"
PKG_URI = f"quilt+s3://{TEST_BKT}#package={TEST_PKG}"
PKG2_URI = f"quilt+s3://{TEST_BKT}#package=examples/echarts"

TEST_URIS = [TEST_URI, REG_URI, PKG_URI, PKG2_URI]

SKIP_LONG_TESTS = os.environ.get("SKIP_LONG_TESTS")
print("SKIP_LONG_TESTS {SKIP_LONG_TESTS}")
