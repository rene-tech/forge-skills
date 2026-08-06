---
name: use-forge-neuml-pubmedbert-base-embeddings-vllm-cuda13
description: Use exact Forge model neuml-pubmedbert-base-embeddings-vllm-cuda13 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use PubMedBERT Base Embeddings

- Model slug: `neuml-pubmedbert-base-embeddings-vllm-cuda13`
- Family: `neuml-pubmedbert-base-embeddings`
- Version: `hf-b79526d-vllm-0.21.0-cuda13-pooling` (`hf-b79526d-vllm-0-21-0-cuda13-pooling`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

NeuML PubMedBERT Base Embeddings is an Apache-2.0 sentence-transformers model fine-tuned from PubMedBERT for biomedical sentence and paragraph embeddings.

## Use this exact model when

- Use this exact `neuml-pubmedbert-base-embeddings-vllm-cuda13` version when the task supplies text and needs embedding.
- NeuML PubMedBERT Base Embeddings is an Apache-2.0 sentence-transformers model fine-tuned from PubMedBERT for biomedical sentence and paragraph embeddings.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Title: Protein language models for antibody engineering\nAbstract: Dense embeddings can help retrieve related biomedical literature and cluster nonclinical research summaries by mechanism, assay type, and target family.'): Biomedical text
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

1. Load this skill and pin model slug `neuml-pubmedbert-base-embeddings-vllm-cuda13` with version key `hf-b79526d-vllm-0-21-0-cuda13-pooling`.
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
- Research key: `huggingface-co-neuml-pubmedbert-base-embeddings-537c836d9d`
- Recommended: Biomedical sentence and paragraph semantic embeddings for clustering and semantic search — Evidence gap: The inspected checkpoint-scoped blobs (commit page, config.json, tokenizer_config.json at the cited commit) do not contain an explicit upstream recommended-use statement for this exact checkpoint; the model's config and tokenizer blobs record architecture and tokenizer metadata but do not themselves assert recommended downstream use cases.
- Avoid: Direct clinical decision-making without expert review and validation — Evidence gap: The inspected checkpoint-scoped blobs (commit page, config.json, tokenizer_config.json at the cited commit) do not provide checkpoint-scoped clinical-use validation, PHI-handling guidance, or regulatory compliance instructions.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/neuml-pubmedbert-base-embeddings-vllm-cuda13`
- Routes: `/v1/models/neuml-pubmedbert-base-embeddings-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/neuml-pubmedbert-base-embeddings-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/neuml-pubmedbert-base-embeddings-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/neuml-pubmedbert-base-embeddings-vllm-cuda13/SKILL.md
