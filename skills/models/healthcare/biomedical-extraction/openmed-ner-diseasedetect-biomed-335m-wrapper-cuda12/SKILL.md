---
name: use-forge-openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12
description: Use exact Forge model openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12 for text to json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenMed DiseaseDetect BioMed 335M

- Model slug: `openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12`
- Family: `openmed-ner-diseasedetect-biomed-335m`
- Version: `hf-a62e2a2-cuda12-cvefix-20260604t05z-r2` (`hf-a62e2a2-cuda12-cvefix-20260604t05z-r2`)
- Hierarchy: `models / healthcare / biomedical-extraction`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

OpenMed-NER-DiseaseDetect-BioMed-335M is an Apache-2.0 Hugging Face Transformers token-classification model for disease entity recognition in biomedical text.

## Use this exact model when

- Use this exact `openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12` version when the task supplies text and needs json.
- OpenMed-NER-DiseaseDetect-BioMed-335M is an Apache-2.0 Hugging Face Transformers token-classification model for disease entity recognition in biomedical text.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `text` (textarea; optional; default "A possible link between Crohn's disease and gut microbiota is being investigated in PubMed abstracts."): Biomedical text
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

1. Load this skill and pin model slug `openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12` with version key `hf-a62e2a2-cuda12-cvefix-20260604t05z-r2`.
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
- Research key: `huggingface-co-openmed-openmed-ner-diseasedetect-biomed-335m-8e29af3034`
- Recommended: Extracting disease mentions/entities from biomedical and healthcare text for downstream information-extraction pipelines (research or non-clinical analytics). — The Hugging Face model card for the exact checkpoint describes the model as engineered for disease entity recognition and reports BC5CDR‑Disease performance metrics for this checkpoint.
- Recommended: On-device or local inference for entity extraction in constrained runtimes (research, prototyping, or non-regulated analytics) after downstream validation. — The checkpoint has an ONNX/Android artifact published by the OpenMed owner that is documented to run locally (Python CPU), in the browser, and on Android; use on-device deployments only after validating span/offset mapping and calibration on target data.
- Avoid: Automated clinical diagnosis or clinical decision-making without human oversight. — Evidence gap: the checked primary sources for this checkpoint and its ONNX/Android artifact do not provide explicit documentation of calibrated thresholds, regulatory validation, or clinical-grade certification required to support automated diagnosis without human oversight.
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

- Model: `/v1/models/openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12`
- Routes: `/v1/models/openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-extraction/openmed-ner-diseasedetect-biomed-335m-wrapper-cuda12/SKILL.md
