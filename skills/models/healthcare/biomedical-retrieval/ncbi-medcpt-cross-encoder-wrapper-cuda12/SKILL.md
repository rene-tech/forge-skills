---
name: use-forge-ncbi-medcpt-cross-encoder-wrapper-cuda12
description: Use exact Forge model ncbi-medcpt-cross-encoder-wrapper-cuda12 for text to scores. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MedCPT Cross Encoder

- Model slug: `ncbi-medcpt-cross-encoder-wrapper-cuda12`
- Family: `ncbi-medcpt-cross-encoder`
- Version: `hf-71caf65-wrapper-cuda12-safe-state-dict` (`hf-71caf65-wrapper-cuda12-safe-state-dict`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `true`
- License: `public-domain`
- Research status: `source-linked`

## Purpose

MedCPT Cross Encoder is NCBI's public-domain biomedical reranker for scoring a query jointly with candidate PubMed-style article text.

## Use this exact model when

- Use this exact `ncbi-medcpt-cross-encoder-wrapper-cuda12` version when the task supplies text and needs scores.
- MedCPT Cross Encoder is NCBI's public-domain biomedical reranker for scoring a query jointly with candidate PubMed-style article text.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['scores'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'diabetes treatment'): Biomedical query
- `texts` (json_editor; optional; default ['Type 1 and 2 diabetes mellitus: A review on current treatment approach and gene therapy as potential intervention.', 'Diagnosis and Management of Central Diabetes Insipidus in Adults.', 'Impact of Salt Intake on the Pathogenesis and Treatment of Hypertension.']): Candidate PubMed-style article texts
- `raw_scores` (checkbox; optional; default True): Raw logits
- `return_text` (checkbox; optional; default True): Return text
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /rerank`

```json
{
  "model": "{{model_slug}}",
  "query": "{{query}}",
  "raw_scores": "{{raw_scores}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_text": "{{return_text}}",
  "texts": "{{texts}}"
}
```

## Exact output

- `scores`

## Required workflow

1. Load this skill and pin model slug `ncbi-medcpt-cross-encoder-wrapper-cuda12` with version key `hf-71caf65-wrapper-cuda12-safe-state-dict`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /rerank` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-ncbi-medcpt-cross-encoder-d1e8297dde`
- Recommended: Biomedical query + candidate-article reranking (second-stage re-ranker) — The repository README demonstrates loading the tokenizer and AutoModelForSequenceClassification and shows example usage for ranking articles for a given query; the config.json identifies a sequence-classification (cross-encoder) head consistent with reranking use.
- Avoid: Direct diagnostic decision-making without clinical oversight — Evidence gap: the upstream repository artifacts do not provide checkpoint-scoped clinical-use guidance, validation, or PHI/data-handling instructions; no upstream primary-source clinical disclaimer was located in the checked blobs, so clinical diagnostic use should be avoided unless separate validated clinical guidance and evaluation are provided.
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

- Model: `/v1/models/ncbi-medcpt-cross-encoder-wrapper-cuda12`
- Routes: `/v1/models/ncbi-medcpt-cross-encoder-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/ncbi-medcpt-cross-encoder-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/ncbi-medcpt-cross-encoder-wrapper-cuda12/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/ncbi-medcpt-cross-encoder-wrapper-cuda12/SKILL.md
