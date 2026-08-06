---
name: use-forge-black-forest-labs-flux-1-schnell
description: Use exact Forge model black-forest-labs-flux-1-schnell for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.1 Schnell

- Model slug: `black-forest-labs-flux-1-schnell`
- Family: `black-forest-labs-flux-1-schnell`
- Version: `1.1.3` (`1-1-3`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Distilled FLUX.1 Schnell image generation NIM for fast single-GPU text-to-image experiments.

## Use this exact model when

- Use this exact `black-forest-labs-flux-1-schnell` version when the task supplies text and needs image.
- Distilled FLUX.1 Schnell image generation NIM for fast single-GPU text-to-image experiments.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A bright editorial photo of a data center aisle with a single glowing GPU node, natural perspective, realistic colors'): Prompt
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..12; default 4): Steps

Route: `POST /v1/inference/black-forest-labs-flux-1-schnell`

```json
{
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `black-forest-labs-flux-1-schnell` with version key `1-1-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-1-schnell` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-schnel-145d8ced5b`
- Recommended: Text-to-image generation from plain-text prompts — Primary NVIDIA-hosted Black Forest Labs model card and the Hugging Face repository describe FLUX.1-schnell as a text-to-image model that generates images from text descriptions and provide sampling/reference implementations.
- Recommended: Fast, low-step exploratory image generation (few diffusion steps for prompt exploration) — The NVIDIA-hosted model card and NVIDIA product overview indicate the checkpoint is a distilled model optimized to produce high-quality images in 1–4 diffusion steps suitable for fast local experimentation.
- Avoid: Treating NVIDIA NIM/NGC packaging or NIM container metadata as checkpoint-quality benchmark evidence — The NVIDIA NIM/NGC pages and the NVIDIA-hosted model card provide container identity, packaging, and qualitative capability descriptions but do not provide checkpoint-scoped benchmark tables with dataset/split/metric/value entries or protocol-matched quantitative quality metrics for this exact checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-1-schnell`
- Routes: `/v1/models/black-forest-labs-flux-1-schnell/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-1-schnell/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-1-schnell/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-1-schnell/SKILL.md
