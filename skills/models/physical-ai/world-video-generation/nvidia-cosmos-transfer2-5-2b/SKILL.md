---
name: use-forge-nvidia-cosmos-transfer2-5-2b
description: Use exact Forge model nvidia-cosmos-transfer2-5-2b for text, video to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Transfer2.5 2B

- Model slug: `nvidia-cosmos-transfer2-5-2b`
- Family: `nvidia-cosmos-transfer2-5-2b`
- Version: `1.0.0` (`1-0-0`)
- Hierarchy: `models / physical-ai / world-video-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-open-model-license`
- Research status: `source-linked`

## Purpose

Hidden onboarding manifest for Cosmos Transfer2.5 NIM, a controllable physical-AI world-generation model with edge, segmentation, visual, and depth controls.

## Use this exact model when

- Use this exact `nvidia-cosmos-transfer2-5-2b` version when the task supplies text, video and needs video.
- Hidden onboarding manifest for Cosmos Transfer2.5 NIM, a controllable physical-AI world-generation model with edge, segmentation, visual, and depth controls.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'video'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Convert the driving clip to rainy weather while preserving road geometry and object layout.'): Prompt
- `video` (text; optional; default 'https://raw.githubusercontent.com/abhinavg4/cosmos-transfer2.5/main/assets_nim/low/robot_input.mp4'): Video URL or base64 MP4
- `resolution` (select; optional; choices 480, 720; default '480'): Resolution
- `edge` (json_editor; optional; default {'control': 'https://raw.githubusercontent.com/abhinavg4/cosmos-transfer2.5/main/assets_nim/low/edge/robot_edge.mp4', 'control_weight': 1.0}): Edge Control
- `seg` (json_editor; optional; default {'control': 'https://raw.githubusercontent.com/abhinavg4/cosmos-transfer2.5/main/assets_nim/low/seg/robot_seg.mp4', 'control_weight': 1.0}): Segmentation Control
- `vis` (json_editor; optional; default {'control': 'https://raw.githubusercontent.com/abhinavg4/cosmos-transfer2.5/main/assets_nim/low/vis/robot_vis.mp4', 'control_weight': 1.0}): Visual Control
- `depth` (json_editor; optional; default {'control': 'https://raw.githubusercontent.com/abhinavg4/cosmos-transfer2.5/main/assets_nim/low/depth/robot_depth.mp4', 'control_weight': 1.0}): Depth Control

Route: `POST /v1/inference/nvidia-cosmos-transfer2-5-2b`

```json
{
  "depth": "{{depth}}",
  "edge": "{{edge}}",
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "resolution": "{{resolution}}",
  "seg": "{{seg}}",
  "video": "{{video}}",
  "vis": "{{vis}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-transfer2-5-2b` with version key `1-0-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-transfer2-5-2b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-transfer2-5-2b`
- Routes: `/v1/models/nvidia-cosmos-transfer2-5-2b/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-transfer2-5-2b/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-transfer2-5-2b/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos-transfer2-5-2b/SKILL.md
