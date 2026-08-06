---
name: use-forge-oxpig-antifold
description: Use exact Forge model oxpig-antifold for structure to sequence, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use AntiFold

- Model slug: `oxpig-antifold`
- Family: `oxpig-antifold`
- Version: `latest` (`latest`)
- Hierarchy: `models / life-science / protein-design`
- Stability: `testing`
- Default eligible: `true`
- License: `bsd-3-clause`
- Research status: `source-linked`

## Purpose

Open-source AntiFold onboarding manifest for antibody and nanobody inverse folding.

## Use this exact model when

- Use this exact `oxpig-antifold` version when the task supplies structure and needs sequence, json.
- Open-source AntiFold onboarding manifest for antibody and nanobody inverse folding.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['structure'] → ['sequence', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `task` (select; required; choices antibody, nanobody; default 'antibody'): Task
- `pdb` (textarea; required; default ''): Input antibody PDB
- `heavy_chain` (text; required; default 'H'): Heavy chain ID
- `light_chain` (text; optional; default 'L'): Light chain ID
- `include_antigen` (checkbox; optional; default False): Include antigen context
- `antigen_chain` (text; optional; default ''): Antigen chain ID
- `regions` (json_editor; required; default '["CDR1", "CDR2", "CDR3"]'): Regions to mutate
- `select_custom_residues` (checkbox; optional; default False): Select custom residues
- `custom_heavy_residues` (text; optional; default ''): Custom heavy residues
- `custom_light_residues` (text; optional; default ''): Custom light residues
- `verify_sequences` (select; optional; choices none, alphafold, chai; default 'none'): Verify sequences
- `num_sequences` (number; optional; bounds 1..1000; default 2): Number of sequences
- `temperature` (number; optional; bounds 0..1; default 0.2): Temperature
- `num_batches` (number; optional; bounds 1..1000; default 1): Batches

Route: `POST /v1/inference/oxpig-antifold`

```json
{
  "antigen_chain": "{{antigen_chain}}",
  "custom_heavy_residues": "{{custom_heavy_residues}}",
  "custom_light_residues": "{{custom_light_residues}}",
  "heavy_chain": "{{heavy_chain}}",
  "include_antigen": "{{include_antigen}}",
  "light_chain": "{{light_chain}}",
  "num_batches": "{{num_batches}}",
  "num_sequences": "{{num_sequences}}",
  "pdb": "{{pdb}}",
  "regions": "{{regions}}",
  "select_custom_residues": "{{select_custom_residues}}",
  "task": "{{task}}",
  "temperature": "{{temperature}}",
  "verify_sequences": "{{verify_sequences}}"
}
```

## Exact output

- `sequence`
- `json`

## Required workflow

1. Load this skill and pin model slug `oxpig-antifold` with version key `latest`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/oxpig-antifold` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-oxpig-antifold-aef5c06bce`
- Recommended: Antibody variable‑domain inverse folding (predict amino‑acid sequences conditioned on a provided variable‑domain backbone structure). — Repository materials and files indicate AntiFold is implemented to predict sequences that fit antibody variable‑domain backbone structures and are fine‑tuned on antibody structure data.
- Recommended: Generate sampled candidate antibody sequences in FASTA format for downstream structural validation and design workflows. — The repository contains example sampled FASTA outputs demonstrating sampling functionality and per‑sample metadata fields.
- Recommended: Produce per‑residue log‑likelihood CSV outputs for sequence‑to‑structure compatibility analysis and ranking candidate sequences. — The repository includes CSV residue log‑likelihood outputs as part of inference outputs according to repository files/README.
- Avoid: Clinical diagnostic or therapeutic deployment without further validation or regulatory review. — The inspected repository does not include regulatory approvals, clinical‑use documentation, or materials establishing suitability for clinical deployment; additionally, the repository does not provide an immutable release tag or commit SHA uniquely identifying model.pt to support reproducible checkpoint identification.
- Avoid: Assuming built‑in PHI handling, clinical data governance, or production clinical data pipelines. — Evidence gap: the inspected repository does not include explicit PHI/data‑handling instructions, governance procedures, or clinical data mitigation measures.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/oxpig-antifold`
- Routes: `/v1/models/oxpig-antifold/inference-routes`
- Regional deployment: `/v1/models/oxpig-antifold/regional-deployment`
- Serverless handoff: `/v1/models/oxpig-antifold/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-design/oxpig-antifold/SKILL.md
