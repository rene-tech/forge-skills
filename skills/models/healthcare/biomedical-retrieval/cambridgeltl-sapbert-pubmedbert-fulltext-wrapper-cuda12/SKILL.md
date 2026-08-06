---
name: use-forge-cambridgeltl-sapbert-pubmedbert-fulltext-wra-6f549b5a
description: Use exact Forge model cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use SapBERT PubMedBERT Entity Embeddings

- Model slug: `cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12`
- Family: `cambridgeltl-sapbert-pubmedbert-fulltext`
- Version: `hf-090663c-wrapper-cuda12-slow-tokenizer` (`hf-090663c-wrapper-cuda12-slow-tokenizer`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SapBERT PubMedBERT is an Apache-2.0 biomedical entity representation model trained with UMLS 2020AA entity names using PubMedBERT as the base model.

## Use this exact model when

- Use this exact `cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12` version when the task supplies text and needs embedding.
- SapBERT PubMedBERT is an Apache-2.0 biomedical entity representation model trained with UMLS 2020AA entity names using PubMedBERT as the base model.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Coronavirus infection'): Biomedical entity name
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format
- `normalize` (checkbox; optional; default False): Normalize vector
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "{{encoding_format}}",
  "input": "{{input}}",
  "model": "{{model_slug}}",
  "normalize": "{{normalize}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12` with version key `hf-090663c-wrapper-cuda12-slow-tokenizer`.
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
- Research key: `huggingface-co-cambridgeltl-sapbert-from-pubmedbert-fulltext-767ac42e0a`
- Recommended: Biomedical entity representation / entity-embedding research (embedding tokens/phrases for downstream entity linking or retrieval research) — The repository README and commit metadata present the checkpoint as implementing SapBERT-style biomedical entity representations trained with UMLS and advise using the [CLS] token as the representation, supporting research use to produce entity embeddings consistent with the SapBERT method.
- Avoid: Unreviewed clinical decision-making or direct clinical use without expert oversight — Evidence gap: The inspected primary repository artifacts and commit metadata do not report any clinical-use approvals, certifications, PHI/data-handling guidance, or deployment safety guarantees for clinical settings.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12`
- Routes: `/v1/models/cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/cambridgeltl-sapbert-pubmedbert-fulltext-wrapper-cuda12/SKILL.md
