---
name: use-forge-alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9
description: Use exact Forge model alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9 for text to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use GTE Reranker ModernBERT Base

- Model slug: `alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9`
- Family: `alibaba-nlp-gte-reranker-modernbert-base`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Alibaba-NLP gte-reranker-modernbert-base served by Hugging Face Text Embeddings Inference CUDA 1.9 for English retrieval reranking.

## Use this exact model when

- Use this exact `alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9` version when the task supplies text and needs ranking.
- Alibaba-NLP gte-reranker-modernbert-base served by Hugging Face Text Embeddings Inference CUDA 1.9 for English retrieval reranking.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['ranking'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'How do shared model caches reduce inference cold starts?'): Query
- `texts` (json_editor; optional; default ['A shared cache keeps downloaded weights and runtime artifacts on durable storage so later pods can reuse them instead of hydrating from scratch.', 'Cold starts are usually dominated by frontend CSS parsing and browser layout.', 'Rerankers compare a query with candidate passages and assign relevance scores for retrieval pipelines.']): Candidate texts
- `raw_scores` (checkbox; optional; default False): Raw scores
- `return_text` (checkbox; optional; default True): Return text

Route: `POST /rerank`

```json
{
  "query": "{{query}}",
  "raw_scores": "{{raw_scores}}",
  "return_text": "{{return_text}}",
  "texts": "{{texts}}",
  "truncate": true,
  "truncation_direction": "right"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /rerank` using the declared request template.
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

- Model: `/v1/models/alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9`
- Routes: `/v1/models/alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9/SKILL.md
