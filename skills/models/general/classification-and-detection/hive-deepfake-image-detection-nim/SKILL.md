---
name: use-forge-hive-deepfake-image-detection-nim
description: Use exact Forge model hive-deepfake-image-detection-nim for image to classification. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hive Deepfake Image Detection

- Model slug: `hive-deepfake-image-detection-nim`
- Family: `hive-deepfake-image-detection`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / classification-and-detection`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

Hive deepfake image detection NIM for classifying manipulated face images; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.

## Use this exact model when

- Use this exact `hive-deepfake-image-detection-nim` version when the task supplies image and needs classification.
- Hive deepfake image detection NIM for classifying manipulated face images; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave6.
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

1. Load this skill and pin model slug `hive-deepfake-image-detection-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-hive-deepfake-image-detection-8b102328c6`
- Recommended: Per-face deepfake detection in images (binary classification per detected face) — The NIM API reference describes the model as identifying whether an image is a deepfake and states that the model locates faces and outputs, for each detected face, a bounding box, a classification, and an accompanying confidence score.
- Recommended: Deploying the NIM-distributed Hive Deepfake Image Detection model on NVIDIA GPUs (validate integration and performance on target hardware) — The NIM support matrix documents GPU and engine support (TensorRT on specific GPUs and ONNX for GPUs with sufficient memory) and requires a Docker environment that supports NVIDIA GPUs and the NVIDIA Container Toolkit; implementers must validate throughput/latency on their hardware.
- Avoid: Using the Hive Deepfake Image Detection model for non-image modalities (e.g., text, audio, or embeddings) — The NIM API reference describes the model specifically as identifying whether an image is a deepfake, and the documented behavior is face detection and per-face classification in images; the inspected sources do not document non-image modality support.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/hive-deepfake-image-detection-nim`
- Routes: `/v1/models/hive-deepfake-image-detection-nim/inference-routes`
- Regional deployment: `/v1/models/hive-deepfake-image-detection-nim/regional-deployment`
- Serverless handoff: `/v1/models/hive-deepfake-image-detection-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/classification-and-detection/hive-deepfake-image-detection-nim/SKILL.md
