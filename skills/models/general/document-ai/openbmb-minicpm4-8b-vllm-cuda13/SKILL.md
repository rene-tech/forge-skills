---
name: use-forge-openbmb-minicpm4-8b-vllm-cuda13
description: Use exact Forge model openbmb-minicpm4-8b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MiniCPM4 8B

- Model slug: `openbmb-minicpm4-8b-vllm-cuda13`
- Family: `openbmb-minicpm4-8b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

MiniCPM4 8B is a public Apache-2.0 OpenBMB text-generation model for English/Chinese chat, instruction following, long-context summarization, and efficient edge-oriented general LLM workloads.

## Use this exact model when

- Use this exact `openbmb-minicpm4-8b-vllm-cuda13` version when the task supplies text and needs text.
- MiniCPM4 8B is a public Apache-2.0 OpenBMB text-generation model for English/Chinese chat, instruction following, long-context summarization, and efficient edge-oriented general LLM workloads.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Write a concise engineering handoff for this probe note. Include likely cause, impact, and next action:\n\nA vLLM CUDA 13 candidate uses remote-code MiniCPM architecture, a public Apache-2.0 artifact, and a 32K context cap. It has not yet been live-probed on Forge GPUs.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.8): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 1024): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "add_special_tokens": true,
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

1. Load this skill and pin model slug `openbmb-minicpm4-8b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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

- Model: `/v1/models/openbmb-minicpm4-8b-vllm-cuda13`
- Routes: `/v1/models/openbmb-minicpm4-8b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/openbmb-minicpm4-8b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/openbmb-minicpm4-8b-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/openbmb-minicpm4-8b-vllm-cuda13/SKILL.md
