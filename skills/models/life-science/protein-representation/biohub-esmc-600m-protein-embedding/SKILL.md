---
name: use-forge-biohub-esmc-600m-protein-embedding
description: Use exact Forge model biohub-esmc-600m-protein-embedding for protein_sequence to embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Biohub ESMC 600M Protein Embeddings

- Model slug: `biohub-esmc-600m-protein-embedding`
- Family: `biohub-esmc`
- Version: `hf-465f758-python312-cuda128-wrapper-20260529` (`hf-465f758-python312-cuda128-wrapper-20260529`)
- Hierarchy: `models / life-science / protein-representation`
- Stability: `testing`
- Default eligible: `true`
- License: `mit-with-third-party-notices`
- Research status: `source-linked`

## Purpose

Biohub ESMC 600M is a 2026 protein language model for protein representation learning, protein engineering, variant-effect research, and masked-language modeling.

## Use this exact model when

- Use this exact `biohub-esmc-600m-protein-embedding` version when the task supplies protein_sequence and needs embedding, json.
- Biohub ESMC 600M is a 2026 protein language model for protein representation learning, protein engineering, variant-effect research, and masked-language modeling.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['protein_sequence'] → ['embedding', 'json'] contract.
- Do not hide its `testing` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `sequence` (protein_sequence; required; default 'MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTFSYGVQCFSRYPDHMK'): Protein sequence
- `max_length` (number; optional; bounds 32..2048; default 512): Max sequence length
- `normalize` (checkbox; optional; default True): Normalize embedding
- `return_embedding` (checkbox; optional; default False): Return full embedding vector
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /v1/inference/biohub-esmc-600m-protein-embedding`

```json
{
  "max_length": "{{max_length}}",
  "normalize": "{{normalize}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_embedding": "{{return_embedding}}",
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

1. Load this skill and pin model slug `biohub-esmc-600m-protein-embedding` with version key `hf-465f758-python312-cuda128-wrapper-20260529`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/biohub-esmc-600m-protein-embedding` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 2048.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/biohub-esmc-600m-protein-embedding`
- Routes: `/v1/models/biohub-esmc-600m-protein-embedding/inference-routes`
- Regional deployment: `/v1/models/biohub-esmc-600m-protein-embedding/regional-deployment`
- Serverless handoff: `/v1/models/biohub-esmc-600m-protein-embedding/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/protein-representation/biohub-esmc-600m-protein-embedding/SKILL.md
