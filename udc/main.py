import anyio
import asyncclick as click

@click.command()
@click.argument("name")
async def app(name, **kwargs):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    app(_anyio_backend="trio")  # or asyncio
