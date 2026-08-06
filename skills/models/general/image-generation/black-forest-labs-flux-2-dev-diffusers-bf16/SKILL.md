---
name: use-forge-black-forest-labs-flux-2-dev-diffusers-bf16
description: Use exact Forge model black-forest-labs-flux-2-dev-diffusers-bf16 for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.2 Dev

- Model slug: `black-forest-labs-flux-2-dev-diffusers-bf16`
- Family: `black-forest-labs-flux-2-dev`
- Version: `diffusers-bf16-pytorch2.9.1-cuda12.8-v1` (`diffusers-bf16`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `flux-non-commercial-license`
- Research status: `source-linked`

## Purpose

FLUX.2 Dev is a gated, non-commercial Black Forest Labs image generation and editing model served through a Forge-owned Diffusers Flux2Pipeline BF16 wrapper.

## Use this exact model when

- Use this exact `black-forest-labs-flux-2-dev-diffusers-bf16` version when the task supplies text, image and needs image.
- FLUX.2 Dev is a gated, non-commercial Black Forest Labs image generation and editing model served through a Forge-owned Diffusers Flux2Pipeline BF16 wrapper.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A photorealistic editorial product image of a compact GPU workstation on a clean lab bench, realistic materials, softbox lighting, sharp details, no text'): Prompt
- `input_image` (file_upload; optional; default ''): Input image
- `aspect_ratio` (select; optional; choices 1:1, 4:3, 3:2, 16:9, 3:4, 2:3, 9:16; default '1:1'): Aspect ratio
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..80; default 28): Steps
- `guidance_scale` (number; optional; bounds 0..20; default 4): Guidance
- `width` (number; optional; bounds 256..1536; default 1024): Width
- `height` (number; optional; bounds 256..1536; default 1024): Height
- `caption_upsample_temperature` (number; optional; bounds 0..2; default 0.2): Caption temperature

Route: `POST /v1/inference/black-forest-labs-flux-2-dev-diffusers-bf16`

```json
{
  "aspect_ratio": "{{aspect_ratio}}",
  "caption_upsample_temperature": "{{caption_upsample_temperature}}",
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "image": "{{input_image}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}",
  "width": "{{width}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `black-forest-labs-flux-2-dev-diffusers-bf16` with version key `diffusers-bf16`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-2-dev-diffusers-bf16` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-black-forest-labs-flux-2-dev-1e027ba417`
- Recommended: Text-to-image generation using the Diffusers integration — Upstream model card and repository documentation state FLUX.2 [dev] can generate images from text prompts and provide example Diffusers-based pipeline code indicating Diffusers usage and torch.bfloat16 for the VAE in example wrappers.
- Avoid: Commercial training, fine-tuning, or distillation to produce a competing model — The FLUX Non-Commercial License explicitly restricts training/fine-tuning/distillation that would produce a competing FLUX model and limits model use to non-commercial purposes without a separate commercial license.
- Avoid: Commercial deployment or API provisioning of the FLUX.2-dev weights without a commercial license from Black Forest Labs — Upstream license and model-licenses documentation require a separate commercial license for commercial use; modal and deployment restrictions are stated in the FLUX Non-Commercial License.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-2-dev-diffusers-bf16`
- Routes: `/v1/models/black-forest-labs-flux-2-dev-diffusers-bf16/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-2-dev-diffusers-bf16/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-2-dev-diffusers-bf16/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-2-dev-diffusers-bf16/SKILL.md
