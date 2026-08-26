"""Source adapters and shared schema for the multi-source job board pipeline.

Each adapter returns a list of unified job dicts (see ``sources.schema.Job``).
Adapters are best-effort: on network/anti-bot failure they raise
``SourceUnavailable`` so the orchestrator can skip just that source.
"""
