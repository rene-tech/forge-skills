---
name: use-forge-wan-ai-wan2-2-ti2v-5b-sglang
description: Use exact Forge model wan-ai-wan2-2-ti2v-5b-sglang for text, image to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Wan2.2 TI2V 5B

- Model slug: `wan-ai-wan2-2-ti2v-5b-sglang`
- Family: `wan-ai-wan2-2-ti2v`
- Version: `5b-diffusers-sglang-0.5.11` (`5b`)
- Hierarchy: `models / general / video-generation`
- Stability: `stable`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Wan2.2 TI2V 5B is the compact Apache-2.0 Wan2.2 checkpoint for both text-to-video and image-to-video generation at 1280x704 or portrait orientation.

## Use this exact model when

- Use this exact `wan-ai-wan2-2-ti2v-5b-sglang` version when the task supplies text, image and needs video.
- Wan2.2 TI2V 5B is the compact Apache-2.0 Wan2.2 checkpoint for both text-to-video and image-to-video generation at 1280x704 or portrait orientation.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['video'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `mode` (select; optional; choices text2video, image2video; default 'text2video'): Mode
- `prompt` (textarea; optional; default 'A cinematic aerial shot following a vintage train through a misty mountain valley, volumetric morning light, realistic motion.'): Prompt
- `input_image` (file_upload; optional; default ''): Starting Image
- `size` (select; optional; choices 1280x704, 704x1280; default '1280x704'): Frame Size
- `negative_prompt` (textarea; optional; default ''): Negative Prompt
- `num_frames` (number; optional; bounds 9..121; default 49): Frames
- `fps` (number; optional; bounds 8..30; default 24): FPS
- `num_inference_steps` (number; optional; bounds 1..50; default 20): Inference Steps
- `guidance_scale` (slider; optional; bounds 0..20; default 5): Guidance
- `seed` (number; optional; bounds 0..2147483647; default 42): Seed

Route: `POST /v1/inference/wan-ai-wan2-2-ti2v`

```json
{
  "fps": "{{fps}}",
  "guidance_scale": "{{guidance_scale}}",
  "input_image": "{{input_image}}",
  "mode": "{{mode}}",
  "negative_prompt": "{{negative_prompt}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "size": "{{size}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `wan-ai-wan2-2-ti2v-5b-sglang` with version key `5b`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/wan-ai-wan2-2-ti2v` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/wan-ai-wan2-2-ti2v-5b-sglang`
- Routes: `/v1/models/wan-ai-wan2-2-ti2v-5b-sglang/inference-routes`
- Regional deployment: `/v1/models/wan-ai-wan2-2-ti2v-5b-sglang/regional-deployment`
- Serverless handoff: `/v1/models/wan-ai-wan2-2-ti2v-5b-sglang/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/wan-ai-wan2-2-ti2v-5b-sglang/SKILL.md
