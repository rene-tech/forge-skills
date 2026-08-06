---
name: use-forge-wan-ai-wan2-2-t2v-a14b
description: Use exact Forge model wan-ai-wan2-2-t2v-a14b for text to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Wan2.2 T2V A14B

- Model slug: `wan-ai-wan2-2-t2v-a14b`
- Family: `wan-ai-wan2-2`
- Version: `a14b-diffusers` (`a14b-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Wan2.2 T2V A14B text-to-video generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `wan-ai-wan2-2-t2v-a14b` version when the task supplies text and needs video.
- Wan2.2 T2V A14B text-to-video generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A cinematic product video of a GPU cluster room powering up, cables and LEDs moving subtly, clean realistic lighting'): Prompt
- `negative_prompt` (textarea; optional; default 'overexposed, static, blurry, subtitles, watermark, low quality, distorted'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 23): Seed
- `num_inference_steps` (number; optional; bounds 10..50; default 20): Steps
- `guidance_scale` (number; optional; bounds 1..8; default 5): Guidance
- `num_frames` (number; optional; bounds 17..121; default 49): Frames

Route: `POST /v1/inference/wan-ai-wan2-2-t2v-a14b`

```json
{
  "fps": 24,
  "guidance_scale": "{{guidance_scale}}",
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

1. Load this skill and pin model slug `wan-ai-wan2-2-t2v-a14b` with version key `a14b-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/wan-ai-wan2-2-t2v-a14b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-wan-video-wan2-2-4460f5dc2a`
- Recommended: Prepare inputs for Wan2.2 animate workflows using the repository's animate preprocessing scripts and guidance (animation and replacement modes). — The repository provides an animate preprocessing user guide documenting generation modes, required files, parameters, and example invocations, and ships preprocessing scripts and an example tree showing flags and sample paths.
- Avoid: Assuming the repository code license (Apache-2.0) also licenses checkpoint model weights or using model weights without confirming an explicit model-weights license. — Evidence gap: the research did not find an explicit model-weights license statement for a14b-diffusers in the inspected primary repository files; repository LICENSE.txt documents the code license but does not itself establish a separate model-weights license for a named checkpoint.
- Avoid: Deploying a14b-diffusers at scale or assuming specific single-GPU VRAM requirements without checkpoint-scoped verification. — Evidence gap: the inspected primary repository files provide preprocessing examples and model metadata but do not include authoritative per-checkpoint numeric VRAM or runtime requirements for a14b-diffusers.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/wan-ai-wan2-2-t2v-a14b`
- Routes: `/v1/models/wan-ai-wan2-2-t2v-a14b/inference-routes`
- Regional deployment: `/v1/models/wan-ai-wan2-2-t2v-a14b/regional-deployment`
- Serverless handoff: `/v1/models/wan-ai-wan2-2-t2v-a14b/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/wan-ai-wan2-2-t2v-a14b/SKILL.md
