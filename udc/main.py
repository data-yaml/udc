from argparse import ArgumentParser
from collections.abc import Sequence
from sys import stdout

from anyio import run

from .api.resource import QuiltResource
from .api.types import Listable
from .un.un_cli import UnCli


async def list(uri: str, out=stdout):
    """Show contents of a Quilt+ URI."""
    qr: Listable = QuiltResource(uri)
    for item in await qr.list():
        print(item, file=out)


async def app(argv: Sequence[str] = None, out=stdout):
    config = UnCli()
    parser = ArgumentParser(config.get('doc'))
    subparsers = parser.add_subparsers(dest="command")
    commands = config.get('commands')
    cfl = config.command('list')
    lister = subparsers.add_parser(cfl['name'], help=cfl['help'])
    lister.add_argument("uri", help="uri to list")

    args = parser.parse_args(argv)
    if args.command == "list":
        await list(args.uri, out)
    else:
        parser.print_help(out)
    return out


def main(argv: Sequence[str] = None):
    run(app, argv)


if __name__ == "__main__":
    main()
