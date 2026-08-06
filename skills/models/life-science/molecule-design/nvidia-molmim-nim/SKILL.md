---
name: use-forge-nvidia-molmim-nim
description: Use exact Forge model nvidia-molmim-nim for molecule to molecule, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MolMIM NIM

- Model slug: `nvidia-molmim-nim`
- Family: `nvidia-molmim`
- Version: `1.0.0` (`nim-1-0-0-regional-mirror-20260605`)
- Hierarchy: `models / life-science / molecule-design`
- Stability: `testing`
- Default eligible: `false`
- License: `NVIDIA NIM terms; production use requires NVIDIA AI Enterprise licensing`
- Research status: `source-linked`

## Purpose

NVIDIA MolMIM NIM is a life-science small-molecule generation service over SMILES input.

## Use this exact model when

- Use this exact `nvidia-molmim-nim` version when the task supplies molecule and needs molecule, json.
- NVIDIA MolMIM NIM is a life-science small-molecule generation service over SMILES input.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['molecule'] → ['molecule', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `smi` (textarea; required; default 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'): Seed molecule SMILES
- `algorithm` (select; optional; choices CMA-ES, none; default 'CMA-ES'): Generation algorithm
- `property_name` (select; optional; choices QED, plogP; default 'QED'): Property
- `minimize` (checkbox; optional; default False): Minimize property
- `num_molecules` (number; optional; bounds 1..100; default 5): Molecules
- `min_similarity` (number; optional; bounds 0..0.7; default 0.4): Minimum similarity
- `particles` (number; optional; bounds 2..1000; default 8): Particles
- `iterations` (number; optional; bounds 1..1000; default 3): Iterations
- `scaled_radius` (number; optional; bounds 0..2; default 1): Scaled radius

Route: `POST /generate`

```json
{
  "algorithm": "{{algorithm}}",
  "iterations": "{{iterations}}",
  "min_similarity": "{{min_similarity}}",
  "minimize": "{{minimize}}",
  "num_molecules": "{{num_molecules}}",
  "particles": "{{particles}}",
  "property_name": "{{property_name}}",
  "scaled_radius": "{{scaled_radius}}",
  "smi": "{{smi}}"
}
```

## Exact output

- `molecule`
- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-molmim-nim` with version key `nim-1-0-0-regional-mirror-20260605`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /generate` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-molmim-generate-212f025c33`
- Recommended: Sampling novel small-molecule SMILES by perturbing latent representations from a seed molecule — Primary NVIDIA model card, NIM overview, and the MolMIM preprint describe MolMIM as a probabilistic latent-variable auto-encoder that samples valid SMILES by perturbing clustered latent codes derived from a seed molecule.
- Recommended: Compute fixed-length molecular embeddings from SMILES for downstream machine-learning tasks — The official NIM endpoints documentation documents an /embedding endpoint that returns fixed-length numerical embeddings for a given input SMILES string.
- Recommended: Use MolMIM latent-space representations in optimization workflows (example: CMA-ES guided optimization) for early-stage candidate generation under expert review — NVIDIA primary documentation and the NGC model page describe latent-space optimization capability and document CMA-ES usage for optimization in examples and notebooks.
- Avoid: Clinical diagnostic use or direct medical decision making — Primary NVIDIA model-card and NGC explainability pages present MolMIM for molecular design and research and do not document clinical validation, authorization, or regulatory approval for clinical use.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-molmim-nim`
- Routes: `/v1/models/nvidia-molmim-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-molmim-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-molmim-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecule-design/nvidia-molmim-nim/SKILL.md
