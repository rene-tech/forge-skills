---
name: use-forge-huggingface-lerobot-smolvla-libero
description: Use exact Forge model huggingface-lerobot-smolvla-libero for text, image, robot_state to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hugging Face LeRobot SmolVLA Libero

- Model slug: `huggingface-lerobot-smolvla-libero`
- Family: `huggingface-lerobot-smolvla`
- Version: `libero-31d453f-sm103-sdpa-20z` (`libero`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SmolVLA Libero is a compact LeRobot vision-language-action policy checkpoint trained for LIBERO-style manipulation.

## Use this exact model when

- Use this exact `huggingface-lerobot-smolvla-libero` version when the task supplies text, image, robot_state and needs robot_action, json.
- SmolVLA Libero is a compact LeRobot vision-language-action policy checkpoint trained for LIBERO-style manipulation.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Pick up the red cube and place it in the target bowl.'): Instruction
- `camera1_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 1 Image
- `camera2_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 2 Image
- `camera3_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Camera 3 Image
- `robot_state` (json_editor; optional; default [0, 0, 0, 0, 0, 0, 0, 0]): 8D Robot State
- `robot_type` (select; optional; choices so100_follower, so101_follower; default 'so100_follower'): Robot Type
- `return_chunk` (checkbox; optional; default False): Return Action Chunk

Route: `POST /v1/inference/huggingface-lerobot-smolvla-libero`

```json
{
  "images": {
    "camera1": "{{camera1_image}}",
    "camera2": "{{camera2_image}}",
    "camera3": "{{camera3_image}}"
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

1. Load this skill and pin model slug `huggingface-lerobot-smolvla-libero` with version key `libero`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/huggingface-lerobot-smolvla-libero` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-lerobot-smolvla-libero-13a04e8a43`
- Recommended: Research and development on compact vision-language-action policy modeling (SmolVLA-family) and LIBERO-style sensorimotor policy experiments — The model card/README characterizes the checkpoint as a compact, efficient SmolVLA-family vision-language-action model and the repository config.json documents normalization mappings, tokenizer_max_length, and dimensionality flags that match vision-language-action research payloads.
- Avoid: Clinical, medical, or other regulated safety‑critical decision making — The examined primary artifacts (model card / config.json) do not present documentation of clinical validation, PHI handling, or domain-specific expert-review processes for this checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingface-lerobot-smolvla-libero`
- Routes: `/v1/models/huggingface-lerobot-smolvla-libero/inference-routes`
- Regional deployment: `/v1/models/huggingface-lerobot-smolvla-libero/regional-deployment`
- Serverless handoff: `/v1/models/huggingface-lerobot-smolvla-libero/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/huggingface-lerobot-smolvla-libero/SKILL.md
