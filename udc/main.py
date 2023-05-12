import anyio
import asyncclick as click

@click.command()
@click.argument("name")
@click.argument("count", type=int)
async def app(name, count, **kwargs):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        if x:
            await anyio.sleep(0.1)
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    app(_anyio_backend="trio")  # or asyncio
