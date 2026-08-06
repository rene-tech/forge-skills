---
name: use-forge-nvidia-cosmos3-omni-super
description: Use exact Forge model nvidia-cosmos3-omni-super for text, image to image, video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos 3 Omni (Super)

- Model slug: `nvidia-cosmos3-omni-super`
- Family: `nvidia-cosmos3-omni`
- Version: `super-bf16-ea` (`super-bf16`)
- Hierarchy: `models / physical-ai / world-video-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-software-model-evaluation-license`
- Research status: `source-linked`

## Purpose

Early-access Cosmos 3 Omni Super world-generation model served through a Forge CUDA 13 wrapper.

## Use this exact model when

- Use this exact `nvidia-cosmos3-omni-super` version when the task supplies text, image and needs image, video.
- Early-access Cosmos 3 Omni Super world-generation model served through a Forge CUDA 13 wrapper.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['image', 'video'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `model_mode` (select; optional; choices text2image, text2video, image2video; default 'text2image'): Mode
- `prompt` (textarea; optional; default 'A humanoid robot opens a sliding glass door, steps into a lab, and reaches toward a tray of tools.'): Prompt
- `vision_path` (file_upload; optional; default ''): Conditioning Image
- `resolution` (select; optional; choices 256, 480, 720, 1080; default '256'): Resolution
- `aspect_ratio` (select; optional; choices 1,1, 4,3, 3,4, 16,9, 9,16; default '1,1'): Aspect Ratio
- `num_frames` (number; optional; bounds 1..200; default 1): Frames
- `fps` (number; optional; bounds 10..30; default 24): FPS
- `num_steps` (number; optional; bounds 1..50; default 4): Steps
- `guidance` (slider; optional; bounds 0..7; default 4): Guidance
- `shift` (number; optional; bounds 0..20; default 5): Shift
- `seed` (number; optional; bounds 0..2147483647; default 42): Seed

Route: `POST /v1/inference/nvidia-cosmos3-omni`

```json
{
  "aspect_ratio": "{{aspect_ratio}}",
  "fps": "{{fps}}",
  "guidance": "{{guidance}}",
  "model_mode": "{{model_mode}}",
  "num_frames": "{{num_frames}}",
  "num_steps": "{{num_steps}}",
  "prompt": "{{prompt}}",
  "resolution": "{{resolution}}",
  "seed": "{{seed}}",
  "shift": "{{shift}}",
  "vision_path": "{{vision_path}}"
}
```

## Exact output

- `image`
- `video`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos3-omni-super` with version key `super-bf16`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos3-omni` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-nvidia-cosmos-ea-cosmos3-super-b558901695`
- Recommended: Omnimodal world generation for synthetic data and environment generation (text+image→video, text→image, text→video, audio, and action trajectory generation) — Hugging Face model pages for Cosmos3‑Super state the checkpoint can generate dynamic video, image, audio, and action commands from multimodal inputs; the NVIDIA technical report describes Cosmos3 family capabilities for multimodal/world generation.
- Recommended: Physical AI research and synthetic environment generation for robotics policy training and agent pre‑training (research/experimental use with validation) — Primary NVIDIA materials describe Cosmos3 and the family as intended for Physical AI use cases and world generation to support agent/robotics research.
- Avoid: Safety‑critical closed‑loop autonomous control (e.g., direct robot control or safety‑critical vehicle control) — Model pages and variant cards explicitly warn that generated outputs can be imperfect (temporal inconsistency, inaccurate physical interactions, action/state drift) and that users must implement guardrails; primary sources do not claim safety certification for closed‑loop control.
- Avoid: Substituting Cosmos3‑Super outputs as a certified physics simulator or guaranteed high‑fidelity physical engine — Primary sources state the model lacks an explicit physics simulator and does not provide guaranteed correct 3D geometry, contact dynamics, or full physical laws — physical reasoning is approximated.
- Avoid: Treating generated outputs as calibrated probabilistic confidence scores or ground‑truth labels for certification — Primary sources do not document calibration semantics or per‑output probabilistic confidence scores; model cards caution against treating outputs as reliable ground truth without downstream validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos3-omni-super`
- Routes: `/v1/models/nvidia-cosmos3-omni-super/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos3-omni-super/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos3-omni-super/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos3-omni-super/SKILL.md
