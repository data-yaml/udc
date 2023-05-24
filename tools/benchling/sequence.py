from udc import UdcUri

from .root import BenchlingRoot


class BenchlingSequence(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)


class BenchlingSequenceList(BenchlingRoot):
    def __init__(self, uri: UdcUri) -> None:
        super().__init__(uri)
