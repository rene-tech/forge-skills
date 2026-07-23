---
name: use-forge-lightricks-ltx-video
description: Use exact Forge model lightricks-ltx-video for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use LTX-Video

- Model slug: `lightricks-ltx-video`
- Family: `lightricks-ltx-video`
- Version: `diffusers` (`diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `openrail`
- Research status: `source-linked`

## Purpose

LTX-Video text-to-video generation through the reusable Forge Diffusers media wrapper.

## Use this exact model when

- Use this exact `lightricks-ltx-video` version when the task supplies text and needs video.
- LTX-Video text-to-video generation through the reusable Forge Diffusers media wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A close-up product shot of a compact AI workstation powering on, indicator lights pulsing, smooth camera push-in, realistic motion'): Prompt
- `negative_prompt` (textarea; optional; default 'worst quality, inconsistent motion, blurry, jittery, distorted'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 11): Seed
- `num_inference_steps` (number; optional; bounds 4..50; default 20): Steps
- `guidance_scale` (number; optional; bounds 1..10; default 5): Guidance
- `width` (number; optional; bounds 320..1280; default 768): Width
- `height` (number; optional; bounds 320..768; default 512): Height
- `num_frames` (number; optional; bounds 17..161; default 49): Frames
- `decode_timestep` (number; optional; bounds 0..0.1; default 0.03): Decode Timestep
- `decode_noise_scale` (number; optional; bounds 0..0.1; default 0.025): Decode Noise

Route: `POST /v1/inference/lightricks-ltx-video`

```json
{
  "decode_noise_scale": "{{decode_noise_scale}}",
  "decode_timestep": "{{decode_timestep}}",
  "fps": 24,
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "negative_prompt": "{{negative_prompt}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "width": "{{width}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `lightricks-ltx-video` with version key `diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/lightricks-ltx-video` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/lightricks-ltx-video`
- Routes: `/v1/models/lightricks-ltx-video/inference-routes`
- Regional deployment: `/v1/models/lightricks-ltx-video/regional-deployment`
- Serverless handoff: `/v1/models/lightricks-ltx-video/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/lightricks-ltx-video/SKILL.md
