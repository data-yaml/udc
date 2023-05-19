from .un_yaml import UnYaml
CLI_YAML = 'cli.yaml'


class UnCli(UnYaml):
    
    def __init__(self, file=CLI_YAML) -> None:
        super().__init__(file)
