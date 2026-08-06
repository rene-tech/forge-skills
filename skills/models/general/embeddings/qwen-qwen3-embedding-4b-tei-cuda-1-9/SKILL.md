---
name: use-forge-qwen-qwen3-embedding-4b-tei-cuda-1-9
description: Use exact Forge model qwen-qwen3-embedding-4b-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 Embedding 4B

- Model slug: `qwen-qwen3-embedding-4b-tei-cuda-1-9`
- Family: `qwen-qwen3-embedding-4b`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 Embedding 4B served by Hugging Face Text Embeddings Inference CUDA 1.9.3 for mid-tier multilingual semantic search, code retrieval, clustering, and RAG.

## Use this exact model when

- Use this exact `qwen-qwen3-embedding-4b-tei-cuda-1-9` version when the task supplies text and needs embedding.
- Qwen3 Embedding 4B served by Hugging Face Text Embeddings Inference CUDA 1.9.3 for mid-tier multilingual semantic search, code retrieval, clustering, and RAG.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: How does a shared model cache reduce GPU inference cold starts?'): Input text
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

1. Load this skill and pin model slug `qwen-qwen3-embedding-4b-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Research key: `huggingface-co-qwen-qwen3-embedding-4b-5fc440f4b7`
- Recommended: Multilingual semantic search / text retrieval — The Hugging Face model page and the checkpoint README present Qwen3-Embedding-4B as a text embedding model intended for retrieval and multilingual use; README includes retrieval-oriented examples and MTEB-style benchmark results for the checkpoint.
- Recommended: Embedding-based code search / code retrieval (programming-language text) — Primary checkpoint-level materials list natural-language and programming-language text among intended inputs and retrieval-oriented examples applicable to code contexts.
- Recommended: Text clustering and unsupervised organization — The checkpoint is published as a text embedding model intended for similarity, retrieval, clustering, and related downstream uses as shown on the Hugging Face model page and README benchmark summaries.
- Avoid: Direct multimodal (image/video) inputs to this checkpoint — The checkpoint README and model card describe the Qwen3-Embedding series as a text-only embedding model; multimodal/VL embedding variants are documented at the family/repository level as separate variants, not as this exact checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen3-embedding-4b-tei-cuda-1-9`
- Routes: `/v1/models/qwen-qwen3-embedding-4b-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-embedding-4b-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-embedding-4b-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/qwen-qwen3-embedding-4b-tei-cuda-1-9/SKILL.md
