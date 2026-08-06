---
name: use-forge-baai-bge-small-en-v1-5-vllm-cuda13
description: Use exact Forge model baai-bge-small-en-v1-5-vllm-cuda13 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BGE Small EN v1.5

- Model slug: `baai-bge-small-en-v1-5-vllm-cuda13`
- Family: `baai-bge-small-en-v1-5`
- Version: `hf-5c38ec7-vllm-0.21.0-cuda13-pooling` (`hf-5c38ec7-vllm-0-21-0-cuda13-pooling`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

Active non-default CUDA 13 vLLM pooling fallback for BAAI bge-small-en-v1.5, a public MIT-licensed English embedding model for semantic search, short RAG retrieval, clustering, and low-cost passage ranking.

## Use this exact model when

- Use this exact `baai-bge-small-en-v1-5-vllm-cuda13` version when the task supplies text and needs embedding.
- Active non-default CUDA 13 vLLM pooling fallback for BAAI bge-small-en-v1.5, a public MIT-licensed English embedding model for semantic search, short RAG retrieval, clustering, and low-cost passage ranking.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Represent this sentence for searching relevant passages: Lightweight embeddings help support teams rank short knowledge-base answers quickly.'): Input text
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "{{encoding_format}}",
  "input": "{{input}}",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `baai-bge-small-en-v1-5-vllm-cuda13` with version key `hf-5c38ec7-vllm-0-21-0-cuda13-pooling`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-baai-bge-small-en-v1-5-58bedb4dd7`
- Recommended: Semantic search / similarity search in vector databases — The Hugging Face model page documents embedding extraction and an embedding-first retrieval workflow; the config.json and model page report a 384-dimensional embedding hidden size suitable for fixed-length vector similarity workflows.
- Recommended: Clustering of document embeddings — The config.json reports hidden_size = 384 (fixed-length embeddings) and the model page describes embedding extraction; fixed-size vectors of that dimensionality are appropriate inputs for vector clustering algorithms.
- Recommended: Low-cost passage ranking (embedding stage for retrieval followed by a reranker) — The model page and commit-level notes document an embedding+reranker workflow where a BGE embedding model retrieves candidates and a cross-encoder reranker re-ranks them; the README examples demonstrate loading a reranker with AutoModelForSequenceClassification.
- Avoid: High-stakes clinical decision-making or processing of PHI without documented risk controls — Evidence gap: The inspected canonical v1.5 locators (README, commit, config.json, vocab) do not provide checkpoint-specific clinical/PHI handling, privacy, or deployment guidance; do not deploy for PHI/clinical decision tasks without expert review and documented controls.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/baai-bge-small-en-v1-5-vllm-cuda13`
- Routes: `/v1/models/baai-bge-small-en-v1-5-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/baai-bge-small-en-v1-5-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/baai-bge-small-en-v1-5-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/baai-bge-small-en-v1-5-vllm-cuda13/SKILL.md
