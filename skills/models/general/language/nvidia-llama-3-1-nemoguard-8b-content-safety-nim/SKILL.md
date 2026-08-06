---
name: use-forge-nvidia-llama-3-1-nemoguard-8b-content-safety-nim
description: Use exact Forge model nvidia-llama-3-1-nemoguard-8b-content-safety-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Llama 3.1 NemoGuard 8B Content Safety

- Model slug: `nvidia-llama-3-1-nemoguard-8b-content-safety-nim`
- Family: `nvidia-llama-3-1-nemoguard-8b-content-safety`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-ai-foundation-models-community-license`
- Research status: `source-linked`

## Purpose

NVIDIA Llama 3.1 NemoGuard 8B Content Safety packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.

## Use this exact model when

- Use this exact `nvidia-llama-3-1-nemoguard-8b-content-safety-nim` version when the task supplies text and needs text.
- NVIDIA Llama 3.1 NemoGuard 8B Content Safety packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default "Classify whether this user request is safe: 'Explain how to rotate a Kubernetes image pull secret without revealing credentials.' Return a short rationale."): Prompt
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

1. Load this skill and pin model slug `nvidia-llama-3-1-nemoguard-8b-content-safety-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-llama-3-1-nemoguard-8b-content-safety-15a952b714`
- Recommended: Content moderation / safety classification of user prompts and LLM responses — Hugging Face model repository and README blobs and the NIM prompt-template documentation describe this checkpoint as a content safety moderator that classifies prompts and model responses as safe or unsafe and returns violated category labels per the vendor taxonomy; example prompt templates and example output JSON are provided.
- Recommended: Integration into NIM/NemoGuard microservice safety pipelines for moderated agent workflows — NIM/container deploy documentation and build.nvidia deploy page document NIM packaging and container invocation patterns appropriate for integration into guarded inference pipelines.
- Avoid: Assuming vendor-published numeric benchmark tables exist for this exact LoRA-tuned checkpoint and using them as-is for selection/tuning decisions — Inspected primary sources do not publish numeric benchmark table rows scoped to the exact tuned checkpoint (dataset/split/metric/model-tag/conditions) for nvidia/llama-3.1-nemoguard-8b-content-safety; upstream Llama-3.1-8B-Instruct materials are upstream-checkpoint evidence only and do not substitute for tuned-checkpoint evidence.
- Avoid: Using the checkpoint as a general-purpose high-reasoning/math assistant without validation — Vendor materials frame Nemoguard as a moderation/judge model intended to classify safety risks rather than as a general-purpose high-reasoning assistant; the model card and README emphasize content-safety classification.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-1-nemoguard-8b-content-safety-nim`
- Routes: `/v1/models/nvidia-llama-3-1-nemoguard-8b-content-safety-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-1-nemoguard-8b-content-safety-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-1-nemoguard-8b-content-safety-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/nvidia-llama-3-1-nemoguard-8b-content-safety-nim/SKILL.md
