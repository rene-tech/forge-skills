---
name: use-forge-snowflake-arctic-embed-m-v2-0-tei-cuda-1-9
description: Use exact Forge model snowflake-arctic-embed-m-v2-0-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Snowflake Arctic Embed M v2.0

- Model slug: `snowflake-arctic-embed-m-v2-0-tei-cuda-1-9`
- Family: `snowflake-arctic-embed-m-v2-0`
- Version: `tei-cuda-1.9.3` (`tei-cuda-1-9-3`)
- Hierarchy: `models / general / embeddings`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Snowflake Arctic Embed M v2.0 served by Hugging Face Text Embeddings Inference CUDA 1.9 for lower-latency multilingual semantic search, enterprise RAG, clustering, and retrieval workloads.

## Use this exact model when

- Use this exact `snowflake-arctic-embed-m-v2-0-tei-cuda-1-9` version when the task supplies text and needs embedding.
- Snowflake Arctic Embed M v2.0 served by Hugging Face Text Embeddings Inference CUDA 1.9 for lower-latency multilingual semantic search, enterprise RAG, clustering, and retrieval workloads.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'query: How can a smaller multilingual embedding model improve RAG latency?'): Input text

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

1. Load this skill and pin model slug `snowflake-arctic-embed-m-v2-0-tei-cuda-1-9` with version key `tei-cuda-1-9-3`.
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
- Research key: `huggingface-co-snowflake-snowflake-arctic-embed-m-v2-0-0afc1336c2`
- Recommended: Multilingual semantic search and retrieval over text queries and documents — The Hugging Face model card and README position the checkpoint for retrieval and embedding workloads and include retrieval-oriented guidance (CLS pooling recommendation and normalized-embeddings usage in example code).
- Recommended: Embedding text for nearest-neighbor ranking or semantic-similarity workflows using dot-product scoring between normalized embeddings — The model card/README provide example code computing dot-product similarity between query and document embeddings and set normalize=true in usage examples, and the README reports 768-dimensional embeddings intended for dot-product similarity of normalized vectors.
- Avoid: Use for high-stakes clinical or life-critical decision making without separate domain validation and human oversight — Evidence gap: The checked upstream Hugging Face model card and README do not provide clinical validation, healthcare deployment guidance, or life‑critical decision‑support evidence for this exact checkpoint.
- Avoid: Rely on this dossier for exact tokenizer internals, token limits, truncation/padding policies, or immutable upstream-to-Forge revision mapping when strict reproducibility is required — Evidence gap: The checked upstream sources do not document special-token definitions, an immutable upstream artifact-to-serving mapping, or a safetensors checksum locator for this exact checkpoint.
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

- Model: `/v1/models/snowflake-arctic-embed-m-v2-0-tei-cuda-1-9`
- Routes: `/v1/models/snowflake-arctic-embed-m-v2-0-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/snowflake-arctic-embed-m-v2-0-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/snowflake-arctic-embed-m-v2-0-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/embeddings/snowflake-arctic-embed-m-v2-0-tei-cuda-1-9/SKILL.md
