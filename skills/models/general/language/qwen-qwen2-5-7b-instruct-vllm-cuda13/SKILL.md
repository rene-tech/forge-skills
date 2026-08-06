---
name: use-forge-qwen-qwen2-5-7b-instruct-vllm-cuda13
description: Use exact Forge model qwen-qwen2-5-7b-instruct-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen2.5 7B Instruct

- Model slug: `qwen-qwen2-5-7b-instruct-vllm-cuda13`
- Family: `qwen-qwen2-5-7b-instruct`
- Version: `hf-a09a354-vllm-0.21.0-cuda13` (`hf-a09a354-vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen2.5 7B Instruct is a public, ungated Apache-2.0 general instruction-following chat model for multilingual customer support, summarization, reasoning, and long-context text workflows.

## Use this exact model when

- Use this exact `qwen-qwen2-5-7b-instruct-vllm-cuda13` version when the task supplies text and needs text.
- Qwen2.5 7B Instruct is a public, ungated Apache-2.0 general instruction-following chat model for multilingual customer support, summarization, reasoning, and long-context text workflows.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Draft a concise customer-facing status update for this incident. Include impact, current mitigation, and the next verification step:\n\nThe model endpoint is healthy in us-central1 and eu-north1. A new uk-south1 pod is still hydrating weights from the shared cache, so first-token latency is elevated for cold requests.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.4): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.8): Top P
- `max_tokens` (number; optional; bounds 1..8192; default 768): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": false,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen2-5-7b-instruct-vllm-cuda13` with version key `hf-a09a354-vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-qwen-qwen2-5-7b-instruct-f5949308c7`
- Recommended: Long-context multilingual text generation and summarization where large context windows are required (contexts up to 128,000 tokens; responses up to ~8,000 tokens). — The Hugging Face model page for Qwen2.5-7B-Instruct documents long-context window capability of up to 128,000 tokens and generation output up to 8,000 tokens, and lists multilingual support for 29+ languages.
- Avoid: Evidence gap: No checkpoint-scoped avoidance guidance (for example, explicit prohibitions for clinical, legal, or other high-stakes domains) was found in the inspected primary sources. — Evidence gap: The inspected primary sources do not contain checkpoint-scoped avoid-use boundaries or task-specific prohibitions.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen2-5-7b-instruct-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen2-5-7b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen2-5-7b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen2-5-7b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/qwen-qwen2-5-7b-instruct-vllm-cuda13/SKILL.md
