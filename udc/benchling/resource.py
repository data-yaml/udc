from .entry import BenchlingEntry, BenchlingEntryList
from .root import BenchlingRoot
from .schema import BenchlingSchema, BenchlingSchemaList
from .sequence import BenchlingSequence, BenchlingSequenceList

RESOURCE_MAP = {
    "entries": [BenchlingEntryList, BenchlingEntry],
    "dna_sequences": [BenchlingSequenceList, BenchlingSequence],
    "schemas": [BenchlingSchemaList, BenchlingSchema],
}

RESOURCES = [
    "aa_sequences",
    "api",
    "apps",
    "assay_results",
    "assay_runs",
    "blobs",
    "boxes",
    "client",
    "containers",
    "custom_entities",
    "dna_alignments",
    "dna_oligos",
    "dna_sequences",
    "dropdowns",
    "entries",
    "events",
    "exports",
    "feature_libraries",
    "folders",
    "inventory",
    "lab_automation",
    "label_templates",
    "locations",
    "mixtures",
    "molecules",
    "nucleotide_alignments",
    "oligos",
    "organizations",
    "plates",
    "printers",
    "projects",
    "registry",
    "requests",
    "rna_oligos",
    "rna_sequences",
    "schemas",
    "tasks",
    "teams",
    "users",
    "v2",
    "warehouse",
    "workflow_outputs",
    "workflow_task_groups",
    "workflow_tasks",
]


def BenchlingResource(attrs: dict):
    root = BenchlingRoot(attrs)
    type = root.type
    klasses = RESOURCE_MAP.get(type)
    if not klasses:
        raise ValueError(f"Unknown resource type[{type}]: {attrs}")
    klass = klasses[0] if not root.id else klasses[1]
    return klass(attrs)
