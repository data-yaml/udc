import asyncclick as click

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


def main():
    cli(_anyio_backend="trio")  # or asyncio


if __name__ == "__main__":
    main()
