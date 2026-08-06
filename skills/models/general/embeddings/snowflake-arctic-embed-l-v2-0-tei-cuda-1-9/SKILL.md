---
name: use-forge-snowflake-arctic-embed-l-v2-0-tei-cuda-1-9
description: Use exact Forge model snowflake-arctic-embed-l-v2-0-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Snowflake Arctic Embed L v2.0

- Model slug: `snowflake-arctic-embed-l-v2-0-tei-cuda-1-9`
- Family: `snowflake-arctic-embed-l-v2-0`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Snowflake Arctic Embed L v2.0 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual semantic search, enterprise RAG, clustering, and retrieval workloads.

## Use this exact model when

- Use this exact `snowflake-arctic-embed-l-v2-0-tei-cuda-1-9` version when the task supplies text and needs embedding.
- Snowflake Arctic Embed L v2.0 served by Hugging Face Text Embeddings Inference CUDA 1.9 for multilingual semantic search, enterprise RAG, clustering, and retrieval workloads.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'query: How can shared GPU caches reduce model inference cold starts?'): Input text

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "float",
  "input": "{{input}}",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `snowflake-arctic-embed-l-v2-0-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-snowflake-snowflake-arctic-embed-l-v2-0-d8e9bdd569`
- Recommended: Multilingual semantic search and retrieval — Hugging Face model card and Snowflake Cortex Search documentation present this checkpoint as a multilingual text embedding model with 1024 output dimensions and report retrieval-oriented evaluation aggregates.
- Recommended: Enterprise retrieval / RAG pipelines, clustering and indexing of text — Owner model card and Snowflake AI_EMBED/Cortex embed runtime docs describe the model and how Snowflake exposes embeddings for SQL and REST consumption; the 1024-dim embedding shape is suitable for vector-store indexing and similarity search.
- Avoid: Using this checkpoint as a generative language model (text completion / LM logits source) — Upstream owner-provided materials document this checkpoint as a text embedding model that emits dense vectors (1024-dim). There is no primary-source evidence in the inspected owner materials that the checkpoint exposes LM logits or a decoding/generation head appropriate for text generation.
- Avoid: Assuming clinical or regulated suitability without formal validation — Primary owner materials inspected do not label this checkpoint as clinically validated or certified; such deployments require domain expert review and formal validation beyond the documented owner materials.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/snowflake-arctic-embed-l-v2-0-tei-cuda-1-9`
- Routes: `/v1/models/snowflake-arctic-embed-l-v2-0-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/snowflake-arctic-embed-l-v2-0-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/snowflake-arctic-embed-l-v2-0-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/snowflake-arctic-embed-l-v2-0-tei-cuda-1-9/SKILL.md
