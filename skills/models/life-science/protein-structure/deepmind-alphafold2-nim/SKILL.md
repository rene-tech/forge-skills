---
name: use-forge-deepmind-alphafold2-nim
description: Use exact Forge model deepmind-alphafold2-nim for protein_sequence to structure, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use AlphaFold2

- Model slug: `deepmind-alphafold2-nim`
- Family: `deepmind-alphafold2`
- Version: `v1` (`v1`)
- Hierarchy: `models / life-science / protein-structure`
- Stability: `testing`
- Default eligible: `true`
- License: `apache-2.0/cc-by-4.0`
- Research status: `source-linked`

## Purpose

DeepMind AlphaFold2 NVIDIA NIM for protein structure prediction from amino acid sequence.

## Use this exact model when

- Use this exact `deepmind-alphafold2-nim` version when the task supplies protein_sequence and needs structure, json.
- DeepMind AlphaFold2 NVIDIA NIM for protein structure prediction from amino acid sequence.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['structure', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF'): Protein sequence
- `algorithm` (select; optional; choices jackhmmer, mmseqs2; default 'mmseqs2'): MSA algorithm
- `databases` (json_editor; optional; default '["uniref90", "mgnify", "small_bfd"]'): MSA databases
- `relax_prediction` (checkbox; optional; default False): Perform geometry refinement
- `structure_model_preset` (select; optional; choices monomer, casp14, monomer_ptm; default 'monomer'): Structure model preset
- `structure_models_to_relax` (select; optional; choices none, best, all; default 'none'): Models to relax
- `e_value` (number; optional; bounds 0..10; default 1): E-value
- `iterations` (number; optional; bounds 1..3; default 1): MSA iterations

Route: `POST /protein-structure/alphafold2/predict-structure-from-sequence`

```json
{
  "algorithm": "{{algorithm}}",
  "databases": "{{databases}}",
  "e_value": "{{e_value}}",
  "iterations": "{{iterations}}",
  "relax_prediction": "{{relax_prediction}}",
  "sequence": "{{sequence}}",
  "structure_model_preset": "{{structure_model_preset}}",
  "structure_models_to_relax": "{{structure_models_to_relax}}"
}
```

## Exact output

- `structure`
- `json`

## Required workflow

1. Load this skill and pin model slug `deepmind-alphafold2-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /protein-structure/alphafold2/predict-structure-from-sequence` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/deepmind-alphafold2-nim`
- Routes: `/v1/models/deepmind-alphafold2-nim/inference-routes`
- Regional deployment: `/v1/models/deepmind-alphafold2-nim/regional-deployment`
- Serverless handoff: `/v1/models/deepmind-alphafold2-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-structure/deepmind-alphafold2-nim/SKILL.md
