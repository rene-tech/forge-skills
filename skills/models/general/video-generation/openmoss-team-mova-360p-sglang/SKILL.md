---
name: use-forge-openmoss-team-mova-360p-sglang
description: Use exact Forge model openmoss-team-mova-360p-sglang for text, image to video, audio. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MOVA 360p

- Model slug: `openmoss-team-mova-360p-sglang`
- Family: `openmoss-team-mova`
- Version: `360p-sglang-0.5.11` (`360p`)
- Hierarchy: `models / general / video-generation`
- Stability: `stable`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

MOVA 360p generates a synchronized video-and-audio clip from a starting image and text direction.

## Use this exact model when

- Use this exact `openmoss-team-mova-360p-sglang` version when the task supplies text, image and needs video, audio.
- MOVA 360p generates a synchronized video-and-audio clip from a starting image and text direction.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['video', 'audio'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A cinematic tracking shot as the subject turns toward the camera, natural motion, realistic lighting, synchronized ambient sound.'): Prompt
- `input_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Starting Image
- `size` (select; optional; choices 640x352, 352x640; default '640x352'): Frame Size
- `negative_prompt` (textarea; optional; default ''): Negative Prompt
- `num_frames` (number; optional; bounds 9..193; default 49): Frames
- `fps` (number; optional; bounds 8..30; default 24): FPS
- `num_inference_steps` (number; optional; bounds 1..50; default 20): Inference Steps
- `guidance_scale` (slider; optional; bounds 0..20; default 5): Guidance
- `seed` (number; optional; bounds 0..2147483647; default 42): Seed

Route: `POST /v1/inference/openmoss-team-mova`

```json
{
  "fps": "{{fps}}",
  "guidance_scale": "{{guidance_scale}}",
  "input_image": "{{input_image}}",
  "mode": "image2video",
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
- `audio`

## Required workflow

1. Load this skill and pin model slug `openmoss-team-mova-360p-sglang` with version key `360p`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/openmoss-team-mova` using the declared request template.
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

- Model: `/v1/models/openmoss-team-mova-360p-sglang`
- Routes: `/v1/models/openmoss-team-mova-360p-sglang/inference-routes`
- Regional deployment: `/v1/models/openmoss-team-mova-360p-sglang/regional-deployment`
- Serverless handoff: `/v1/models/openmoss-team-mova-360p-sglang/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/openmoss-team-mova-360p-sglang/SKILL.md
