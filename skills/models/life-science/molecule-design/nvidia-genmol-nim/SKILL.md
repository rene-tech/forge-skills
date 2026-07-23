---
name: use-forge-nvidia-genmol-nim
description: Use exact Forge model nvidia-genmol-nim for molecule to molecule, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use GenMol

- Model slug: `nvidia-genmol-nim`
- Family: `nvidia-genmol`
- Version: `v1` (`v1`)
- Hierarchy: `models / life-science / molecule-design`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-ai-foundation-models-community/mit`
- Research status: `source-linked`

## Purpose

NVIDIA GenMol NIM for fragment-based molecular generation with SMILES or SAFE input.

## Use this exact model when

- Use this exact `nvidia-genmol-nim` version when the task supplies molecule and needs molecule, json.
- NVIDIA GenMol NIM for fragment-based molecular generation with SMILES or SAFE input.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['molecule'] → ['molecule', 'json'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `smiles` (textarea; optional; default 'C124CN3C1.S3(=O)(=O)CC.C4C#N.[*{20-20}]'): SMILES or SAFE sequence
- `scoring` (select; optional; choices QED, LogP; default 'QED'): Scoring
- `unique` (checkbox; optional; default False): Unique molecules only
- `num_molecules` (number; optional; bounds 1..1000; default 30): Number of molecules
- `temperature` (number; optional; bounds 0.01..10; default 1): Temperature
- `noise` (number; optional; bounds 0..2; default 1): Noise
- `step_size` (number; optional; bounds 1..10; default 1): Diffusion step size

Route: `POST /generate`

```json
{
  "noise": "{{noise}}",
  "num_molecules": "{{num_molecules}}",
  "scoring": "{{scoring}}",
  "smiles": "{{smiles}}",
  "step_size": "{{step_size}}",
  "temperature": "{{temperature}}",
  "unique": "{{unique}}"
}
```

## Exact output

- `molecule`
- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-genmol-nim` with version key `v1`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /generate` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-genmol-nim`
- Routes: `/v1/models/nvidia-genmol-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-genmol-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-genmol-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecule-design/nvidia-genmol-nim/SKILL.md
