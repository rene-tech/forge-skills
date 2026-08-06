---
name: use-forge-mit-diffdock-nim
description: Use exact Forge model mit-diffdock-nim for protein_structure, molecule, sdf, mol2, json to docked_pose, sdf, confidence, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MIT DiffDock NIM

- Model slug: `mit-diffdock-nim`
- Family: `mit-diffdock`
- Version: `2.2.0` (`nim-2-2-0-regional-mirror-onboarding`)
- Hierarchy: `models / life-science / docking-affinity`
- Stability: `experimental`
- Default eligible: `false`
- License: `NVIDIA Open Model License; MIT (upstream DiffDock); NVIDIA NIM terms`
- Research status: `source-linked`

## Purpose

DiffDock NIM is NVIDIA's packaged MIT DiffDock service for small-molecule blind docking: it accepts protein PDB text and ligand SDF/MOL2/SMILES-style text, samples protein-ligand poses, and returns ranked docked ligand positions with confidence scores.

## Use this exact model when

- Use this exact `mit-diffdock-nim` version when the task supplies protein_structure, molecule, sdf, mol2, json and needs docked_pose, sdf, confidence, json.
- DiffDock NIM is NVIDIA's packaged MIT DiffDock service for small-molecule blind docking: it accepts protein PDB text and ligand SDF/MOL2/SMILES-style text, samples protein-ligand poses, and returns ranked docked ligand positions with confidence scores.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_structure', 'molecule', 'sdf', 'mol2', 'json'] → ['docked_pose', 'sdf', 'confidence', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `protein` (textarea; required; default 'ATOM      1  N   PRO A1109      -7.773  -8.599   8.647  1.00 19.10           N  \nATOM      2  CA  PRO A1109      -6.848  -8.162   7.581  1.00 17.21           C  \nATOM      3  C   PRO A1109      -7.190  -8.893   6.273  1.00 16.69           C  \nATOM      4  O   PRO A1109      -8.032  -9.790   6.284  1.00 16.90           O  \nATOM      5  CB  PRO A1109      -5.460  -8.555   8.085  1.00 18.07           C  \nATOM      6  CG  PRO A1109      -5.729  -9.745   8.998  1.00 20.63           C  \nATOM      7  CD  PRO A1109      -7.061  -9.412   9.617  1.00 18.77           C  \nATOM      8  N   LEU A1110      -6.573  -8.507   5.152  1.00 13.72           N  \nATOM      9  CA  LEU A1110      -6.611  -9.342   3.931  1.00 13.43           C  \nATOM     10  C   LEU A1110      -5.910 -10.662   4.212  1.00 13.65           C  \nATOM     11  O   LEU A1110      -4.829 -10.727   4.818  1.00 13.16           O  \nATOM     12  CB  LEU A1110      -5.896  -8.666   2.758  1.00 13.75           C  \nATOM     13  CG  LEU A1110      -6.437  -7.340   2.264  1.00 15.04           C  \nATOM     14  CD1 LEU A1110      -5.512  -6.724   1.227  1.00 16.47           C  \nATOM     15  CD2 LEU A1110      -7.818  -7.521   1.685  1.00 17.01           C  \nATOM     16  N   PRO A1111      -6.468 -11.804   3.750  1.00 12.32           N  \nATOM     17  CA  PRO A1111      -5.813 -13.095   3.925  1.00 11.94           C  \nATOM     18  C   PRO A1111      -4.661 -13.388   2.968  1.00 11.95           C  \nATOM     19  O   PRO A1111      -4.036 -14.433   3.057  1.00 15.07           O  \nATOM     20  CB  PRO A1111      -6.986 -14.063   3.701  1.00 13.44           C  \nATOM     21  CG  PRO A1111      -7.853 -13.339   2.710  1.00 13.79           C  \nATOM     22  CD  PRO A1111      -7.819 -11.898   3.166  1.00 13.72           C  \nEND'): Protein PDB ATOM records
- `ligand` (textarea; required; default 'ZU6\n  CCTOOLS-0919241044\n\n 36 37  0  0  0  0  0  0  0  0999 V2000\n    4.7700    0.6810    0.3130 C   0  0  0  0  0\n    3.9180   -0.3290   -0.0750 C   0  0  0  0  0\n    1.5920   -1.1170   -0.5690 C   0  0  0  0  0\n   -0.8170   -2.2390    1.2270 O   0  0  0  0  0\n   -1.2310   -2.5010    0.1180 C   0  0  0  0  0\n   -2.1610   -3.4640   -0.0440 N   0  0  0  0  0\n   -2.6710   -4.1920    1.1190 C   0  0  0  0  0\n   -0.7060   -1.7510   -1.0790 C   0  0  0  0  0\n    0.2870   -0.7670   -0.6410 N   0  0  0  0  0\n    1.9630   -2.2390   -0.8620 O   0  0  0  0  0\n    2.5500   -0.0780   -0.1620 C   0  0  0  0  0\n    4.2770    1.9420    0.6220 C   0  0  0  0  0\n    2.9280    2.2090    0.5480 C   0  0  0  0  0\n    2.0450    1.2050    0.1470 C   0  0  0  0  0\n    0.7090    1.4240    0.0610 N   0  0  0  0  0\n   -0.1110    0.4900   -0.3110 C   0  0  0  0  0\n   -1.5810    0.8150   -0.3810 C   0  0  0  0  0\n   -1.8010    2.2730    0.0290 C   0  0  0  0  0\n   -3.2700    2.5980   -0.0410 C   0  0  0  0  0\n   -3.7010    3.8290    0.2770 O   0  0  0  0  0\n   -4.0610    1.7510   -0.3840 O   0  0  0  0  0\n    5.8310    0.4900    0.3810 H   0  0  0  0  0\n    4.3070   -1.3090   -0.3110 H   0  0  0  0  0\n   -2.4910   -3.6730   -0.9320 H   0  0  0  0  0\n   -3.4090   -4.9250    0.7940 H   0  0  0  0  0\n   -1.8480   -4.7030    1.6180 H   0  0  0  0  0\n   -3.1360   -3.4910    1.8120 H   0  0  0  0  0\n   -0.2400   -2.4530   -1.7720 H   0  0  0  0  0\n   -1.5290   -1.2400   -1.5780 H   0  0  0  0  0\n    4.9600    2.7220    0.9250 H   0  0  0  0  0\n    2.5560    3.1930    0.7920 H   0  0  0  0  0\n   -1.9380    0.6670   -1.4010 H   0  0  0  0  0\n   -2.1310    0.1610    0.2950 H   0  0  0  0  0\n   -1.4440    2.4210    1.0480 H   0  0  0  0  0\n   -1.2510    2.9270   -0.6470 H   0  0  0  0  0\n   -4.6530    3.9900    0.2170 H   0  0  0  0  0\n  1  2  1  0  0  0\n  1 22  1  0  0  0\n  2 11  2  0  0  0\n  2 23  1  0  0  0\n  3 10  2  0  0  0\n  3  9  1  0  0  0\n  5  4  2  0  0  0\n  5  6  1  0  0  0\n  6  7  1  0  0  0\n  6 24  1  0  0  0\n  7 25  1  0  0  0\n  7 26  1  0  0  0\n  7 27  1  0  0  0\n  8  5  1  0  0  0\n  8 28  1  0  0  0\n  8 29  1  0  0  0\n  9  8  1  0  0  0\n 11  3  1  0  0  0\n 12  1  2  0  0  0\n 12 13  1  0  0  0\n 12 30  1  0  0  0\n 13 14  2  0  0  0\n 13 31  1  0  0  0\n 14 11  1  0  0  0\n 14 15  1  0  0  0\n 15 16  1  0  0  0\n 16  9  1  0  0  0\n 16 17  1  0  0  0\n 17 32  1  0  0  0\n 17 33  1  0  0  0\n 18 19  1  0  0  0\n 18 17  1  0  0  0\n 18 34  1  0  0  0\n 18 35  1  0  0  0\n 19 20  1  0  0  0\n 20 36  1  0  0  0\n 21 19  2  0  0  0\nM  END\n$$$$'): Ligand SDF, MOL2, or SMILES text
- `ligand_file_type` (select; required; choices sdf, mol2, txt; default 'sdf'): Ligand file type
- `save_trajectory` (checkbox; optional; default False): Save trajectory
- `skip_gen_conformer` (checkbox; optional; default False): Skip conformer generation
- `is_staged` (checkbox; optional; default False): Use staged docking
- `num_poses` (number; optional; bounds 1..40; default 1): Generated poses
- `steps` (number; optional; bounds 1..100; default 18): Diffusion steps
- `time_divisions` (number; optional; bounds 20..100; default 20): Diffusion time divisions

Route: `POST /molecular-docking/diffdock/generate`

```json
{
  "is_staged": "{{is_staged}}",
  "ligand": "{{ligand}}",
  "ligand_file_type": "{{ligand_file_type}}",
  "num_poses": "{{num_poses}}",
  "protein": "{{protein}}",
  "save_trajectory": "{{save_trajectory}}",
  "skip_gen_conformer": "{{skip_gen_conformer}}",
  "steps": "{{steps}}",
  "time_divisions": "{{time_divisions}}"
}
```

## Exact output

- `docked_pose`
- `sdf`
- `confidence`
- `json`

## Required workflow

1. Load this skill and pin model slug `mit-diffdock-nim` with version key `nim-2-2-0-regional-mirror-onboarding`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /molecular-docking/diffdock/generate` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `build-nvidia-com-mit-diffdock-7ae8526856`
- Recommended: Generate blind docking poses of small‑molecule ligands against a provided protein structure for downstream validation workflows (pose sampling and ranking). — NVIDIA's DiffDock model card documents the model's purpose as predicting 3D protein–ligand binding poses and states that the model outputs sampled poses ranked by a Confidence model; the NIM API and deployment examples expose a pose-generation endpoint and example response fields for ranked poses and confidence scores. Upstream DiffDock paper and canonical repository describe the score-and-confidence architecture that underlies pose sampling and ranking.
- Avoid: Use as the sole evidence source for clinical decision-making or safety‑critical drug development without orthogonal experimental validation and expert review. — NVIDIA model card and NIM documentation describe pose generation and confidence ranking but do not provide clinical‑grade guarantees, numeric calibration of confidence scores to experimental success metrics, or immutable checkpoint checksums tying a published benchmark to the exact NIM-served artifact.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/mit-diffdock-nim`
- Routes: `/v1/models/mit-diffdock-nim/inference-routes`
- Regional deployment: `/v1/models/mit-diffdock-nim/regional-deployment`
- Serverless handoff: `/v1/models/mit-diffdock-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/docking-affinity/mit-diffdock-nim/SKILL.md
