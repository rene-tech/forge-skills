---
name: use-forge-mistralai-devstral-small-2507-vllm-cuda13
description: Use exact Forge model mistralai-devstral-small-2507-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Devstral Small 1.1 2507

- Model slug: `mistralai-devstral-small-2507-vllm-cuda13`
- Family: `mistralai-devstral-small-2507`
- Version: `vllm-0.22.0-cuda13-tp1` (`vllm-0-22-0-cuda13-tp1`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Devstral Small 1.1 2507 is a public Apache-2.0 text-only coding and software-engineering agent model from Mistral AI and All Hands AI.

## Use this exact model when

- Use this exact `mistralai-devstral-small-2507-vllm-cuda13` version when the task supplies text and needs text.
- Devstral Small 1.1 2507 is a public Apache-2.0 text-only coding and software-engineering agent model from Mistral AI and All Hands AI.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'You are helping repair a repository. Identify the likely bug, propose the smallest patch, and list two regression tests.\\n\\nA retry helper should try three times, but production logs show it returns after the first TimeoutError.'): Prompt
- `tools` (json_editor; optional; default [{'type': 'function', 'function': {'name': 'read_file', 'parameters': {'type': 'object', 'required': ['path'], 'properties': {'path': {'type': 'string', 'description': 'Repository-relative file path.'}}}, 'description': 'Read a repository file by path.'}}]): Tool definitions
- `temperature` (number; optional; bounds 0..2; default 0.15): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..8192; default 1024): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "You are Devstral Small 1.1, a coding and software-engineering agent model. Prefer concise, actionable answers and emit tool calls only when a provided tool is useful.",
      "role": "system"
    },
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}",
  "tool_choice": "auto",
  "tools": "{{tools}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `mistralai-devstral-small-2507-vllm-cuda13` with version key `vllm-0-22-0-cuda13-tp1`.
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

- Model: `/v1/models/mistralai-devstral-small-2507-vllm-cuda13`
- Routes: `/v1/models/mistralai-devstral-small-2507-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/mistralai-devstral-small-2507-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/mistralai-devstral-small-2507-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/mistralai-devstral-small-2507-vllm-cuda13/SKILL.md
