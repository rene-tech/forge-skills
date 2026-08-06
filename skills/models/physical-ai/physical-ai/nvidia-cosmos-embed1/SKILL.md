---
name: use-forge-nvidia-cosmos-embed1
description: Use exact Forge model nvidia-cosmos-embed1 for text, video to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Embed1

- Model slug: `nvidia-cosmos-embed1`
- Family: `nvidia-cosmos-embed1`
- Version: `1.1.0` (`1-1-0`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-open-model-license`
- Research status: `source-linked`

## Purpose

Digest-pinned onboarding manifest for the official Cosmos Embed1 1.1.0 NIM.

## Use this exact model when

- Use this exact `nvidia-cosmos-embed1` version when the task supplies text, video and needs embedding.
- Digest-pinned onboarding manifest for the official Cosmos Embed1 1.1.0 NIM.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'video'] → ['embedding'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'A rainy dashcam clip with wet road reflections and windshield wipers.'): Text, video URL, or data URI
- `request_type` (select; optional; choices query, bulk_text, bulk_video; default 'query'): Request Type

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": "{{input}}",
  "model": "{{model_slug}}",
  "request_type": "{{request_type}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-embed1` with version key `1-1-0`.
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
- Research key: `docs-nvidia-com-nim-cosmos-embed1-latest-quickstart-guide-html-9090228f0f`
- Recommended: Text-to-video retrieval (semantic search) using embeddings — NIM introduction, VSS model doc, NGC/TAO listings and the NIM API reference describe Cosmos‑Embed1 as producing aligned embeddings for text and short‑form videos enabling text‑to‑video retrieval and semantic search. The NIM serves embeddings via POST /v1/embeddings.
- Recommended: Video-to-video retrieval and similarity matching — NGC TAO model listing and VSS documentation list inverse video search and video‑to‑video search as intended applications, describing a unified embedding space for videos and text.
- Recommended: Semantic deduplication, content clustering, and k‑NN downstream tasks — NGC catalog, NIM introduction and TAO documentation list semantic deduplication, clustering, and k‑NN style downstream usage as supported downstream applications for embeddings.
- Avoid: Use as a generative language model for token‑level text generation — Primary NIM docs and API describe Cosmos‑Embed1 as a joint video‑text embedder returning embedding vectors via POST /v1/embeddings; there is no primary‑source evidence in the inspected NIM docs that the model exposes token‑level generation/completion capability.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-embed1`
- Routes: `/v1/models/nvidia-cosmos-embed1/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-embed1/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-embed1/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-embed1/SKILL.md
