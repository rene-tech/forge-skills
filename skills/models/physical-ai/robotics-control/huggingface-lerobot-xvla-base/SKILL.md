---
name: use-forge-huggingface-lerobot-xvla-base
description: Use exact Forge model huggingface-lerobot-xvla-base for text, image, robot_state to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hugging Face LeRobot X-VLA Base

- Model slug: `huggingface-lerobot-xvla-base`
- Family: `huggingface-lerobot-xvla`
- Version: `base-cdb7964e-wrapper-artifactkeys-20260529t07z` (`base`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

X-VLA Base is an Apache-2.0 LeRobot vision-language-action policy checkpoint with 0.9B parameters, soft-prompted flow matching, three visual observations, an 8D robot state, and 20D ee6d robot actions.

## Use this exact model when

- Use this exact `huggingface-lerobot-xvla-base` version when the task supplies text, image, robot_state and needs robot_action, json.
- X-VLA Base is an Apache-2.0 LeRobot vision-language-action policy checkpoint with 0.9B parameters, soft-prompted flow matching, three visual observations, an 8D robot state, and 20D ee6d robot actions.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Pick up the object and place it at the target location.'): Instruction
- `image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAACAElEQVR42u3TQQ0AAAjEsJOKBCQgnTcaaFIFS5bqgbciAQYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABMIAKGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAbAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAGUAEDgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwAFwLkuoTsZ4H69MAAAAASUVORK5CYII='): Image
- `image2` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAACAElEQVR42u3TQQ0AAAjEsJOKBCQgnTcaaFIFS5bpgrciAQYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABMIAKGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAYAA4ABwABgADAAGAAMAAbAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAGUAEDgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAAGAAMAAYAAwABgADgAHAABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwABgADAAGAAOAAcAAYAAwAFwLlqoTsaF6wR8AAAAASUVORK5CYII='): Image 2
- `image3` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOAAAADgCAIAAACVT/22AAABr0lEQVR42u3SAQkAAAgEsY9qBCMY3RoKgyU4Lj0FZ0UCDAoGxaBgUDAoBgWDYlAwKBgUg4JBMSgYFAyKQcGgGBQMCgbFoGBQDKoCBgWDYlAwKBgUg4JBMSgYFAyKQcGgGBQMCgbFoGBQDAoGBYNiUDAoBlUBg4JBMSgYFAyKQcGgGBQMCgbFoGBQDAoGBYNiUDAoBgWDgkExKBgUg4JBwaAYFAwKBsWgYFAMCgYFg2JQMCgGBYOCQTEoGBSDgkHBoBgUDIpBwaBgUAwKBgWDYlAwKAYFg4JBMSgYFIOCQcGgGBQMikHBoGBQDAoGxaBgUDAoBgWDgkExKBgUg4JBwaAYFAyKQcGgYFAMCgbFoGBQMCgGBYNiUDAoGBSDgkHBoBgUDIpBwaBgUAwKBsWgYFAwKAYFg2JQMCgYFIOCQTEoGBQMikHBoGBQDAoGxaBgUDAoBgWDYlAwKBgUg4JBMSgYFAyKQcGgGBQMCgbFoGBQMCgGBYNiUDAoGBSDgkExKBgUDIpBwaAYFAwKBsWgYFAMCgYFg2JQMCgYFIOCQTEoGBQMikHBoBgUDAoG5aMFsn9PELKPO74AAAAASUVORK5CYII='): Image 3
- `robot_state` (json_editor; optional; default [0, 0, 0, 0, 0, 0, 0, 0]): 8D Robot State
- `robot_type` (select; optional; choices libero; default 'libero'): Robot Type
- `domain_id` (number; optional; bounds 0..6; default 0): Domain ID
- `return_chunk` (checkbox; optional; default True): Return Action Chunk

Route: `POST /v1/inference/huggingface-lerobot-xvla-base`

```json
{
  "domain_id": "{{domain_id}}",
  "images": {
    "image": "{{image}}",
    "image2": "{{image2}}",
    "image3": "{{image3}}"
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

1. Load this skill and pin model slug `huggingface-lerobot-xvla-base` with version key `base`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/huggingface-lerobot-xvla-base` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-lerobot-xvla-base-b834a228b7`
- Recommended: Foundation policy pretraining and backbone for cross-embodiment research (Phase I pretrained backbone for downstream Phase II adaptation). — Hugging Face docs and the model card present the checkpoint as the X-VLA base model intended for Phase I pretraining and as a pretrained backbone for Phase II adaptation; the paper and docs describe soft prompts and cross-embodiment methodology supporting this use.
- Recommended: Research and development of soft-prompted cross-embodiment policies and Phase II domain-adaptation experiments (simulation and multi-platform pretraining research). — The canonical paper and Hugging Face docs describe soft prompts as the mechanism to represent hardware/domain variation and document Phase II domain adaptation practices, indicating the base checkpoint is suitable as a research backbone for soft-prompt and cross-embodiment method development.
- Avoid: Direct deployment of the raw base checkpoint as a final real-robot controller without Phase II adaptation or appropriate action postprocessing. — Primary documentation describes the base checkpoint as offering a 20-dimensional output for pretrained compatibility and documents padding/trimming behavior (20↔real_dim) and an `auto` action mode; the base checkpoint is presented as a pretrained backbone that requires Phase II adaptation and appropriate postprocessing for deployment.
- Avoid: Assuming numeric benchmarked performance (checkpoint-scoped success rates) for lerobot/xvla-base without Phase II evaluation. — Hugging Face documentation reports numeric results for other named checkpoints (e.g., lerobot/xvla-libero, lerobot/xvla-widowx, lerobot/xvla-folding) but does not attribute checkpoint-scoped numeric evaluation tables to lerobot/xvla-base in the inspected canonical sources.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingface-lerobot-xvla-base`
- Routes: `/v1/models/huggingface-lerobot-xvla-base/inference-routes`
- Regional deployment: `/v1/models/huggingface-lerobot-xvla-base/regional-deployment`
- Serverless handoff: `/v1/models/huggingface-lerobot-xvla-base/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/huggingface-lerobot-xvla-base/SKILL.md
