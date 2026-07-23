---
name: use-forge-facebook-esm-2-650m
description: Use exact Forge model facebook-esm-2-650m for protein_sequence to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ESM-2 650M

- Model slug: `facebook-esm-2-650m`
- Family: `facebook-esm-2`
- Version: `650m` (`650m`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `stable`
- Default eligible: `true`
- License: `mit`
- Research status: `reviewed`

## Purpose

Meta ESM-2 650M protein language model served as a Forge protein-sequence embedding endpoint.

## Use this exact model when

- Use this exact `facebook-esm-2-650m` version when the task supplies protein_sequence and needs embedding.
- Meta ESM-2 650M protein language model served as a Forge protein-sequence embedding endpoint.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'MTEITAAMVKELRESTGAGMMDCKNALSETQHEK'): Protein sequence
- `max_length` (number; optional; bounds 32..2048; default 1024): Max sequence length

Route: `POST /v1/inference/facebook-esm-2-650m`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `facebook-esm-2-650m` with version key `650m`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/facebook-esm-2-650m` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
Read `references/evidence.md` for 1 reviewed public claim(s) and their exact scope.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/facebook-esm-2-650m`
- Routes: `/v1/models/facebook-esm-2-650m/inference-routes`
- Regional deployment: `/v1/models/facebook-esm-2-650m/regional-deployment`
- Serverless handoff: `/v1/models/facebook-esm-2-650m/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/facebook-esm-2-650m/SKILL.md
