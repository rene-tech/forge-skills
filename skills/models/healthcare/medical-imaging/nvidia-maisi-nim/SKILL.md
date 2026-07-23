---
name: use-forge-nvidia-maisi-nim
description: Use exact Forge model nvidia-maisi-nim for structured to image, segmentation, file. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA MAISI

- Model slug: `nvidia-maisi-nim`
- Family: `nvidia-maisi`
- Version: `1.0.1` (`nim-1-0-1-latest-digest`)
- Hierarchy: `models / healthcare / medical-imaging`
- Stability: `experimental`
- Default eligible: `false`
- License: `NVIDIA software and model evaluation license agreement; NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

NVIDIA MAISI is a medical-imaging NIM for generating synthetic 3D CT volumes and paired segmentation labels from requested body regions, anatomies, voxel spacing, and output-size controls.

## Use this exact model when

- Use this exact `nvidia-maisi-nim` version when the task supplies structured and needs image, segmentation, file.
- NVIDIA MAISI is a medical-imaging NIM for generating synthetic 3D CT volumes and paired segmentation labels from requested body regions, anatomies, voxel spacing, and output-size controls.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['structured'] → ['image', 'segmentation', 'file'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `body_region` (json_editor; required; default '["abdomen"]'): Body regions JSON array
- `anatomy_list` (json_editor; optional; default '["liver", "spleen"]'): Anatomies JSON array
- `num_output_samples` (number; required; bounds 1..1; default 1): Number of output samples
- `num_inference_steps` (number; optional; bounds 1..1000; default 20): Inference steps
- `output_size` (json_editor; optional; default '[256, 256, 128]'): Output size [x,y,z]
- `spacing` (json_editor; optional; default '[1.0, 1.0, 1.0]'): Spacing [x,y,z]
- `image_output_ext` (select; optional; choices .nii.gz, .nii, .nrrd, .dcm; default '.nii.gz'): Image output extension
- `label_output_ext` (select; optional; choices .nii.gz, .nii, .nrrd, .dcm; default '.nii.gz'): Label output extension

Route: `POST /v1/maisi/run`

```json
{
  "anatomy_list": "{{anatomy_list}}",
  "body_region": "{{body_region}}",
  "image_output_ext": "{{image_output_ext}}",
  "label_output_ext": "{{label_output_ext}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "num_output_samples": "{{num_output_samples}}",
  "output_size": "{{output_size}}",
  "spacing": "{{spacing}}"
}
```

## Exact output

- `image`
- `segmentation`
- `file`

## Required workflow

1. Load this skill and pin model slug `nvidia-maisi-nim` with version key `nim-1-0-1-latest-digest`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/maisi/run` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-maisi-nim`
- Routes: `/v1/models/nvidia-maisi-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-maisi-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-maisi-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/medical-imaging/nvidia-maisi-nim/SKILL.md
