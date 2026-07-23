---
name: use-forge-nvidia-cosmos-policy-libero-predict2-cuda13
description: Use exact Forge model nvidia-cosmos-policy-libero-predict2-cuda13 for text, image, proprio to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Policy LIBERO Predict2 2B (CUDA 13)

- Model slug: `nvidia-cosmos-policy-libero-predict2-cuda13`
- Family: `nvidia-cosmos-policy-libero-predict2`
- Version: `cuda13` (`cuda13`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Cosmos Policy LIBERO checkpoint wrapped as a Forge custom container.

## Use this exact model when

- Use this exact `nvidia-cosmos-policy-libero-predict2-cuda13` version when the task supplies text, image, proprio and needs json.
- Cosmos Policy LIBERO checkpoint wrapped as a Forge custom container.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'proprio'] → ['json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `task_description` (textarea; optional; default 'put both the alphabet soup and the tomato sauce in the basket'): Task Description
- `observation` (json_editor; optional; default '{"use_sample_observation": true}'): Observation JSON
- `seed` (number; optional; bounds 0..999999; default 195): Seed
- `num_denoising_steps_action` (number; optional; bounds 1..32; default 5): Denoising Steps

Route: `POST /v1/inference/nvidia-cosmos-policy-libero-predict2-2b`

```json
{
  "model": "{{model_slug}}",
  "num_denoising_steps_action": "{{num_denoising_steps_action}}",
  "observation": "{{observation}}",
  "seed": "{{seed}}",
  "task_description": "{{task_description}}"
}
```

## Exact output

- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-policy-libero-predict2-cuda13` with version key `cuda13`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-policy-libero-predict2-2b` using the declared request template.
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

- Model: `/v1/models/nvidia-cosmos-policy-libero-predict2-cuda13`
- Routes: `/v1/models/nvidia-cosmos-policy-libero-predict2-cuda13/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-policy-libero-predict2-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-policy-libero-predict2-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-policy-libero-predict2-cuda13/SKILL.md
