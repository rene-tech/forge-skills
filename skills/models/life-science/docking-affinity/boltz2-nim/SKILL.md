---
name: use-forge-boltz2-nim
description: Use exact Forge model boltz2-nim for protein_sequence, nucleotide_sequence, molecule, restraints, json to structure, affinity, confidence, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Boltz-2 NIM

- Model slug: `boltz2-nim`
- Family: `mit-boltz2`
- Version: `1.7.0` (`1-7-0`)
- Hierarchy: `models / life-science / docking-affinity`
- Stability: `experimental`
- Default eligible: `false`
- License: `MIT; NVIDIA Community Model License; NVIDIA NIM terms`
- Research status: `reviewed`

## Purpose

Boltz-2 NIM is NVIDIA's packaged Boltz-2 structural-biology service for protein, nucleic-acid, ligand, restraint, structure, and binding-affinity prediction.

## Use this exact model when

- Use this exact `boltz2-nim` version when the task supplies protein_sequence, nucleotide_sequence, molecule, restraints, json and needs structure, affinity, confidence, json.
- Boltz-2 NIM is NVIDIA's packaged Boltz-2 structural-biology service for protein, nucleic-acid, ligand, restraint, structure, and binding-affinity prediction.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence', 'nucleotide_sequence', 'molecule', 'restraints', 'json'] → ['structure', 'affinity', 'confidence', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `polymers` (polymer_list; required; default [{'id': 'A', 'sequence': 'MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF', 'molecule_type': 'protein'}]): Polymer chains
- `ligands` (json_editor; optional; default '[]'): Ligands
- `constraints` (json_editor; optional; default '[]'): Pocket or bond constraints
- `output_format` (select; optional; choices mmcif; default 'mmcif'): Output format
- `without_potentials` (checkbox; optional; default False): Disable inference-time potentials
- `concatenate_msas` (checkbox; optional; default False): Concatenate MSAs
- `write_full_pae` (checkbox; optional; default False): Return full PAE matrix
- `recycling_steps` (number; optional; bounds 1..10; default 3): Recycling steps
- `sampling_steps` (number; optional; bounds 10..1000; default 50): Sampling steps
- `diffusion_samples` (number; optional; bounds 1..25; default 1): Diffusion samples
- `step_scale` (number; optional; bounds 0.5..5; default 1.638): Step scale
- `sampling_steps_affinity` (number; optional; bounds 10..1000; default 200): Affinity sampling steps
- `diffusion_samples_affinity` (number; optional; bounds 1..10; default 5): Affinity diffusion samples

Route: `POST /biology/mit/boltz2/predict`

```json
{
  "concatenate_msas": "{{concatenate_msas}}",
  "constraints": "{{constraints}}",
  "diffusion_samples": "{{diffusion_samples}}",
  "diffusion_samples_affinity": "{{diffusion_samples_affinity}}",
  "ligands": "{{ligands}}",
  "output_format": "{{output_format}}",
  "polymers": "{{polymers}}",
  "recycling_steps": "{{recycling_steps}}",
  "sampling_steps": "{{sampling_steps}}",
  "sampling_steps_affinity": "{{sampling_steps_affinity}}",
  "step_scale": "{{step_scale}}",
  "without_potentials": "{{without_potentials}}",
  "write_full_pae": "{{write_full_pae}}"
}
```

## Exact output

- `structure`
- `affinity`
- `confidence`
- `json`

## Required workflow

1. Load this skill and pin model slug `boltz2-nim` with version key `1-7-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /biology/mit/boltz2/predict` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
Read `references/evidence.md` for 1 reviewed public claim(s) and their exact scope.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
- Declared context/sequence window: 4096.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/boltz2-nim`
- Routes: `/v1/models/boltz2-nim/inference-routes`
- Regional deployment: `/v1/models/boltz2-nim/regional-deployment`
- Serverless handoff: `/v1/models/boltz2-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/docking-affinity/boltz2-nim/SKILL.md
