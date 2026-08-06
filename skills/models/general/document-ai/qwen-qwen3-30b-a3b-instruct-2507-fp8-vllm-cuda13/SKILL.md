---
name: use-forge-qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13
description: Use exact Forge model qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 30B A3B Instruct 2507 FP8

- Model slug: `qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13`
- Family: `qwen-qwen3-30b-a3b-instruct-2507`
- Version: `fp8-vllm-0.21.0-cuda13` (`fp8-vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 30B A3B Instruct 2507 FP8 is a public Apache-2.0 non-thinking MoE chat model for general instruction following, coding, multilingual knowledge, long-context understanding, and tool-use style prompts.

## Use this exact model when

- Use this exact `qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13` version when the task supplies text and needs text.
- Qwen3 30B A3B Instruct 2507 FP8 is a public Apache-2.0 non-thinking MoE chat model for general instruction following, coding, multilingual knowledge, long-context understanding, and tool-use style prompts.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'You are reviewing a model deployment plan. Summarize the main risk, list two validation steps, and give one concise recommendation:\\n\\nA new 30B-A3B FP8 MoE chat model will reuse an existing vLLM CUDA 13 image, hydrate public safetensors from Hugging Face into the shared cache, and start with a 32K context cap before broader long-context probes.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.8): Top P
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
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13` with version key `fp8-vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-qwen-qwen3-30b-a3b-instruct-2507-fp8-6399ab64f2`
- Recommended: Benchmark evaluation and empirical performance measurement on the tasks listed on the FP8 model card (e.g., MultiPL-E, IFEval, Arena-Hard v2, Creative Writing v3, WritingBench, BFCL-v3, TAU variants, MMLU variants, GPQA, SuperGPQA, AIME25, HMMT25, ZebraLogic, LiveBench, LiveCodeBench, MultiIF, MMLU-ProX, INCLUDE, PolyMATH). — The Hugging Face model card for the FP8 checkpoint explicitly lists per-checkpoint numeric scores for these benchmarks in its Benchmarks table.
- Recommended: Use in text-generation / instruction-following workflows to produce textual outputs for downstream evaluation. — The checkpoint is presented on the model card under a name that includes the token 'Instruct' and the Benchmarks table contains many text-task benchmark results, indicating checkpoint-scoped use for textual generation/evaluation.
- Avoid: Assuming checkpoint-scoped parameter counts, architecture details, immutable weights revision identifiers, or an explicit weights license for this FP8 artifact. — The inspected Hugging Face model card presents the checkpoint name and benchmark table values but does not report checkpoint-scoped parameter-count strings, architecture text, an immutable revision identifier, or an explicit weights-license declaration.
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

- Model: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/qwen-qwen3-30b-a3b-instruct-2507-fp8-vllm-cuda13/SKILL.md
