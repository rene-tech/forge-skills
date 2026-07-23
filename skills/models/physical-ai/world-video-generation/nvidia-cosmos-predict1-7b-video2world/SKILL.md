---
name: use-forge-nvidia-cosmos-predict1-7b-video2world
description: Use exact Forge model nvidia-cosmos-predict1-7b-video2world for text, image, video to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Predict1 7B Video2World

- Model slug: `nvidia-cosmos-predict1-7b-video2world`
- Family: `nvidia-cosmos-predict1-7b-video2world`
- Version: `1.0.0` (`1-0-0`)
- Hierarchy: `models / physical-ai / world-video-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-ai-foundation-models-community`
- Research status: `source-linked`

## Purpose

Cosmos Predict1 NIM for image/video-conditioned world generation.

## Use this exact model when

- Use this exact `nvidia-cosmos-predict1-7b-video2world` version when the task supplies text, image, video and needs video.
- Cosmos Predict1 NIM for image/video-conditioned world generation.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'video'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Continue this driving scene as a rainy evening sequence, preserving road layout, vehicle motion, and camera perspective.'): Prompt
- `video` (text; optional; default 'https://assets.ngc.nvidia.com/products/api-catalog/cosmos/ar_result_default_robot.mp4'): Video URL or base64 MP4
- `negative_prompt` (textarea; optional; default 'blurry, low quality, artifacts, people'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 42): Seed

Route: `POST /v1/inference/nvidia-cosmos-predict1-7b-video2world`

```json
{
  "model": "{{model_slug}}",
  "negative_prompt": "{{negative_prompt}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "video": "{{video}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-predict1-7b-video2world` with version key `1-0-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-predict1-7b-video2world` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-predict1-7b-video2world`
- Routes: `/v1/models/nvidia-cosmos-predict1-7b-video2world/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-predict1-7b-video2world/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-predict1-7b-video2world/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos-predict1-7b-video2world/SKILL.md
