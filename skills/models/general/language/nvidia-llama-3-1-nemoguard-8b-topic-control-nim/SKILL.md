---
name: use-forge-nvidia-llama-3-1-nemoguard-8b-topic-control-nim
description: Use exact Forge model nvidia-llama-3-1-nemoguard-8b-topic-control-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.1 NemoGuard 8B Topic Control

- Model slug: `nvidia-llama-3-1-nemoguard-8b-topic-control-nim`
- Family: `nvidia-llama-3-1-nemoguard-8b-topic-control`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-ai-foundation-models-community-license`
- Research status: `source-linked`

## Purpose

NVIDIA Llama 3.1 NemoGuard 8B Topic Control packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.

## Use this exact model when

- Use this exact `nvidia-llama-3-1-nemoguard-8b-topic-control-nim` version when the task supplies text and needs text.
- NVIDIA Llama 3.1 NemoGuard 8B Topic Control packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default "Classify the topic of this request: 'Summarize the GPU support matrix for a model rollout.' Return a short rationale."): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 256): Max Tokens

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

1. Load this skill and pin model slug `nvidia-llama-3-1-nemoguard-8b-topic-control-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-1-nemoguard-8b-topic-control-nim`
- Routes: `/v1/models/nvidia-llama-3-1-nemoguard-8b-topic-control-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-1-nemoguard-8b-topic-control-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-1-nemoguard-8b-topic-control-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/nvidia-llama-3-1-nemoguard-8b-topic-control-nim/SKILL.md
