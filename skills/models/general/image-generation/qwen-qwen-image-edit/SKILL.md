---
name: use-forge-qwen-qwen-image-edit
description: Use exact Forge model qwen-qwen-image-edit for text, image to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen-Image-Edit

- Model slug: `qwen-qwen-image-edit`
- Family: `qwen-qwen-image-edit`
- Version: `1.0.0` (`1-0-0`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen-Image-Edit Visual GenAI NIM for prompt-driven image editing on a single 80GB GPU.

## Use this exact model when

- Use this exact `qwen-qwen-image-edit` version when the task supplies text, image and needs image.
- Qwen-Image-Edit Visual GenAI NIM for prompt-driven image editing on a single 80GB GPU.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Transform the input image into a polished watercolor illustration'): Prompt
- `image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC+aJAAAAT0lEQVR42u3PQQkAAAgEsItqFKMZzQi+hcEKLNXzWgQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQELgvywgGHuIjfVAAAAABJRU5ErkJggg=='): Input Image
- `disable_safety_checker` (checkbox; optional; default False): Disable safety checker
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 5..20; default 5): Steps

Route: `POST /v1/inference/qwen-qwen-image-edit`

```json
{
  "disable_safety_checker": "{{disable_safety_checker}}",
  "image": [
    "{{image}}"
  ],
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen-image-edit` with version key `1-0-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/qwen-qwen-image-edit` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-qwen-qwen-image-edit-8b48716485`
- Recommended: Prompt-driven image editing (semantic edits and appearance/style adjustments) via the NIM OpenAI-compatible image-editing endpoint — NVIDIA NIM API and NVIDIA Build model page describe Qwen-Image-Edit as an image editing model where a natural-language 'prompt' instructs the edit and input image(s) are processed by the pipeline (Qwen2.5-VL for semantic control and a VAE encoder for appearance control).
- Recommended: Use tag-specific variants for workflows where per-tag release notes indicate variant behavior; validate empirically on target data before production use — NVIDIA Build and NGC list supported variant tags selectable via NIM_MODEL_VERSION and the nvpcb artifact documents a targeted fine-tuning for PCB-style transfer; tag-specific variants can be selected and validated.
- Avoid: Assuming auditable, checkpoint-scoped numeric benchmark performance for NIM tags without additional provenance — No primary-source, checkpoint-scoped numeric benchmark rows (dataset, split, metric, numeric value) explicitly tied to the exact Qwen-Image-Edit NIM tags were found in the reviewed primary sources; family-level results in the technical report do not substitute for checkpoint-scoped evidence.
- Avoid: Relying on NIM offloading policies (disk/system_ram/none) for Qwen-Image-Edit — NVIDIA documentation explicitly states that offloading policies are not supported by Qwen-Image and Qwen-Image-Edit NIMs.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen-image-edit`
- Routes: `/v1/models/qwen-qwen-image-edit/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen-image-edit/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen-image-edit/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/qwen-qwen-image-edit/SKILL.md
