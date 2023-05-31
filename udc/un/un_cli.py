import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from importlib.metadata import version
from pathlib import Path  # NOQA F401
from sys import stdout

__version__ = version("udc")

from ..types import Listable
from .un_uri import UnUri
from .un_yaml import UnYaml

class UnUdc():
    async def list(self, args: Namespace):
        """Return contents of a URI."""
        res = self.get_resource(args.uri)
        return await res.list(vars(args))

    async def remote(self, args: Namespace):
        """Perform Remote action on a URI."""
        res = self.get_resource(args.uri)
        return await res.list(vars(args))


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
        doc = UnUdc()

        if cmd in "get,put,patch".split(","):
            results = await self.remote(args)
        elif cmd in "add,rm".split(","):
            results = await self.stage(args)
        else:
            # lookup method by name
            method = getattr(self, cmd)
            results = await method(args)
        return self.echo(results, out)

    def echo(self, results: list, out=stdout):
        """Print result of calling a method."""
        [print(f'"{item}"', file=out) for item in results]
        return out

    async def list(self, args: Namespace):
        """Return contents of a URI."""
        res = self.get_resource(args.uri)
        return await res.list(vars(args))

    async def remote(self, args: Namespace):
        """Perform Remote action on a URI."""
        res = self.get_resource(args.uri)
        return await res.list(vars(args))
