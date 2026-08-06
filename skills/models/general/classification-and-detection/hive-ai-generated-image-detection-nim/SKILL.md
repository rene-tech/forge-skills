---
name: use-forge-hive-ai-generated-image-detection-nim
description: Use exact Forge model hive-ai-generated-image-detection-nim for image to classification. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hive AI-Generated Image Detection

- Model slug: `hive-ai-generated-image-detection-nim`
- Family: `hive-ai-generated-image-detection`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / classification-and-detection`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

Hive AI-generated image detection NIM for classifying synthetic images; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.

## Use this exact model when

- Use this exact `hive-ai-generated-image-detection-nim` version when the task supplies image and needs classification.
- Hive AI-generated image detection NIM for classifying synthetic images; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['image'] → ['classification'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `image_url` (text; optional; default 'https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg'): Image URL

Route: `POST /v1/infer`

```json
{
  "input": [
    {
      "type": "image_url",
      "url": "{{image_url}}"
    }
  ]
}
```

## Exact output

- `classification`

## Required workflow

1. Load this skill and pin model slug `hive-ai-generated-image-detection-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/infer` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-hive-ai-generated-image-detection-36e2b7f1b1`
- Recommended: Binary classification to detect whether an image is AI-generated or modified (surface likely AI-generated content for downstream workflows). — Primary Hive documentation and the NIM catalog/reference describe a binary classification head that indicates whether an image is AI-generated accompanied by a confidence score.
- Recommended: Source attribution: return the likely generative engine that produced an image when identifiable (use as a signal for triage or investigative workflows). — Creator documentation and NIM references describe a source-attribution head that returns the likely AI synthesis model or "none" if unidentified.
- Avoid: Any vision task outside AI-generated image detection or source attribution (for example: fine-grained species identification, OCR, general object detection). — Primary sources describe the model specifically as an AI-generated image detector with a binary head and a source-attribution head; there is no primary-source evidence the checkpoint supports other vision tasks.
- Avoid: Deploying the model without reviewing or complying with Hive's terms-of-use and NIM/NGC access/governance requirements. — Creator terms of use and NGC catalog documentation include usage restrictions and access requirements; users must review contractual/terms requirements prior to deployment.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/hive-ai-generated-image-detection-nim`
- Routes: `/v1/models/hive-ai-generated-image-detection-nim/inference-routes`
- Regional deployment: `/v1/models/hive-ai-generated-image-detection-nim/regional-deployment`
- Serverless handoff: `/v1/models/hive-ai-generated-image-detection-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/classification-and-detection/hive-ai-generated-image-detection-nim/SKILL.md
