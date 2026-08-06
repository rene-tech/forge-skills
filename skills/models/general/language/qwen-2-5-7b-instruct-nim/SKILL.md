---
name: use-forge-qwen-2-5-7b-instruct-nim
description: Use exact Forge model qwen-2-5-7b-instruct-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen 2.5 7B Instruct

- Model slug: `qwen-2-5-7b-instruct-nim`
- Family: `qwen-2-5-7b-instruct`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen 2.5 7B instruction model packaged as an NVIDIA NIM, useful for multilingual and coding-adjacent chat workloads.

## Use this exact model when

- Use this exact `qwen-2-5-7b-instruct-nim` version when the task supplies text and needs text.
- Qwen 2.5 7B instruction model packaged as an NVIDIA NIM, useful for multilingual and coding-adjacent chat workloads.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Give a bilingual English/German summary of why regional image mirrors reduce cold-start time.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
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

1. Load this skill and pin model slug `qwen-2-5-7b-instruct-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-qwen-qwen-2-5-7b-instruct-94e0f4a536`
- Recommended: Assistant/chat and instruction-following text generation — The upstream Hugging Face model card identifies the checkpoint as instruction-tuned and appropriate for instruction-following / chat-style generation.
- Avoid: High-stakes clinical or safety-critical decision making — Evidence gap: the inspected primary sources do not provide clinical validation, certification, or safety-critical readiness statements for this exact checkpoint; do not rely on the model as the sole basis for safety-critical decisions without domain validation.
- Avoid: Substituting the Qwen2.5-7B base checkpoint for the Instruct checkpoint in conversation workloads — Base-model evidence is a separate upstream checkpoint and should not be substituted for the instruction-tuned checkpoint without explicit evidence; keep base-versus-instruct claims scoped to their respective checkpoints.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-2-5-7b-instruct-nim`
- Routes: `/v1/models/qwen-2-5-7b-instruct-nim/inference-routes`
- Regional deployment: `/v1/models/qwen-2-5-7b-instruct-nim/regional-deployment`
- Serverless handoff: `/v1/models/qwen-2-5-7b-instruct-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/qwen-2-5-7b-instruct-nim/SKILL.md
