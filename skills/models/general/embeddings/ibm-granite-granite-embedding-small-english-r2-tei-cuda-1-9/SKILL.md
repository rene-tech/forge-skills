---
name: use-forge-ibm-granite-granite-embedding-small-english-6b88c4a7
description: Use exact Forge model ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Granite Embedding Small English R2

- Model slug: `ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9`
- Family: `ibm-granite-granite-embedding-small-english-r2`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

IBM Granite Embedding Small English R2 is a public Apache-2.0, non-HCLS, non-physical-AI English dense embedding model for enterprise semantic search, RAG retrieval, long-document retrieval, code retrieval, table retrieval, and multi-turn conversational retrieval.

## Use this exact model when

- Use this exact `ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9` version when the task supplies text and needs embedding.
- IBM Granite Embedding Small English R2 is a public Apache-2.0, non-HCLS, non-physical-AI English dense embedding model for enterprise semantic search, RAG retrieval, long-document retrieval, code retrieval, table retrieval, and multi-turn conversational retrieval.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Granite Embedding Small English R2 creates compact vectors for enterprise semantic search over support tickets, runbooks, product docs, and code-adjacent knowledge.'): Input text

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

1. Load this skill and pin model slug `ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Research key: `huggingface-co-ibm-granite-granite-embedding-small-english-r2-c0cb6b7a27`
- Recommended: Semantic search and document retrieval (query↔passage bi-encoder embeddings) — Hugging Face checkpoint model card and the family README/paper describe the checkpoint as a retrieval-oriented bi-encoder producing fixed-length vectors and report retrieval benchmark aggregates supporting retrieval use.
- Recommended: Retrieval-Augmented Generation (RAG) retrieval stage using dense embeddings (embedding-only retrieval stage) — Primary model-card and family README describe the checkpoint as producing fixed-length vectors suitable for retrieval stages in RAG pipelines (encoder-only bi-encoder).
- Recommended: Long-document retrieval using sliding-window chunking (encoding long documents into chunk embeddings) — Primary README and the paper report a maximum context length of 8192 tokens and describe benchmarking with a sliding-window 512-token chunking protocol for encoding-speed measurement; follow those chunking protocols when reproducing throughput numbers.
- Avoid: Non-English inputs or multilingual retrieval — Primary artifacts identify this checkpoint as English-targeted; authors label the checkpoint and family artifacts as English models and training provenance notes indicate English-targeted data.
- Avoid: Code retrieval tasks — Primary repository and model-card artifacts document English checkpoints targeted at text retrieval and do not claim code-specialized training; authors recommend code-specific models for code retrieval in family-level notes.
- Avoid: Clinical decision-making or medical diagnostics — Primary artifacts do not report evaluation on medical/clinical datasets and authors do not claim clinical validation for this checkpoint.
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

- Model: `/v1/models/ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9`
- Routes: `/v1/models/ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/ibm-granite-granite-embedding-small-english-r2-tei-cuda-1-9/SKILL.md
