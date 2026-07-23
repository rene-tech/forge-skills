---
name: use-forge-qwen-qwen3-reranker-0-6b-vllm-cuda13
description: Use exact Forge model qwen-qwen3-reranker-0-6b-vllm-cuda13 for text to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 Reranker 0.6B

- Model slug: `qwen-qwen3-reranker-0-6b-vllm-cuda13`
- Family: `qwen-qwen3-reranker-0-6b`
- Version: `vllm-0.21.0-cuda13-rerank` (`vllm-0-21-0-cuda13-rerank`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 Reranker 0.6B is an Apache-2.0 multilingual text reranking model for retrieval, RAG, code retrieval, and cross-lingual search.

## Use this exact model when

- Use this exact `qwen-qwen3-reranker-0-6b-vllm-cuda13` version when the task supplies text and needs ranking.
- Qwen3 Reranker 0.6B is an Apache-2.0 multilingual text reranking model for retrieval, RAG, code retrieval, and cross-lingual search.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['ranking'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'How do shared model caches reduce inference cold starts?'): Query
- `documents` (json_editor; optional; default ['A shared cache keeps downloaded weights and runtime artifacts on durable storage so later pods can reuse them instead of hydrating from scratch.', 'Cold starts are usually dominated by frontend CSS parsing and browser layout.', 'Rerankers compare a query with candidate passages and assign relevance scores for retrieval pipelines.']): Candidate documents
- `top_n` (number; optional; bounds 1..10; default 3): Top N

Route: `POST /v1/inference/qwen-qwen3-reranker-0-6b-vllm-cuda13`

```json
{
  "documents": "{{documents}}",
  "model": "{{model_slug}}",
  "query": "{{query}}",
  "top_n": "{{top_n}}"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-reranker-0-6b-vllm-cuda13` with version key `vllm-0-21-0-cuda13-rerank`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/qwen-qwen3-reranker-0-6b-vllm-cuda13` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen3-reranker-0-6b-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-reranker-0-6b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-reranker-0-6b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-reranker-0-6b-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/qwen-qwen3-reranker-0-6b-vllm-cuda13/SKILL.md
