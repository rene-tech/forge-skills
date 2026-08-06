---
name: use-forge-baai-bge-reranker-v2-m3-tei-cuda-1-9
description: Use exact Forge model baai-bge-reranker-v2-m3-tei-cuda-1-9 for text to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BGE Reranker v2 M3

- Model slug: `baai-bge-reranker-v2-m3-tei-cuda-1-9`
- Family: `baai-bge-reranker-v2-m3`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

BAAI bge-reranker-v2-m3 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual retrieval reranking.

## Use this exact model when

- Use this exact `baai-bge-reranker-v2-m3-tei-cuda-1-9` version when the task supplies text and needs ranking.
- BAAI bge-reranker-v2-m3 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual retrieval reranking.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['ranking'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'What does a reranker do in a retrieval pipeline?'): Query
- `texts` (json_editor; optional; default ['A reranker receives a query and candidate passages from an initial retrieval step, scores each query-passage pair, and orders the passages by relevance.', 'A shared model cache stores downloaded weights and compiled runtime artifacts on durable storage so later pods can avoid first-run hydration.', 'Browser CSS controls typography, layout, and responsive styling for a web application.']): Candidate texts
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

1. Load this skill and pin model slug `baai-bge-reranker-v2-m3-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /rerank` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-baai-bge-reranker-v2-m3-3891d3dadf`
- Recommended: Reranking top-k retrieval candidates (query, passage pairs) in multilingual retrieval and open-domain QA pipelines — Upstream README documents that the model accepts a query (question) and a document (passage) and directly outputs a similarity/relevance score; config.json shows a sequence-classification head appropriate for cross-encoder reranking.
- Avoid: Using this reranker checkpoint as an embedding model (embedding-model substitute) — Upstream README and config identify the artifact as a cross-encoder reranker with a sequence-classification head that directly outputs a single scalar relevance score per query–document pair rather than producing fixed vector embeddings for each input.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/baai-bge-reranker-v2-m3-tei-cuda-1-9`
- Routes: `/v1/models/baai-bge-reranker-v2-m3-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/baai-bge-reranker-v2-m3-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/baai-bge-reranker-v2-m3-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/baai-bge-reranker-v2-m3-tei-cuda-1-9/SKILL.md
