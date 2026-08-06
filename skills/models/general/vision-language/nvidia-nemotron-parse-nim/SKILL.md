---
name: use-forge-nvidia-nemotron-parse-nim
description: Use exact Forge model nvidia-nemotron-parse-nim for document, image to text, layout. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Nemotron Parse

- Model slug: `nvidia-nemotron-parse-nim`
- Family: `nvidia-nemotron-parse`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / vision-language`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

NVIDIA Nemotron Parse NIM for parsing document images into structured text; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.

## Use this exact model when

- Use this exact `nvidia-nemotron-parse-nim` version when the task supplies document, image and needs text, layout.
- NVIDIA Nemotron Parse NIM for parsing document images into structured text; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['document', 'image'] → ['text', 'layout'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `image_url` (text; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII='): Image URL or data URL

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": 256,
  "messages": [
    {
      "content": [
        {
          "image_url": {
            "url": "{{image_url}}"
          },
          "type": "image_url"
        }
      ],
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": false
}
```

## Exact output

- `text`
- `layout`

## Required workflow

1. Load this skill and pin model slug `nvidia-nemotron-parse-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-nemotron-parse-7466ab787f`
- Recommended: Document transcription from PDFs and document images into structured text with spatial annotations (formatted/extracted text + bounding boxes + semantic class labels). — NGC container listing and build.nvidia model card describe Nemotron Parse producing structured annotations (formatted text, bounding boxes, semantic classes) from document inputs; NeMo Curator PDF pipeline documents how Nemotron Parse integrates into PDF ingestion and emits interleaved Parquet outputs for downstream workflows.
- Avoid: Pure text-only processing workflows that accept only raw text (no image/PDF input). — NIM API documentation states text input is not supported and examples show image/PDF-focused inputs; Nemotron Parse is documented as image/PDF-focused.
- Avoid: Assuming model confidences are calibrated for direct acceptance without application-specific validation. — Primary sources do not provide prescriptive confidence calibration mappings or acceptance thresholds for Nemotron Parse outputs.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-nemotron-parse-nim`
- Routes: `/v1/models/nvidia-nemotron-parse-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-nemotron-parse-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-nemotron-parse-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/nvidia-nemotron-parse-nim/SKILL.md
