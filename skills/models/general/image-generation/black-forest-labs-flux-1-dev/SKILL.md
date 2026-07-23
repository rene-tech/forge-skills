---
name: use-forge-black-forest-labs-flux-1-dev
description: Use exact Forge model black-forest-labs-flux-1-dev for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.1 Dev

- Model slug: `black-forest-labs-flux-1-dev`
- Family: `black-forest-labs-flux-1-dev`
- Version: `1.2.2` (`1-2-2`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `black-forest-labs-flux-1-dev-license`
- Research status: `source-linked`

## Purpose

Black Forest Labs FLUX.1 Dev image generation packaged as NVIDIA Visual GenAI NIM.

## Use this exact model when

- Use this exact `black-forest-labs-flux-1-dev` version when the task supplies text, image and needs image.
- Black Forest Labs FLUX.1 Dev image generation packaged as NVIDIA Visual GenAI NIM.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A cinematic product photo of a compact GPU server in a clean studio, softbox lighting, sharp details'): Prompt
- `mode` (select; optional; choices base; default 'base'): Mode
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..50; default 50): Steps

Route: `POST /v1/inference/black-forest-labs-flux-1-dev`

```json
{
  "mode": "{{mode}}",
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `black-forest-labs-flux-1-dev` with version key `1-2-2`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-1-dev` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-1-dev`
- Routes: `/v1/models/black-forest-labs-flux-1-dev/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-1-dev/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-1-dev/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-1-dev/SKILL.md
