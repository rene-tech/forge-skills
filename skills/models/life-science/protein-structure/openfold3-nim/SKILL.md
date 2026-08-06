---
name: use-forge-openfold3-nim
description: Use exact Forge model openfold3-nim for protein_sequence, nucleotide_sequence, molecule, msa, template, json to structure, confidence, pdb, cif, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenFold3 NIM

- Model slug: `openfold3-nim`
- Family: `openfold3`
- Version: `1.5.0-rc1` (`nim-1-5-0-rc1-security-upgrade`)
- Hierarchy: `models / life-science / protein-structure`
- Stability: `testing`
- Default eligible: `false`
- License: `NVIDIA Open Model License; Apache-2.0 additional information; NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

OpenFold3 NIM is NVIDIA's packaged OpenFold3 biomolecular complex structure-prediction service.

## Use this exact model when

- Use this exact `openfold3-nim` version when the task supplies protein_sequence, nucleotide_sequence, molecule, msa, template, json and needs structure, confidence, pdb, cif, json.
- OpenFold3 NIM is NVIDIA's packaged OpenFold3 biomolecular complex structure-prediction service.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence', 'nucleotide_sequence', 'molecule', 'msa', 'template', 'json'] → ['structure', 'confidence', 'pdb', 'cif', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; required; default 'MKTVRQERLKSIVR'): Protein sequence
- `chain_id` (text; optional; default 'A'): Chain ID
- `msa_a3m` (textarea; optional; default '>query\nMKTVRQERLKSIVR'): A3M MSA
- `output_format` (select; optional; choices pdb, cif; default 'pdb'): Output format
- `diffusion_samples` (number; optional; bounds 1..5; default 1): Diffusion samples

Route: `POST /biology/openfold/openfold3/predict`

```json
{
  "inputs": [
    {
      "diffusion_samples": "{{diffusion_samples}}",
      "input_id": "primary",
      "molecules": [
        {
          "id": "{{chain_id}}",
          "msa": {
            "main": {
              "a3m": {
                "alignment": "{{msa_a3m}}",
                "format": "a3m"
              }
            }
          },
          "sequence": "{{sequence}}",
          "type": "protein"
        }
      ],
      "output_format": "{{output_format}}"
    }
  ],
  "request_id": "forge-openfold3"
}
```

## Exact output

- `structure`
- `confidence`
- `pdb`
- `cif`
- `json`

## Required workflow

1. Load this skill and pin model slug `openfold3-nim` with version key `nim-1-5-0-rc1-security-upgrade`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /biology/openfold/openfold3/predict` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `docs-nvidia-com-nim-bionemo-openfold3-latest-fcfde9d30f`
- Recommended: Predicting all-atom 3D structures of biomolecular complexes composed of proteins, DNA, RNA, and non-covalent ligands for research and discovery workflows. — NVIDIA NIM overview and modelcard state the OpenFold3 NIM predicts all-atom 3D structures of complexes including proteins, DNA, RNA, and ligands and provides confidence scores; NVIDIA NIM packaging provides an accelerated inference backend for these tasks.
- Recommended: Generating multiple independent structure predictions per request (ensemble-style sampling) via the diffusion_samples parameter. — NIM documentation documents diffusion_samples as an inference parameter that controls the number of independent structures to generate and example requests use this parameter.
- Recommended: Accelerated inference on NVIDIA GPUs using the TensorRT-optimized backend within the NIM container for lower latency vs the open-source baseline. — NVIDIA NIM performance pages report speedups versus the open-source OpenFold3 baseline and catalog/model pages describe an NVIDIA-optimized inference backend.
- Avoid: Modeling covalently bound ligands (covalent docking) relying on NIM or current OpenFold3 inference. — Primary sources indicate ligand inputs are accepted as SMILES or CCD and that covalent ligand support is planned but not currently available in upstream inference and NIM documentation.
- Avoid: Relying on the NIM to perform automatic online MSA pairing (i.e., assuming the service will fetch and pair MSAs automatically without user-provided MSAs). — NIM release notes and API docs indicate MSAs are accepted and required for protein/RNA, and that supported MSA types include paired/unpaired inputs; the docs do not claim the NIM will perform automatic online pairing for all use cases—users must provide MSAs or follow the documented MSA modes.
- Avoid: Assuming numeric calibration thresholds that map per-structure confidence scores to precise expected positional accuracy for the exact NIM-served checkpoint. — Primary sources do not publish a numeric confidence-to-accuracy mapping for the exact NIM-served checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/openfold3-nim`
- Routes: `/v1/models/openfold3-nim/inference-routes`
- Regional deployment: `/v1/models/openfold3-nim/regional-deployment`
- Serverless handoff: `/v1/models/openfold3-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-structure/openfold3-nim/SKILL.md
