---
name: use-forge-nvidia-cosmos-policy-libero-predict2-fp8
description: Use exact Forge model nvidia-cosmos-policy-libero-predict2-fp8 for text, image, proprio to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Policy LIBERO 2B (FP8, Blackwell/Hopper)

- Model slug: `nvidia-cosmos-policy-libero-predict2-fp8`
- Family: `nvidia-cosmos-policy-libero-predict2`
- Version: `fp8` (`fp8`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `experimental`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

FP8 dynamic-activation/weight variant of the LIBERO checkpoint using torchao Float8DynamicActivationFloat8WeightConfig(PerTensor) and torch.compile(max-autotune).

## Use this exact model when

- Use this exact `nvidia-cosmos-policy-libero-predict2-fp8` version when the task supplies text, image, proprio and needs json.
- FP8 dynamic-activation/weight variant of the LIBERO checkpoint using torchao Float8DynamicActivationFloat8WeightConfig(PerTensor) and torch.compile(max-autotune).
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'proprio'] → ['json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `task_description` (textarea; optional; default 'put both the alphabet soup and the tomato sauce in the basket'): Task Description
- `observation` (json_editor; optional; default '{"use_sample_observation": true}'): Observation JSON
- `seed` (number; optional; bounds 0..999999; default 195): Seed
- `num_denoising_steps_action` (number; optional; bounds 1..32; default 5): Denoising Steps

Route: `POST /v1/inference/nvidia-cosmos-policy-libero-2b-nvfp4`

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

1. Load this skill and pin model slug `nvidia-cosmos-policy-libero-predict2-fp8` with version key `fp8`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos-policy-libero-2b-nvfp4` using the declared request template.
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

- Model: `/v1/models/nvidia-cosmos-policy-libero-predict2-fp8`
- Routes: `/v1/models/nvidia-cosmos-policy-libero-predict2-fp8/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-policy-libero-predict2-fp8/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-policy-libero-predict2-fp8/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-policy-libero-predict2-fp8/SKILL.md
