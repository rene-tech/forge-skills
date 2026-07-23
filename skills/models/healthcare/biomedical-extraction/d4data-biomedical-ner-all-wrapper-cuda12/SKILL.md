---
name: use-forge-d4data-biomedical-ner-all-wrapper-cuda12
description: Use exact Forge model d4data-biomedical-ner-all-wrapper-cuda12 for text to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use d4data Biomedical NER All

- Model slug: `d4data-biomedical-ner-all-wrapper-cuda12`
- Family: `d4data-biomedical-ner-all`
- Version: `hf-015a405-wrapper-cuda12-mirrored-20260605t04z` (`hf-015a405-wrapper-cuda12-mirrored-20260605t04z`)
- Hierarchy: `models / healthcare / biomedical-extraction`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

d4data/biomedical-ner-all is an Apache-2.0 Hugging Face Transformers token-classification model for broad biomedical named entity recognition over case-report and biomedical text.

## Use this exact model when

- Use this exact `d4data-biomedical-ner-all-wrapper-cuda12` version when the task supplies text and needs json.
- d4data/biomedical-ner-all is an Apache-2.0 Hugging Face Transformers token-classification model for broad biomedical named entity recognition over case-report and biomedical text.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `text` (textarea; optional; default 'The patient reported palpitations, dyspnea, and no recurrence of symptoms six months after catheter ablation.'): Biomedical text
- `aggregation_strategy` (select; optional; choices simple, first, average, max, none; default 'simple'): Aggregation
- `batch_size` (number; optional; bounds 1..16; default 8): Batch size
- `return_text` (checkbox; optional; default True): Return source text
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /token_classification`

```json
{
  "aggregation_strategy": "{{aggregation_strategy}}",
  "batch_size": "{{batch_size}}",
  "model": "{{model_slug}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_text": "{{return_text}}",
  "text": "{{text}}"
}
```

## Exact output

- `json`

## Required workflow

1. Load this skill and pin model slug `d4data-biomedical-ner-all-wrapper-cuda12` with version key `hf-015a405-wrapper-cuda12-mirrored-20260605t04z`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /token_classification` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/d4data-biomedical-ner-all-wrapper-cuda12`
- Routes: `/v1/models/d4data-biomedical-ner-all-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/d4data-biomedical-ner-all-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/d4data-biomedical-ner-all-wrapper-cuda12/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-extraction/d4data-biomedical-ner-all-wrapper-cuda12/SKILL.md
