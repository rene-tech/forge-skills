---
name: use-forge-stabilityai-stable-diffusion-3-5-large
description: Use exact Forge model stabilityai-stable-diffusion-3-5-large for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Stable Diffusion 3.5 Large

- Model slug: `stabilityai-stable-diffusion-3-5-large`
- Family: `stabilityai-stable-diffusion-3-5-large`
- Version: `1.1.0` (`1-1-0`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `stability-ai-community-license`
- Research status: `source-linked`

## Purpose

Stability AI Stable Diffusion 3.5 Large Visual GenAI NIM for high-quality text-to-image generation on a single GPU.

## Use this exact model when

- Use this exact `stabilityai-stable-diffusion-3-5-large` version when the task supplies text, image and needs image.
- Stability AI Stable Diffusion 3.5 Large Visual GenAI NIM for high-quality text-to-image generation on a single GPU.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A high-resolution concept art render of a cloud GPU control room, cinematic lighting, detailed but realistic'): Prompt
- `mode` (select; optional; choices base; default 'base'): Mode
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..50; default 50): Steps

Route: `POST /v1/inference/stabilityai-stable-diffusion-3-5-large`

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

1. Load this skill and pin model slug `stabilityai-stable-diffusion-3-5-large` with version key `1-1-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/stabilityai-stable-diffusion-3-5-large` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-stabilityai-stable-diffusion-3-e2f0f75a5d`
- Recommended: High-quality text-to-image generation for creative media, concept art, and prototyping (single-prompt synthesis). — The official Hugging Face model card describes the checkpoint as an MMDiT text-to-image model and provides example outputs and usage recommendations for local/self-hosted inference tools.
- Recommended: Performance-oriented inference experiments using ONNX/TensorRT exports provided in the stable-diffusion-3.5-large-tensorrt repository (repository-level optimized inference artifacts). — The stable-diffusion-3.5-large-tensorrt repository publishes ONNX exports for T5, MMDiT, and VAE components and reports repository-level end-to-end timing profiles for BF16 and FP8 inference flows.
- Avoid: Clinical or regulated medical decision-making (diagnosis, treatment recommendation). — Evidence gap: the checked primary sources do not publish checkpoint-scoped clinical validation or regulatory approval documentation for the upstream checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/stabilityai-stable-diffusion-3-5-large`
- Routes: `/v1/models/stabilityai-stable-diffusion-3-5-large/inference-routes`
- Regional deployment: `/v1/models/stabilityai-stable-diffusion-3-5-large/regional-deployment`
- Serverless handoff: `/v1/models/stabilityai-stable-diffusion-3-5-large/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/stabilityai-stable-diffusion-3-5-large/SKILL.md
