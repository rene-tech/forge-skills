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

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-dev-51a0d62834`
- Recommended: Text-to-image generation (single text prompt → generated image) — Upstream model card and the Hugging Face model landing describe FLUX.1 [dev] as a generative text→image model and provide usage examples and Diffusers-style runtime guidance.
- Recommended: Image-conditioned generation/editing using explicitly enumerated FLUX.1 [dev] variants (e.g., Fill, Canny, Depth, Kontext) when those variants are selected upstream — The upstream model card and repository enumerate dev variants intended for image-conditioned uses and document variant-specific usage.
- Avoid: Commercial or production deployment without obtaining a separate commercial license from Black Forest Labs — The upstream FLUX.1 [dev] license files published in the upstream repository and on the Hugging Face model repo identify the FLUX.1 [dev] Non‑Commercial License and restrict the dev-model weights and inference code to non-commercial/non-production use per the upstream license text.
- Avoid: Relying on model-generated calibrated likelihoods/log-probabilities/confidence scores for automated decision-making — Inspected upstream documentation (model card and README) describes generated image artifacts and usage examples but does not document probabilistic numeric outputs (likelihoods/log-probabilities/calibrated confidence scores) for the checkpoint at those locators.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-1-dev/SKILL.md
