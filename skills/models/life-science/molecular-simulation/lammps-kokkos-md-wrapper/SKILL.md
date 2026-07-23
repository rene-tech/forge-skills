---
name: use-forge-lammps-kokkos-md-wrapper
description: Use exact Forge model lammps-kokkos-md-wrapper for simulation_parameters, topology, potential, json to trajectory, energy, log, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use LAMMPS/Kokkos Molecular Dynamics

- Model slug: `lammps-kokkos-md-wrapper`
- Family: `lammps-md`
- Version: `lammps-22jul2025u4-cuda128-sm80-20260616` (`lammps-22jul2025u4-sm80-20260616`)
- Hierarchy: `models / life-science / molecular-simulation`
- Stability: `testing`
- Default eligible: `true`
- License: `GPL-2.0-only; NVIDIA CUDA container terms`
- Research status: `source-linked`

## Purpose

LAMMPS/Kokkos Molecular Dynamics is a live-tested Forge runtime for bounded nonclinical LAMMPS simulations with Kokkos/CUDA acceleration.

## Use this exact model when

- Use this exact `lammps-kokkos-md-wrapper` version when the task supplies simulation_parameters, topology, potential, json and needs trajectory, energy, log, json.
- LAMMPS/Kokkos Molecular Dynamics is a live-tested Forge runtime for bounded nonclinical LAMMPS simulations with Kokkos/CUDA acceleration.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['simulation_parameters', 'topology', 'potential', 'json'] → ['trajectory', 'energy', 'log', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input_script` (textarea; optional; default ''): LAMMPS input script
- `data_file` (textarea; optional; default ''): LAMMPS data file
- `steps` (number; optional; bounds 1..1000000; default 100): Steps
- `timestep_fs` (number; optional; bounds 1e-06..1000000; default 1): Timestep (fs)
- `temperature_k` (number; optional; bounds 1..10000; default 120): Temperature (K)
- `seed` (number; optional; bounds 0..2147483647; default 17): Seed
- `gpu_mode` (select; optional; choices auto, gpu, cpu; default 'auto'): GPU mode
- `mpi_ranks` (number; optional; bounds 1..8; default 1): MPI ranks
- `omp_threads` (number; optional; bounds 1..64; default 1): OpenMP threads
- `gpu_count` (number; optional; bounds 1..8; default 1): Kokkos GPUs
- `kokkos_suffix` (checkbox; optional; default True): Use Kokkos suffix
- `kokkos_gpu_aware` (checkbox; optional; default False): GPU-aware MPI
- `research_use_acknowledgement` (checkbox; required; default True): Research-use acknowledgement

Route: `POST /v1/inference/lammps-kokkos-md-wrapper`

```json
{
  "data_file": "{{data_file}}",
  "gpu_count": "{{gpu_count}}",
  "gpu_mode": "{{gpu_mode}}",
  "input_script": "{{input_script}}",
  "kokkos_gpu_aware": "{{kokkos_gpu_aware}}",
  "kokkos_suffix": "{{kokkos_suffix}}",
  "mpi_ranks": "{{mpi_ranks}}",
  "omp_threads": "{{omp_threads}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}",
  "temperature_k": "{{temperature_k}}",
  "timestep_fs": "{{timestep_fs}}"
}
```

## Exact output

- `trajectory`
- `energy`
- `log`
- `json`

## Required workflow

1. Load this skill and pin model slug `lammps-kokkos-md-wrapper` with version key `lammps-22jul2025u4-sm80-20260616`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/lammps-kokkos-md-wrapper` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/lammps-kokkos-md-wrapper`
- Routes: `/v1/models/lammps-kokkos-md-wrapper/inference-routes`
- Regional deployment: `/v1/models/lammps-kokkos-md-wrapper/regional-deployment`
- Serverless handoff: `/v1/models/lammps-kokkos-md-wrapper/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecular-simulation/lammps-kokkos-md-wrapper/SKILL.md
