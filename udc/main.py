from collections.abc import Sequence
from sys import stdout

from anyio import run

from .un.un_cli import UnCli


async def app(argv: Sequence[str] = [], out=stdout):
    cli = UnCli()
    await cli.run(argv, out)
    return out


def main(argv: Sequence[str] = []):
    run(app, argv)


if __name__ == "__main__":
    main()
