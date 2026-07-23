---
name: use-forge-gromacs-md-ngc-wrapper
description: Use exact Forge model gromacs-md-ngc-wrapper for structure, topology, simulation_parameters, json to trajectory, energy, log, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use GROMACS Molecular Dynamics

- Model slug: `gromacs-md-ngc-wrapper`
- Family: `gromacs-md`
- Version: `ngc-2023.2-wrapper-20260602` (`ngc-2023-2-wrapper-20260602`)
- Hierarchy: `models / life-science / molecular-simulation`
- Stability: `testing`
- Default eligible: `true`
- License: `LGPL-2.1-or-later; NVIDIA CUDA/HPC container terms`
- Research status: `source-linked`

## Purpose

GROMACS Molecular Dynamics is an active Forge runtime for bounded nonclinical MD simulations.

## Use this exact model when

- Use this exact `gromacs-md-ngc-wrapper` version when the task supplies structure, topology, simulation_parameters, json and needs trajectory, energy, log, json.
- GROMACS Molecular Dynamics is an active Forge runtime for bounded nonclinical MD simulations.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['structure', 'topology', 'simulation_parameters', 'json'] → ['trajectory', 'energy', 'log', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `template` (select; optional; choices argon; default 'argon'): Template
- `coordinate_gro` (textarea; optional; default ''): Coordinate .gro
- `topology_top` (textarea; optional; default ''): Topology .top
- `mdp` (textarea; optional; default ''): MD parameter .mdp
- `tpr_base64` (textarea; optional; default ''): Prepared .tpr (base64)
- `steps` (number; optional; bounds 1..100000; default 100): Steps
- `timestep_ps` (number; optional; bounds 0.0001..0.02; default 0.001): Timestep (ps)
- `temperature_k` (number; optional; bounds 1..1000; default 120): Temperature (K)
- `seed` (number; optional; bounds 0..2147483647; default 17): Seed
- `gpu_mode` (select; optional; choices auto, gpu, cpu; default 'auto'): GPU mode
- `threads` (number; optional; bounds 1..32; default 1): CPU threads
- `research_use_acknowledgement` (checkbox; required; default True): Research-use acknowledgement

Route: `POST /v1/inference/gromacs-md-ngc-wrapper`

```json
{
  "coordinate_gro": "{{coordinate_gro}}",
  "gpu_mode": "{{gpu_mode}}",
  "mdp": "{{mdp}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}",
  "temperature_k": "{{temperature_k}}",
  "template": "{{template}}",
  "threads": "{{threads}}",
  "timestep_ps": "{{timestep_ps}}",
  "topology_top": "{{topology_top}}",
  "tpr_base64": "{{tpr_base64}}"
}
```

## Exact output

- `trajectory`
- `energy`
- `log`
- `json`

## Required workflow

1. Load this skill and pin model slug `gromacs-md-ngc-wrapper` with version key `ngc-2023-2-wrapper-20260602`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/gromacs-md-ngc-wrapper` using the declared request template.
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

- Model: `/v1/models/gromacs-md-ngc-wrapper`
- Routes: `/v1/models/gromacs-md-ngc-wrapper/inference-routes`
- Regional deployment: `/v1/models/gromacs-md-ngc-wrapper/regional-deployment`
- Serverless handoff: `/v1/models/gromacs-md-ngc-wrapper/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecular-simulation/gromacs-md-ngc-wrapper/SKILL.md
