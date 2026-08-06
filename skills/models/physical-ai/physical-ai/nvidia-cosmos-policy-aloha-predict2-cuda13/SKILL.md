---
name: use-forge-nvidia-cosmos-policy-aloha-predict2-cuda13
description: Use exact Forge model nvidia-cosmos-policy-aloha-predict2-cuda13 for text, image, proprio to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Policy ALOHA Predict2 2B (CUDA 13, B300)

- Model slug: `nvidia-cosmos-policy-aloha-predict2-cuda13`
- Family: `nvidia-cosmos-policy-aloha-predict2`
- Version: `cuda13` (`cuda13`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

B300-oriented Cosmos Policy ALOHA serving build.

## Use this exact model when

- Use this exact `nvidia-cosmos-policy-aloha-predict2-cuda13` version when the task supplies text, image, proprio and needs json.
- B300-oriented Cosmos Policy ALOHA serving build.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'proprio'] → ['json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `task_description` (textarea; optional; default 'fold the shirt'): Task Description
- `use_sample_observation` (checkbox; optional; default True): Use Placeholder Observation
- `primary_image` (file_upload; optional; default ''): Primary Camera Image
- `left_wrist_image` (file_upload; optional; default ''): Left Wrist Camera Image
- `right_wrist_image` (file_upload; optional; default ''): Right Wrist Camera Image
- `proprio` (json_editor; optional; default '[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'): ALOHA Proprioception
- `randomize_seed` (checkbox; optional; default False): Randomize Seed
- `seed` (number; optional; bounds 0..999999; default 195): Seed
- `num_denoising_steps_action` (number; optional; bounds 1..32; default 10): Action Denoising Steps

Route: `POST /v1/inference/nvidia-cosmos-policy-aloha-predict2-2b`

```json
{
  "model": "{{model_slug}}",
  "num_denoising_steps_action": "{{num_denoising_steps_action}}",
  "observation": {
    "left_wrist_image": "{{left_wrist_image}}",
    "primary_image": "{{primary_image}}",
    "proprio": "{{proprio}}",
    "right_wrist_image": "{{right_wrist_image}}",
    "use_sample_observation": "{{use_sample_observation}}"
  },
  "randomize_seed": "{{randomize_seed}}",
  "seed": "{{seed}}",
  "task_description": "{{task_description}}"
}
```

## Exact output

- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-policy-aloha-predict2-cuda13` with version key `cuda13`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-policy-aloha-predict2-2b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-nvlabs-cosmos-policy-blob-main-aloha-md-93a4d0fefa`
- Recommended: Research and development of bimanual robot manipulation policies and evaluation on the ALOHA platform (contact-rich manipulation, imitation from human teleoperation demonstrations). — Primary model artifacts and repository guidance document the checkpoint as a 2B-parameter policy fine-tuned from a Predict2-2B video foundation model on ALOHA teleoperation data and provide ALOHA experiment guidance and example evaluation scripts suitable for R&D evaluation.
- Avoid: Commercial deployment without obtaining an appropriate commercial license. — Primary checkpoint artifacts declare the NVIDIA One‑Way Noncommercial License (NSCLv1) for the base and planning checkpoints, which restricts commercial use per the model README/config artifacts.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-policy-aloha-predict2-cuda13`
- Routes: `/v1/models/nvidia-cosmos-policy-aloha-predict2-cuda13/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-policy-aloha-predict2-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-policy-aloha-predict2-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-policy-aloha-predict2-cuda13/SKILL.md
