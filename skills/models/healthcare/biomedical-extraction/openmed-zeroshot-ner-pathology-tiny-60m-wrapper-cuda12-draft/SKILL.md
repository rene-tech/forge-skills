---
name: use-forge-openmed-zeroshot-ner-pathology-tiny-60m-wrap-9361106c
description: Use exact Forge model openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft for text to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenMed ZeroShot NER Pathology Tiny 60M

- Model slug: `openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft`
- Family: `openmed-zeroshot-ner-pathology-tiny-60m`
- Version: `hf751c87f-gliner026-cvefix-20260604t01z` (`hf751c87f-gliner026-cvefix-20260604t01z`)
- Hierarchy: `models / healthcare / biomedical-extraction`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

OpenMed ZeroShot NER Pathology Tiny 60M is a public Apache-2.0 GLiNER token-classification model for disease and pathology-oriented biomedical entity extraction.

## Use this exact model when

- Use this exact `openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft` version when the task supplies text and needs json.
- OpenMed ZeroShot NER Pathology Tiny 60M is a public Apache-2.0 GLiNER token-classification model for disease and pathology-oriented biomedical entity extraction.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `text` (textarea; optional; default 'The pathology report describes invasive ductal carcinoma with lymphovascular invasion and no evidence of melanoma.'): Biomedical or pathology text
- `labels` (textarea; optional; default 'DISEASE\nPATHOLOGY_FINDING\nANATOMY'): Entity labels
- `threshold` (number; optional; bounds 0..1; default 0.35): Score threshold
- `return_text` (checkbox; optional; default True): Return source text
- `flat_ner` (checkbox; optional; default True): Flat spans only
- `multi_label` (checkbox; optional; default False): Allow multiple labels per span
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /token_classification`

```json
{
  "flat_ner": "{{flat_ner}}",
  "labels": "{{labels}}",
  "model": "{{model_slug}}",
  "multi_label": "{{multi_label}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_text": "{{return_text}}",
  "text": "{{text}}",
  "threshold": "{{threshold}}"
}
```

## Exact output

- `json`

## Required workflow

1. Load this skill and pin model slug `openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft` with version key `hf751c87f-gliner026-cvefix-20260604t01z`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /token_classification` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-openmed-openmed-zeroshot-ner-pathology-tiny-60m-39d50bbdf4`
- Recommended: Zero-shot disease/entity extraction from biomedical English text using GLiNER label lists — The model card and repository commit-level examples present the checkpoint as a GLiNER zero-shot token-classification model specialized for disease/entity recognition and include example usage loading the model via GLiNER.from_pretrained and passing a label list (['DISEASE']).
- Avoid: Unvalidated use for clinical decision-making or diagnostics without local validation — Evidence gap: The inspected primary sources do not provide explicit creator-authorized clinical-use validation, deployment guidance, or statements authorizing the model for clinical decision-making.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft`
- Routes: `/v1/models/openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft/inference-routes`
- Regional deployment: `/v1/models/openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft/regional-deployment`
- Serverless handoff: `/v1/models/openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-extraction/openmed-zeroshot-ner-pathology-tiny-60m-wrapper-cuda12-draft/SKILL.md
