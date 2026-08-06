---
name: use-forge-deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13
description: Use exact Forge model deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use DeepSeek R1 Distill Qwen 14B

- Model slug: `deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13`
- Family: `deepseek-ai-deepseek-r1-distill-qwen-14b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `mit; qwen2.5 base apache-2.0`
- Research status: `source-linked`

## Purpose

DeepSeek R1 Distill Qwen 14B is a public reasoning-oriented text-generation model derived from Qwen2.5-14B and fine-tuned with DeepSeek-R1 samples.

## Use this exact model when

- Use this exact `deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13` version when the task supplies text and needs text.
- DeepSeek R1 Distill Qwen 14B is a public reasoning-oriented text-generation model derived from Qwen2.5-14B and fine-tuned with DeepSeek-R1 samples.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Reason carefully, then give a concise final answer: A batch job has 64 shards. Three eighths finish, 10 fail, and the rest are still running. How many shards are still running?'): Prompt
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
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-deepseek-ai-deepseek-r1-distill-qwen-14b-2691341a52`
- Recommended: Text-only conversational generation and reasoning-oriented chat — Primary Hugging Face model page documents the checkpoint as a distilled model derived from Qwen2.5-14B and highlights reasoning-oriented capabilities and chain-of-thought/self-verification behaviors for the DeepSeek-R1 family that motivate use in text-generation/chat reasoning settings.
- Avoid: Applications requiring documented checkpoint-specific safety policies, bias-mitigation guidance, or content-filtering guarantees — Primary sources for this exact checkpoint do not provide explicit safety warnings, bias mitigation statements, or content-filtering guidelines.
- Avoid: Workflows that require formally specified confidence scores or a documented calibrated output contract — Primary documentation for this exact checkpoint lacks a formal output contract or confidence-score specification; outputs are documented only as generated text/token continuations.
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

- Model: `/v1/models/deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13`
- Routes: `/v1/models/deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/deepseek-ai-deepseek-r1-distill-qwen-14b-vllm-cuda13/SKILL.md
