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

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-cosmos-transfer2-5-2b-modelcard-e510edc819`
- Recommended: Physics-aware video/world-state generation conditioned on text plus multiple structured video control modalities for Physical AI research and synthetic-data generation (robotics, autonomous-vehicle perception) — Model card, product docs, and the research lab page describe the model as purpose-built for Physical AI and accepting multiple structured video control modalities for generating world-state video/images.
- Recommended: Controlled video-to-video transfer and sim-to-real synthetic-data generation using simulator-derived control maps (depth, segmentation, edges, blur) for data augmentation and training downstream perception models — Product documentation and research lab examples describe workflows for simulation-to-photorealism and scaling world-state diversity using structured control inputs accepted by Transfer2.5.
- Recommended: Multi-view/multi-camera conditional generation producing view-consistent frames per camera in multi-camera world scenarios — Model card and research examples document multi-view/multi-camera example inputs (seven-camera examples) and show view-consistent generation examples at 1280×720 resolution.
- Avoid: Applications requiring provable, formal physical‑law guarantees or certified multi-agent-dynamics correctness without downstream validation — Evidence gap: primary NVIDIA model card, product docs, and research lab page describe physics-aware world-state generation but do not provide proofs, formal guarantees, or evaluation protocols certifying provable physics-grounding or multi-agent dynamics correctness for the named checkpoint.
- Avoid: Production deployment on non-Linux operating systems without vendor validation — Evidence gap: available primary documentation includes Docker/NIM container usage and runtime flags but does not publish explicit cross-platform (non-Linux) support claims or validated runtime matrices for non-Linux OSes.
- Avoid: Assuming upstream-checkpoint parity with NIM/container TensorRT/FP8 quantized performance/precision without explicit validation — Evidence gap / NIM-only: NGC container listing documents container-level optimizations (TensorRT, FP8) but primary model pages do not publish the exact precisions tested/supported for the upstream checkpoint itself; treat container optimizations as NIM-level evidence.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos-transfer2-5-2b/SKILL.md
