---
name: use-forge-black-forest-labs-flux-1-kontext-dev
description: Use exact Forge model black-forest-labs-flux-1-kontext-dev for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.1 Kontext Dev

- Model slug: `black-forest-labs-flux-1-kontext-dev`
- Family: `black-forest-labs-flux-1-kontext-dev`
- Version: `1.1.3` (`1-1-3`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `black-forest-labs-flux-1-kontext-dev-license`
- Research status: `source-linked`

## Purpose

FLUX.1 Kontext Dev NIM for prompt-driven in-context image editing on a single GPU.

## Use this exact model when

- Use this exact `black-forest-labs-flux-1-kontext-dev` version when the task supplies text, image and needs image.
- FLUX.1 Kontext Dev NIM for prompt-driven in-context image editing on a single GPU.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Transform the input image into a clean watercolor icon on a white background'): Prompt
- `image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII='): Input Image
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..40; default 30): Steps

Route: `POST /v1/inference/black-forest-labs-flux-1-kontext-dev`

```json
{
  "image": "{{image}}",
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `black-forest-labs-flux-1-kontext-dev` with version key `1-1-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-1-kontext-dev` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-kontex-9e23211569`
- Recommended: Instruction-driven in-context image editing (local inpainting and masked/targeted modification) — The FLUX.1 Kontext technical report and the upstream Hugging Face model repository describe the model and demonstrate examples and usage patterns oriented to in-context image editing and masked/local edits.
- Recommended: Iterative multi-turn edits preserving character and composition consistency (multi-step editing workflows) — The technical report documents character consistency and multi-turn editing as design goals and evaluation directions; the upstream README and examples describe multi-step editing use patterns.
- Recommended: Text-to-image generation and global style transfer at example generation sizes (e.g., 1024×1024 as used in paper/examples) — The paper and repository examples demonstrate text-to-image and image-to-image operations at 1024×1024 in reported examples and timing statements.
- Avoid: Using model outputs to train, fine‑tune, distill, or create a competitive model for commercial/production purposes — Model weights are distributed under the FLUX.1 [dev] Non‑Commercial License which restricts non‑commercial/non‑production use; redistribution or commercial use requires separate commercial terms from publisher.
- Avoid: Assuming outputs can be used commercially without obtaining a vendor/publisher commercial license — Upstream license artifacts and the NVIDIA model card indicate weights are distributed under a Non‑Commercial license and commercial terms must be obtained from publisher for commercial deployment or redistribution.
- Avoid: Expecting automatic preservation of input DPI or arbitrary input resolutions without preprocessing — Upstream documentation and packaging describe supported sizes and example usage but do not publish authoritative guarantees that arbitrary input DPI or arbitrary resolutions are preserved without explicit preprocessing; users should validate preprocessing/resolution behavior.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-1-kontext-dev`
- Routes: `/v1/models/black-forest-labs-flux-1-kontext-dev/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-1-kontext-dev/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-1-kontext-dev/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-1-kontext-dev/SKILL.md
