---
name: use-forge-facebook-esm-2-3b-protein-embedding
description: Use exact Forge model facebook-esm-2-3b-protein-embedding for protein_sequence to embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ESM-2 3B Protein Embeddings

- Model slug: `facebook-esm-2-3b-protein-embedding`
- Family: `facebook-esm-2-3b`
- Version: `hf-476b639-wrapper-20260427-timing` (`hf-476b639-wrapper-20260427-timing`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `testing`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

ESM-2 3B is a nonclinical protein language model for sequence representation learning and downstream protein analysis.

## Use this exact model when

- Use this exact `facebook-esm-2-3b-protein-embedding` version when the task supplies protein_sequence and needs embedding, json.
- ESM-2 3B is a nonclinical protein language model for sequence representation learning and downstream protein analysis.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; required; default 'MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTFSYGVQCFSRYPDHMK'): Protein sequence
- `max_length` (number; optional; bounds 32..1024; default 512): Max sequence length

Route: `POST /v1/inference/facebook-esm-2-3b-protein-embedding`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `task`
- `sequence_length`
- `embedding_dim`
- `embedding_preview`
- `embedding_l2`
- `model_time_ms`

## Required workflow

1. Load this skill and pin model slug `facebook-esm-2-3b-protein-embedding` with version key `hf-476b639-wrapper-20260427-timing`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/facebook-esm-2-3b-protein-embedding` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/facebook-esm-2-3b-protein-embedding`
- Routes: `/v1/models/facebook-esm-2-3b-protein-embedding/inference-routes`
- Regional deployment: `/v1/models/facebook-esm-2-3b-protein-embedding/regional-deployment`
- Serverless handoff: `/v1/models/facebook-esm-2-3b-protein-embedding/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/facebook-esm-2-3b-protein-embedding/SKILL.md
