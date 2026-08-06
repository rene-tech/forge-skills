---
name: use-forge-mistralai-ministral-3-3b-instruct-2512-vllm-cuda13
description: Use exact Forge model mistralai-ministral-3-3b-instruct-2512-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Ministral 3 3B Instruct 2512

- Model slug: `mistralai-ministral-3-3b-instruct-2512-vllm-cuda13`
- Family: `mistralai-ministral-3-3b-instruct-2512`
- Version: `vllm-0.22.0-cuda13` (`vllm-0-22-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Ministral 3 3B Instruct 2512 is a public Apache-2.0 compact instruction model from Mistral AI for lightweight chat, multilingual generation, JSON-style extraction, and agentic prompts.

## Use this exact model when

- Use this exact `mistralai-ministral-3-3b-instruct-2512-vllm-cuda13` version when the task supplies text and needs text.
- Ministral 3 3B Instruct 2512 is a public Apache-2.0 compact instruction model from Mistral AI for lightweight chat, multilingual generation, JSON-style extraction, and agentic prompts.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Draft a concise incident handoff for this note and include two concrete next checks:\n\nA vLLM CUDA 13 model probe is being staged for a compact FP8 instruct model. The first pass should validate text-only chat at a bounded 32K context before any tool or image inputs are exposed.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.1): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

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
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `mistralai-ministral-3-3b-instruct-2512-vllm-cuda13` with version key `vllm-0-22-0-cuda13`.
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
- Research key: `huggingface-co-mistralai-ministral-3-3b-instruct-2512-463ef33dd1`
- Recommended: Chat and instruction-focused natural-language generation — The repository and ONNX-variant README describe this artifact as an instruct post-trained variant intended for instruction/chat tasks; repository files include an explicit SYSTEM_PROMPT and chat template supporting instruction-style usage.
- Recommended: Local/edge deployment using quantized variants to reduce VRAM — The checkpoint config.json contains quantization metadata (quant_method = "fp8") and a GGUF artifact page in the findings lists quantization levels and an FP8 VRAM-fit claim, supporting variant-scoped deployment for lower-VRAM scenarios.
- Avoid: High-stakes clinical, safety-critical, or other regulated decision-making without human expert review — Evidence gap: The inspected checkpoint-scoped upstream artifacts (repository tree, config.json blob, and SYSTEM_PROMPT blob) do not provide checkpoint-scoped documentation, validation, or certification procedures for clinical or regulated high-stakes use.
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

- Model: `/v1/models/mistralai-ministral-3-3b-instruct-2512-vllm-cuda13`
- Routes: `/v1/models/mistralai-ministral-3-3b-instruct-2512-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/mistralai-ministral-3-3b-instruct-2512-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/mistralai-ministral-3-3b-instruct-2512-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/mistralai-ministral-3-3b-instruct-2512-vllm-cuda13/SKILL.md
