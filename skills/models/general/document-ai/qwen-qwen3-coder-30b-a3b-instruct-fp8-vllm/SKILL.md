---
name: use-forge-qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm
description: Use exact Forge model qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3-Coder 30B A3B Instruct FP8

- Model slug: `qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm`
- Family: `qwen-qwen3-coder-30b-a3b-instruct-fp8`
- Version: `vllm-0.10.2-cuda12.8` (`vllm-0-10-2-cuda12-8`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3-Coder 30B A3B Instruct FP8 is a public Apache-2.0 coding-focused mixture-of-experts model for agentic coding, browser-use style tasks, repository-scale prompts, tool-call style workflows, and general code generation.

## Use this exact model when

- Use this exact `qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm` version when the task supplies text and needs text.
- Qwen3-Coder 30B A3B Instruct FP8 is a public Apache-2.0 coding-focused mixture-of-experts model for agentic coding, browser-use style tasks, repository-scale prompts, tool-call style workflows, and general code generation.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default "Refactor this Python function for clarity, explain the main tradeoffs, and include one focused unit test:\\n\\ndef group(lines):\\n    d = {}\\n    for line in lines:\\n        k = line.split(':')[0]\\n        if k not in d:\\n            d[k] = []\\n        d[k].append(line)\\n    return d"): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.8): Top P
- `max_tokens` (number; optional; bounds 1..8192; default 1024): Max Tokens

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

1. Load this skill and pin model slug `qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm` with version key `vllm-0-10-2-cuda12-8`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm`
- Routes: `/v1/models/qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/qwen-qwen3-coder-30b-a3b-instruct-fp8-vllm/SKILL.md
