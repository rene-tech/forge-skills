---
name: use-forge-huggingfacetb-smollm3-3b-vllm-cuda13
description: Use exact Forge model huggingfacetb-smollm3-3b-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use SmolLM3 3B

- Model slug: `huggingfacetb-smollm3-3b-vllm-cuda13`
- Family: `huggingfacetb-smollm3-3b`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SmolLM3 3B is a public Apache-2.0 small general language model from Hugging Face for instruction following, hybrid reasoning, multilingual chat, tool-use style prompts, and long-context summarization.

## Use this exact model when

- Use this exact `huggingfacetb-smollm3-3b-vllm-cuda13` version when the task supplies text and needs text.
- SmolLM3 3B is a public Apache-2.0 small general language model from Hugging Face for instruction following, hybrid reasoning, multilingual chat, tool-use style prompts, and long-context summarization.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Summarize this incident note for an engineering handoff, then list three follow-up questions:\n\nThe EU model probe hit readiness timeout after image pull completed. Logs show weight hydration still running in the shared cache path. No OOM event was recorded.'): Prompt
- `enable_thinking` (checkbox; optional; default False): Thinking
- `temperature` (number; optional; bounds 0..2; default 0.6): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.95): Top P
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

1. Load this skill and pin model slug `huggingfacetb-smollm3-3b-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-huggingfacetb-smollm3-3b-b2e5c24199`
- Recommended: Instruction following and general reasoning tasks — The upstream HuggingFace model page and README present SmolLM3-3B as a multilingual, long-context reasoning model and include an evaluation table with reasoning/instruction-style benchmark results, supporting use for instruction-following and general reasoning tasks insofar as these align with a decoder-only LM.
- Recommended: Long-context summarization and long-context chat (engineering required to reach extended context) — The repository base config documents max_position_embeddings = 65536 and the model page/README present the model as supporting long context, indicating the checkpoint is published with a long native context configuration.
- Avoid: Clinical decision-making or other safety-critical healthcare use — Evidence gap: the upstream repository, README, and canonical config artifacts do not document clinical validation, medical licensing, or expert-reviewed clinical benchmarks for SmolLM3-3B; no primary-source clinical validation evidence is present in the checked HuggingFaceTB artifacts.
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

- Model: `/v1/models/huggingfacetb-smollm3-3b-vllm-cuda13`
- Routes: `/v1/models/huggingfacetb-smollm3-3b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/huggingfacetb-smollm3-3b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/huggingfacetb-smollm3-3b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/huggingfacetb-smollm3-3b-vllm-cuda13/SKILL.md
