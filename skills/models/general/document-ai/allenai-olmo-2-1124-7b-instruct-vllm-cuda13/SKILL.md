---
name: use-forge-allenai-olmo-2-1124-7b-instruct-vllm-cuda13
description: Use exact Forge model allenai-olmo-2-1124-7b-instruct-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OLMo-2 7B Instruct

- Model slug: `allenai-olmo-2-1124-7b-instruct-vllm-cuda13`
- Family: `allenai-olmo-2-1124-7b-instruct`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

AllenAI OLMo-2 1124 7B Instruct is a public Apache-2.0 English instruction-following and chat model in the OLMo-2 open-science family.

## Use this exact model when

- Use this exact `allenai-olmo-2-1124-7b-instruct-vllm-cuda13` version when the task supplies text and needs text.
- AllenAI OLMo-2 1124 7B Instruct is a public Apache-2.0 English instruction-following and chat model in the OLMo-2 open-science family.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Draft a concise release note for an open-science instruction model that is available for testing, including one risk and one recommended validation step.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.4): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..2048; default 512): Max Tokens

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

1. Load this skill and pin model slug `allenai-olmo-2-1124-7b-instruct-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-allenai-olmo-2-1124-7b-instruct-aa6456fc5a`
- Recommended: English instruction-following and chat-style text generation — The Hugging Face model card for the exact checkpoint names this model among the family final instruction-tuned (RLVR) checkpoints and the model page provides usage instructions; the family-level preprint and repository provide contextual evidence that the family includes instruction-finetuned checkpoints.
- Avoid: Any workflow that requires inputs longer than the documented context window without truncation or chunking — The official checkpoint config.json documents max_position_embeddings = 4096, which constrains single-sequence input length for this exact checkpoint.
- Avoid: High-stakes decisions made from the model output without downstream validation — Evidence gap: The checked primary sources do not report calibrated confidence semantics, a certified decision-use policy, or a documented post-output validation pipeline for this exact checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/allenai-olmo-2-1124-7b-instruct-vllm-cuda13`
- Routes: `/v1/models/allenai-olmo-2-1124-7b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/allenai-olmo-2-1124-7b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/allenai-olmo-2-1124-7b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/allenai-olmo-2-1124-7b-instruct-vllm-cuda13/SKILL.md
