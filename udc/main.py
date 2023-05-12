import anyio
import asyncclick as click


@click.group()
def cli() -> None:
    pass

@cli.command()
@click.argument("uri")
async def list(uri: str):
    """Simple program that lists contents URI."""
    click.echo(f"URI: {uri}")


def main():
    cli(_anyio_backend="trio")  # or asyncio

if __name__ == '__main__':
    main()
