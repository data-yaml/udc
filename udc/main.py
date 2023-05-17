import asyncclick as click
from argparse import ArgumentParser
from sys import stdout
from .resource import QuiltResource
from .types import Listable


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.argument("uri")
async def list(uri: str):
    """Show contents of a Quilt+ URI."""
    qr: Listable = QuiltResource(uri)
    for item in await qr.list():
        click.echo(item)


def main(argv=None):
    cli(_anyio_backend="trio")  # or asyncio


def app(argv=None, out=stdout):
    parser = ArgumentParser('udc')
    subparsers = parser.add_subparsers(dest='command')
    lister = subparsers.add_parser('list', help='list uri')
    lister.add_argument('uri', help='uri to list')

    args = parser.parse_args(argv)
    print(f'Hello {args}', file=out)
    return out

if __name__ == "__main__":
    app()
    main()
