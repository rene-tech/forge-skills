---
name: use-forge-nvidia-cosmos-reason2-8b
description: Use exact Forge model nvidia-cosmos-reason2-8b for text, image, video to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Reason 2 (8B)

- Model slug: `nvidia-cosmos-reason2-8b`
- Family: `nvidia-cosmos-reason2`
- Version: `v1` (`v1`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-open-model-license`
- Research status: `source-linked`

## Purpose

Physical AI reasoning model for robotics and world understanding, packaged as a self-hosted NVIDIA NIM.

## Use this exact model when

- Use this exact `nvidia-cosmos-reason2-8b` version when the task supplies text, image, video and needs text.
- Physical AI reasoning model for robotics and world understanding, packaged as a self-hosted NVIDIA NIM.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'video'] → ['text'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'What are three safe next steps for a robot approaching a glass door?'): Prompt
- `temperature` (slider; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (slider; optional; bounds 1..4096; default 256): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": "{{messages}}",
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos-reason2-8b` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-cosmos-reason2-8b-8b6e315315`
- Recommended: Multimodal physical-AI reasoning and explanatory text generation (image/video + text) for research, development, and non-safety-critical prototyping — The upstream Hugging Face model page and NVIDIA cookbook/repository materials describe the model as an ~8B multimodal reasoning vision-language model intended for Physical AI/robotics reasoning tasks and provide example prompts, recipes, and inference workflows supporting this use.
- Avoid: Treating generated text as calibrated probabilities or using raw model text outputs as calibrated confidence scores for direct actuation without external validation — No publisher-provided checkpoint-scoped calibration semantics or canonical post-inference calibration procedures for textual outputs were found in the inspected upstream artifacts; do not assume generated text corresponds to calibrated probability scores without external calibration/validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-reason2-8b`
- Routes: `/v1/models/nvidia-cosmos-reason2-8b/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-reason2-8b/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-reason2-8b/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-reason2-8b/SKILL.md
