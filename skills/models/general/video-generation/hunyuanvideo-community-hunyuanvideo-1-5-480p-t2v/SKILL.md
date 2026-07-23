---
name: use-forge-hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v
description: Use exact Forge model hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use HunyuanVideo 1.5 480p T2V

- Model slug: `hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v`
- Family: `hunyuanvideo-community-hunyuanvideo-1-5`
- Version: `480p-t2v-diffusers` (`480p-t2v-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

HunyuanVideo 1.5 480p text-to-video generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v` version when the task supplies text and needs video.
- HunyuanVideo 1.5 480p text-to-video generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A fluffy teddy bear sits beside a compact GPU workstation while generated images appear on a monitor, gentle cinematic camera move'): Prompt
- `negative_prompt` (textarea; optional; default 'low quality, blurry, distorted, watermark, text artifacts'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 55): Seed
- `num_inference_steps` (number; optional; bounds 4..50; default 16): Steps
- `num_frames` (number; optional; bounds 17..121; default 61): Frames

Route: `POST /v1/inference/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v`

```json
{
  "fps": 15,
  "height": 480,
  "negative_prompt": "{{negative_prompt}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "width": 832
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v` with version key `480p-t2v-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v` using the declared request template.
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

- Model: `/v1/models/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v`
- Routes: `/v1/models/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v/inference-routes`
- Regional deployment: `/v1/models/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v/regional-deployment`
- Serverless handoff: `/v1/models/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v/SKILL.md
