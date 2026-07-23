---
name: use-forge-nvidia-llama-nemotron-rerank-vl-1b-v2-nim
description: Use exact Forge model nvidia-llama-nemotron-rerank-vl-1b-v2-nim for text, image to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Nvidia Llama Nemotron Rerank VL 1b V2

- Model slug: `nvidia-llama-nemotron-rerank-vl-1b-v2-nim`
- Family: `nvidia-llama-nemotron-rerank-vl-1b-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

NVIDIA Llama Nemotron Rerank VL 1B v2 NIM for multimodal retrieval reranking; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.

## Use this exact model when

- Use this exact `nvidia-llama-nemotron-rerank-vl-1b-v2-nim` version when the task supplies text, image and needs ranking.
- NVIDIA Llama Nemotron Rerank VL 1B v2 NIM for multimodal retrieval reranking; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['ranking'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (text; optional; default 'Which image contains a flower?'): Query
- `passages` (textarea; optional; default 'A photo of a flower\nA diagram of a GPU'): Candidate text/images

Route: `POST /v1/ranking`

```json
{
  "model": "{{model_slug}}",
  "passages": [
    {
      "text": "A photo of a flower"
    },
    {
      "text": "A diagram of a GPU"
    }
  ],
  "query": {
    "text": "{{query}}"
  },
  "truncate": "END"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-nemotron-rerank-vl-1b-v2-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/ranking` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-nemotron-rerank-vl-1b-v2-nim`
- Routes: `/v1/models/nvidia-llama-nemotron-rerank-vl-1b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-nemotron-rerank-vl-1b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-nemotron-rerank-vl-1b-v2-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/nvidia-llama-nemotron-rerank-vl-1b-v2-nim/SKILL.md
