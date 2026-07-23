---
name: use-forge-pixart-alpha-pixart-sigma-xl-2-1024-ms
description: Use exact Forge model pixart-alpha-pixart-sigma-xl-2-1024-ms for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use PixArt-Sigma XL 2 1024 MS

- Model slug: `pixart-alpha-pixart-sigma-xl-2-1024-ms`
- Family: `pixart-alpha-pixart-sigma`
- Version: `xl-2-1024-ms-diffusers` (`xl-2-1024-ms-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

PixArt-Sigma XL 1024 text-to-image generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `pixart-alpha-pixart-sigma-xl-2-1024-ms` version when the task supplies text and needs image.
- PixArt-Sigma XL 1024 text-to-image generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A clean editorial illustration of image generation benchmarks across GPU cards, crisp labels, modern technical magazine style'): Prompt
- `seed` (number; optional; bounds 0..999999; default 14): Seed
- `steps` (number; optional; bounds 4..50; default 20): Steps
- `guidance_scale` (number; optional; bounds 1..10; default 4.5): Guidance

Route: `POST /v1/inference/pixart-alpha-pixart-sigma-xl-2-1024-ms`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "max_sequence_length": 300,
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `pixart-alpha-pixart-sigma-xl-2-1024-ms` with version key `xl-2-1024-ms-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/pixart-alpha-pixart-sigma-xl-2-1024-ms` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 300.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/pixart-alpha-pixart-sigma-xl-2-1024-ms`
- Routes: `/v1/models/pixart-alpha-pixart-sigma-xl-2-1024-ms/inference-routes`
- Regional deployment: `/v1/models/pixart-alpha-pixart-sigma-xl-2-1024-ms/regional-deployment`
- Serverless handoff: `/v1/models/pixart-alpha-pixart-sigma-xl-2-1024-ms/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/pixart-alpha-pixart-sigma-xl-2-1024-ms/SKILL.md
