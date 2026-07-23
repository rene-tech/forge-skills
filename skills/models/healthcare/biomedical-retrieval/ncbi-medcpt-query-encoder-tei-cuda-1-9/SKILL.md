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
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/ncbi-medcpt-query-encoder-tei-cuda-1-9/SKILL.md
