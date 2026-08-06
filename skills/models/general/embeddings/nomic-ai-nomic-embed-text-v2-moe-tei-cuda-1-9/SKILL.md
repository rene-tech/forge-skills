---
name: use-forge-nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9
description: Use exact Forge model nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Nomic Embed Text v2 MoE

- Model slug: `nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9`
- Family: `nomic-ai-nomic-embed-text-v2-moe`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Nomic Embed Text v2 MoE is a public Apache-2.0 multilingual text embedding model for retrieval, RAG indexing, semantic search, and clustering.

## Use this exact model when

- Use this exact `nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9` version when the task supplies text and needs embedding.
- Nomic Embed Text v2 MoE is a public Apache-2.0 multilingual text embedding model for retrieval, RAG indexing, semantic search, and clustering.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'search_query: How can multilingual embeddings improve support-ticket retrieval across English, Spanish, and Japanese knowledge bases?'): Input text
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

1. Load this skill and pin model slug `nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Research key: `huggingface-co-nomic-ai-nomic-embed-text-v2-moe-6010f512ca`
- Recommended: Multilingual retrieval — The upstream model card and README describe the checkpoint as a multilingual embedding model and report multilingual retrieval benchmarks (BEIR and MIRACL) for this checkpoint.
- Recommended: Embedding generation for RAG indexing (feature extraction for retrieval-augmented-generation pipelines) — The model card and README indicate the checkpoint is intended for sentence-similarity/feature-extraction and embedding-generation tasks suitable for RAG-style indexing.
- Recommended: Semantic search and clustering using dense embeddings — The upstream model page and README report dense embedding outputs (default dim=768) and list sentence-similarity / feature-extraction usage suitable for semantic search and clustering.
- Avoid: Using unprefixed retrieval inputs for search tasks (omitting documented task/document/query prefixes) — The checkpoint README documents retrieval-style formatting that includes a task-instruction prefix and explicit query/document prefixes; omitting those documented prefixes is not aligned with the documented usage.
- Avoid: Inputs longer than the supported maximum without truncation awareness — A commit/blame view of the README and the checkpoint config indicate maximum sequence settings (max_trained_positions or README-specified) that require validation; exceeding the documented maximum can invalidate tokenization/embedding behavior.
- Avoid: Assuming uniform per-language performance without per-language validation — Primary sources report aggregate multilingual benchmarks but do not provide per-language guarantees in the supplied evidence; do not assume uniform quality across all languages without downstream validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9`
- Routes: `/v1/models/nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/nomic-ai-nomic-embed-text-v2-moe-tei-cuda-1-9/SKILL.md
