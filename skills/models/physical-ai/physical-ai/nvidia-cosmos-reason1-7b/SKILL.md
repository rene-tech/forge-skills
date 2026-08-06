---
name: use-forge-nvidia-cosmos-reason1-7b
description: Use exact Forge model nvidia-cosmos-reason1-7b for text, image, video to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Reason 1 (7B)

- Model slug: `nvidia-cosmos-reason1-7b`
- Family: `nvidia-cosmos-reason1`
- Version: `v1` (`v1`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `experimental`
- Default eligible: `false`
- License: `nvidia-open-model-license`
- Research status: `source-linked`

## Purpose

Deprecated but still self-hostable NVIDIA Physical AI reasoning VLM for robotics and world understanding.

## Use this exact model when

- Use this exact `nvidia-cosmos-reason1-7b` version when the task supplies text, image, video and needs text.
- Deprecated but still self-hostable NVIDIA Physical AI reasoning VLM for robotics and world understanding.
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

1. Load this skill and pin model slug `nvidia-cosmos-reason1-7b` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-cosmos-reason1-7b-aa71847c2f`
- Recommended: Plan and reason about embodied actions in physical environments for robotic systems — Research findings (Hugging Face model card and NVIDIA research page) describe Cosmos-Reason1-7B as designed for physical AI and embodied reasoning and list robot-planning/embodied reasoning as intended application classes.
- Recommended: Multimodal scene understanding to support robotics planning and non-clinical safety-relevant reasoning pipelines — The Hugging Face model page and repository commit facts in the findings state the model accepts text, image, and video and is intended for physical-AI and embodied-reasoning tasks.
- Avoid: High-stakes clinical or medical decision-making without explicit expert validation and authorization — Evidence gap: the supplied primary findings do not include a primary-source statement authorizing clinical use or enumerating clinical-authorization/validation procedures for Cosmos-Reason1-7B; therefore the dossier cannot confirm safe/authorized clinical use from the provided artifacts.
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

- Model: `/v1/models/nvidia-cosmos-reason1-7b`
- Routes: `/v1/models/nvidia-cosmos-reason1-7b/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-reason1-7b/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-reason1-7b/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-reason1-7b/SKILL.md
