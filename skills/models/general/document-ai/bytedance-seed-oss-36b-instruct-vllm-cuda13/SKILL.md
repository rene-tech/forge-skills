---
name: use-forge-bytedance-seed-oss-36b-instruct-vllm-cuda13
description: Use exact Forge model bytedance-seed-oss-36b-instruct-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Seed-OSS 36B Instruct

- Model slug: `bytedance-seed-oss-36b-instruct-vllm-cuda13`
- Family: `bytedance-seed-oss-36b-instruct`
- Version: `vllm-0.22.0-cuda13-hidden` (`vllm-0-22-0-cuda13-hidden`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Seed-OSS 36B Instruct is a public Apache-2.0 dense causal language model from ByteDance Seed for long-context reasoning, coding, agentic workflows, tool-use style prompts, and international English/Chinese usage.

## Use this exact model when

- Use this exact `bytedance-seed-oss-36b-instruct-vllm-cuda13` version when the task supplies text and needs text.
- Seed-OSS 36B Instruct is a public Apache-2.0 dense causal language model from ByteDance Seed for long-context reasoning, coding, agentic workflows, tool-use style prompts, and international English/Chinese usage.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'You are helping review a pull request. Summarize the likely bug, propose the smallest safe fix, and list two tests to add.\n\nThe retry loop should try three times, but production logs show it exits after the first timeout.'): Prompt
- `thinking_budget` (number; optional; bounds 0..8192; default 512): Thinking Budget
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 768): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "chat_template_kwargs": {
    "thinking_budget": "{{thinking_budget}}"
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

1. Load this skill and pin model slug `bytedance-seed-oss-36b-instruct-vllm-cuda13` with version key `vllm-0-22-0-cuda13-hidden`.
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
- Research key: `huggingface-co-bytedance-seed-seed-oss-36b-instruct-e3a0d537dd`
- Recommended: Instruction‑following and chat-style generation (instruct/checkpoint canonical formatting) — The HF model page identifies this checkpoint as the Instruct variant and the repository includes a chat_template.jinja that defines canonical chat tokens and thinking_budget mapping, indicating repository intent and formatting for instruction/chat usage.
- Recommended: Long-context tasks that require large context windows (use checkpoint defaults with downstream validation) — The checkpoint config.json reports max_position_embeddings=524288 and repository/model-card materials and release README describe long-context design goals for the Seed-OSS family; the config.json value supports using the checkpoint for very long contexts subject to downstream validation of enforcement semantics.
- Avoid: Clinical, medical, or PHI-sensitive applications without explicit upstream clinical validation or PHI-handling guidance — Evidence gap: the checkpoint-scoped model card and HF repo README/MODEL_CARD blobs inspected do not provide explicit clinical validation, PHI handling policies, or deployment guidance for medical use; do not assume clinical safety or PHI suitability from upstream checkpoint files alone.
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

- Model: `/v1/models/bytedance-seed-oss-36b-instruct-vllm-cuda13`
- Routes: `/v1/models/bytedance-seed-oss-36b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/bytedance-seed-oss-36b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/bytedance-seed-oss-36b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/bytedance-seed-oss-36b-instruct-vllm-cuda13/SKILL.md
