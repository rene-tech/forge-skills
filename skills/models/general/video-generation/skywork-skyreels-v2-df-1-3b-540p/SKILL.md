---
name: use-forge-skywork-skyreels-v2-df-1-3b-540p
description: Use exact Forge model skywork-skyreels-v2-df-1-3b-540p for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use SkyReels-V2 DF 1.3B 540p

- Model slug: `skywork-skyreels-v2-df-1-3b-540p`
- Family: `skywork-skyreels-v2`
- Version: `df-1-3b-540p-diffusers` (`df-1-3b-540p-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SkyReels-V2 diffusion-forcing text-to-video generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `skywork-skyreels-v2-df-1-3b-540p` version when the task supplies text and needs video.
- SkyReels-V2 diffusion-forcing text-to-video generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A cat and a dog inspect a compact GPU server in a cozy lab, smooth film-like motion, natural light'): Prompt
- `negative_prompt` (textarea; optional; default 'low quality, blurry, flicker, watermark, distorted anatomy'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 77): Seed
- `num_inference_steps` (number; optional; bounds 4..50; default 20): Steps
- `guidance_scale` (number; optional; bounds 1..10; default 6): Guidance
- `num_frames` (number; optional; bounds 25..121; default 97): Frames

Route: `POST /v1/inference/skywork-skyreels-v2-df-1-3b-540p`

```json
{
  "addnoise_condition": 20,
  "ar_step": 5,
  "base_num_frames": "{{num_frames}}",
  "causal_block_size": 5,
  "fps": 24,
  "guidance_scale": "{{guidance_scale}}",
  "height": 544,
  "negative_prompt": "{{negative_prompt}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "width": 960
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `skywork-skyreels-v2-df-1-3b-540p` with version key `df-1-3b-540p-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/skywork-skyreels-v2-df-1-3b-540p` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/skywork-skyreels-v2-df-1-3b-540p`
- Routes: `/v1/models/skywork-skyreels-v2-df-1-3b-540p/inference-routes`
- Regional deployment: `/v1/models/skywork-skyreels-v2-df-1-3b-540p/regional-deployment`
- Serverless handoff: `/v1/models/skywork-skyreels-v2-df-1-3b-540p/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/skywork-skyreels-v2-df-1-3b-540p/SKILL.md
