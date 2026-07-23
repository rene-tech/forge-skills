---
name: use-forge-microsoft-bioemu-v1-1
description: Use exact Forge model microsoft-bioemu-v1-1 for protein_sequence, msa to structure_ensemble, trajectory, pdb, xtc, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BioEmu v1.1

- Model slug: `microsoft-bioemu-v1-1`
- Family: `microsoft-bioemu`
- Version: `bioemu-v1.1-via-bioemu-1.3.1-wrapper` (`bioemu-v1-1-bioemu-1-3-1-wrapper`)
- Hierarchy: `models / life-science / molecular-simulation`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

BioEmu v1.1 is a Microsoft Research AI for Science protein monomer conformational ensemble sampler.

## Use this exact model when

- Use this exact `microsoft-bioemu-v1-1` version when the task supplies protein_sequence, msa and needs structure_ensemble, trajectory, pdb, xtc, json.
- BioEmu v1.1 is a Microsoft Research AI for Science protein monomer conformational ensemble sampler.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence', 'msa'] → ['structure_ensemble', 'trajectory', 'pdb', 'xtc', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; required; default 'GYDPETGTWG'): Protein sequence
- `a3m` (textarea; optional; default ''): A3M alignment
- `num_samples` (number; optional; bounds 1..1000; default 10): Samples
- `model_name` (select; optional; choices bioemu-v1.1, bioemu-v1.0, bioemu-v1.2; default 'bioemu-v1.1'): Checkpoint
- `filter_samples` (select; optional; choices true, false; default 'true'): Filter unphysical samples
- `denoiser_type` (select; optional; choices dpm, heun; default 'dpm'): Denoiser
- `batch_size_100` (number; optional; bounds 1..100; default 10): Batch size at 100 aa
- `base_seed` (number; optional; bounds 0..4294967295; default 101): Base seed

Route: `POST /v1/inference/microsoft-bioemu-v1-1`

```json
{
  "a3m": "{{a3m}}",
  "base_seed": "{{base_seed}}",
  "batch_size_100": "{{batch_size_100}}",
  "denoiser_type": "{{denoiser_type}}",
  "filter_samples": "{{filter_samples}}",
  "model_name": "{{model_name}}",
  "num_samples": "{{num_samples}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `structure_ensemble`
- `trajectory`
- `pdb`
- `xtc`
- `json`

## Required workflow

1. Load this skill and pin model slug `microsoft-bioemu-v1-1` with version key `bioemu-v1-1-bioemu-1-3-1-wrapper`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/microsoft-bioemu-v1-1` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/microsoft-bioemu-v1-1`
- Routes: `/v1/models/microsoft-bioemu-v1-1/inference-routes`
- Regional deployment: `/v1/models/microsoft-bioemu-v1-1/regional-deployment`
- Serverless handoff: `/v1/models/microsoft-bioemu-v1-1/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecular-simulation/microsoft-bioemu-v1-1/SKILL.md
