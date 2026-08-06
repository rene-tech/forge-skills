---
name: use-forge-ncbi-medcpt-query-encoder-tei-cuda-1-9
description: Use exact Forge model ncbi-medcpt-query-encoder-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MedCPT Query Encoder

- Model slug: `ncbi-medcpt-query-encoder-tei-cuda-1-9`
- Family: `ncbi-medcpt-query-encoder`
- Version: `hf-d83a36c-tei-cuda-1.9.3` (`hf-d83a36c-tei-cuda-1-9-3`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `public-domain`
- Research status: `reviewed`

## Purpose

MedCPT Query Encoder is NCBI's public-domain biomedical dense retrieval encoder for short texts such as search queries, questions, and sentences.

## Use this exact model when

- Use this exact `ncbi-medcpt-query-encoder-tei-cuda-1-9` version when the task supplies text and needs embedding.
- MedCPT Query Encoder is NCBI's public-domain biomedical dense retrieval encoder for short texts such as search queries, questions, and sentences.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'How do PARP inhibitors affect homologous recombination deficient ovarian cancer?'): Biomedical query
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

1. Load this skill and pin model slug `ncbi-medcpt-query-encoder-tei-cuda-1-9` with version key `hf-d83a36c-tei-cuda-1-9-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
Read `references/evidence.md` for 1 reviewed public claim(s) and their exact scope.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-ncbi-medcpt-query-encoder-5de2774603`
- Recommended: Biomedical semantic search and dense retrieval for short biomedical texts (queries, questions, sentences) — Hugging Face model card and README identify the checkpoint as the MedCPT Query Encoder producing embeddings for semantic search; the paper/arXiv frame MedCPT as contrastively pre-trained for retrieval and report zero-shot embedding-based retrieval and sentence-similarity evaluations that support this use.
- Recommended: Biomedical sentence-similarity representation (zero-shot evaluation contexts) — The authors report BIOSSES and MedSTS Pearson correlation scores for the MedCPT query encoder in their primary paper/preprint, indicating the checkpoint produces embeddings applicable to sentence-similarity evaluation, subject to the protocol caveats below.
- Avoid: Using the model as a standalone clinical decision-maker or diagnostic system — Primary sources do not report clinical validation, regulatory approval, or decision-making clinical evaluation for the checkpoint; the model is presented for semantic search / retrieval tasks and evaluated in zero-shot retrieval and sentence-similarity benchmarks, not as a diagnostic system.
- Avoid: Treating retrieval or similarity outputs as calibrated probabilities or confidence scores — Primary sources do not report per-output confidence, calibration, or uncertainty outputs for the checkpoint; benchmark scores are aggregated Pearson correlations and do not supply per-output calibration.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/ncbi-medcpt-query-encoder-tei-cuda-1-9`
- Routes: `/v1/models/ncbi-medcpt-query-encoder-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/ncbi-medcpt-query-encoder-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/ncbi-medcpt-query-encoder-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/ncbi-medcpt-query-encoder-tei-cuda-1-9/SKILL.md
