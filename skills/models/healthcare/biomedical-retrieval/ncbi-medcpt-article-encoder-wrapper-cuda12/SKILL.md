---
name: use-forge-ncbi-medcpt-article-encoder-wrapper-cuda12
description: Use exact Forge model ncbi-medcpt-article-encoder-wrapper-cuda12 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MedCPT Article Encoder

- Model slug: `ncbi-medcpt-article-encoder-wrapper-cuda12`
- Family: `ncbi-medcpt-article-encoder`
- Version: `hf-d05a736-wrapper-cuda12-pair-tokenizer-ack` (`hf-d05a736-wrapper-cuda12-pair-tokenizer-ack`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `public-domain`
- Research status: `source-linked`

## Purpose

MedCPT Article Encoder is NCBI's public-domain biomedical dense retrieval encoder for PubMed-style article titles and abstracts.

## Use this exact model when

- Use this exact `ncbi-medcpt-article-encoder-wrapper-cuda12` version when the task supplies text and needs embedding.
- MedCPT Article Encoder is NCBI's public-domain biomedical dense retrieval encoder for PubMed-style article titles and abstracts.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `title` (textarea; optional; default 'Single-cell RNA sequencing reveals immune cell states in inflammatory bowel disease'): Article title
- `abstract` (textarea; optional; default 'Single-cell transcriptomic profiling of intestinal biopsies identifies disease-associated macrophage, fibroblast, and T cell populations and links inflammatory programs to treatment response in inflammatory bowel disease.'): Article abstract
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format
- `normalize` (checkbox; optional; default True): Normalize vector
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /v1/embeddings`

```json
{
  "abstract": "{{abstract}}",
  "encoding_format": "{{encoding_format}}",
  "model": "{{model_slug}}",
  "normalize": "{{normalize}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "title": "{{title}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `ncbi-medcpt-article-encoder-wrapper-cuda12` with version key `hf-d05a736-wrapper-cuda12-pair-tokenizer-ack`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/ncbi-medcpt-article-encoder-wrapper-cuda12`
- Routes: `/v1/models/ncbi-medcpt-article-encoder-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/ncbi-medcpt-article-encoder-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/ncbi-medcpt-article-encoder-wrapper-cuda12/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/ncbi-medcpt-article-encoder-wrapper-cuda12/SKILL.md
