---
name: use-forge-huggingface-lerobot-smolvla-libero-plus
description: Use exact Forge model huggingface-lerobot-smolvla-libero-plus for text, image, robot_state to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hugging Face LeRobot SmolVLA Libero Plus

- Model slug: `huggingface-lerobot-smolvla-libero-plus`
- Family: `huggingface-lerobot-smolvla`
- Version: `libero-plus-7bb70aa-state8-sm103-sdpa-02z` (`libero-plus`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `experimental`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SmolVLA Libero Plus is a compact LeRobot vision-language-action policy checkpoint trained for LIBERO Plus-style manipulation.

## Use this exact model when

- Use this exact `huggingface-lerobot-smolvla-libero-plus` version when the task supplies text, image, robot_state and needs robot_action, json.
- SmolVLA Libero Plus is a compact LeRobot vision-language-action policy checkpoint trained for LIBERO Plus-style manipulation.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Pick up the red cube and place it in the target bowl.'): Instruction
- `camera1_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 1 Image
- `camera2_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 2 Image
- `camera3_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 3 Image
- `empty_camera_0_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Empty Camera 0
- `empty_camera_1_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Empty Camera 1
- `robot_state` (json_editor; optional; default [0, 0, 0, 0, 0, 0, 0, 0]): 8D Robot State
- `robot_type` (select; optional; choices so100_follower, so101_follower; default 'so100_follower'): Robot Type
- `return_chunk` (checkbox; optional; default False): Return Action Chunk

Route: `POST /v1/inference/huggingface-lerobot-smolvla-libero-plus`

```json
{
  "images": {
    "camera1": "{{camera1_image}}",
    "camera2": "{{camera2_image}}",
    "camera3": "{{camera3_image}}",
    "empty_camera_0": "{{empty_camera_0_image}}",
    "empty_camera_1": "{{empty_camera_1_image}}"
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

1. Load this skill and pin model slug `huggingface-lerobot-smolvla-libero-plus` with version key `libero-plus`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/huggingface-lerobot-smolvla-libero-plus` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-lerobot-smolvla-libero-plus-2c9c8f8e10`
- Recommended: Research and prototyping of vision-language-action policies for manipulation tasks (simulation or lab), using the checkpoint's VLM and action head as provided. — The model card and config.json describe a compact SmolVLA vision-language-action checkpoint, document inputs (text, images, state) and an action output feature, and state the model is intended as a compact/efficient VLA model suitable for consumer-grade hardware and research use.
- Recommended: Low-resource local inference for robotics experimentation where a compact VLM is required (research/prototyping only). — The model card text and model naming describe SmolVLA as compact and deployable on consumer-grade hardware; configuration indicates use_amp=false and device 'cuda' in the repo guidance.
- Avoid: Deployment for safety-critical autonomous robotic operation without human oversight or expert system-level validation. — Evidence gap: Safety-critical autonomous deployment without human oversight or expert-system validation is not documented in primary sources.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingface-lerobot-smolvla-libero-plus`
- Routes: `/v1/models/huggingface-lerobot-smolvla-libero-plus/inference-routes`
- Regional deployment: `/v1/models/huggingface-lerobot-smolvla-libero-plus/regional-deployment`
- Serverless handoff: `/v1/models/huggingface-lerobot-smolvla-libero-plus/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/huggingface-lerobot-smolvla-libero-plus/SKILL.md
