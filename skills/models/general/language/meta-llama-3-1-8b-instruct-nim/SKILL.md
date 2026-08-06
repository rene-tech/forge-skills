---
name: use-forge-meta-llama-3-1-8b-instruct-nim
description: Use exact Forge model meta-llama-3-1-8b-instruct-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Meta Llama 3.1 8B Instruct

- Model slug: `meta-llama-3-1-8b-instruct-nim`
- Family: `meta-llama-3-1-8b-instruct`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `llama-3.1-community`
- Research status: `source-linked`

## Purpose

General-purpose Llama 3.1 8B chat model for instruction following, summarization, and lightweight agent workflows.

## Use this exact model when

- Use this exact `meta-llama-3-1-8b-instruct-nim` version when the task supplies text and needs text.
- General-purpose Llama 3.1 8B chat model for instruction following, summarization, and lightweight agent workflows.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Explain the difference between cache-warm and first-run model startup.'): Prompt
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

1. Load this skill and pin model slug `meta-llama-3-1-8b-instruct-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-meta-llama-3-1-8b-instruct-365e0f344a`
- Recommended: Instruction-following and conversational dialogue — Upstream model card and the Hugging Face presentation describe the checkpoint as instruction-tuned and optimized for assistant-like chat and dialogue.
- Recommended: Code-evaluation and coding assistance experiments (requires downstream validation and calibration) — Upstream evaluation documentation and MODEL_CARD.md report code-evaluation metrics (HumanEval / MBPP family entries) for the post-trained/instruct variants, indicating the checkpoint was evaluated on code tasks; adopters must validate sampling/decoding and perform task-specific calibration before production use.
- Recommended: Summarization and general multilingual text generation — Upstream model card and Hugging Face documentation present the tuned models as intended for coherent multilingual text generation and instruction-following tasks.
- Avoid: Unreviewed deployment in high-risk domains without expert oversight — Upstream model card documents limitations including hallucination risk and recommends human review for high-risk applications; do not deploy without domain experts and validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 131072.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/meta-llama-3-1-8b-instruct-nim`
- Routes: `/v1/models/meta-llama-3-1-8b-instruct-nim/inference-routes`
- Regional deployment: `/v1/models/meta-llama-3-1-8b-instruct-nim/regional-deployment`
- Serverless handoff: `/v1/models/meta-llama-3-1-8b-instruct-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/meta-llama-3-1-8b-instruct-nim/SKILL.md
