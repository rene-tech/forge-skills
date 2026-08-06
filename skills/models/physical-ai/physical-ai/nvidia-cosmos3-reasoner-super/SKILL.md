---
name: use-forge-nvidia-cosmos3-reasoner-super
description: Use exact Forge model nvidia-cosmos3-reasoner-super for text, image, video to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Cosmos 3 Reasoner (Super)

- Model slug: `nvidia-cosmos3-reasoner-super`
- Family: `nvidia-cosmos3-reasoner`
- Version: `super-bf16-ea` (`super-bf16`)
- Hierarchy: `models / physical-ai / physical-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `nvidia-software-model-evaluation-license`
- Research status: `source-linked`

## Purpose

Early-access Cosmos 3 Super Reasoner VLM served through a Forge-owned Qwen3-VL runtime.

## Use this exact model when

- Use this exact `nvidia-cosmos3-reasoner-super` version when the task supplies text, image, video and needs text.
- Early-access Cosmos 3 Super Reasoner VLM served through a Forge-owned Qwen3-VL runtime.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image', 'video'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `mode` (select; optional; choices text, image, video; default 'text'): Mode
- `messages` (chat_history; optional; default 'Analyze whether a humanoid robot should open a glass door in this scene and explain the physical evidence.'): Prompt
- `input_image` (file_upload; optional; default ''): Input Image
- `input_video` (file_upload; optional; default ''): Input Video
- `temperature` (slider; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

Route: `POST /v1/inference/nvidia-cosmos3-reasoner`

```json
{
  "image": "{{input_image}}",
  "max_tokens": "{{max_tokens}}",
  "messages": "{{messages}}",
  "mode": "{{mode}}",
  "temperature": "{{temperature}}",
  "video": "{{input_video}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `nvidia-cosmos3-reasoner-super` with version key `super-bf16`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvidia-cosmos3-reasoner` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-nvidia-cosmos-ea-cosmos3-super-reasoner-e2bbd9dcb7`
- Recommended: Multimodal vision-language reasoning and text responses grounded in images and video for Physical AI research and prototyping — Hugging Face model page and the NGC container listing describe Cosmos3 Super/Reasoner as a multimodal VLM that accepts text, images, and video and returns coherent text responses aimed at Physical AI/robotics reasoning.
- Avoid: Treating Reasoner outputs as safety-certified control commands or as guaranteed physically accurate simulations for closed-loop control — Evidence gap: The provided primary findings do not include a primary-source statement or certification that Cosmos3 Super-Reasoner outputs are suitable as safety-certified control commands or guaranteed physically accurate simulation; per-input bounds, safety certification, and validated control guarantees were not found in the checked primary sources.
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

- Model: `/v1/models/nvidia-cosmos3-reasoner-super`
- Routes: `/v1/models/nvidia-cosmos3-reasoner-super/inference-routes`
- Regional deployment: `/v1/models/nvidia-cosmos3-reasoner-super/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-cosmos3-reasoner-super/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/physical-ai/physical-ai/nvidia-cosmos3-reasoner-super/SKILL.md
