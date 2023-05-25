from .root import BenchlingRoot


class BenchlingSequence(BenchlingRoot):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)


class BenchlingSequenceList(BenchlingRoot):
    def __init__(self, attrs: dict) -> None:
        super().__init__(attrs)

    def pages(self):
        return BenchlingRoot.CLIENT.dna_sequences.list()