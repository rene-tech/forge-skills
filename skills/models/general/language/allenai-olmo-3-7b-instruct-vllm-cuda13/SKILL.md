---
name: use-forge-allenai-olmo-3-7b-instruct-vllm-cuda13
description: Use exact Forge model allenai-olmo-3-7b-instruct-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OLMo 3 7B Instruct

- Model slug: `allenai-olmo-3-7b-instruct-vllm-cuda13`
- Family: `allenai-olmo-3-7b-instruct`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

AllenAI OLMo 3 7B Instruct is a public, ungated Apache-2.0 English instruction-following model in the fully open OLMo 3 family, aimed at chat, tool-use style prompts, coding, math, general reasoning, and long-context workflows.

## Use this exact model when

- Use this exact `allenai-olmo-3-7b-instruct-vllm-cuda13` version when the task supplies text and needs text.
- AllenAI OLMo 3 7B Instruct is a public, ungated Apache-2.0 English instruction-following model in the fully open OLMo 3 family, aimed at chat, tool-use style prompts, coding, math, general reasoning, and long-context workflows.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Draft a concise engineering handoff for this rollout note. Include one likely risk and two validation steps:\n\nA fully open 7B instruction model is being staged on the CUDA 13 vLLM image with a bounded 32K context window before any default routing decision.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.6): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
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
  "stream": false,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `allenai-olmo-3-7b-instruct-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-allenai-olmo-3-7b-instruct-c0cec6c2c6`
- Recommended: Instruction-following / chat-style system+user prompts — Family-level description of Olmo 3 Instruct behavior (instruction-following) appears in the Olmo 3 writeup/preprint and the checkpoint's generation defaults and config indicate instruction-tuned sampling defaults and a causal LM architecture consistent with instruction-following usage.
- Recommended: Long-context workflows (family-level long-context support reported) — The config.json reports extended positional-related fields (max_position_embeddings = 65536 and rope_scaling.original_max_position_embeddings = 8192 and sliding_window = 4096) and the Olmo 3 family writeup describes long-context modeling as a family target; these blobs support using the checkpoint for long-context experiments but the config fields are not authoritatively reconciled in the checked blobs.
- Avoid: Safety-critical or high-stakes decision making — Evidence gap: the inspected checkpoint-scoped blobs and commits do not contain a checkpoint-scoped upstream risk/bias mitigation statement, calibrated-probability guidance, or documented post-deployment monitoring protocol tied to this exact checkpoint commit.
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

- Model: `/v1/models/allenai-olmo-3-7b-instruct-vllm-cuda13`
- Routes: `/v1/models/allenai-olmo-3-7b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/allenai-olmo-3-7b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/allenai-olmo-3-7b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/allenai-olmo-3-7b-instruct-vllm-cuda13/SKILL.md
