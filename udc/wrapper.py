from un_yaml import UnUri  # type: ignore


class Wrapper:
    """Wrap resource methods"""

    async def execute(self, cmd: str, argv: dict):
        callee = argv[UnUri.ARG_RESOURCE] if UnUri.ARG_URI in argv else self
        method = getattr(callee, cmd)
        return await method(argv)
