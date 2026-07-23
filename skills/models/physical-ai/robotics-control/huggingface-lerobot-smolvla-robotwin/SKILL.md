---
name: use-forge-huggingface-lerobot-smolvla-robotwin
description: Use exact Forge model huggingface-lerobot-smolvla-robotwin for text, image, robot_state to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hugging Face LeRobot SmolVLA RobotWin

- Model slug: `huggingface-lerobot-smolvla-robotwin`
- Family: `huggingface-lerobot-smolvla`
- Version: `robotwin-967623a-wrapper-candidate-20260528t09z` (`robotwin`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SmolVLA RobotWin is an Apache-2.0 LeRobot SmolVLA policy checkpoint fine-tuned from lerobot/smolvla_base on the pepijn223/robotwin_unified_v3 dataset.

## Use this exact model when

- Use this exact `huggingface-lerobot-smolvla-robotwin` version when the task supplies text, image, robot_state and needs robot_action, json.
- SmolVLA RobotWin is an Apache-2.0 LeRobot SmolVLA policy checkpoint fine-tuned from lerobot/smolvla_base on the pepijn223/robotwin_unified_v3 dataset.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Pick up the object and place it at the target location.'): Instruction
- `cam_high_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): High Camera Image
- `cam_left_wrist_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Left Wrist Camera Image
- `cam_right_wrist_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Right Wrist Camera Image
- `robot_state` (json_editor; optional; default [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]): 14D Robot State
- `robot_type` (select; optional; choices so100_follower, so101_follower; default 'so100_follower'): Robot Type
- `return_chunk` (checkbox; optional; default True): Return Action Chunk

Route: `POST /v1/inference/huggingface-lerobot-smolvla-robotwin`

```json
{
  "images": {
    "cam_high": "{{cam_high_image}}",
    "cam_left_wrist": "{{cam_left_wrist_image}}",
    "cam_right_wrist": "{{cam_right_wrist_image}}"
  },
  "instruction": "{{instruction}}",
  "model": "{{model_slug}}",
  "return_chunk": "{{return_chunk}}",
  "robot_state": "{{robot_state}}",
  "robot_type": "{{robot_type}}"
}
```

## Exact output

- `robot_action`
- `json`

## Required workflow

1. Load this skill and pin model slug `huggingface-lerobot-smolvla-robotwin` with version key `robotwin`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/huggingface-lerobot-smolvla-robotwin` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingface-lerobot-smolvla-robotwin`
- Routes: `/v1/models/huggingface-lerobot-smolvla-robotwin/inference-routes`
- Regional deployment: `/v1/models/huggingface-lerobot-smolvla-robotwin/regional-deployment`
- Serverless handoff: `/v1/models/huggingface-lerobot-smolvla-robotwin/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/huggingface-lerobot-smolvla-robotwin/SKILL.md
