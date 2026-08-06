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

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-sentence-transformers-all-minilm-l6-v2-32e2db27ec`
- Recommended: Semantic textual similarity for sentences and short paragraphs — The upstream model card and README document the checkpoint as a sentence/short-paragraph encoder mapping inputs to 384-d vectors and list sentence-similarity as an intended use.
- Recommended: Semantic search / information retrieval over short text — The upstream model card and README cite information retrieval and semantic search as intended uses for the produced sentence embeddings.
- Recommended: Clustering of short-text embeddings — The upstream model card and README list clustering as an intended use for the model's sentence embeddings.
- Avoid: Token-level prediction tasks (e.g., token classification, token-level tagging) relying on a token-head output — Upstream README and model card document this checkpoint as a sentence/short-paragraph encoder using mean-pooling to produce sentence embeddings rather than exposing a token-level prediction head.
- Avoid: Encoding long or unsegmented documents with the expectation that the entire document content is always preserved without segmentation — Tokenizer configuration reports model_max_length = 512 but the README examples call truncation=True without stating an explicit default truncation length in the provided findings; effective runtime truncation behavior for long inputs is not specified in the checked primary blobs.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/sentence-transformers-all-minilm-l6-v2-tei-cuda-1-9/SKILL.md
