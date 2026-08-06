---
name: use-forge-huggingface-lerobot-smolvla-robocasa
description: Use exact Forge model huggingface-lerobot-smolvla-robocasa for text, image, robot_state to robot_action. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Hugging Face LeRobot SmolVLA RoboCasa

- Model slug: `huggingface-lerobot-smolvla-robocasa`
- Family: `huggingface-lerobot-smolvla`
- Version: `robocasa-38d38bf-wrapper-candidate-20260601t03z` (`robocasa`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Hidden onboarding candidate for lerobot/smolvla_robocasa, a SmolVLA-family vision-language-action policy fine-tuned on the RoboCasa target-human unified dataset.

## Use this exact model when

- Use this exact `huggingface-lerobot-smolvla-robocasa` version when the task supplies text, image, robot_state and needs robot_action.
- Hidden onboarding candidate for lerobot/smolvla_robocasa, a SmolVLA-family vision-language-action policy fine-tuned on the RoboCasa target-human unified dataset.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Open the cabinet and place the mug on the counter.'): Instruction
- `robot0_agentview_left_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Left Agent View
- `robot0_agentview_right_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Right Agent View
- `robot0_eye_in_hand_image` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYGAAAAAEAAGjChXjAAAAAElFTkSuQmCC'): Eye In Hand
- `robot_state` (json_editor; optional; default [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]): 16D Robot State
- `robot_type` (select; optional; choices so100_follower, so101_follower; default 'so100_follower'): Robot Type
- `return_chunk` (checkbox; optional; default True): Return Action Chunk

Route: `POST /v1/inference/huggingface-lerobot-smolvla-robocasa`

```json
{
  "images": {
    "robot0_agentview_left": "{{robot0_agentview_left_image}}",
    "robot0_agentview_right": "{{robot0_agentview_right_image}}",
    "robot0_eye_in_hand": "{{robot0_eye_in_hand_image}}"
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

## Required workflow

1. Load this skill and pin model slug `huggingface-lerobot-smolvla-robocasa` with version key `robocasa`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/huggingface-lerobot-smolvla-robocasa` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-lerobot-smolvla-robocasa-88ddb05336`
- Recommended: Use as a RoboCasa robotics policy checkpoint within the LeRobot framework — The Hugging Face model card identifies the checkpoint as lerobot/smolvla_robocasa and describes SmolVLA as a compact vision-language-action model trained/pushed using LeRobot (model-card).
- Recommended: Family-level SmolVLA fine-tuning or adaptation workflows using the LeRobot toolchain (apply cautiously to this checkpoint) — The model card indicates SmolVLA family intent and that the model was trained/pushed with LeRobot; this supports family-level fine-tuning/adaptation guidance but not checkpoint-scoped templates.
- Recommended: RoboCasa-targeted development using the training-data lineage stated in the checkpoint commit metadata — The commit metadata lists pretrained_path 'lerobot/smolvla_base' and identifies the checkpoint as tied to RoboCasa-target training metadata (commit page).
- Avoid: Selecting this checkpoint on the basis of verified public benchmark superiority — No checkpoint-scoped public benchmark table rows (dataset, split, metric, value) were present in the checked primary sources for lerobot/smolvla_robocasa.
- Avoid: Treating the checkpoint as a fully specified control-interface contract (serialized request schema, robot-state field names, action units/bounds, confidence semantics) — Commit metadata and model card provide configuration values but do not expose a full serialized request schema, explicit robot-state field names, action units or bounds, or output-confidence semantics for this checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingface-lerobot-smolvla-robocasa`
- Routes: `/v1/models/huggingface-lerobot-smolvla-robocasa/inference-routes`
- Regional deployment: `/v1/models/huggingface-lerobot-smolvla-robocasa/regional-deployment`
- Serverless handoff: `/v1/models/huggingface-lerobot-smolvla-robocasa/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/huggingface-lerobot-smolvla-robocasa/SKILL.md
