# URI: benchling+https://DNS#resource=entry&id=entry_id&author=author_id
from udc import UdcUri

from .entry import BenchlingEntry, BenchlingEntryList
from .root import BenchlingRoot
from .sequence import BenchlingSequence, BenchlingSequenceList
from .schema import BenchlingSchema, BenchlingSchemaList

RESOURCE_MAP = {
    "entry": [BenchlingEntry, BenchlingEntryList],
    "sequence": [BenchlingSequence, BenchlingSequenceList],
    "schema": [BenchlingSchema, BenchlingSchemaList],
}


def BenchlingResource(uri: UdcUri):
    root = BenchlingRoot(uri)
    if not root.id:
        return root
    if root.type == "entry":
        return BenchlingEntry(uri)
    elif root.type == "sequence":
        return BenchlingSequence(uri)
    else:
        raise ValueError(f"Unknown resource type: {root.type}")
