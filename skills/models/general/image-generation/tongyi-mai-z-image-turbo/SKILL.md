---
name: use-forge-tongyi-mai-z-image-turbo
description: Use exact Forge model tongyi-mai-z-image-turbo for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Z-Image Turbo

- Model slug: `tongyi-mai-z-image-turbo`
- Family: `tongyi-mai-z-image`
- Version: `turbo-diffusers` (`turbo-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Z-Image Turbo text-to-image generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `tongyi-mai-z-image-turbo` version when the task supplies text and needs image.
- Z-Image Turbo text-to-image generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A bilingual poster for a cloud GPU image generation platform, crisp product typography, photorealistic workstation, English and Chinese text, studio lighting'): Prompt
- `seed` (number; optional; bounds 0..999999; default 42): Seed
- `steps` (number; optional; bounds 4..20; default 8): Steps
- `guidance_scale` (number; optional; bounds 0..6; default 0): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 512..1536; default 1024): Height

Route: `POST /v1/inference/tongyi-mai-z-image-turbo`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "max_sequence_length": 512,
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}",
  "width": "{{width}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `tongyi-mai-z-image-turbo` with version key `turbo-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/tongyi-mai-z-image-turbo` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-docs-diffusers-v0-38-0-en-api-pipelines-z-image-5995c81381`
- Recommended: Text-to-image generation (photorealistic outputs) — Model README and commit metadata describe Z-Image-Turbo as a distilled variant optimized for photorealistic generation and list the pipeline tag as text-to-image; the arXiv paper describes Z-Image as an image-generation foundation model built on S3-DiT.
- Recommended: Image-to-image editing / img2img workflows (where supported by pipeline instantiation) — Model README and model_index.json enumerate multiple Z-Image pipeline classes and the model repository describes generation and editing task scope; the model_index.json declares a pipeline of class "ZImagePipeline" and the model README describes generation and editing capabilities for the family.
- Recommended: Inpainting / mask-guided editing (pipeline variants within the Z-Image family) — The README and model-index describe inpainting/editing variants in the Z-Image family and the model repository exposes pipeline classes tied to editing tasks.
- Avoid: Clinical or medical diagnostic use — No primary-source clinical validation, regulatory claims, or PHI-handling guidance for this checkpoint are present in the inspected upstream artifacts; the model repository and paper do not provide documented clinical validation materials for Turbo.
- Avoid: Safety-/compliance-critical use requiring built-in NSFW flags or calibrated safety/confidence outputs — The examined primary upstream artifacts do not document emitted NSFW scores, calibrated confidence outputs, or built-in safety flags for the checkpoint; no upstream evidence shows the checkpoint provides such signals.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/tongyi-mai-z-image-turbo`
- Routes: `/v1/models/tongyi-mai-z-image-turbo/inference-routes`
- Regional deployment: `/v1/models/tongyi-mai-z-image-turbo/regional-deployment`
- Serverless handoff: `/v1/models/tongyi-mai-z-image-turbo/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/tongyi-mai-z-image-turbo/SKILL.md
