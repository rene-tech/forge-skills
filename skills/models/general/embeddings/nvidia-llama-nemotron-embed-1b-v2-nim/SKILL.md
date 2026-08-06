---
name: use-forge-nvidia-llama-nemotron-embed-1b-v2-nim
description: Use exact Forge model nvidia-llama-nemotron-embed-1b-v2-nim for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama Nemotron Embed 1B v2

- Model slug: `nvidia-llama-nemotron-embed-1b-v2-nim`
- Family: `nvidia-llama-nemotron-embed-1b-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / embeddings`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-open-model-license; llama-3.2-community-license`
- Research status: `source-linked`

## Purpose

1B NVIDIA NeMo Retriever text embedding NIM for semantic retrieval/RAG; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.

## Use this exact model when

- Use this exact `nvidia-llama-nemotron-embed-1b-v2-nim` version when the task supplies text and needs embedding.
- 1B NVIDIA NeMo Retriever text embedding NIM for semantic retrieval/RAG; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave4.
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

1. Load this skill and pin model slug `nvidia-llama-nemotron-embed-1b-v2-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-llama-nemotron-embed-1b-v2-e33887bdd4`
- Recommended: Multilingual semantic/dense retrieval for question-answering over large text corpora — Build.NVIDIA model card and the NIM reference describe intended use for multilingual dense retrieval and long-document QA support across 26 languages using 2048-dimensional embeddings produced by a bi-encoder.
- Recommended: Embedding generation for retrieval-augmented generation (RAG) backends and multilingual/cross-lingual retrieval pipelines — Primary sources state the model is a bi-encoder trained with contrastive learning producing 2048-dimensional embeddings intended for indexing and similarity search; Hugging Face and Build.NVIDIA list RAG/retrieval scenarios as intended uses.
- Avoid: Using the text-only checkpoint for image or multimodal embedding tasks — Primary sources document multimodal image support on separate NeMo Retriever/embedded VL variants and the text-only checkpoint is described as text-only; do not assume image inputs are supported by this text-only checkpoint.
- Avoid: Treating embeddings as calibrated probabilistic confidences or final decision outputs without downstream validation — Primary sources describe embeddings as retrieval features produced by a contrastive-trained bi-encoder and do not provide calibration semantics or recommended decision thresholds.
- Avoid: Clinical or PHI-sensitive decision making without documented PHI handling or clinical validation — Primary sources do not publish PHI handling or clinical/regulatory validation guidance tied to this checkpoint (see safety evidence gap).
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

- Model: `/v1/models/nvidia-llama-nemotron-embed-1b-v2-nim`
- Routes: `/v1/models/nvidia-llama-nemotron-embed-1b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-nemotron-embed-1b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-nemotron-embed-1b-v2-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nvidia-llama-nemotron-embed-1b-v2-nim/SKILL.md
