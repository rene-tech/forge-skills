---
name: use-forge-dauparas-proteinmpnn-suite
description: Use exact Forge model dauparas-proteinmpnn-suite for structure, json to protein_sequence, score, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ProteinMPNN Suite

- Model slug: `dauparas-proteinmpnn-suite`
- Family: `dauparas-proteinmpnn`
- Version: `proteinmpnn-solublempnn-ca` (`proteinmpnn-solublempnn-ca`)
- Hierarchy: `models / life-science / protein-design`
- Stability: `experimental`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

ProteinMPNN inverse-folding and sequence-design wrapper for vanilla, soluble, and CA-only ProteinMPNN.

## Use this exact model when

- Use this exact `dauparas-proteinmpnn-suite` version when the task supplies structure, json and needs protein_sequence, score, json.
- ProteinMPNN inverse-folding and sequence-design wrapper for vanilla, soluble, and CA-only ProteinMPNN.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['structure', 'json'] → ['protein_sequence', 'score', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `pdb_file` (textarea; optional; default ''): Protein structure PDB content
- `designed_chains` (text; optional; default 'A'): Designed chains
- `designed_residues` (json_editor; optional; default '{"A":"1-20"}'): Designed residues
- `model_type` (select; optional; choices proteinmpnn, solublempnn, ca-proteinmpnn; default 'proteinmpnn'): Model type
- `noise_level` (select; optional; choices 0.02, 0.1, 0.2, 0.3; default '0.2'): Noise level
- `omit_aas` (text; optional; default 'C'): Amino acids to omit
- `verify_sequences` (select; optional; choices , verify-alphafold, verify-chai; default ''): Verify sequences
- `bias_aa` (text; optional; default ''): Bias AA
- `bias_aa_per_residue` (textarea; optional; default ''): Bias AA per residue
- `omit_aa_per_residue` (textarea; optional; default ''): Omit AA per residue
- `num_sequences` (number; optional; bounds 1..10000; default 2): Number of sequences
- `temperature` (number; optional; bounds 0..1; default 0.1): Temperature
- `homo_oligomer` (number; optional; bounds 0..24; default 0): Homo-oligomer copies

Route: `POST /v1/inference/dauparas-proteinmpnn-suite`

```json
{
  "bias_AA": "{{bias_aa}}",
  "bias_AA_per_residue": "{{bias_aa_per_residue}}",
  "designedChains": "{{designed_chains}}",
  "designedResidues": "{{designed_residues}}",
  "homo_oligomer": "{{homo_oligomer}}",
  "modelType": "{{model_type}}",
  "noiseLevel": "{{noise_level}}",
  "numSequences": "{{num_sequences}}",
  "omitAAs": "{{omit_aas}}",
  "omit_AA_per_residue": "{{omit_aa_per_residue}}",
  "pdbFile": "{{pdb_file}}",
  "temperature": "{{temperature}}",
  "verifySequences": "{{verify_sequences}}"
}
```

## Exact output

- `protein_sequence`
- `score`
- `json`

## Required workflow

1. Load this skill and pin model slug `dauparas-proteinmpnn-suite` with version key `proteinmpnn-solublempnn-ca`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/dauparas-proteinmpnn-suite` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-dauparas-proteinmpnn-9039aae134`
- Recommended: Structure-conditioned protein sequence design / inverse folding (vanilla ProteinMPNN) — Repository contains vanilla model weight directory and end-to-end runtime and utility scripts implementing structure-conditioned sequence-design workflows; protein_mpnn_run.py and protein_mpnn_utils.py implement backbone parsing, featurization, and design/scoring paths consistent with inverse-folding usage.
- Avoid: Clinical or regulated use without expert review and experimental validation — Evidence gap: No primary-source evidence in the inspected repository files documents clinical validation, regulated-use approval, or operationalized safety validations for any upstream weight variant.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/dauparas-proteinmpnn-suite`
- Routes: `/v1/models/dauparas-proteinmpnn-suite/inference-routes`
- Regional deployment: `/v1/models/dauparas-proteinmpnn-suite/regional-deployment`
- Serverless handoff: `/v1/models/dauparas-proteinmpnn-suite/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-design/dauparas-proteinmpnn-suite/SKILL.md
