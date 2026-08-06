---
name: use-forge-qwen-qwen3-14b-vllm-cuda13
description: Use exact Forge model qwen-qwen3-14b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 14B

- Model slug: `qwen-qwen3-14b-vllm-cuda13`
- Family: `qwen-qwen3-14b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 14B is a public Apache-2.0 dense text-generation model for hybrid reasoning, instruction following, coding, agent-style prompts, multilingual chat, and long-context summarization.

## Use this exact model when

- Use this exact `qwen-qwen3-14b-vllm-cuda13` version when the task supplies text and needs text.
- Qwen3 14B is a public Apache-2.0 dense text-generation model for hybrid reasoning, instruction following, coding, agent-style prompts, multilingual chat, and long-context summarization.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Use /think to reason briefly, then answer: A service processes 18 batches. It retries 4 failed batches and splits 3 large batches into two each. How many batch executions run in total?'): Prompt
- `enable_thinking` (checkbox; optional; default True): Thinking Mode
- `temperature` (number; optional; bounds 0..2; default 0.6): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..8192; default 1024): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "chat_template_kwargs": {
    "enable_thinking": "{{enable_thinking}}"
  },
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-14b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-qwen-qwen3-14b-245877f208`
- Recommended: Instruction-following text generation — Upstream model card and Qwen3-14B-GGUF documentation describe Qwen3-14B as a causal text-generation model designed for instruction-following and related text-generation tasks.
- Recommended: Agent-style multi-turn interaction and reasoning over text — Upstream descriptions in the official model card and the Qwen3 series documentation indicate agent-style capabilities and multi-turn reasoning as intended uses for Qwen3-14B.
- Avoid: Non-text modalities or expecting a structured numeric/serialized output contract — Evidence gap: upstream primary sources inspected do not document support for multimodal inputs/outputs or a formal structured numeric output schema for Qwen3-14B.
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

- Model: `/v1/models/qwen-qwen3-14b-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-14b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-14b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-14b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/qwen-qwen3-14b-vllm-cuda13/SKILL.md
