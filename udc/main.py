from collections.abc import Sequence
from sys import stdout

from anyio import run
from un_yaml import UnCli  # type: ignore


async def app(argv: Sequence[str] | None, out=stdout):
    cli = UnCli("udc")
    await cli.run(argv, out)
    return out


def main(argv: Sequence[str] | None = None):
    run(app, argv)


if __name__ == "__main__":
    main()
