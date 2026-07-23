---
name: use-forge-rail-berkeley-octo-small-1-5
description: Use exact Forge model rail-berkeley-octo-small-1-5 for text, image to robot_action, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use RAIL Berkeley Octo Small

- Model slug: `rail-berkeley-octo-small-1-5`
- Family: `rail-berkeley-octo`
- Version: `small-1.5-cuda13-jax-clip-20260528tcurrent` (`small-1-5`)
- Hierarchy: `models / physical-ai / robotics-control`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

Octo Small 1.5 is a 27M-parameter transformer-based generalist robot policy trained on a mix of Open X-Embodiment robot datasets.

## Use this exact model when

- Use this exact `rail-berkeley-octo-small-1-5` version when the task supplies text, image and needs robot_action, json.
- Octo Small 1.5 is a 27M-parameter transformer-based generalist robot policy trained on a mix of Open X-Embodiment robot datasets.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['robot_action', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `instruction` (textarea; optional; default 'pick up the spoon'): Instruction
- `image_primary_t_minus_1` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Primary Image T-1
- `image_primary_t` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Primary Image T
- `image_wrist_t_minus_1` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Wrist Image T-1
- `image_wrist_t` (file_upload; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAIAAAD91JpzAAAAFklEQVR42mP8//8/AwMDEwMDAwMDAwAkBgMB/umWrAAAAABJRU5ErkJggg=='): Wrist Image T
- `stats_key` (select; optional; choices bridge_dataset; default 'bridge_dataset'): Action Statistics
- `num_samples` (number; optional; bounds 1..4; default 1): Samples
- `argmax` (checkbox; optional; default False): Deterministic
- `temperature` (number; optional; bounds 0.1..2.0; default 1.0): Temperature

Route: `POST /v1/inference/rail-berkeley-octo-small-1-5`

```json
{
  "argmax": "{{argmax}}",
  "image_primary_t": "{{image_primary_t}}",
  "image_primary_t_minus_1": "{{image_primary_t_minus_1}}",
  "image_wrist_t": "{{image_wrist_t}}",
  "image_wrist_t_minus_1": "{{image_wrist_t_minus_1}}",
  "language_instruction": "{{instruction}}",
  "model": "{{model_slug}}",
  "num_samples": "{{num_samples}}",
  "stats_key": "{{stats_key}}",
  "temperature": "{{temperature}}"
}
```

## Exact output

- `robot_action`
- `json`

## Required workflow

1. Load this skill and pin model slug `rail-berkeley-octo-small-1-5` with version key `small-1-5`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/rail-berkeley-octo-small-1-5` using the declared request template.
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

- Model: `/v1/models/rail-berkeley-octo-small-1-5`
- Routes: `/v1/models/rail-berkeley-octo-small-1-5/inference-routes`
- Regional deployment: `/v1/models/rail-berkeley-octo-small-1-5/regional-deployment`
- Serverless handoff: `/v1/models/rail-berkeley-octo-small-1-5/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/robotics-control/rail-berkeley-octo-small-1-5/SKILL.md
