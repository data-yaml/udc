import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from importlib.metadata import version
from pathlib import Path  # NOQA F401
from sys import stdout
from typing import Any

__version__ = version("udc")

from ..types import Listable
from .un_uri import UnUri
from .un_yaml import UnYaml

class UnUdc():
    async def execute(self, cmd: str, argv: dict):
        callee = argv[UnUri.ARG_RESOURCE] if UnUri.ARG_URI in argv else self
        method = getattr(callee, cmd)
        return await method(argv)


class UnCli(UnYaml):
    """Use UnYaml to create a CLI from a YAML file."""
    CLI_YAML = "cli.yaml"
    CMD = "commands"
    ARG_KEYS = "dest,metavar,type,default,required,choices,action,nargs,const,help".split(',')

    @staticmethod
    def ARG_KWS(arg: dict):
        kwargs = {k: v for k, v in arg.items() if k in UnCli.ARG_KEYS}
        kwargs['type'] = eval(kwargs['type']) if 'type' in kwargs else str
        return kwargs

    def __init__(self, file=CLI_YAML) -> None:
        yaml_data = UnYaml.load_yaml(file, "udc", "un")
        super().__init__(yaml_data)
        if UnCli.CMD not in self.cfg:
            raise ValueError(f"'{UnCli.CMD}' not in file '{file}':\n{self.cfg}")
        self.cmds = self.get(UnCli.CMD)
        self.doc = eval(self.info('doc_class'))

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
            if cmd[0] != "_":
                subparser = subparsers.add_parser(cmd, help=opts["help"])
                args = opts.get("arguments")
                for arg in args or []:
                    subparser.add_argument(arg["name"], **UnCli.ARG_KWS(arg))
        return parser

    async def run(self, argv: Sequence[str] = [], out=stdout):
        args: Any = self.parse(argv)
        if not args:
            return False
        if args.version:
            print(args.version, file=out)
            return False
        return await self.execute(args, out)

    def parse(self, argv: Sequence[str] = []) -> Namespace:
        parser = self.make_parser()
        args = parser.parse_args(argv)
        if args.command is None and not args.version:
            parser.print_help()
            return Namespace()
        return args

    def get_resource(self, uri: UnUri) -> Listable:
        handler = self.get_handler(uri.tool())
        logging.debug(f"handler: {handler}")
        return handler(uri)

    def resource(self, argv: dict) -> dict:
        """Hardcode resource transformation, for now"""
        if UnUri.ARG_URI in argv:
            uri = argv[UnUri.ARG_URI]
            argv[UnUri.ARG_RESOURCE] = self.get_resource(uri)
        return argv

    async def execute(self, args: Namespace, out=stdout):
        """Invoke Appropriate Command."""
        cmd = args.command
        if not cmd in self.cmds:
            logging.error(f"Unknown command: {cmd}\n{args}")
            exit(1)

        argv = vars(args)
        self.resource(argv)

        if cmd in "get,put,patch".split(","):
            results = await self.remote(argv)
        elif cmd in "add,rm".split(","):
            results = await self.stage(argv)
        else:
            # lookup method by name
            method = getattr(self, cmd)
            results = await method(argv)
        return self.echo(results, out)

    def echo(self, results: list, out=stdout):
        """Print result of calling a method."""
        [print(f'"{item}"', file=out) for item in results]
        return out

    async def list(self, argv: dict):
        """Return contents of a URI."""
        res = argv[UnUri.ARG_RESOURCE]
        return await res.list(argv)

    async def remote(self, argv: dict):
        """Perform Remote action on a URI."""
        res = argv[UnUri.ARG_RESOURCE]
        return await res.list(argv)

    async def stage(self, argv: dict):
        """Perform Remote action on a URI."""
        res = argv[UnUri.ARG_RESOURCE]
        return await res.list(argv)
