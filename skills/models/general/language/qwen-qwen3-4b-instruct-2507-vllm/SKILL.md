---
name: use-forge-qwen-qwen3-4b-instruct-2507-vllm
description: Use exact Forge model qwen-qwen3-4b-instruct-2507-vllm for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 4B Instruct 2507

- Model slug: `qwen-qwen3-4b-instruct-2507-vllm`
- Family: `qwen-qwen3-4b-instruct-2507`
- Version: `vllm-0.10.2-cuda12.8` (`vllm-0-10-2-cuda12-8`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 4B Instruct 2507 is a public Apache-2.0 text-generation model for instruction following, coding, multilingual knowledge, tool-use style prompts, and long-context understanding.

## Use this exact model when

- Use this exact `qwen-qwen3-4b-instruct-2507-vllm` version when the task supplies text and needs text.
- Qwen3 4B Instruct 2507 is a public Apache-2.0 text-generation model for instruction following, coding, multilingual knowledge, tool-use style prompts, and long-context understanding.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Write a concise Python function that groups log lines by severity, then explain its time complexity.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
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
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-4b-instruct-2507-vllm` with version key `vllm-0-10-2-cuda12-8`.
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
- Research key: `huggingface-co-qwen-qwen3-4b-instruct-2507-74d4771762`
- Recommended: General instruction-following and general knowledge research/evaluation — The checkpoint README.md lists instruction-style benchmark scores (e.g., MMLU‑Pro and MMLU‑Redux) for this exact checkpoint, indicating it has been evaluated on such tasks at the checkpoint level; downstream validation is required because the README does not publish prompt templates or dataset splits.
- Recommended: Coding-assistance and code-evaluation research — The checkpoint README.md reports coding-oriented benchmark scores (e.g., LiveCodeBench v6, MultiPL‑E, LiveBench) for this checkpoint, indicating the model has been evaluated on coding tasks; use for production requires downstream test-suite validation and safety filtering.
- Recommended: Mathematical/problem-solving benchmark research — The checkpoint README.md lists math/reasoning benchmark scores (e.g., AIME25, HMMT25, ZebraLogic) for this exact checkpoint, supporting use in research or assisted workflows after careful validation.
- Avoid: Clinical, medical-diagnostic, or other safety-critical decision-making without expert oversight — Inspected checkpoint primary sources (model card, config.json, LICENSE) do not provide checkpoint-scoped clinical validation, certification, PHI-handling guidance, or creator-stated clinical-use instructions for Qwen3-4B-Instruct-2507.
- Avoid: Any safety-critical deployment that requires creator-provided operational/safety controls — Inspected checkpoint primary sources do not include explicit creator-provided operational safety checklists or runtime mitigation guidance for this exact checkpoint.
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

- Model: `/v1/models/qwen-qwen3-4b-instruct-2507-vllm`
- Routes: `/v1/models/qwen-qwen3-4b-instruct-2507-vllm/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-4b-instruct-2507-vllm/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-4b-instruct-2507-vllm/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/qwen-qwen3-4b-instruct-2507-vllm/SKILL.md
