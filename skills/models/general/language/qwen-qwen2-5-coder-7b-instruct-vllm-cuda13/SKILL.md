---
name: use-forge-qwen-qwen2-5-coder-7b-instruct-vllm-cuda13
description: Use exact Forge model qwen-qwen2-5-coder-7b-instruct-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen2.5-Coder 7B Instruct

- Model slug: `qwen-qwen2-5-coder-7b-instruct-vllm-cuda13`
- Family: `qwen-qwen2-5-coder-7b-instruct`
- Version: `hf-c03e6d3-vllm-0.21.0-cuda13` (`hf-c03e6d3-vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen2.5-Coder 7B Instruct is a public, ungated Apache-2.0 code-specialized instruction model for code generation, code repair, code reasoning, agentic developer workflows, and long-context code assistance.

## Use this exact model when

- Use this exact `qwen-qwen2-5-coder-7b-instruct-vllm-cuda13` version when the task supplies text and needs text.
- Qwen2.5-Coder 7B Instruct is a public, ungated Apache-2.0 code-specialized instruction model for code generation, code repair, code reasoning, agentic developer workflows, and long-context code assistance.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default "Refactor this Python helper so it handles empty inputs, keeps the return type stable, and includes one short test case:\n\n```python\ndef top_extensions(paths):\n    counts = {}\n    for path in paths:\n        ext = path.split('.')[-1]\n        counts[ext] = counts.get(ext, 0) + 1\n    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[:3]\n```"): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
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

1. Load this skill and pin model slug `qwen-qwen2-5-coder-7b-instruct-vllm-cuda13` with version key `hf-c03e6d3-vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-qwen-qwen2-5-coder-7b-instruct-1fed2cd4d7`
- Recommended: Code generation (single-file and multi-file snippets) — Primary evidence identifies the Qwen2.5‑Coder series as code-specialized and confirms an instruction‑tuned 7B checkpoint exists in the repository; therefore the instruct 7B checkpoint is presented upstream for code-focused instruction use.
- Recommended: Code completion and code repair (with downstream validation) — Primary sources present the Qwen2.5‑Coder series as code-focused and document the existence of an instruction‑tuned 7B checkpoint intended for instruction-style code tasks; checkpoint-scoped numeric protocol or performance details are not available in the supplied primary evidence and downstream validation is required.
- Recommended: Instruction-following for developer workflows and agentic coding assistants — The repository-level evidence and the technical report collectively document an instruction-tuned member of the Qwen2.5‑Coder family at the 7B scale, indicating upstream intent for instruction-following in code contexts.
- Avoid: Using an unmodified base 7B model for conversational/dialogue tasks without instruction tuning — Evidence gap: The supplied primary findings do not contain an explicit upstream statement advising against conversational use of a base (non‑instruction‑tuned) 7B checkpoint, nor a checkpoint-scoped upstream comparison establishing such a caution. Only the instruction‑tuned 7B repository is confirmed upstream in the inspected sources.
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

- Model: `/v1/models/qwen-qwen2-5-coder-7b-instruct-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen2-5-coder-7b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen2-5-coder-7b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen2-5-coder-7b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/qwen-qwen2-5-coder-7b-instruct-vllm-cuda13/SKILL.md
