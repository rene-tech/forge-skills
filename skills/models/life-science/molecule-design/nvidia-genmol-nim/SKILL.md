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

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-nvidia-genmol-generate-c1a2135e2c`
- Recommended: Fragment‑conditioned molecule generation: motif extension and scaffold decoration — NVIDIA GenMol NIM benchmarks page and the GenMol model card identify motif-extension and scaffold-decoration as supported fragment-completion tasks and provide v2 numeric metrics and hyperparameters for these tasks.
- Recommended: De novo molecule generation (empty template) — NIM endpoints documentation and getting-started examples state that passing a null/empty 'smiles' template to the /generate endpoint triggers de novo generation and that outputs are SAFE/SMILES strings.
- Recommended: Component in hit-generation and lead-optimization pipelines with downstream scoring and filtering — NVIDIA model card and NIM benchmarks present an integrated workflow expectation (generate then compute properties and apply filters); using GenMol as a generative component combined with downstream property scoring is supported by the provided primary artifacts.
- Avoid: One‑step linker design without downstream validation — Primary sources do not provide a verified immutable-checkpoint-mapped numeric table tying the arXiv paper's one-step linker numbers to NV-GenMol-89M-v2; the paper reports upstream experimental metrics and NIM release notes claim v2 improves linker success but no immutable-checkpoint mapping is published in the provided findings (provenance/evidence gap).
- Avoid: Assuming FP32 output property scores are calibrated posterior probabilities for clinical decision-making — NIM benchmarks and model card present FP32 property scores but do not publish a calibration protocol or threshold semantics in the available primary sources (evidence gap).
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

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
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/molecule-design/nvidia-genmol-nim/SKILL.md
