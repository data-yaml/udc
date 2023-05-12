from typer.testing import CliRunner

from udc import main

runner = CliRunner()
TEST_URI = "quilt+s3://quilt-example"

def test_list():
    result = runner.invoke(main, [TEST_URI])
    assert result.exit_code == 0
    assert TEST_URI in result.stdout
