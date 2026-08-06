---
name: use-forge-qwen-qwen-image
description: Use exact Forge model qwen-qwen-image for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen-Image

- Model slug: `qwen-qwen-image`
- Family: `qwen-qwen-image`
- Version: `1.0.0` (`1-0-0`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen-Image Visual GenAI NIM for high-quality multilingual text-to-image generation, with the container default pinned to the qwen-image-2512 model version.

## Use this exact model when

- Use this exact `qwen-qwen-image` version when the task supplies text and needs image.
- Qwen-Image Visual GenAI NIM for high-quality multilingual text-to-image generation, with the container default pinned to the qwen-image-2512 model version.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default "A bilingual poster that says 'Nebius Forge' and 'Image Generation' with crisp typography and a clean modern layout"): Prompt
- `seed` (number; optional; bounds 0..999999; default 0): Seed

Route: `POST /v1/inference/qwen-qwen-image`

```json
{
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen-image` with version key `1-0-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/qwen-qwen-image` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-qwen-qwen-image-d3119f508b`
- Recommended: Multilingual text-to-image generation with strong text rendering emphasis — NVIDIA overview documentation describes Qwen-Image as a text-to-image foundation model with strong capabilities in complex text rendering for English and Chinese, high-resolution output, and versatile styles. The upstream Qwen-Image model card also states strong capabilities in complex text rendering for alphabetic and logographic scripts.
- Recommended: Self-hosted NVIDIA NIM deployment for Qwen-Image text-to-image inference — NVIDIA getting-started documentation explicitly documents the Qwen-Image NIM runtime, the NIM_MODEL_VERSION selector, and that the container defaults to qwen-image-2512 when unset.
- Avoid: Using base Qwen-Image for image-editing workflows that require image inputs — NVIDIA documents Qwen-Image as a text-to-image foundation-model family, while Qwen-Image-Edit is separately documented as the image-editing family built on Qwen-Image.
- Avoid: Deploying the NVIDIA NIM container without guardrails and safety mechanisms — The NGC Qwen-Image container page states that users are responsible for model inputs and outputs and must implement guardrails and safety mechanisms before deployment.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen-image`
- Routes: `/v1/models/qwen-qwen-image/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen-image/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen-image/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/qwen-qwen-image/SKILL.md
