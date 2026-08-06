---
name: use-forge-models
description: Route any inference or deployment task to one exact Nebius Forge model/version skill. Use for model selection, request construction, output interpretation, comparison, or Nebius Serverless handoff; load only the selected model skill.
---

# Use Forge Models

## Progressive loading

1. State the required input, output, task, quality criterion, data boundary,
   latency/cost constraints, and whether experimental models are acceptable.
2. Read `catalog/hierarchy.json` to select a category and group. Do not load
   every skill.
3. Load only that group's entry from `catalog/groups.json`, then its
   `researchMarkdownPath`. Use the audited questions, comparability gates, and
   conditional routing rules; do not declare a winner when the dossier records
   an evidence gap.
4. Search `catalog/models.json` within that group. Compare exact model slug,
   version, modalities, stability, default eligibility, license, evidence
   status, and live availability.
5. Load exactly one candidate's `SKILL.md`. Load a second only for an explicit
   comparison.
6. Follow the chosen skill's exact input fields, request template, route,
   output validation, evidence scope, limitations, and safety rules.
7. Re-fetch the live Forge model and inference-route endpoints immediately
   before inference. Repository skills are reviewed knowledge; live APIs are
   authoritative for current routes, regions, images, pricing, readiness, and
   runtime metrics.
8. For deployment, load `$use-nebius` and
   `$nebius-forge-model-deployment`, then the Serverless endpoint/job leaf
   skill required by the selected model.

## Selection rules

- Never select from a name or broad category alone.
- Never substitute a family-level or neighboring-checkpoint benchmark.
- Never present Forge GPU latency or throughput as scientific-quality evidence.
- If evidence is `source-linked`, disclose that no reviewed public claim is
  attached and consult the primary source before making a quality comparison.
- Prefer stable, default-eligible versions when candidates meet the same
  contract unless the task requires an experimental capability.
- Surface licenses, gated artifacts, required secrets, unsupported regions,
  and research-only status before inference or deployment.

## Context discipline

Return the selected model slug, version key, skill path/hash, why it fits,
rejected alternatives, exact request/output contract, evidence status, live
route, region/GPU choice, and cleanup expectations. Do not paste the full
catalog or unrelated skills into context.
