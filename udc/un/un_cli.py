from .un_yaml import UnYaml
CLI_YAML = 'cli.yaml'


class UnCli(UnYaml):
    CMD='commands'
    
    def __init__(self, file=CLI_YAML) -> None:
        super().__init__(file)
        if not UnCli.CMD in self.cfg:
            raise ValueError(f"'{UnCli.CMD}' not in file '{file}':\n{self.cfg}")
        self.cmds = self.get(UnCli.CMD)

    def command(self, cmd: str):
        result = self.cmds[cmd]
        result['name'] = cmd
        return result
