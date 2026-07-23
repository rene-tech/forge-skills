---
name: use-forge-facebook-esm-2-3b
description: Use exact Forge model facebook-esm-2-3b for protein_sequence to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ESM-2 3B

- Model slug: `facebook-esm-2-3b`
- Family: `facebook-esm-2`
- Version: `3b` (`3b`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `stable`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

Meta ESM-2 3B protein language model served as a Forge protein-sequence embedding endpoint.

## Use this exact model when

- Use this exact `facebook-esm-2-3b` version when the task supplies protein_sequence and needs embedding.
- Meta ESM-2 3B protein language model served as a Forge protein-sequence embedding endpoint.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'MTEITAAMVKELRESTGAGMMDCKNALSETQHEK'): Protein sequence
- `max_length` (number; optional; bounds 32..2048; default 1024): Max sequence length

Route: `POST /v1/inference/facebook-esm-2-3b`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `facebook-esm-2-3b` with version key `3b`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/facebook-esm-2-3b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/facebook-esm-2-3b`
- Routes: `/v1/models/facebook-esm-2-3b/inference-routes`
- Regional deployment: `/v1/models/facebook-esm-2-3b/regional-deployment`
- Serverless handoff: `/v1/models/facebook-esm-2-3b/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/facebook-esm-2-3b/SKILL.md
