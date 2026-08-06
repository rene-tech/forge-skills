---
name: use-forge-openai-gpt-oss-20b-vllm
description: Use exact Forge model openai-gpt-oss-20b-vllm for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenAI gpt-oss 20B

- Model slug: `openai-gpt-oss-20b-vllm`
- Family: `openai-gpt-oss-20b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

OpenAI gpt-oss 20B is a public Apache-2.0 open-weight text reasoning model for instruction following, coding, tool-use style prompts, structured outputs, and agentic workflows.

## Use this exact model when

- Use this exact `openai-gpt-oss-20b-vllm` version when the task supplies text and needs text.
- OpenAI gpt-oss 20B is a public Apache-2.0 open-weight text reasoning model for instruction following, coding, tool-use style prompts, structured outputs, and agentic workflows.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Solve this step by step, then give the final answer only: A deployment starts 18 model pods. Two thirds become ready, then 3 more pods fail readiness. How many pods are ready?'): Prompt
- `reasoning_effort` (select; optional; choices low, medium, high; default 'low'): Reasoning Effort
- `include_reasoning` (checkbox; optional; default False): Include Reasoning
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "include_reasoning": "{{include_reasoning}}",
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "reasoning_effort": "{{reasoning_effort}}",
  "stream": true,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `openai-gpt-oss-20b-vllm` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-openai-gpt-oss-20b-4fb7165743`
- Recommended: Agentic instruction-following workflows with tool use (function calling, structured outputs, multi-step reasoning) — OpenAI official model card and repository materials describe the GPT-OSS family as designed for agentic workflows with structured outputs, chain-of-thought style reasoning, and tool-enabled capabilities; the upstream repository provides Harmony-format templates/adapters intended for such flows.
- Recommended: Text-only coding, STEM, and general-knowledge reasoning tasks suitable for a text-only MoE model — OpenAI model card and vendor documentation characterize gpt-oss-20b as a text-only model with instruction-following and reasoning capabilities applicable to coding and STEM tasks.
- Avoid: Deploying or querying the model in agentic/tool workflows without applying Harmony response-format templates or repository-provided adapters — Upstream repository and model-card materials indicate the models were trained on the Harmony response format and provide Harmony-format templates/adapters; agentic flows are documented as relying on Harmony-format templates/adapters for correct structured outputs and tool interactions.
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

- Model: `/v1/models/openai-gpt-oss-20b-vllm`
- Routes: `/v1/models/openai-gpt-oss-20b-vllm/inference-routes`
- Regional deployment: `/v1/models/openai-gpt-oss-20b-vllm/regional-deployment`
- Serverless handoff: `/v1/models/openai-gpt-oss-20b-vllm/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/openai-gpt-oss-20b-vllm/SKILL.md
