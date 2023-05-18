from argparse import ArgumentParser
from collections.abc import Sequence
from sys import stdout

from anyio import run

from .api.resource import QuiltResource
from .api.types import Listable


async def list(uri: str, out=stdout):
    """Show contents of a Quilt+ URI."""
    qr: Listable = QuiltResource(uri)
    for item in await qr.list():
        print(item, file=out)


async def app(argv: Sequence[str] | None = None, out=stdout):
    parser = ArgumentParser("udc")
    subparsers = parser.add_subparsers(dest="command")
    lister = subparsers.add_parser("list", help="list uri")
    lister.add_argument("uri", help="uri to list")

    args = parser.parse_args(argv)
    await list(args.uri, out)
    return out


def main(argv: Sequence[str] | None = None):
    run(app, argv)


if __name__ == "__main__":
    main()
