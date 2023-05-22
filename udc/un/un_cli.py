from argparse import ArgumentParser
from collections.abc import Sequence
from sys import stdout

from quiltplus import QuiltResource

from ..types import Listable
from .un_yaml import UnYaml


class UnCli(UnYaml):

    CLI_YAML = 'cli.yaml'
    CMD = 'commands'
    
    def __init__(self, file=CLI_YAML) -> None:
        yaml_data = UnYaml.load_yaml(file, 'tools')
        super().__init__(yaml_data)
        if not UnCli.CMD in self.cfg:
            raise ValueError(f"'{UnCli.CMD}' not in file '{file}':\n{self.cfg}")
        self.cmds = self.get(UnCli.CMD)

    def command(self, cmd: str):
        result = self.cmds[cmd]
        result['name'] = cmd
        return result
    
    async def run(self, argv: Sequence[str] = None, out=stdout):
        parser = ArgumentParser(self.get('doc'))
        subparsers = parser.add_subparsers(dest="command")
        commands = self.get('commands')
        cfl = self.command('list')
        lister = subparsers.add_parser(cfl['name'], help=cfl['help'])
        lister.add_argument("uri", help="uri to list")

        args = parser.parse_args(argv)
        if args.command == "list":
            await self.list(args.uri, out)
        else:
            parser.print_help(out)
        return out

    async def list(self, uri: str, out=stdout):
        """Show contents of a Quilt+ URI."""
        qr: Listable = QuiltResource(uri)
        for item in await qr.list():
            print(item, file=out)


