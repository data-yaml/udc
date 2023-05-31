from .entry import BenchlingEntry, BenchlingEntryList
from .root import BenchlingRoot
from .schema import BenchlingSchema, BenchlingSchemaList
from .sequence import BenchlingSequence, BenchlingSequenceList

RESOURCE_MAP = {
    "entries": [BenchlingEntryList, BenchlingEntry],
    "dna_sequences": [BenchlingSequenceList, BenchlingSequence],
    "schemas": [BenchlingSchemaList, BenchlingSchema],
}


def BenchlingResource(attrs: dict):
    root = BenchlingRoot(attrs)
    type = root.type
    klasses = RESOURCE_MAP.get(type)
    if not klasses:
        raise ValueError(f"Unknown resource type[{type}]: {attrs}")
    klass = klasses[0] if not root.id else klasses[1]
    return klass(attrs)
