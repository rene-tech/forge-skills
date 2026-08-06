---
name: use-forge-genmo-mochi-1-preview
description: Use exact Forge model genmo-mochi-1-preview for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Mochi 1 Preview

- Model slug: `genmo-mochi-1-preview`
- Family: `genmo-mochi`
- Version: `preview-bf16-diffusers` (`preview-bf16-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Mochi 1 Preview text-to-video generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `genmo-mochi-1-preview` version when the task supplies text and needs video.
- Mochi 1 Preview text-to-video generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A cinematic slow pan across a dense rack of GPU servers, status lights reflecting on brushed metal, smooth realistic motion'): Prompt
- `seed` (number; optional; bounds 0..999999; default 33): Seed
- `num_inference_steps` (number; optional; bounds 4..64; default 16): Steps
- `guidance_scale` (number; optional; bounds 1..10; default 4.5): Guidance
- `num_frames` (number; optional; bounds 25..85; default 49): Frames

Route: `POST /v1/inference/genmo-mochi-1-preview`

```json
{
  "fps": 30,
  "guidance_scale": "{{guidance_scale}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `genmo-mochi-1-preview` with version key `preview-bf16-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/genmo-mochi-1-preview` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-genmoai-mochi-e002a7537d`
- Recommended: Text-to-video generation (research and experimentation) with text prompts — The Hugging Face model page and the Diffusers Mochi pipeline documentation describe Mochi 1 as a video-generation model that encodes text prompts with a single T5-XXL encoder and is intended for text-conditioned video generation experiments.
- Recommended: Research & development of text-conditioned video inference harnesses (integration with Diffusers) — The Genmo repository README and Diffusers documentation provide code examples and pipeline integration points suitable for R&D and controlled experimentation using the checkpoint.
- Avoid: Commercial deployment without organizational safety protocols and review — The named commit README for the checkpoint states steps have been taken to limit NSFW content but explicitly advises organizations to implement additional safety protocols before commercial deployment.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/genmo-mochi-1-preview`
- Routes: `/v1/models/genmo-mochi-1-preview/inference-routes`
- Regional deployment: `/v1/models/genmo-mochi-1-preview/regional-deployment`
- Serverless handoff: `/v1/models/genmo-mochi-1-preview/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/genmo-mochi-1-preview/SKILL.md
