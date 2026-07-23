---
name: use-forge-nvidia-genmol-2-0-0-nim
description: Use exact Forge model nvidia-genmol-2-0-0-nim for molecule to molecule, score, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use GenMol NIM

- Model slug: `nvidia-genmol-2-0-0-nim`
- Family: `nvidia-genmol`
- Version: `2.0.0` (`nim-2-0-0-candidate`)
- Hierarchy: `models / life-science / molecule-design`
- Stability: `testing`
- Default eligible: `true`
- License: `Apache-2.0 source code; NVIDIA Open Model License weights; NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

NVIDIA GenMol 2.0.0 NIM is a life-science molecular generation service for de novo and fragment-guided molecule design using SMILES or SAFE templates.

## Use this exact model when

- Use this exact `nvidia-genmol-2-0-0-nim` version when the task supplies molecule and needs molecule, score, json.
- NVIDIA GenMol 2.0.0 NIM is a life-science molecular generation service for de novo and fragment-guided molecule design using SMILES or SAFE templates.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['molecule'] → ['molecule', 'score', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `smiles` (textarea; optional; default '[C@H]1O[C@@H](CO)[C@H](O)[C@@H]1O.[*{15-15}]'): SMILES or SAFE template
- `scoring` (select; optional; choices QED, LogP; default 'QED'): Scoring
- `unique` (checkbox; optional; default True): Unique molecules only
- `filter` (checkbox; optional; default False): Preserve input fragment
- `num_molecules` (number; optional; bounds 1..1000; default 5): Molecules
- `temperature` (number; optional; bounds 0.01..10; default 1): Temperature
- `noise` (number; optional; bounds 0..2; default 1): Noise
- `gamma` (number; optional; bounds 0..1; default 0): Guidance
- `min_add_len` (number; optional; bounds 1..128; default 24): Minimum added MASK tokens

Route: `POST /generate`

```json
{
  "filter": "{{filter}}",
  "gamma": "{{gamma}}",
  "min_add_len": "{{min_add_len}}",
  "noise": "{{noise}}",
  "num_molecules": "{{num_molecules}}",
  "scoring": "{{scoring}}",
  "smiles": "{{smiles}}",
  "temperature": "{{temperature}}",
  "unique": "{{unique}}"
}
```

## Exact output

- `molecule`
- `score`
- `json`

## Required workflow

1. Load this skill and pin model slug `nvidia-genmol-2-0-0-nim` with version key `nim-2-0-0-candidate`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /generate` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-genmol-2-0-0-nim`
- Routes: `/v1/models/nvidia-genmol-2-0-0-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-genmol-2-0-0-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-genmol-2-0-0-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecule-design/nvidia-genmol-2-0-0-nim/SKILL.md
