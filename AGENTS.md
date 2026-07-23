# Repository Guidelines

This repository contains portable agent skills. Keep each `SKILL.md` concise
and place large evidence or metadata under its `references/` directory.

- Never invent benchmark results or transfer a claim between checkpoints.
- Cite primary sources and preserve model scope, dataset/split, metric,
  conditions, provenance, and caveats.
- Never treat Forge latency, throughput, cold-start, or accelerator support
  probes as model-quality benchmarks.
- Never commit credentials, secret selectors, signed URLs, private artifacts,
  or customer data.
- Generated model skill changes must come from `scripts/sync_from_forge.py`.
- Run `python3 -m unittest discover -s tests` before committing.
