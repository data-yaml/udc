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
