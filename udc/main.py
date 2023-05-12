import anyio
import asyncclick as click

@click.command()
@click.pass_context
@click.argument("uri")
async def app(ctx, uri, **kwargs):
    """Simple program that echos URI."""
    click.echo(f"URI: {uri}")


def main():
    app(_anyio_backend="trio")  # or asyncio

if __name__ == '__main__':
    main()
