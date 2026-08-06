---
name: use-forge-lightricks-ltx-2-3-sglang
description: Use exact Forge model lightricks-ltx-2-3-sglang for text, image to video, audio. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use LTX-2.3

- Model slug: `lightricks-ltx-2-3-sglang`
- Family: `lightricks-ltx-2`
- Version: `2.3-one-stage-sglang-0.5.11` (`2-3-one-stage`)
- Hierarchy: `models / general / video-generation`
- Stability: `stable`
- Default eligible: `true`
- License: `ltx-2-community-license-agreement`
- Research status: `source-linked`

## Purpose

LTX-2.3 generates video with synchronized audio from text or a starting image.

## Use this exact model when

- Use this exact `lightricks-ltx-2-3-sglang` version when the task supplies text, image and needs video, audio.
- LTX-2.3 generates video with synchronized audio from text or a starting image.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['video', 'audio'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `mode` (select; optional; choices text2video, image2video; default 'text2video'): Mode
- `prompt` (textarea; optional; default 'A cinematic wide shot of a rain-soaked city street at blue hour, slow dolly forward, realistic reflections, natural traffic ambience.'): Prompt
- `input_image` (file_upload; optional; default ''): Starting Image
- `license_acknowledgement` (checkbox; optional; default False): I accept the LTX-2 Community License and confirm this use is authorized
- `size` (select; optional; choices 768x512, 512x768; default '768x512'): Frame Size
- `negative_prompt` (textarea; optional; default ''): Negative Prompt
- `num_frames` (number; optional; bounds 9..121; default 49): Frames
- `fps` (number; optional; bounds 8..30; default 24): FPS
- `num_inference_steps` (number; optional; bounds 1..40; default 20): Inference Steps
- `guidance_scale` (slider; optional; bounds 0..20; default 3): Guidance
- `seed` (number; optional; bounds 0..2147483647; default 42): Seed

Route: `POST /v1/inference/lightricks-ltx-2`

```json
{
  "fps": "{{fps}}",
  "guidance_scale": "{{guidance_scale}}",
  "input_image": "{{input_image}}",
  "license_acknowledgement": "{{license_acknowledgement}}",
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
- `audio`

## Required workflow

1. Load this skill and pin model slug `lightricks-ltx-2-3-sglang` with version key `2-3-one-stage`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/lightricks-ltx-2` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-lightricks-ltx-2-3-4bb7928cc7`
- Recommended: Text-to-video generation with synchronized audio — The Hugging Face model card and the README blob for LTX-2.3 describe support for text-to-video and joint audio-video generation and identify the model as an audio-video DiT-based foundation model.
- Recommended: Image-conditioned video generation (image-to-video / image+text-to-video) — The Hugging Face model card and README blob list image-to-video and image+text-to-video among supported tasks and pipeline tags.
- Avoid: Unvalidated clinical, medical, or safety‑critical decision‑making — Upstream model card and README do not provide clinical validation, PHI handling guidance, or certifications for clinical use; no creator‑published clinical use approvals were found in the inspected primary sources.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/lightricks-ltx-2-3-sglang`
- Routes: `/v1/models/lightricks-ltx-2-3-sglang/inference-routes`
- Regional deployment: `/v1/models/lightricks-ltx-2-3-sglang/regional-deployment`
- Serverless handoff: `/v1/models/lightricks-ltx-2-3-sglang/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/lightricks-ltx-2-3-sglang/SKILL.md
