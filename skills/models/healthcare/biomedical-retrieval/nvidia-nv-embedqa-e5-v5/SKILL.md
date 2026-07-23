---
name: use-forge-nvidia-nv-embedqa-e5-v5
description: Use exact Forge model nvidia-nv-embedqa-e5-v5 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NV EmbedQA E5

- Model slug: `nvidia-nv-embedqa-e5-v5`
- Family: `nvidia-nv-embedqa-e5`
- Version: `v5` (`v5`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `stable`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Domain-tuned embedding model suitable for retrieval, semantic search, and document ranking.

## Use this exact model when

- Use this exact `nvidia-nv-embedqa-e5-v5` version when the task supplies text and needs embedding.
- Domain-tuned embedding model suitable for retrieval, semantic search, and document ranking.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Cold starts matter for public inference systems.'): Text to embed

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": "{{input}}",
  "input_type": "query",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `nvidia-nv-embedqa-e5-v5` with version key `v5`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-nv-embedqa-e5-v5`
- Routes: `/v1/models/nvidia-nv-embedqa-e5-v5/inference-routes`
- Regional deployment: `/v1/models/nvidia-nv-embedqa-e5-v5/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-nv-embedqa-e5-v5/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/nvidia-nv-embedqa-e5-v5/SKILL.md
