import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from sys import stdout

from quiltplus import QuiltResource

from ..types import Listable
from .un_yaml import UnYaml


class UnCli(UnYaml):
    CLI_YAML = "cli.yaml"
    CMD = "commands"

    def __init__(self, file=CLI_YAML) -> None:
        yaml_data = UnYaml.load_yaml(file, "tools")
        super().__init__(yaml_data)
        if UnCli.CMD not in self.cfg:
            raise ValueError(f"'{UnCli.CMD}' not in file '{file}':\n{self.cfg}")
        self.cmds = self.get(UnCli.CMD)

    def command(self, cmd: str) -> dict:
        result = self.cmds[cmd]
        result["name"] = cmd
        return result

    def make_parser(self) -> ArgumentParser:
        parser = ArgumentParser(self.get("doc"))
        subparsers = parser.add_subparsers(dest="command")
        for cmd, opts in self.cmds.items():
            subparser = subparsers.add_parser(cmd, help=opts["help"])
            args = opts.get("arguments")
            for arg in args or []:
                subparser.add_argument(arg["name"], help=arg["help"])
        return parser

    async def run(self, argv: Sequence[str] = None, out=stdout):
        args = self.parse(argv)
        return await self.execute(args, out)

    def parse(self, argv: Sequence[str] = None) -> dict:
        parser = self.make_parser()
        args = parser.parse_args(argv)
        return args

    async def execute(self, args: Namespace, out=stdout):
        if args.command == "list":
            await self.list(args.uri, out)
        else:
            logging.error(f"Unknown command: {args.command}\n{args}")
        return out

    async def list(self, uri: str, out=stdout):
        """Show contents of a Quilt+ URI."""
        qr: Listable = QuiltResource(uri)
        for item in await qr.list():
            print(item, file=out)
