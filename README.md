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
│   ├── forge-model-deployment/
│   ├── serverless-endpoints/
│   └── serverless-jobs/
└── models/
    └── <category>/<group>/
        ├── research.md           # audited group selection/comparison guide
        ├── research.json         # machine-readable group dossier
        └── <model-slug>/
            ├── SKILL.md          # concise exact-model operating skill
            ├── agents/openai.yaml
            ├── evals/evals.json
            └── references/
                ├── research.md   # full audited checkpoint dossier
                ├── research.json
                ├── forge-model.json
                ├── forge-skill.json
                └── evidence.md
```

Start with [`skills/forge-models/SKILL.md`](skills/forge-models/SKILL.md).
It reads the compact catalog, narrows by category/group, and loads only the
selected exact model skill. Raw metadata and evidence stay under `references/`
until needed, preventing the full catalog from consuming an agent's context.

## Catalog

- `catalog/models.json` — compact exact-model lookup.
- `catalog/hierarchy.json` — category/group/family tree.
- `catalog/groups.json` — lazy links to audited group-selection dossiers.
- `catalog/groups.schema.json` — machine-readable group-catalog contract.
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

## Deep research

The catalog is researched in two layers:

- 178 checkpoint/source units cover all 203 exact Forge serving variants;
- 28 category/group dossiers define model-selection questions, comparable
  benchmark protocols, and evidence-backed conditional routing rules. Group
  rules may name only exact Forge slugs (or `insufficient-evidence`) and must
  collectively cover every candidate in the group.

Each checkpoint dossier covers identity/license, use and non-use cases,
input preparation, output interpretation, public benchmarks, comparisons,
limitations, safety, primary sources, and evidence gaps. Every input/output
claim carries source URLs; every benchmark includes exact checkpoint scope and
a table/figure/section locator.

Research is two-pass. A second independent pass opens and verifies the sources,
removes secondary material, checks checkpoint and numeric benchmark scope, and
returns a corrected dossier in the same schema as the draft. The runner derives
the accepted/revised audit record from that correction and preserves every
deterministic draft defect supplied to the second pass. Keeping the provider
contract flat avoids losing fields from deeply nested structured output. A
result is publishable only after the audit and local schema/source checks pass.
An empty benchmark or comparison section is valid only with a specific
evidence-gap statement after the official starting source, canonical model
card/repository, and original paper have been checked. Serving packages such
as NIMs and wrappers are traced to the underlying checkpoint where primary
identity evidence permits it; upstream quality evidence remains explicitly
separate from container and Forge-runtime measurements.
For a third-party model packaged through NVIDIA Build, publication additionally
requires a primary source controlled by the original creator. NVIDIA's serving
documentation remains required for the package/runtime contract, but cannot by
itself establish the upstream checkpoint's task identity, behavior, or quality.
Redistribution catalogs such as Ollama and third-party model-card mirrors are
not accepted as primary evidence.
Representative manual checks are recorded in
`research/manual-review-hints.json`. They point the independent auditor at a
primary-source locator to verify; they are not copied into a dossier as trusted
claims.

```bash
python3 scripts/research_catalog.py plan
python3 scripts/research_catalog.py run \
  --kind models --model pro --workers 16 --max-active 16 --max-attempts 30
python3 scripts/research_catalog.py run \
  --kind groups --model pro --workers 4 --max-active 4 --max-attempts 30
python3 scripts/research_catalog.py prepare-publication --kind all
python3 scripts/research_catalog.py validate --kind all
```

Model and group controllers use separate ignored state files and per-kind
process locks. This permits those two queues to run concurrently while
preventing two controllers from racing over the same queue provenance.
Rejected audit attempts are preserved, and the next retry starts from the
prior correction with the fewest deterministic validation errors rather than
discarding good corrections and returning to the original draft.
`prepare-publication` removes provider request IDs from accepted public
dossiers; ignored local state retains the operational request history.

For NVIDIA models, `research/upstream-agent-skills.json` pins relevant official
NVIDIA Agent Skills for MAISI, Cosmos-Embed, Cosmos Reason, and Nemotron
customization/retrieval; the separate NVIDIA BioNeMo Agent Toolkit model/NIM
skills and multi-model pipelines; and the Nebius BioNeMo agent integration.
Their payload, artifact, validator, failure-mode, recipe, and deployment
guidance is reused only at the exact declared scope. Version-mismatched
workflows and deterministic integration harnesses are labeled as related
guidance and are never treated as model-quality evidence.

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

Deep research adds a stricter publication state: the checkpoint and group
dossiers must have an independent `accepted` or `revised` audit, all source and
scope gates must pass, and every exact catalog slug must be covered exactly
once.

## Security

Skills contain no credentials. Forge API keys, Nebius IAM tokens, MysteryBox
selectors, registry passwords, signed URLs, and customer data must remain
runtime secrets. Model inference is remote processing; agents must apply the
data-use and safety constraints in the selected skill.
