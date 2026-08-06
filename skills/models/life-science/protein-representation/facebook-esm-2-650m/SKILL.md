---
name: use-forge-facebook-esm-2-650m
description: Use exact Forge model facebook-esm-2-650m for protein_sequence to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ESM-2 650M

- Model slug: `facebook-esm-2-650m`
- Family: `facebook-esm-2`
- Version: `650m` (`650m`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `stable`
- Default eligible: `true`
- License: `mit`
- Research status: `reviewed`

## Purpose

Meta ESM-2 650M protein language model served as a Forge protein-sequence embedding endpoint.

## Use this exact model when

- Use this exact `facebook-esm-2-650m` version when the task supplies protein_sequence and needs embedding.
- Meta ESM-2 650M protein language model served as a Forge protein-sequence embedding endpoint.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; optional; default 'MTEITAAMVKELRESTGAGMMDCKNALSETQHEK'): Protein sequence
- `max_length` (number; optional; bounds 32..2048; default 1024): Max sequence length

Route: `POST /v1/inference/facebook-esm-2-650m`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `facebook-esm-2-650m` with version key `650m`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/facebook-esm-2-650m` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
Read `references/evidence.md` for 1 reviewed public claim(s) and their exact scope.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-facebook-esm2-t33-650m-ur50d-e087b68cac`
- Recommended: Produce per-residue and per-sequence protein sequence embeddings for downstream representation learning — The checkpoint is an ESM-2 embedding model checkpoint producing embeddings for protein sequences as described on the Hugging Face checkpoint page and in the ESM-2 paper; embeddings are appropriate as input features for downstream protein tasks.
- Recommended: Fine-tuning or adapter-based supervised learning using the checkpoint embeddings as input features — The ESM-2 family and the checkpoint are presented in primary sources as models whose embeddings are usable for downstream tasks and fine-tuning; the checkpoint provides token-level embeddings suitable for downstream predictors.
- Avoid: Assuming the base embedding checkpoint alone performs structure prediction (end-to-end) — Structure-prediction results reported in the ESM-2 paper (e.g., CASP/CAMEO TM-scores) depend on a downstream structure prediction pipeline/head (e.g., ESMFold) rather than solely the base embedding outputs; the base embedding checkpoint by itself is not shown in the primary sources to directly produce folded structures.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/facebook-esm-2-650m`
- Routes: `/v1/models/facebook-esm-2-650m/inference-routes`
- Regional deployment: `/v1/models/facebook-esm-2-650m/regional-deployment`
- Serverless handoff: `/v1/models/facebook-esm-2-650m/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/facebook-esm-2-650m/SKILL.md
