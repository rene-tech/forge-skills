---
name: use-forge-embo-soda-vec-dot-std-cov-losses-vllm-cuda13
description: Use exact Forge model embo-soda-vec-dot-std-cov-losses-vllm-cuda13 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use EMBO SODA-VEC Dot/Std/Cov

- Model slug: `embo-soda-vec-dot-std-cov-losses-vllm-cuda13`
- Family: `embo-soda-vec-dot-std-cov-losses`
- Version: `hf-ec602c1-vllm-0.21.0-cuda13-pooling` (`hf-ec602c1-vllm-0-21-0-cuda13-pooling`)
- Hierarchy: `models / life-science / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

EMBO SODA-VEC Dot/Std/Cov is a MIT-licensed sentence-transformers ModernBERT biomedical and life-science literature embedding model trained on PubMed Central title-abstract pairs with a VICReg-style dot, standard deviation, and covariance objective.

## Use this exact model when

- Use this exact `embo-soda-vec-dot-std-cov-losses-vllm-cuda13` version when the task supplies text and needs embedding.
- EMBO SODA-VEC Dot/Std/Cov is a MIT-licensed sentence-transformers ModernBERT biomedical and life-science literature embedding model trained on PubMed Central title-abstract pairs with a VICReg-style dot, standard deviation, and covariance objective.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Query: CRISPR-Cas9 editing in human induced pluripotent stem cells\n\nCandidate abstract: Genome editing workflows use CRISPR-Cas nucleases to introduce targeted DNA changes, enabling functional studies of disease-associated variants in cellular models.'): Biomedical literature text
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

1. Load this skill and pin model slug `embo-soda-vec-dot-std-cov-losses-vllm-cuda13` with version key `hf-ec602c1-vllm-0-21-0-cuda13-pooling`.
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
- Research key: `huggingface-co-embo-soda-vec-dot-std-cov-losses-81dbb7b5f9`
- Recommended: Training sentence-transformer-style embedding models for text similarity/feature-extraction on PMC title-abstract pairs — The dataset commit page documents a paired (anchor-positive) format with fields 'anchor' (title) and 'positive' (abstract) and lists task categories 'text-similarity' and 'feature-extraction'.
- Avoid: Direct deployment of a model checkpoint for clinical decision-making or production healthcare without further validation — Evidence gap: The inspected primary source is a dataset commit page and does not provide any model checkpoint clinical validation, safety, or calibration statements for a checkpoint.
- Avoid: Assuming model-checkpoint-specific tokenizer, pooling, or calibrated scores for inference — Evidence gap: No model checkpoint, tokenizer metadata, pooling rules, or score-interpretation guidance for a checkpoint are present in the inspected primary source.
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

- Model: `/v1/models/embo-soda-vec-dot-std-cov-losses-vllm-cuda13`
- Routes: `/v1/models/embo-soda-vec-dot-std-cov-losses-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/embo-soda-vec-dot-std-cov-losses-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/embo-soda-vec-dot-std-cov-losses-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/biomedical-retrieval/embo-soda-vec-dot-std-cov-losses-vllm-cuda13/SKILL.md
