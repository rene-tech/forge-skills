---
name: use-forge-nvidia-llama-3-2-nv-rerankqa-1b-v2-nim
description: Use exact Forge model nvidia-llama-3-2-nv-rerankqa-1b-v2-nim for text to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.2 NV-RerankQA 1B v2

- Model slug: `nvidia-llama-3-2-nv-rerankqa-1b-v2-nim`
- Family: `nvidia-llama-3-2-nv-rerankqa-1b-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-open-model-license; llama-3.2-community-license`
- Research status: `source-linked`

## Purpose

1B NVIDIA retrieval reranking NIM for question-answer ranking; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.

## Use this exact model when

- Use this exact `nvidia-llama-3-2-nv-rerankqa-1b-v2-nim` version when the task supplies text and needs ranking.
- 1B NVIDIA retrieval reranking NIM for question-answer ranking; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave5.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['ranking'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'what is retrieval augmented generation?'): Query
- `passages` (json_editor; optional; default [{'text': 'Retrieval augmented generation combines search over external documents with language model generation.'}, {'text': 'A graphics processing unit accelerates parallel numerical workloads.'}, {'text': 'Embeddings map text into vectors for semantic search.'}]): Passages

Route: `POST /v1/inference/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim`

```json
{
  "model": "{{model_slug}}",
  "passages": "{{passages}}",
  "query": {
    "text": "{{query}}"
  },
  "truncate": "END"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-3-2-nv-rerankqa-1b-v2-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-llama-3-2-nv-rerankqa-1b-v2-3e8a5720eb`
- Recommended: Reranking candidate passages/documents for a given query in a two-stage retrieval pipeline — NVIDIA NIM reference and the NVIDIA Build product page describe the checkpoint as intended to improve multilingual retrieval tasks by reranking candidate passages and emitting a relevance logit for each candidate
- Avoid: Using this checkpoint as a generative chat or free-form text generation model — Primary NVIDIA documentation for the exact reranker/runtime describes a reranking model that accepts query-passage pairs and outputs relevance logits; the Build and NIM reference pages do not document generative text outputs for this checkpoint/runtime
- Avoid: Using the model beyond its documented evaluated language set without validation — The NIM reference documents evaluation on 26 listed languages; there is no checkpoint-scoped primary-source evidence that validates broader language coverage for this exact NIM-served reranker
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim`
- Routes: `/v1/models/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/nvidia-llama-3-2-nv-rerankqa-1b-v2-nim/SKILL.md
