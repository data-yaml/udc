from collections.abc import Sequence
from importlib.metadata import version
from sys import stdout

from anyio import run
from un_yaml import UnCli  # type: ignore

__version__ = version("udc")


async def app(argv: Sequence[str] | None, out=stdout):
    cli = UnCli("udc", __version__)
    await cli.run(argv, out)
    return out


def main(argv: Sequence[str] | None = None):
    run(app, argv)


if __name__ == "__main__":
    main()
