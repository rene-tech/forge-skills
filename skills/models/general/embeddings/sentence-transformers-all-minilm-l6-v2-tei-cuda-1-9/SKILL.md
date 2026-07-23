---
name: use-forge-sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9
description: Use exact Forge model sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use All-MiniLM-L6-v2

- Model slug: `sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9`
- Family: `sentence-transformers-all-minilm-l6-v2`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

sentence-transformers/all-MiniLM-L6-v2 is a public Apache-2.0 sentence-transformers embedding model for semantic search, sentence similarity, clustering, and compact RAG retrieval over short English text.

## Use this exact model when

- Use this exact `sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9` version when the task supplies text and needs embedding.
- sentence-transformers/all-MiniLM-L6-v2 is a public Apache-2.0 sentence-transformers embedding model for semantic search, sentence similarity, clustering, and compact RAG retrieval over short English text.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'A compact embedding model is useful for semantic search, clustering, and retrieval-augmented generation over short support articles.'): Input text

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

1. Load this skill and pin model slug `sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Declared context/sequence window: 256.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9`
- Routes: `/v1/models/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9/SKILL.md
