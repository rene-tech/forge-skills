---
name: use-forge-black-forest-labs-flux-2-klein-base-4b-diffusers
description: Use exact Forge model black-forest-labs-flux-2-klein-base-4b-diffusers for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.2 Klein 4B Base

- Model slug: `black-forest-labs-flux-2-klein-base-4b-diffusers`
- Family: `black-forest-labs-flux-2-klein-4b`
- Version: `base-4b-diffusers-cuda12.8-v1` (`base-4b-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Higher-quality FLUX.2 Klein 4B Base variant running in a Forge-owned Diffusers container.

## Use this exact model when

- Use this exact `black-forest-labs-flux-2-klein-base-4b-diffusers` version when the task supplies text, image and needs image.
- Higher-quality FLUX.2 Klein 4B Base variant running in a Forge-owned Diffusers container.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A photorealistic editorial image of a compact GPU workstation in a clean studio, natural perspective, softbox lighting, realistic materials, sharp details, no text'): Prompt
- `image` (file_upload; optional): Input image
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..100; default 50): Steps
- `guidance_scale` (number; optional; bounds 1..8; default 4): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 512..1536; default 1024): Height

Route: `POST /v1/inference/black-forest-labs-flux-2-klein-base-4b-diffusers`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "image": "{{image}}",
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

1. Load this skill and pin model slug `black-forest-labs-flux-2-klein-base-4b-diffusers` with version key `base-4b-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-2-klein-base-4b-diffusers` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-2-klein-base-4b-diffusers`
- Routes: `/v1/models/black-forest-labs-flux-2-klein-base-4b-diffusers/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-2-klein-base-4b-diffusers/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-2-klein-base-4b-diffusers/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-2-klein-base-4b-diffusers/SKILL.md
