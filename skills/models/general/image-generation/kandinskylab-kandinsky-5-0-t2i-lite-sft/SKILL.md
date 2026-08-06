---
name: use-forge-kandinskylab-kandinsky-5-0-t2i-lite-sft
description: Use exact Forge model kandinskylab-kandinsky-5-0-t2i-lite-sft for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Kandinsky 5.0 T2I Lite SFT

- Model slug: `kandinskylab-kandinsky-5-0-t2i-lite-sft`
- Family: `kandinskylab-kandinsky-5-0`
- Version: `t2i-lite-sft-diffusers` (`t2i-lite-sft-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Kandinsky 5.0 Image Lite SFT text-to-image generation through the Forge Diffusers wrapper.

## Use this exact model when

- Use this exact `kandinskylab-kandinsky-5-0-t2i-lite-sft` version when the task supplies text and needs image.
- Kandinsky 5.0 Image Lite SFT text-to-image generation through the Forge Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A clean product photograph of a cloud GPU console showing generated image previews, crisp typography, realistic lighting'): Prompt
- `seed` (number; optional; bounds 0..999999; default 123): Seed
- `steps` (number; optional; bounds 8..60; default 30): Steps
- `guidance_scale` (number; optional; bounds 1..8; default 3.5): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 512..1536; default 1024): Height

Route: `POST /v1/inference/kandinskylab-kandinsky-5-0-t2i-lite-sft`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
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

1. Load this skill and pin model slug `kandinskylab-kandinsky-5-0-t2i-lite-sft` with version key `t2i-lite-sft-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/kandinskylab-kandinsky-5-0-t2i-lite-sft` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-docs-diffusers-api-pipelines-kandinsky5-image-e9e2461bb8`
- Recommended: Text-to-image generation (single prompt or batched prompts → generated image artifacts) — The model repository README and model_index.json identify this checkpoint as a Kandinsky5 text-to-image checkpoint (Kandinsky5T2IPipeline) and the repository README describes the Kandinsky 5.0 Image Lite family and T2I usage.
- Avoid: Assuming checkpoint-scoped numeric benchmarks for model selection — No checkpoint-scoped numeric benchmark tables (dataset, split, metric, numeric value, and experiment conditions) are present in the inspected primary sources for this exact Diffusers checkpoint.
- Avoid: Relying on built-in content-filtering or assuming the checkpoint enforces content-safety — The canonical arXiv preprint (v1 and v2) documents that authors did not implement built-in content-filtering systems and places responsibility on users; the checkpoint blobs do not provide checkpoint-scoped content-filtering mechanisms.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/kandinskylab-kandinsky-5-0-t2i-lite-sft`
- Routes: `/v1/models/kandinskylab-kandinsky-5-0-t2i-lite-sft/inference-routes`
- Regional deployment: `/v1/models/kandinskylab-kandinsky-5-0-t2i-lite-sft/regional-deployment`
- Serverless handoff: `/v1/models/kandinskylab-kandinsky-5-0-t2i-lite-sft/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/kandinskylab-kandinsky-5-0-t2i-lite-sft/SKILL.md
