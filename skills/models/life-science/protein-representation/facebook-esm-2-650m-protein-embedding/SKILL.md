---
name: use-forge-facebook-esm-2-650m-protein-embedding
description: Use exact Forge model facebook-esm-2-650m-protein-embedding for protein_sequence to embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use ESM-2 650M Protein Embeddings

- Model slug: `facebook-esm-2-650m-protein-embedding`
- Family: `facebook-esm-2-650m`
- Version: `hf-08e4846-wrapper-20260427-timing` (`hf-08e4846-wrapper-20260427-timing`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `testing`
- Default eligible: `true`
- License: `mit`
- Research status: `reviewed`

## Purpose

ESM-2 650M is a non-clinical protein language model for sequence representation learning.

## Use this exact model when

- Use this exact `facebook-esm-2-650m-protein-embedding` version when the task supplies protein_sequence and needs embedding, json.
- ESM-2 650M is a non-clinical protein language model for sequence representation learning.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; required; default 'MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTFSYGVQCFSRYPDHMK'): Protein sequence
- `max_length` (number; optional; bounds 32..1024; default 512): Max sequence length

Route: `POST /v1/inference/facebook-esm-2-650m-protein-embedding`

```json
{
  "max_length": "{{max_length}}",
  "sequence": "{{sequence}}"
}
```

## Exact output

- `task`
- `sequence_length`
- `embedding_dim`
- `embedding_preview`
- `embedding_l2`
- `model_time_ms`

## Required workflow

1. Load this skill and pin model slug `facebook-esm-2-650m-protein-embedding` with version key `hf-08e4846-wrapper-20260427-timing`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/facebook-esm-2-650m-protein-embedding` using the declared request template.
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

- Catalog stability is `testing` and default-eligible is `true`.
- Reviewed public benchmark claims are attached below. Keep their model scope, dataset, split, metric, conditions, and caveats intact.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/facebook-esm-2-650m-protein-embedding`
- Routes: `/v1/models/facebook-esm-2-650m-protein-embedding/inference-routes`
- Regional deployment: `/v1/models/facebook-esm-2-650m-protein-embedding/regional-deployment`
- Serverless handoff: `/v1/models/facebook-esm-2-650m-protein-embedding/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/facebook-esm-2-650m-protein-embedding/SKILL.md
