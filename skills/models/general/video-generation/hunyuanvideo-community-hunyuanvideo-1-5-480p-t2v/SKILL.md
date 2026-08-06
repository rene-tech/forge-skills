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

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-docs-diffusers-v0-38-0-en-api-pipelines-hunyuan-video15-0154145706`
- Recommended: Short-form text-to-video generation for rapid prototyping and social/web content — Primary upstream artifacts document text-to-video capability and lightweight video generation with consumer-GPU efficiency, supporting short-form video generation workflows.
- Recommended: Image-to-video (I2V) generation using the HunyuanVideo-1.5 I2V pipeline variant — Primary sources describe both text-to-video and image-to-video capabilities for the family and document an I2V workflow in the Diffusers pipeline documentation and upstream repository.
- Recommended: Consumer-GPU inference using published HunyuanVideo-1.5 variants (e.g., 720p example shown upstream) — Upstream documentation and the model page indicate the family is designed to run efficiently on consumer-grade GPUs and provide example generation settings (including an example using 50 inference steps).
- Avoid: Clinical, PHI-bearing, or safety-critical decision-making workflows — Evidence gap: The audited primary sources do not provide domain-specific validation, clinical disclaimers, or governance documentation for use in medical or other safety-critical contexts; no primary-source statements were found that establish clinical validation for HunyuanVideo-1.5 for such uses.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v/SKILL.md
