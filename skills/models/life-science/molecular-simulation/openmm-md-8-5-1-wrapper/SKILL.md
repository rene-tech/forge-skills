---
name: use-forge-openmm-md-8-5-1-wrapper
description: Use exact Forge model openmm-md-8-5-1-wrapper for simulation_parameters, json to trajectory, energy, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenMM Molecular Dynamics

- Model slug: `openmm-md-8-5-1-wrapper`
- Family: `openmm-md`
- Version: `8.5.1-cuda12-wrapper-profiler-optimized-20260604` (`8-5-1-cuda12-wrapper-profiler-optimized-20260604`)
- Hierarchy: `models / life-science / molecular-simulation`
- Stability: `testing`
- Default eligible: `true`
- License: `MIT and LGPL components; NVIDIA CUDA container terms`
- Research status: `source-linked`

## Purpose

OpenMM Molecular Dynamics is an active Forge runtime for bounded nonclinical MD simulations.

## Use this exact model when

- Use this exact `openmm-md-8-5-1-wrapper` version when the task supplies simulation_parameters, json and needs trajectory, energy, json.
- OpenMM Molecular Dynamics is an active Forge runtime for bounded nonclinical MD simulations.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['simulation_parameters', 'json'] → ['trajectory', 'energy', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `particle_count` (number; optional; bounds 1..4096; default 8): Particles
- `steps` (number; optional; bounds 1..1000000; default 100): Steps
- `timestep_fs` (number; optional; bounds 0.1..10; default 2): Timestep (fs)
- `temperature_k` (number; optional; bounds 1..1000; default 120): Temperature (K)
- `friction_per_ps` (number; optional; bounds 0.001..100; default 1): Friction (1/ps)
- `nonbonded_method` (select; optional; choices NoCutoff, CutoffNonPeriodic, CutoffPeriodic; default 'NoCutoff'): Nonbonded method
- `cutoff_nm` (number; optional; bounds 0.1..5; default 1.2): Cutoff (nm)
- `integrator` (select; optional; choices LangevinMiddle, Verlet; default 'LangevinMiddle'): Integrator
- `platform` (select; optional; choices auto, CUDA, CPU; default 'auto'): Platform
- `precision` (select; optional; choices mixed, single, double; default 'mixed'): CUDA precision
- `return_state` (checkbox; optional; default True): Return final state
- `research_use_acknowledgement` (checkbox; required; default True): Research-use acknowledgement

Route: `POST /v1/inference/openmm-md-8-5-1-wrapper`

```json
{
  "cutoff_nm": "{{cutoff_nm}}",
  "friction_per_ps": "{{friction_per_ps}}",
  "integrator": "{{integrator}}",
  "nonbonded_method": "{{nonbonded_method}}",
  "particle_count": "{{particle_count}}",
  "platform": "{{platform}}",
  "precision": "{{precision}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_state": "{{return_state}}",
  "steps": "{{steps}}",
  "temperature_k": "{{temperature_k}}",
  "timestep_fs": "{{timestep_fs}}"
}
```

## Exact output

- `trajectory`
- `energy`
- `json`

## Required workflow

1. Load this skill and pin model slug `openmm-md-8-5-1-wrapper` with version key `8-5-1-cuda12-wrapper-profiler-optimized-20260604`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/openmm-md-8-5-1-wrapper` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-openmm-openmm-bf9d80932d`
- Recommended: Inspect and build the OpenMM 8.5.1 source snapshot for code-level inspection, compilation, and testing. — The project provides an official release page for 8.5.1 documenting the release contents and a tags index mapping the release to commit f7fa0c2; these primary artifacts support treating the release as a canonical source snapshot to inspect and build from.
- Avoid: Clinical decision-making or clinical-readiness deployment — The provided primary findings do not document clinical validation, PHI-specific processing guarantees, or regulatory compliance statements tied to OpenMM 8.5.1; therefore the checkpoint cannot be relied upon as clinically validated from the inspected upstream artifacts.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/openmm-md-8-5-1-wrapper`
- Routes: `/v1/models/openmm-md-8-5-1-wrapper/inference-routes`
- Regional deployment: `/v1/models/openmm-md-8-5-1-wrapper/regional-deployment`
- Serverless handoff: `/v1/models/openmm-md-8-5-1-wrapper/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecular-simulation/openmm-md-8-5-1-wrapper/SKILL.md
