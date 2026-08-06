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

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-lightricks-ltx-video-b0012664eb`
- Recommended: Text-to-video generation of short videos (creative content) using the upstream checkpoint — Upstream model card and README identify the pipeline and examples as text-to-video and provide prompts and example generation parameters for short video synthesis using the named checkpoint variants.
- Recommended: Image+text-conditioned video generation (image-to-video / multi-keyframe conditioning) using the upstream trainer/configured pipelines — Trainer configuration and repository README document an 'images' parameter and image-conditioned generation examples; these are provided as upstream trainer/repo configuration evidence for image+text conditioning with named checkpoints.
- Recommended: Video extension (forward/backward extension) and video-to-video transformations within documented endpoint limits (upstream API docs describe extend behavior) — Upstream API documentation for the video-extend endpoint describes using input context frames to generate additional frames and preserving input resolution; it documents parameters and limits for the extend operation.
- Avoid: Generating harmful or disallowed content (defamation, impersonation, PII misuse, sexual content, child sexual abuse material, trafficking, biometric ID, etc.) — Upstream RAIL‑M / Open Weights license and acceptable-use policy explicitly prohibit many harmful and disallowed uses and impose distribution/use restrictions.
- Avoid: Clinical/medical decision-making or other regulated professional applications without expert review — Upstream acceptable-use guidance and license require disclosure and caution; the model and license do not assert clinical-grade validation.
- Avoid: Domain-specific tasks (e.g., multi-view synthesis, fine-grained editing) without downstream validation — Upstream paper and documentation note limited testing/validation for domain-specialized adaptation; such uses require downstream task-specific validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/lightricks-ltx-video/SKILL.md
