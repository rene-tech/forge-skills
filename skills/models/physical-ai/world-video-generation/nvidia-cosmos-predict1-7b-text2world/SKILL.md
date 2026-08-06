---
name: use-forge-nvidia-cosmos-predict1-7b-text2world
description: Use exact Forge model nvidia-cosmos-predict1-7b-text2world for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Predict1 7B Text2World

- Model slug: `nvidia-cosmos-predict1-7b-text2world`
- Family: `nvidia-cosmos-predict1-7b-text2world`
- Version: `1.0.0` (`1-0-0`)
- Hierarchy: `models / physical-ai / world-video-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-ai-foundation-models-community`
- Research status: `source-linked`

## Purpose

Cosmos Predict1 NIM for text-to-world video generation.

## Use this exact model when

- Use this exact `nvidia-cosmos-predict1-7b-text2world` version when the task supplies text and needs video.
- Cosmos Predict1 NIM for text-to-world video generation.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'first person dashcam view from a car driving down a two lane suburban street on a rainy day, wet road, puddles, windshield wipers'): Prompt
- `seed` (number; optional; bounds 0..999999; default 4): Seed

Route: `POST /v1/inference/nvidia-cosmos-predict1-7b-text2world`

```json
{
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-predict1-7b-text2world` with version key `1-0-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-predict1-7b-text2world` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-cosmos-latest-quickstart-guide-html-nvidia-cosmos-predict1-7b-text2world-c88f94644e`
- Recommended: Text-to-world video generation (short physics-aware simulation clips) using the 7B Text2World diffusion checkpoint — Official model pages, the Predict1 model matrix, NGC container listing, and repository examples describe the checkpoint as producing dynamic videos from text and optional visual conditioning and provide inference/deployment guidance for Text2World workflows.
- Recommended: Multi-view/trajectory-conditioned generation for research workflows (requires downstream revalidation on target datasets) — Repository contains a multiview inference example demonstrating inference format and conditioning patterns; Hugging Face model pages and repo describe multiview/trajectory-conditioned sample variants.
- Recommended: Deploying the NIM/container for GPU-accelerated inference of Text2World workflows — NGC container listing, Predict1 model matrix, and NIM release notes identify an NIM container image and provide deployment/runtime guidance for the 7B Text2World variant.
- Avoid: Selecting this checkpoint as a general-purpose text-only LLM for natural-language tasks — Primary evidence describes the checkpoint and NIM as diffusion-based visual/world-generation models (video/image generation) with a visual/world output head rather than a general-purpose text LLM.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-predict1-7b-text2world`
- Routes: `/v1/models/nvidia-cosmos-predict1-7b-text2world/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-predict1-7b-text2world/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-predict1-7b-text2world/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos-predict1-7b-text2world/SKILL.md
