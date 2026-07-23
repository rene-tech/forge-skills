---
name: use-forge-qwen-qwen3-embedding-0-6b-vllm-cuda13
description: Use exact Forge model qwen-qwen3-embedding-0-6b-vllm-cuda13 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3 Embedding 0.6B

- Model slug: `qwen-qwen3-embedding-0-6b-vllm-cuda13`
- Family: `qwen-qwen3-embedding-0-6b`
- Version: `vllm-0.21.0-cuda13-embed` (`vllm-0-21-0-cuda13-embed`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3 Embedding 0.6B served by the already mirrored official vLLM 0.21.0 CUDA 13 OpenAI-compatible image in pooling runner mode.

## Use this exact model when

- Use this exact `qwen-qwen3-embedding-0-6b-vllm-cuda13` version when the task supplies text and needs embedding.
- Qwen3 Embedding 0.6B served by the already mirrored official vLLM 0.21.0 CUDA 13 OpenAI-compatible image in pooling runner mode.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery: How can shared GPU caches reduce model inference cold starts?'): Input text
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "{{encoding_format}}",
  "input": "{{input}}",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-embedding-0-6b-vllm-cuda13` with version key `vllm-0-21-0-cuda13-embed`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
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

- Model: `/v1/models/qwen-qwen3-embedding-0-6b-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-embedding-0-6b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-embedding-0-6b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-embedding-0-6b-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/qwen-qwen3-embedding-0-6b-vllm-cuda13/SKILL.md
