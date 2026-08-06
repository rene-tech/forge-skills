---
name: use-forge-nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim
description: Use exact Forge model nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.2 NeMo Retriever 300M Embed v2

- Model slug: `nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim`
- Family: `nvidia-llama-3-2-nemoretriever-300m-embed-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / embeddings`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-community-model-license; llama-3.2-community-license`
- Research status: `source-linked`

## Purpose

Multilingual, cross-lingual text embedding NVIDIA NIM for long-document QA retrieval; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.

## Use this exact model when

- Use this exact `nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim` version when the task supplies text and needs embedding.
- Multilingual, cross-lingual text embedding NVIDIA NIM for long-document QA retrieval; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.
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

1. Load this skill and pin model slug `nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-llama-3-2-nemoretriever-300m-embed-v2-f53275e56f`
- Recommended: Multilingual / cross-lingual dense retrieval for question-answering over large text corpora — The official NIM model reference and NGC catalog describe the v2 NeMo Retriever embedding model as optimized for multilingual and cross-lingual QA retrieval and list evaluation on 26 languages; the model is published as a retrieval embedding NIM suitable for extracting per-input embeddings.
- Recommended: Long-document retrieval via chunking/truncation up to the model-supported context length — NeMo support matrices and the model reference document model support for inputs up to 8192 tokens for the 300M model and the NIM inference API exposes truncate controls enabling chunking/truncation workflows.
- Recommended: Extracting per-input embedding vectors (float or supported encodings) for downstream retrieval pipelines — NeMo Retriever REST reference documents an embeddings endpoint returning an array of embedding objects with embedding_type and encoding_format options; support matrices list embedding dimension 2048 and supported embedding types.
- Avoid: Submitting inputs with the wrong input_type (mismatched 'query' vs 'passage') for retrieval — The inference API reference documents that input_type must be set (query|passage) and that using the wrong type reduces retrieval accuracy (mode-sensitive bi-encoder semantics).
- Avoid: Running the 300M embedding NIM on GPU clusters configured with Multi-instance GPU (MIG) mode — NeMo getting-started and support documentation state that GPU clusters with GPUs in MIG mode are not supported for this NIM (MIG unsupported guidance).
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

- Model: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim`
- Routes: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nvidia-llama-3-2-nemoretriever-300m-embed-v2-nim/SKILL.md
