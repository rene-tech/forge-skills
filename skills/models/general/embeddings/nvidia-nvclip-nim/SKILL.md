---
name: use-forge-nvidia-nvclip-nim
description: Use exact Forge model nvidia-nvclip-nim for text, image to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Nvidia Nvclip

- Model slug: `nvidia-nvclip-nim`
- Family: `nvidia-nvclip`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / embeddings`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

NVIDIA NVCLIP NIM for multimodal text/image embeddings; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.

## Use this exact model when

- Use this exact `nvidia-nvclip-nim` version when the task supplies text, image and needs embedding.
- NVIDIA NVCLIP NIM for multimodal text/image embeddings; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'A small red flower'): Text input
- `image_url` (text; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII='): Optional image URL or data URL

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": [
    "{{input}}"
  ],
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `nvidia-nvclip-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-nvclip-99e2d86333`
- Recommended: Multimodal semantic search and embedding-based retrieval over text and image data — NVIDIA documents NV-CLIP NIM as providing state-of-the-art embedding capabilities usable for semantic search and Retrieval Augmented Generation (RAG).
- Recommended: Zero-shot image classification (as a validated evaluation mode) — NVIDIA reports zero-shot ImageNet top-1 accuracy for a ViT-H-224 NV-CLIP model variant and lists zero-shot image classification as an application.
- Avoid: Clinical or healthcare decision support — Primary NVIDIA and upstream OpenAI sources do not provide NV-CLIP-specific clinical validation, PHI handling, or healthcare safety guidance for this exact model/runtime scope; OpenAI's CLIP model card explicitly states the model was not developed for general deployment.
- Avoid: Selecting this model for object detection as a directly exposed Forge/NIM output — Although NVIDIA documents downstream computer vision tasks in broad terms, the verified NV-CLIP NIM API evidence in scope documents only an embeddings endpoint; there is no primary-source documentation of a direct object-detection output head exposed by the NV-CLIP NIM API.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-nvclip-nim`
- Routes: `/v1/models/nvidia-nvclip-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-nvclip-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-nvclip-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nvidia-nvclip-nim/SKILL.md
