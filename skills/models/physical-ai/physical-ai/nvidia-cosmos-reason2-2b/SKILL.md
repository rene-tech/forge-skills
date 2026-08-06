---
name: use-forge-nvidia-cosmos-reason2-2b
description: Use exact Forge model nvidia-cosmos-reason2-2b for text, image, video to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos Reason 2 (2B)

- Model slug: `nvidia-cosmos-reason2-2b`
- Family: `nvidia-cosmos-reason2`
- Version: `2b` (`2b`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `nvidia-open-model-license`
- Research status: `source-linked`

## Purpose

Downloadable Cosmos Reason2 2B NIM for physical-world image/video reasoning.

## Use this exact model when

- Use this exact `nvidia-cosmos-reason2-2b` version when the task supplies text, image, video and needs text.
- Downloadable Cosmos Reason2 2B NIM for physical-world image/video reasoning.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'video'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Given a rainy dashcam clip, list the physical cues that show the road is wet and explain how they affect autonomous-driving perception.'): Prompt
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

1. Load this skill and pin model slug `nvidia-cosmos-reason2-2b` with version key `2b`.
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
- Research key: `build-nvidia-com-nvidia-cosmos-reason2-8b-modelcard-ef0d7d8880`
- Recommended: Physical-AI and robotics reasoning over text, image, and video inputs — Primary NVIDIA model-card and documentation sources describe Cosmos Reason 2 as an open reasoning VLM for physical AI and robotics that understands space, time, and fundamental physics and can support embodied-agent reasoning.
- Recommended: Text-only or multimodal query answering for Cosmos-Reason2-8B — Official NVIDIA API documentation states that text-only queries are supported for nvidia/cosmos-reason2-8b, and the model card reports support for text, image, and video inputs.
- Avoid: Clinical or other safety-critical decision-making without expert review and external guardrails — Primary NVIDIA sources say users are responsible for model inputs and outputs and must implement guardrails before deployment, while the audited findings do not provide clinical validation, calibration, or safety-critical deployment guarantees for this checkpoint.
- Avoid: Tasks requiring an immutable published checkpoint revision for strict reproducibility — The audited primary findings do not report an immutable revision identifier for this exact checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Validate outputs in simulation or a bounded sandbox before connecting them to physical systems.
- Do not permit unreviewed model output to actuate safety-critical equipment; retain interlocks, emergency stops, and human control.
- Keep model revision, request, response, environment, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-cosmos-reason2-2b`
- Routes: `/v1/models/nvidia-cosmos-reason2-2b/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos-reason2-2b/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos-reason2-2b/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos-reason2-2b/SKILL.md
