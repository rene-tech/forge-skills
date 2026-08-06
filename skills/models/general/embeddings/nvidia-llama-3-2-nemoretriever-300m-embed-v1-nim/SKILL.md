---
name: use-forge-nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim
description: Use exact Forge model nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.2 NeMo Retriever 300M Embed v1

- Model slug: `nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim`
- Family: `nvidia-llama-3-2-nemoretriever-300m-embed-v1`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / embeddings`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-community-model-license; llama-3.2-community-license`
- Research status: `source-linked`

## Purpose

Earlier 300M multilingual text embedding NVIDIA NIM for retrieval version comparison; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.

## Use this exact model when

- Use this exact `nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim` version when the task supplies text and needs embedding.
- Earlier 300M multilingual text embedding NVIDIA NIM for retrieval version comparison; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'What is the capital of France?'): Input text

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

1. Load this skill and pin model slug `nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-llama-3-2-nemoretriever-300m-embed-v1-a557c043fc`
- Recommended: Multilingual dense retrieval and long-document question-answering retrieval — NVIDIA documents the model and Build.NVIDIA entry as optimized for multilingual and cross-lingual text question-and-answer retrieval and lists evaluation across 26 languages.
- Recommended: Embedding production component for semantic search and RAG pipelines — NGC catalog and NVIDIA NIM documentation list semantic search and Retrieval-Augmented Generation (RAG) among intended use cases for the Text Embedding NIMs and describe the NIM as a production-ready microservice.
- Avoid: Treating this package as a general text-generation (LM) service — Primary-source NIM documentation and the NeMo Retriever Embedding NIM references describe embedding endpoints and retrieval-oriented inference controls; they do not document generative-text endpoints for this NIM.
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

- Model: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim`
- Routes: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nvidia-llama-3-2-nemoretriever-300m-embed-v1-nim/SKILL.md
