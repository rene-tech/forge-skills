---
name: use-forge-stabilityai-stable-diffusion-xl-base-1-0
description: Use exact Forge model stabilityai-stable-diffusion-xl-base-1-0 for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Stable Diffusion XL Base 1.0

- Model slug: `stabilityai-stable-diffusion-xl-base-1-0`
- Family: `stabilityai-stable-diffusion-xl`
- Version: `base-1.0-diffusers` (`base-1-0-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `openrail++`
- Research status: `source-linked`

## Purpose

Stable Diffusion XL Base 1.0 text-to-image generation through the Forge Diffusers media wrapper.

## Use this exact model when

- Use this exact `stabilityai-stable-diffusion-xl-base-1-0` version when the task supplies text and needs image.
- Stable Diffusion XL Base 1.0 text-to-image generation through the Forge Diffusers media wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A clean product photograph of a high-end GPU server in a bright lab, precise lighting, realistic reflections, sharp details'): Prompt
- `negative_prompt` (textarea; optional; default 'low quality, blurry, warped text, distorted geometry'): Negative Prompt
- `seed` (number; optional; bounds 0..999999; default 101): Seed
- `num_inference_steps` (number; optional; bounds 10..60; default 25): Steps
- `guidance_scale` (number; optional; bounds 1..15; default 7.5): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 512..1536; default 1024): Height

Route: `POST /v1/inference/stabilityai-stable-diffusion-xl-base-1-0`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "negative_prompt": "{{negative_prompt}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "width": "{{width}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `stabilityai-stable-diffusion-xl-base-1-0` with version key `base-1-0-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/stabilityai-stable-diffusion-xl-base-1-0` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-stabilityai-stable-diffusion-xl-base-1-0-3c44be280a`
- Recommended: High-resolution text-to-image generation using the StableDiffusionXLPipeline with this checkpoint's artifacts — model_index.json enumerates StableDiffusionXLPipeline as the pipeline class and lists UNet ("diffusers","UNet2DConditionModel") and VAE ("diffusers","AutoencoderKL") components; unet/config.json specifies UNet sample_size = 128 and vae_decoder/config.json specifies VAE sample_size = 1024 and scaling_factor = 0.13025. Diffusers image_processor.py documents VaeImageProcessor defaults including vae_scale_factor = 8 and do_resize = True; the combination of UNet sample_size (unet/config.json) and VAE/image-processor vae_scale_factor (image_processor.py) are the upstream-declared numeric constants relevant to default sample-size/resolution behavior.
- Avoid: Avoid assuming there are no license obligations or usage terms when deploying this checkpoint — The repository README lists the license name "CreativeML Open RAIL++-M License" and the repository LICENSE.md contains license-grant language (perpetual, worldwide, non-exclusive, royalty-free patent and copyright licenses); implementers must consult LICENSE.md for obligations rather than assuming no restrictions.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 77.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/stabilityai-stable-diffusion-xl-base-1-0`
- Routes: `/v1/models/stabilityai-stable-diffusion-xl-base-1-0/inference-routes`
- Regional deployment: `/v1/models/stabilityai-stable-diffusion-xl-base-1-0/regional-deployment`
- Serverless handoff: `/v1/models/stabilityai-stable-diffusion-xl-base-1-0/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/stabilityai-stable-diffusion-xl-base-1-0/SKILL.md
