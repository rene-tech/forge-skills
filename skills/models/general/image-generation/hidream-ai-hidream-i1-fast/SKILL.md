---
name: use-forge-hidream-ai-hidream-i1-fast
description: Use exact Forge model hidream-ai-hidream-i1-fast for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use HiDream-I1 Fast

- Model slug: `hidream-ai-hidream-i1-fast`
- Family: `hidream-ai-hidream-i1`
- Version: `fast-diffusers` (`fast-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

HiDream-I1 Fast text-to-image generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `hidream-ai-hidream-i1-fast` version when the task supplies text and needs image.
- HiDream-I1 Fast text-to-image generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A realistic product photo of a next-generation GPU server rendering a gallery of generated images on a wall display'): Prompt
- `seed` (number; optional; bounds 0..999999; default 99): Seed
- `steps` (number; optional; bounds 4..40; default 16): Steps
- `guidance_scale` (number; optional; bounds 0..8; default 3.5): Guidance

Route: `POST /v1/inference/hidream-ai-hidream-i1-fast`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "max_sequence_length": 128,
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `hidream-ai-hidream-i1-fast` with version key `fast-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/hidream-ai-hidream-i1-fast` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-hidream-ai-hidream-i1-e16c7971da`
- Recommended: Text-to-image generation (general-purpose image synthesis from text prompts). — Primary repository and model-card materials present HiDream-I1 as a text-to-image generative foundation model family and expose an inference entrypoint and Fast variant intended for lower-step generation.
- Avoid: Clinical diagnostic, medical decision-making, or other clinical-ready deployments. — Primary sources (repository README, Hugging Face model card, and technical report) do not provide clinical validation, PHI-handling guidance, or statements clearing the model for clinical or diagnostic use.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 128.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/hidream-ai-hidream-i1-fast`
- Routes: `/v1/models/hidream-ai-hidream-i1-fast/inference-routes`
- Regional deployment: `/v1/models/hidream-ai-hidream-i1-fast/regional-deployment`
- Serverless handoff: `/v1/models/hidream-ai-hidream-i1-fast/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/hidream-ai-hidream-i1-fast/SKILL.md
