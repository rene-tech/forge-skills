---
name: use-forge-deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13
description: Use exact Forge model deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use DeepSeek R1 0528 Qwen3 8B

- Model slug: `deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13`
- Family: `deepseek-ai-deepseek-r1-0528-qwen3-8b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `mit; qwen3 base apache-2.0`
- Research status: `source-linked`

## Purpose

DeepSeek R1 0528 Qwen3 8B is a public, non-gated MIT reasoning-oriented text-generation model distilled from DeepSeek-R1-0528 into a Qwen3 8B base model.

## Use this exact model when

- Use this exact `deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13` version when the task supplies text and needs text.
- DeepSeek R1 0528 Qwen3 8B is a public, non-gated MIT reasoning-oriented text-generation model distilled from DeepSeek-R1-0528 into a Qwen3 8B base model.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Reason carefully, then give a concise final answer: A rollout has 80 validation checks. Three fifths pass, 9 fail, and the rest are waiting on logs. How many checks are waiting on logs?'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.6): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.95): Top P
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

1. Load this skill and pin model slug `deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-deepseek-ai-deepseek-r1-0528-qwen3-8b-4600e20454`
- Recommended: Long-context text reasoning and long-context-aware tasks — The canonical config.json and tokenizer_config.json on the model's Hugging Face repository indicate support for very large context windows: max_position_embeddings = 131072 (config.json) and model_max_length = 131072 (tokenizer_config.json).
- Avoid: Multimodal inputs (image input) — Evidence gap: canonical primary sources for this exact checkpoint do not document image or other multimodal input support; tokenizer and config files indicate a text tokenizer and tokenizer settings only (no image encoders or multimodal adapters listed in the canonical files).
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

- Model: `/v1/models/deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13`
- Routes: `/v1/models/deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/deepseek-ai-deepseek-r1-0528-qwen3-8b-vllm-cuda13/SKILL.md
