# URI: benchling+https://DNS#resource=entry&id=entry_id&author=author_id
from udc import UdcUri

from .entry import BenchlingEntry, BenchlingEntryList
from .root import BenchlingRoot
from .sequence import BenchlingSequence, BenchlingSequenceList
from .schema import BenchlingSchema, BenchlingSchemaList

RESOURCE_MAP = {
    "entries": [BenchlingEntry, BenchlingEntryList],
    "dna_sequences": [BenchlingSequence, BenchlingSequenceList],
    "schemas": [BenchlingSchema, BenchlingSchemaList],
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
    if not root.id:
        return root
    if root.type == "entries":
        return BenchlingEntry(uri)
    elif root.type == "sequence":
        return BenchlingSequence(uri)
    else:
        raise ValueError(f"Unknown resource type: {root.type}")
