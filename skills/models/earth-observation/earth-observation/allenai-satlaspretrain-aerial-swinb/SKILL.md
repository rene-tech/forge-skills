---
name: use-forge-allenai-satlaspretrain-aerial-swinb
description: Use exact Forge model allenai-satlaspretrain-aerial-swinb for image to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use SatlasPretrain Aerial SwinB

- Model slug: `allenai-satlaspretrain-aerial-swinb`
- Family: `allenai-satlaspretrain-aerial-swinb`
- Version: `usable-highres` (`usable-highres`)
- Hierarchy: `models / earth-observation / earth-observation`
- Stability: `experimental`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Public Satlas high-resolution multi-task model for 8-bit RGB aerial/satellite imagery.

## Use this exact model when

- Use this exact `allenai-satlaspretrain-aerial-swinb` version when the task supplies image and needs json.
- Public Satlas high-resolution multi-task model for 8-bit RGB aerial/satellite imagery.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['image'] → ['json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `image` (url; optional; default 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/15/12663/7710'): Image URL or data URI
- `labels` (list; optional; default ['buildings', 'roads', 'water', 'fields', 'forest']): Labels
- `metadata` (json_editor; optional; default {}): Optional Plot Metadata
- `tile_size` (number; optional; bounds 256..2048; default 512): Tile Size
- `max_tiles` (number; optional; bounds 1..16; default 4): Max Tiles
- `mask_threshold` (number; optional; bounds 0.1..0.9; default 0.5): Mask Threshold
- `return_centinela_report` (checkbox; optional; default True): Return Centinela report

Route: `POST /v1/inference/allenai-satlaspretrain-aerial-swinb`

```json
{
  "image": "{{image}}",
  "labels": "{{labels}}",
  "mask_threshold": "{{mask_threshold}}",
  "max_tiles": "{{max_tiles}}",
  "metadata": "{{metadata}}",
  "return_centinela_report": "{{return_centinela_report}}",
  "tile_size": "{{tile_size}}"
}
```

## Exact output

- `json`

## Required workflow

1. Load this skill and pin model slug `allenai-satlaspretrain-aerial-swinb` with version key `usable-highres`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/allenai-satlaspretrain-aerial-swinb` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-allenai-satlas-2d73f9d0db`
- Recommended: Representation learning and downstream fine‑tuning for remote‑sensing tasks on high‑resolution aerial imagery (0.5–2.0 m/pixel RGB). — SatlasPretrain is presented as a large‑scale pretraining dataset and foundation model family intended for representation learning and downstream fine‑tuning; repository/package docs and the ICCV 2023/arXiv paper describe pretrained backbones for aerial imagery and recommend fine‑tuning for downstream tasks.
- Recommended: Fine‑tuning a SatlasPretrain backbone with task‑specific prediction heads for supervised downstream tasks (classification/segmentation/detection) on aerial imagery. — The satlaspretrain_models package and repository document pretrained backbones paired with prediction heads intended for downstream supervised fine‑tuning rather than turnkey inference.
- Avoid: Using a pretrained checkpoint plus the provided prediction heads as a finalized production classifier/segmenter without fine‑tuning. — Primary documentation and package metadata state prediction heads are randomly initialized and intended for fine‑tuning; direct use without fine‑tuning is unsupported by the authors.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Confirm imagery, geospatial data, and derived-output rights before processing or redistribution.
- Require human review before consequential environmental, security, property, or emergency-response decisions.
- Keep model revision, request, response, source imagery, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/allenai-satlaspretrain-aerial-swinb`
- Routes: `/v1/models/allenai-satlaspretrain-aerial-swinb/inference-routes`
- Regional deployment: `/v1/models/allenai-satlaspretrain-aerial-swinb/regional-deployment`
- Serverless handoff: `/v1/models/allenai-satlaspretrain-aerial-swinb/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/earth-observation/earth-observation/allenai-satlaspretrain-aerial-swinb/SKILL.md
