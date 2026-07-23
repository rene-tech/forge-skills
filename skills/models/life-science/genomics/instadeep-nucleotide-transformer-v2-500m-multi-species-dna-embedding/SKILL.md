---
name: use-forge-instadeep-nucleotide-transformer-v2-500m-mul-8de8ff3a
description: Use exact Forge model instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding for dna_sequence to embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Nucleotide Transformer v2 500M Multi-Species DNA Embeddings

- Model slug: `instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding`
- Family: `instadeep-nucleotide-transformer-v2-500m-multi-species`
- Version: `hf-main-clawbio-dna-mlm-20260605` (`hf-main-clawbio-dna-mlm-20260605`)
- Hierarchy: `models / life-science / genomics`
- Stability: `experimental`
- Default eligible: `false`
- License: `cc-by-nc-sa-4.0`
- Research status: `source-linked`

## Purpose

InstaDeep Nucleotide Transformer v2 500M multi-species is a DNA foundation model for sequence representation and regulatory/genomics tasks.

## Use this exact model when

- Use this exact `instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding` version when the task supplies dna_sequence and needs embedding, json.
- InstaDeep Nucleotide Transformer v2 500M multi-species is a DNA foundation model for sequence representation and regulatory/genomics tasks.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['dna_sequence'] → ['embedding', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (textarea; required; default 'ACGTGTCAGTGATCGTAGCTAGCTAGCTAGCTA'): DNA sequence
- `max_length` (number; optional; bounds 32..1000; default 512): Max sequence length

Route: `POST /v1/inference/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `embedding`
- `json`

## Required workflow

1. Load this skill and pin model slug `instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding` with version key `hf-main-clawbio-dna-mlm-20260605`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1000.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding`
- Routes: `/v1/models/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding/inference-routes`
- Regional deployment: `/v1/models/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding/regional-deployment`
- Serverless handoff: `/v1/models/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/genomics/instadeep-nucleotide-transformer-v2-500m-multi-species-dna-embedding/SKILL.md
