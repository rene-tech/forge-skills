---
name: use-forge-openbmb-minicpm5-1b-vllm-cuda13
description: Use exact Forge model openbmb-minicpm5-1b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MiniCPM5 1B

- Model slug: `openbmb-minicpm5-1b-vllm-cuda13`
- Family: `openbmb-minicpm5-1b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

MiniCPM5 1B is a public Apache-2.0 compact causal language model from OpenBMB for local assistants, coding agents, tool-use style prompts, hybrid reasoning, English/Chinese chat, and long-context summarization.

## Use this exact model when

- Use this exact `openbmb-minicpm5-1b-vllm-cuda13` version when the task supplies text and needs text.
- MiniCPM5 1B is a public Apache-2.0 compact causal language model from OpenBMB for local assistants, coding agents, tool-use style prompts, hybrid reasoning, English/Chinese chat, and long-context summarization.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Write a concise handoff for this model probe note and include two next checks:\n\nA compact 1B chat model is being tested on the CUDA 13 vLLM image. The first target is a bounded 32K context smoke before any long-context or tool-calling exposure.'): Prompt
- `enable_thinking` (checkbox; optional; default False): Thinking
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "chat_template_kwargs": {
    "enable_thinking": "{{enable_thinking}}"
  },
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

1. Load this skill and pin model slug `openbmb-minicpm5-1b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-openbmb-minicpm5-1b-e330c92570`
- Recommended: Local / on-device assistant and resource-constrained deployments using the upstream MiniCPM5-1B checkpoint — The Hugging Face model page lists supported local deployment backends (Transformers BF16/FP16, llama.cpp (GGUF), Ollama, LM Studio, MLX/4-bit), and the project README and model hosting emphasize local / on-device deployment and supported runtime backends.
- Recommended: Applications requiring very long context windows (research or evaluation of long-context performance), after runtime validation — The model config and model card state a native maximum position embeddings / context length of 131,072 tokens; using such long contexts requires validating the chosen runtime and memory behavior.
- Recommended: Reasoning, multi-step math, and coding tasks using the model's documented generation defaults (when validated for the target runtime) — The model-hosted generation_config.json sets do_sample true with temperature 0.9 and top_p 0.95; the project documents a Think/No-Think mode concept on the model card and README (switching generation mode is a documented feature of the upstream artifacts).
- Avoid: Clinical decision-making, PHI-sensitive automated processing, or other regulated clinical deployments — No primary-source documentation in the reviewed model-hosted blobs or repository README provides clinical validation, PHI handling guidance, regulatory compliance statements, or operational clinical safeguards for MiniCPM5-1B.
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

- Model: `/v1/models/openbmb-minicpm5-1b-vllm-cuda13`
- Routes: `/v1/models/openbmb-minicpm5-1b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/openbmb-minicpm5-1b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/openbmb-minicpm5-1b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/openbmb-minicpm5-1b-vllm-cuda13/SKILL.md
