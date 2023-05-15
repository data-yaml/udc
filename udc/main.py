import anyio
import asyncclick as click
from .resource import QuiltResource


@click.group()
def cli() -> None:
    pass

@cli.command()
@click.argument("uri")
async def list(uri: str):
    """Simple program that lists contents URI."""
    click.echo(f"URI: {uri}")
    qr = QuiltResource(uri)
    for item in await qr.list():
        click.echo(item)


def main():
    cli(_anyio_backend="trio")  # or asyncio

if __name__ == '__main__':
    main()
