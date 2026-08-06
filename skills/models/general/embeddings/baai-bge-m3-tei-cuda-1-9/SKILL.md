---
name: use-forge-baai-bge-m3-tei-cuda-1-9
description: Use exact Forge model baai-bge-m3-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BGE-M3

- Model slug: `baai-bge-m3-tei-cuda-1-9`
- Family: `baai-bge-m3`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

BAAI BGE-M3 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual semantic retrieval, long-document RAG, and dense embedding use.

## Use this exact model when

- Use this exact `baai-bge-m3-tei-cuda-1-9` version when the task supplies text and needs embedding.
- BAAI BGE-M3 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual semantic retrieval, long-document RAG, and dense embedding use.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'How can shared GPU caches reduce model inference cold starts?'): Input text

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": "{{input}}",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `baai-bge-m3-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Research key: `huggingface-co-baai-bge-m3-2eda4773a3`
- Recommended: Multilingual dense retrieval (semantic search / vector retrieval) — Model page and README demonstrate embedding/retrieval usage and show dense retrieval scores; config.json shows hidden_size=1024 which corresponds to the dense vector dimensionality.
- Recommended: Hybrid retrieval combining dense + sparse lexical scores — README and model page show dense and sparse components and list retrieval scores for sparse, dense, and combined sparse+dense.
- Recommended: ColBERT-style multi-vector retrieval (multi-vector outputs) — README and model page indicate ColBERT component outputs and list colbert retrieval scores; examples in README demonstrate 'colbert' in returned scoring dictionaries.
- Avoid: Using BAAI/bge-m3 as a standalone generative language model for text generation / LM tasks — No primary-file evidence documents a generation head, logits/head weights, or a generation/text-LM API for this checkpoint; the provided blobs and README present the model as an embedding/retrieval model.
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

- Model: `/v1/models/baai-bge-m3-tei-cuda-1-9`
- Routes: `/v1/models/baai-bge-m3-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/baai-bge-m3-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/baai-bge-m3-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/baai-bge-m3-tei-cuda-1-9/SKILL.md
