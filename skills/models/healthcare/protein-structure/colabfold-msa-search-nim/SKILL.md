---
name: use-forge-colabfold-msa-search-nim
description: Use exact Forge model colabfold-msa-search-nim for sequence to alignment. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ColabFold MSA Search

- Model slug: `colabfold-msa-search-nim`
- Family: `colabfold-msa-search`
- Version: `latest` (`latest`)
- Hierarchy: `models / healthcare / protein-structure`
- Stability: `stable`
- Default eligible: `true`
- License: `MIT; NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

ColabFold MSA Search NIM for fast GPU-accelerated multiple sequence alignment search from biological protein sequences.

## Use this exact model when

- Use this exact `colabfold-msa-search-nim` version when the task supplies sequence and needs alignment.
- ColabFold MSA Search NIM for fast GPU-accelerated multiple sequence alignment search from biological protein sequences.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['sequence'] → ['alignment'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'SGSMKTAISLPDETFDRVSRRASELGMSRSEFFTKAAQR'): Protein sequence
- `e_value` (number; optional; default 0.0001): E-value threshold
- `iterations` (number; optional; default 1): Search iterations

Route: `POST /biology/colabfold/msa-search/predict`

```json
{
  "e_value": "{{e_value}}",
  "iterations": "{{iterations}}",
  "output_alignment_formats": [
    "a3m",
    "fasta"
  ],
  "sequence": "{{sequence}}"
}
```

## Exact output

- `alignment`

## Required workflow

1. Load this skill and pin model slug `colabfold-msa-search-nim` with version key `latest`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /biology/colabfold/msa-search/predict` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-colabfold-msa-search-d8cbe43c2f`
- Recommended: Generate multiple-sequence alignments (MSAs) to feed downstream protein-structure prediction workflows (AlphaFold2/ColabFold/OpenFold-style pipelines). — NVIDIA documents the MSA Search NIM as a GPU-accelerated provider of MSAs and structural-template search outputs intended to inform downstream structural-prediction models and describes supported search styles ('alphafold2' and 'colabfold') and output formats suitable for downstream predictors.
- Avoid: Clinical diagnostics or medical decision support (PHI/clinical data processing) where validated clinical workflows and explicit PHI-handling policies are required. — Evidence gap: The inspected NVIDIA primary sources for this NIM do not publish explicit clinical-use endorsements, validated clinical workflows, or PHI-specific handling guidance for this exact Forge variant; checkpoint-scoped clinical validation is not provided in the inspected pages.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/colabfold-msa-search-nim`
- Routes: `/v1/models/colabfold-msa-search-nim/inference-routes`
- Regional deployment: `/v1/models/colabfold-msa-search-nim/regional-deployment`
- Serverless handoff: `/v1/models/colabfold-msa-search-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/protein-structure/colabfold-msa-search-nim/SKILL.md
