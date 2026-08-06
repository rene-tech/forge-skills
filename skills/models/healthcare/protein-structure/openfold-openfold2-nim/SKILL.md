---
name: use-forge-openfold-openfold2-nim
description: Use exact Forge model openfold-openfold2-nim for sequence to structure. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use OpenFold2

- Model slug: `openfold-openfold2-nim`
- Family: `openfold-openfold2`
- Version: `latest` (`latest`)
- Hierarchy: `models / healthcare / protein-structure`
- Stability: `stable`
- Default eligible: `true`
- License: `Apache-2.0; NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

OpenFold2 NIM for protein structure prediction from amino-acid sequences with optional MSA/template support in the upstream API.

## Use this exact model when

- Use this exact `openfold-openfold2-nim` version when the task supplies sequence and needs structure.
- OpenFold2 NIM for protein structure prediction from amino-acid sequences with optional MSA/template support in the upstream API.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['sequence'] → ['structure'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'GGSKENEISHHAKEIERLQKEIERHKQSIKKLKQSEQSNPPPNPEGTRQARRNRRRRWRERQRQKENEISHHAKEIERLQKEIERHKQSIKKLKQSEC'): Protein sequence

Route: `POST /biology/openfold/openfold2/predict-structure-from-msa-and-template`

```json
{
  "sequence": "{{sequence}}"
}
```

## Exact output

- `structure`

## Required workflow

1. Load this skill and pin model slug `openfold-openfold2-nim` with version key `latest`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /biology/openfold/openfold2/predict-structure-from-msa-and-template` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-openfold-openfold2-b5f4d4f07f`
- Recommended: Monomer protein 3D structure prediction from an amino-acid sequence for research purposes (academic and pharmaceutical research, computer-aided drug design). — The NVIDIA Forge modelcard and NVIDIA NIM overview document the NIM's purpose as predicting 3D protein structure from a query amino-acid sequence with optional MSAs and templates; the NIM exposes a predict endpoint in the API reference.
- Avoid: Multimer / complex (multi-chain) structure prediction — The provided NVIDIA primary sources document the NIM as implementing the monomer use-case and do not document multimer/multi-chain prediction support for the NIM in the supplied findings.
- Avoid: Unsupervised clinical decision support or diagnostic use without expert review — Primary NVIDIA documents and the Forge modelcard describe research use (academic and pharmaceutical research) and do not claim regulatory approval or suitability for clinical/diagnostic decision-making in the provided findings.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/openfold-openfold2-nim`
- Routes: `/v1/models/openfold-openfold2-nim/inference-routes`
- Regional deployment: `/v1/models/openfold-openfold2-nim/regional-deployment`
- Serverless handoff: `/v1/models/openfold-openfold2-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/protein-structure/openfold-openfold2-nim/SKILL.md
