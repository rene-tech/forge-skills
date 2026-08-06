---
name: use-forge-qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13
description: Use exact Forge model qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 30B A3B Instruct 2507 BF16

- Model slug: `qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13`
- Family: `qwen-qwen3-30b-a3b-instruct-2507`
- Version: `bf16-vllm-0.21.0-cuda13` (`bf16-vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 30B A3B Instruct 2507 BF16 is a public Apache-2.0 MoE chat model for general instruction following, coding, multilingual knowledge, long-context understanding, and tool-use style prompts.

## Use this exact model when

- Use this exact `qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13` version when the task supplies text and needs text.
- Qwen3 30B A3B Instruct 2507 BF16 is a public Apache-2.0 MoE chat model for general instruction following, coding, multilingual knowledge, long-context understanding, and tool-use style prompts.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'You are comparing two deployment fallbacks for a 30B MoE model. Explain why a BF16 runtime can be useful when an FP8 runtime fails in a GPU kernel, then list the minimum evidence needed before production activation.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.8): Top P
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

1. Load this skill and pin model slug `qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13` with version key `bf16-vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-qwen-qwen3-30b-a3b-instruct-2507-ff761b3644`
- Recommended: General instruction following and conversational/dialog tasks — The repository README demonstrates instruction/chat generation usage and the model page identifies this checkpoint as an Instruct variant.
- Recommended: Long-context document-grounded workflows (conditional on following README/config_1m.json guidance) — The repository contains a config_1m.json intended for length extrapolation and the README provides long-context workflow instructions; tokenizer_config.json and config_1m.json contain fields indicating extended-context support.
- Recommended: Coding assistance and code generation (research/deployment with downstream validation) — The README and model card present this checkpoint as an Instruct variant with coding-related capability claims; use for code generation should include downstream validation and protocol-specific testing.
- Avoid: Clinical or safety-critical medical diagnosis without domain validation — No checkpoint-scoped documentation of clinical validation, PHI handling procedures, or regulatory-clearance guidance was located in the inspected checkpoint repository blobs or the family technical report.
- Avoid: Assuming the model emits calibrated numeric confidence/probability scores in plain text by default — The inspected primary artifacts do not document checkpoint-scoped emission of calibrated numeric confidence/probability fields or calibration guarantees.
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

- Model: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/qwen-qwen3-30b-a3b-instruct-2507-bf16-vllm-cuda13/SKILL.md
