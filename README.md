# Forge Skills

Portable, progressively loaded agent skills for every active model/version in
[Nebius Forge](https://forge.nebius.cloud), plus general Nebius operational
skills.

The repository is designed for agents that can read `SKILL.md` files or fetch
Markdown/JSON over HTTP. It does not require a particular model vendor:

- Codex and Claude Code can clone the repository and expose selected
  directories through their local skill mechanism.
- ChatGPT and other hosted agents can fetch the catalog and skill files through
  the Forge API or a repository/API tool.
- Custom agents such as ClawBio load the small router first, then one exact
  model skill only after model selection.

## Lazy-loading hierarchy

```text
skills/
├── forge-models/                 # top-level model router
├── nebius/                      # Nebius operations router
│   ├── project-discovery/
│   ├── registry-and-secrets/
│   ├── serverless-endpoints/
│   └── serverless-jobs/
└── models/
    └── <category>/<group>/<model-slug>/
        ├── SKILL.md              # concise exact-model operating skill
        └── references/
            ├── forge-model.json  # full public Forge metadata snapshot
            ├── forge-skill.json  # full exact-skill API snapshot
            └── evidence.md       # scoped benchmark/source evidence
```

Start with [`skills/forge-models/SKILL.md`](skills/forge-models/SKILL.md).
It reads the compact catalog, narrows by category/group, and loads only the
selected exact model skill. Raw metadata and evidence stay under `references/`
until needed, preventing the full catalog from consuming an agent's context.

## Catalog

- `catalog/models.json` — compact exact-model lookup.
- `catalog/hierarchy.json` — category/group/family tree.
- `catalog/schema.json` — machine-readable catalog contract.
- `catalog/research-status.json` — evidence coverage and review queue.

Every generated skill records:

- exact Forge slug, family, version, and version key;
- what the model is for and when not to use it;
- declared input fields, bounds, request template, route, and outputs;
- stability, default eligibility, license, and source;
- reviewed public benchmark claims when Forge has curated them;
- an explicit research status when no reviewed public claim is attached;
- live inference and Nebius Serverless deployment handoff URLs.

`references/forge-model.json` preserves the complete public Forge model record,
including all benchmark/probe/artifact metadata available at generation time;
`references/forge-skill.json` preserves the corresponding exact-skill API
record. Operational accelerator latency is never presented as model-quality
evidence.

## Synchronizing

```bash
python3 scripts/sync_from_forge.py \
  --api-base https://forge.nebius.cloud/api/proxy \
  --output-root .
python3 -m unittest discover -s tests
```

The sync is deterministic for a given Forge API snapshot. It updates generated
model skills and catalogs without changing the hand-authored router and Nebius
skills.

## Evidence policy

A model is `reviewed` only when its benchmark claim has a primary source,
model/checkpoint scope, dataset and split, metric and value, conditions,
provenance, and caveats. Otherwise it is `source-linked`: the exact model skill
is usable, but the agent must not invent a quality claim and must consult the
linked primary model card or paper before comparing quality. `pending-review`
means Forge has not yet linked enough primary-source evidence for that exact
version.

## Security

Skills contain no credentials. Forge API keys, Nebius IAM tokens, MysteryBox
selectors, registry passwords, signed URLs, and customer data must remain
runtime secrets. Model inference is remote processing; agents must apply the
data-use and safety constraints in the selected skill.
