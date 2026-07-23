---
name: use-forge-biomedica-bmc-clip-cf
description: Use exact Forge model biomedica-bmc-clip-cf for image, text to embedding, classification, similarity, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BIOMEDICA BMC-CLIP CF

- Model slug: `biomedica-bmc-clip-cf`
- Family: `biomedica-bmc-clip`
- Version: `bmc-clip-cf-wrapper-20260529t18z-ack` (`wrapper-20260529t18z-ack`)
- Hierarchy: `models / healthcare / medical-imaging`
- Stability: `testing`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

BIOMEDICA BMC-CLIP CF is a biomedical CLIP-style vision-language model released with the CVPR 2025 BIOMEDICA work.

## Use this exact model when

- Use this exact `biomedica-bmc-clip-cf` version when the task supplies image, text and needs embedding, classification, similarity, json.
- BIOMEDICA BMC-CLIP CF is a biomedical CLIP-style vision-language model released with the CVPR 2025 BIOMEDICA work.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['image', 'text'] → ['embedding', 'classification', 'similarity', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `mode` (select; required; choices classify, similarity, embed_image, embed_text; default 'classify'): Mode
- `image_base64` (image_base64; required; default 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGOor68HAAL+AX66JXAlAAAAAElFTkSuQmCC'): Image
- `texts` (json_editor; required; default '["a histopathology image", "a radiology image", "a microscopy image"]'): Candidate labels or captions
- `top_k` (number; optional; bounds 1..64; default 3): Top labels
- `return_embeddings` (checkbox; optional; default False): Return embeddings
- `research_use_acknowledgement` (checkbox; required; default True): Research-only use acknowledged

Route: `POST /v1/inference/biomedica-bmc-clip-cf`

```json
{
  "image_base64": "{{image_base64}}",
  "mode": "{{mode}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_embeddings": "{{return_embeddings}}",
  "texts": "{{texts}}",
  "top_k": "{{top_k}}"
}
```

## Exact output

- `embedding`
- `classification`
- `similarity`
- `json`

## Required workflow

1. Load this skill and pin model slug `biomedica-bmc-clip-cf` with version key `wrapper-20260529t18z-ack`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/biomedica-bmc-clip-cf` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 77.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/biomedica-bmc-clip-cf`
- Routes: `/v1/models/biomedica-bmc-clip-cf/inference-routes`
- Regional deployment: `/v1/models/biomedica-bmc-clip-cf/regional-deployment`
- Serverless handoff: `/v1/models/biomedica-bmc-clip-cf/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/medical-imaging/biomedica-bmc-clip-cf/SKILL.md
