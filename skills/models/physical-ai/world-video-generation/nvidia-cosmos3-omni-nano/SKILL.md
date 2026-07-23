---
name: use-forge-nvidia-cosmos3-omni-nano
description: Use exact Forge model nvidia-cosmos3-omni-nano for text, image, video, action to image, video, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos 3 Omni (Nano)

- Model slug: `nvidia-cosmos3-omni-nano`
- Family: `nvidia-cosmos3-omni`
- Version: `nano-bf16-ea` (`nano-bf16`)
- Hierarchy: `models / physical-ai / world-video-generation`
- Stability: `testing`
- Default eligible: `true`
- License: `nvidia-software-model-evaluation-license`
- Research status: `source-linked`

## Purpose

Early-access Cosmos 3 Omni Nano world-generation and action model served through a Forge CUDA 13 wrapper.

## Use this exact model when

- Use this exact `nvidia-cosmos3-omni-nano` version when the task supplies text, image, video, action and needs image, video, json.
- Early-access Cosmos 3 Omni Nano world-generation and action model served through a Forge CUDA 13 wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'video', 'action'] → ['image', 'video', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `model_mode` (select; optional; choices text2image, text2video, image2video, forward_dynamics, inverse_dynamics, policy; default 'text2image'): Mode
- `prompt` (textarea; optional; default 'A warehouse robot carefully navigates around a reflective glass door while soft morning light enters the room.'): Prompt
- `vision_path` (file_upload; optional; default ''): Conditioning Image or Video
- `action_state` (json_editor; optional; default {'actions': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]}): Action Sequence JSON
- `domain_name` (text; optional; default ''): Action Domain
- `resolution` (select; optional; choices 256, 480, 720, 1080; default '256'): Resolution
- `aspect_ratio` (select; optional; choices 1,1, 4,3, 3,4, 16,9, 9,16; default '1,1'): Aspect Ratio
- `num_frames` (number; optional; bounds 1..200; default 1): Frames
- `fps` (number; optional; bounds 10..30; default 24): FPS
- `num_steps` (number; optional; bounds 1..50; default 4): Steps
- `guidance` (slider; optional; bounds 0..7; default 4): Guidance
- `shift` (number; optional; bounds 0..20; default 5): Shift
- `seed` (number; optional; bounds 0..2147483647; default 42): Seed
- `raw_action_dim` (number; optional; bounds 1..1024; default 16): Raw Action Dim
- `action_chunk_size` (number; optional; bounds 1..128; default 16): Action Chunk Size
- `image_size` (number; optional; bounds 64..1024; default 256): Action Image Size

Route: `POST /v1/inference/nvidia-cosmos3-omni`

```json
{
  "action_chunk_size": "{{action_chunk_size}}",
  "action_state": "{{action_state}}",
  "aspect_ratio": "{{aspect_ratio}}",
  "domain_name": "{{domain_name}}",
  "fps": "{{fps}}",
  "guidance": "{{guidance}}",
  "image_size": "{{image_size}}",
  "model_mode": "{{model_mode}}",
  "num_frames": "{{num_frames}}",
  "num_steps": "{{num_steps}}",
  "prompt": "{{prompt}}",
  "raw_action_dim": "{{raw_action_dim}}",
  "resolution": "{{resolution}}",
  "seed": "{{seed}}",
  "shift": "{{shift}}",
  "vision_path": "{{vision_path}}"
}
```

## Exact output

- `image`
- `video`
- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos3-omni-nano` with version key `nano-bf16`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos3-omni` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos3-omni-nano`
- Routes: `/v1/models/nvidia-cosmos3-omni-nano/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos3-omni-nano/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos3-omni-nano/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/world-video-generation/nvidia-cosmos3-omni-nano/SKILL.md
