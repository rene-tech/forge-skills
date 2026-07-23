---
name: use-forge-abhinand-medembed-base-v0-1-vllm-cuda13
description: Use exact Forge model abhinand-medembed-base-v0-1-vllm-cuda13 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MedEmbed Base

- Model slug: `abhinand-medembed-base-v0-1-vllm-cuda13`
- Family: `abhinand-medembed-base`
- Version: `hf-7a90c50-vllm-0.22.0-cuda13-pooling` (`hf-7a90c50-vllm-0-22-0-cuda13-pooling`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

MedEmbed Base is Abhinand Balachandran's Apache-2.0 sentence-transformers embedding model fine-tuned from BAAI/bge-base-en-v1.5 for medical and clinical information retrieval.

## Use this exact model when

- Use this exact `abhinand-medembed-base-v0-1-vllm-cuda13` version when the task supplies text and needs embedding.
- MedEmbed Base is Abhinand Balachandran's Apache-2.0 sentence-transformers embedding model fine-tuned from BAAI/bge-base-en-v1.5 for medical and clinical information retrieval.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Clinical retrieval query: What evidence supports statin therapy for primary prevention in adults with elevated cardiovascular risk?\n\nCandidate passage: Large randomized trials and meta-analyses report lower rates of major vascular events for statin therapy in appropriately selected adults, with absolute benefit depending on baseline risk.'): Medical or clinical text
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

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

1. Load this skill and pin model slug `abhinand-medembed-base-v0-1-vllm-cuda13` with version key `hf-7a90c50-vllm-0-22-0-cuda13-pooling`.
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
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/abhinand-medembed-base-v0-1-vllm-cuda13`
- Routes: `/v1/models/abhinand-medembed-base-v0-1-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/abhinand-medembed-base-v0-1-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/abhinand-medembed-base-v0-1-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/abhinand-medembed-base-v0-1-vllm-cuda13/SKILL.md
