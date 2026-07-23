---
name: use-forge-zai-org-cogvideox-2b
description: Use exact Forge model zai-org-cogvideox-2b for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use CogVideoX 2B

- Model slug: `zai-org-cogvideox-2b`
- Family: `zai-org-cogvideox`
- Version: `2b-diffusers` (`2b-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

CogVideoX 2B text-to-video generation through the reusable Forge Diffusers media wrapper.

## Use this exact model when

- Use this exact `zai-org-cogvideox-2b` version when the task supplies text and needs video.
- CogVideoX 2B text-to-video generation through the reusable Forge Diffusers media wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A detailed wooden toy ship gliding over a plush blue carpet like ocean waves, cinematic motion, soft indoor light'): Prompt
- `seed` (number; optional; bounds 0..999999; default 42): Seed
- `num_inference_steps` (number; optional; bounds 4..50; default 20): Steps
- `guidance_scale` (number; optional; bounds 1..10; default 6): Guidance

Route: `POST /v1/inference/zai-org-cogvideox-2b`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `zai-org-cogvideox-2b` with version key `2b-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/zai-org-cogvideox-2b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 226.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/zai-org-cogvideox-2b`
- Routes: `/v1/models/zai-org-cogvideox-2b/inference-routes`
- Regional deployment: `/v1/models/zai-org-cogvideox-2b/regional-deployment`
- Serverless handoff: `/v1/models/zai-org-cogvideox-2b/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/zai-org-cogvideox-2b/SKILL.md
