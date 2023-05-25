# URI: benchling+https://DNS#resource=entry&id=entry_id&authors=author_id
from udc import UdcUri

from .entry import BenchlingEntry, BenchlingEntryList
from .root import BenchlingRoot
from .sequence import BenchlingSequence, BenchlingSequenceList
from .schema import BenchlingSchema, BenchlingSchemaList

RESOURCE_MAP = {
    "entries": [BenchlingEntryList, BenchlingEntry],
    "dna_sequences": [BenchlingSequenceList, BenchlingSequence],
    "schemas": [BenchlingSchemaList, BenchlingSchema],
}

RESOURCES=['aa_sequences', 'api', 'apps', 'assay_results', 'assay_runs', 'blobs',
           'boxes', 'client', 'containers', 'custom_entities', 'dna_alignments',
           'dna_oligos', 'dna_sequences', 'dropdowns', 'entries', 'events',
           'exports', 'feature_libraries', 'folders', 'inventory', 'lab_automation',
            'label_templates', 'locations', 'mixtures', 'molecules',
            'nucleotide_alignments', 'oligos', 'organizations', 'plates', 'printers',
            'projects', 'registry', 'requests', 'rna_oligos', 'rna_sequences',
            'schemas', 'tasks', 'teams', 'users', 'v2', 'warehouse', 'workflow_outputs',
            'workflow_task_groups', 'workflow_tasks']

def BenchlingResource(uri: UdcUri):
    root = BenchlingRoot(uri)
    types = root.type.split('.')
    type = types[0]
    klasses = RESOURCE_MAP.get(type)
    if not klasses:
        raise ValueError(f"Unknown resource type[{type}]: {uri}")
    klass = klasses[0] if not root.id else klasses[1]
    return klass(uri)