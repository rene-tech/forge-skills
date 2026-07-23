---
name: use-forge-nvidia-llama-3-2-nv-embedqa-1b-v2-nim
description: Use exact Forge model nvidia-llama-3-2-nv-embedqa-1b-v2-nim for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.2 NV-EmbedQA 1B v2

- Model slug: `nvidia-llama-3-2-nv-embedqa-1b-v2-nim`
- Family: `nvidia-llama-3-2-nv-embedqa-1b-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / embeddings`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-open-model-license; llama-3.2-community-license`
- Research status: `source-linked`

## Purpose

1B NVIDIA retrieval embedding NIM for question-answer retrieval; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.

## Use this exact model when

- Use this exact `nvidia-llama-3-2-nv-embedqa-1b-v2-nim` version when the task supplies text and needs embedding.
- 1B NVIDIA retrieval embedding NIM for question-answer retrieval; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'What is retrieval augmented generation?'): Input text

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": "{{input}}",
  "input_type": "query",
  "model": "{{model_slug}}",
  "truncate": "NONE"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-3-2-nv-embedqa-1b-v2-nim` with version key `v1`.
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

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-2-nv-embedqa-1b-v2-nim`
- Routes: `/v1/models/nvidia-llama-3-2-nv-embedqa-1b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-2-nv-embedqa-1b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-2-nv-embedqa-1b-v2-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nvidia-llama-3-2-nv-embedqa-1b-v2-nim/SKILL.md
