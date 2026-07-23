---
name: use-forge-allenai-molmoact2-so100-101
description: Use exact Forge model allenai-molmoact2-so100-101 for text, image, robot_state to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use AllenAI MolmoAct2 SO100/101

- Model slug: `allenai-molmoact2-so100-101`
- Family: `allenai-molmoact2`
- Version: `so100-101-152569f-wrapper-20260529t03z` (`so100-101`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `experimental`
- Default eligible: `false`
- License: `Apache-2.0`
- Research status: `source-linked`

## Purpose

MolmoAct2-SO100_101 is AllenAI's MolmoAct2 checkpoint fine-tuned for SO-100/101 single-arm robot policy inference.

## Use this exact model when

- Use this exact `allenai-molmoact2-so100-101` version when the task supplies text, image, robot_state and needs robot_action, json.
- MolmoAct2-SO100_101 is AllenAI's MolmoAct2 checkpoint fine-tuned for SO-100/101 single-arm robot policy inference.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'robot_state'] → ['robot_action', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'Move the arm towards the lemon, grasp it, lift it up, and drop it into the red bowl.'): Instruction
- `top_cam` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Realsense Top RGB
- `side_cam` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Realsense Side RGB
- `robot_state` (json_editor; optional; default [-0.52734375, 189.140625, 181.40625, 60.64453125, -3.603515625, 1.0971786975860596]): 6D SO100/101 State
- `num_steps` (number; optional; bounds 1..50; default 10): Flow Steps
- `enable_cuda_graph` (checkbox; optional; default False): CUDA Graph

Route: `POST /v1/inference/allenai-molmoact2-so100-101`

```json
{
  "enable_cuda_graph": "{{enable_cuda_graph}}",
  "images": {
    "side": "{{side_cam}}",
    "top": "{{top_cam}}"
  },
  "instruction": "{{instruction}}",
  "model": "{{model_slug}}",
  "num_steps": "{{num_steps}}",
  "robot_state": "{{robot_state}}"
}
```

## Exact output

- `robot_action`
- `json`

## Required workflow

1. Load this skill and pin model slug `allenai-molmoact2-so100-101` with version key `so100-101`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/allenai-molmoact2-so100-101` using the declared request template.
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

- Model: `/v1/models/allenai-molmoact2-so100-101`
- Routes: `/v1/models/allenai-molmoact2-so100-101/inference-routes`
- Regional deployment: `/v1/models/allenai-molmoact2-so100-101/regional-deployment`
- Serverless handoff: `/v1/models/allenai-molmoact2-so100-101/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/allenai-molmoact2-so100-101/SKILL.md
