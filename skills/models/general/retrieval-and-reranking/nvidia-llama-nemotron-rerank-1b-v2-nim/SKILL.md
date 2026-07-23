---
name: use-forge-nvidia-llama-nemotron-rerank-1b-v2-nim
description: Use exact Forge model nvidia-llama-nemotron-rerank-1b-v2-nim for text to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama Nemotron Rerank 1B v2

- Model slug: `nvidia-llama-nemotron-rerank-1b-v2-nim`
- Family: `nvidia-llama-nemotron-rerank-1b-v2`
- Version: `nim-1.10.0-rofs-wrapper-2026-05-27` (`nim-1-10-0-rofs-wrapper-2026-05-27`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `testing`
- Default eligible: `false`
- License: `nvidia-open-model-license; llama-3.2-community-license; nvidia-nim-container-terms`
- Research status: `source-linked`

## Purpose

NVIDIA Llama Nemotron Rerank 1B v2 is a multilingual retrieval reranker that scores query/passage relevance for RAG pipelines.

## Use this exact model when

- Use this exact `nvidia-llama-nemotron-rerank-1b-v2-nim` version when the task supplies text and needs ranking.
- NVIDIA Llama Nemotron Rerank 1B v2 is a multilingual retrieval reranker that scores query/passage relevance for RAG pipelines.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['ranking'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'Which passage explains why regional image mirrors improve inference reliability?'): Query
- `passages` (json_editor; optional; default [{'text': 'Regional container mirrors reduce dependence on a single upstream registry and keep image pulls close to the target compute cluster.'}, {'text': 'Reranking models compare a query with retrieved passages and assign relevance scores before final answer generation.'}, {'text': 'A low temperature setting makes a chat model less random, but it does not change container pull behavior.'}]): Candidate passages
- `truncate` (select; optional; choices END, NONE; default 'END'): Truncate

Route: `POST /v1/ranking`

```json
{
  "model": "{{model_slug}}",
  "passages": "{{passages}}",
  "query": {
    "text": "{{query}}"
  },
  "truncate": "{{truncate}}"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-nemotron-rerank-1b-v2-nim` with version key `nim-1-10-0-rofs-wrapper-2026-05-27`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/ranking` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-nemotron-rerank-1b-v2-nim`
- Routes: `/v1/models/nvidia-llama-nemotron-rerank-1b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-nemotron-rerank-1b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-nemotron-rerank-1b-v2-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/nvidia-llama-nemotron-rerank-1b-v2-nim/SKILL.md
