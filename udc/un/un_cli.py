import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from importlib.metadata import version
from sys import stdout

__version__ = version("udc")

from ..types import Listable
from .un_uri import UnUri
from .un_yaml import UnYaml


class UnCli(UnYaml):
    CLI_YAML = "cli.yaml"
    CMD = "commands"

    def __init__(self, file=CLI_YAML) -> None:
        yaml_data = UnYaml.load_yaml(file, "udc", "un")
        super().__init__(yaml_data)
        if UnCli.CMD not in self.cfg:
            raise ValueError(f"'{UnCli.CMD}' not in file '{file}':\n{self.cfg}")
        self.cmds = self.get(UnCli.CMD)

    def cmd_opts(self, cmd: str) -> dict:
        result = self.cmds[cmd]
        result["name"] = cmd
        return result

    def parse_version(self, parser: ArgumentParser) -> None:
        __version__ = version("udc")
        parser.add_argument(
            "-v",
            "--version",
            action="store_const",
            const=f"{self.info('doc')} {__version__}",
            help="Show version and exit.",
        )

    def make_parser(self) -> ArgumentParser:
        parser = ArgumentParser(self.get("doc"))
        self.parse_version(parser)
        subparsers = parser.add_subparsers(dest="command")
        for cmd, opts in self.cmds.items():
            if cmd != "list":
                continue
            subparser = subparsers.add_parser(cmd, help=opts["help"])
            args = opts.get("arguments")
            for arg in args or []:
                subparser.add_argument(arg["name"], help=arg["help"])
        return parser

    async def run(self, argv: Sequence[str] = None, out=stdout):
        args = self.parse(argv)
        if not args:
            return False
        if args.version:
            print(args.version, file=out)
            return False
        return await self.execute(args, out)

    def parse(self, argv: Sequence[str] = None) -> dict:
        parser = self.make_parser()
        args = parser.parse_args(argv)
        if args.command is None and not args.version:
            parser.print_help()
            return False
        return args

    async def execute(self, args: Namespace, out=stdout):
        """Invoke Appropriate Command."""
        cmd = args.command
        opts = self.cmd_opts(cmd)
        if not opts:
            logging.error(f"Unknown command: {cmd}\n{args}")
            exit(1)

        if cmd in "get,put,patch".split(","):
            results = await self.remote(cmd, args.path, args.uri, args.nocopy)
        elif cmd in "add,rm".split(","):
            results = await self.stage(cmd, args.local, args.path)
        else:
            # lookup method by name
            method = getattr(self, cmd)
            results = await method(args)
        return self.echo(results, out)

    def echo(self, results: list, out=stdout):
        """Print result of calling a method."""
        [print(item, file=out) for item in results]
        return out

    def get_resource(self, uri: str) -> Listable:
        parsed = UnUri(uri)
        handler = self.get_handler(parsed.tool())
        logging.debug(f"handler: {handler}")
        return handler(parsed)

    async def list(self, args: Namespace):
        """Return contents of a URI."""
        res = self.get_resource(args.uri)
        return await res.list()

    async def remote(self, path: str, uri: str, nocopy: bool = False):
        """Perform Remote action on a URI."""
        res = self.get_resource(uri)
        return await res.list()
