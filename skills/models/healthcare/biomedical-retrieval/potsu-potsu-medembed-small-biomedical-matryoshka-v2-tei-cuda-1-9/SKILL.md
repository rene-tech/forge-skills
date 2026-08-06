---
name: use-forge-potsu-potsu-medembed-small-biomedical-matryo-949ac497
description: Use exact Forge model potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9 for text to embedding. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MedEmbed Small Biomedical Matryoshka v2

- Model slug: `potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9`
- Family: `potsu-potsu-medembed-small-biomedical-matryoshka`
- Version: `hf-0e64af8-tei-cuda-1.9.3` (`hf-0e64af8-tei-cuda-1-9-3`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

MedEmbed Small Biomedical Matryoshka v2 is a public Apache-2.0 sentence-transformers embedding model for biomedical semantic similarity and retrieval.

## Use this exact model when

- Use this exact `potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9` version when the task supplies text and needs embedding.
- MedEmbed Small Biomedical Matryoshka v2 is a public Apache-2.0 sentence-transformers embedding model for biomedical semantic similarity and retrieval.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['embedding'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `input` (textarea; optional; default 'Query: How does telomerase activity relate to cancer vaccine targets?\n\nPassage: GV1001 is a 16-amino-acid vaccine peptide derived from the human telomerase reverse transcriptase sequence and has been studied as a cancer vaccine candidate.'): Biomedical text
- `encoding_format` (select; optional; choices float; default 'float'): Encoding format

Route: `POST /v1/embeddings`

```json
{
  "encoding_format": "{{encoding_format}}",
  "input": "{{input}}",
  "model": "{{model_slug}}"
}
```

## Exact output

- `embedding`

## Required workflow

1. Load this skill and pin model slug `potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9` with version key `hf-0e64af8-tei-cuda-1-9-3`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-potsu-potsu-medembed-small-biomedical-matryoshka-v2-8730ebfc38`
- Recommended: Extract dense text embeddings for cosine-based semantic similarity or retrieval — The checked checkpoint configuration file sets similarity_fn_name = "cosine", indicating embeddings are intended for cosine-similarity comparisons as recorded in the model config file.
- Avoid: Direct use for clinical decision-making, diagnosis, or other high-stakes clinical automation without expert review — The checked primary-source configuration file contains only model configuration metadata (library-version requirements, similarity function, empty prompts) and does not provide checkpoint-scoped certification, clinical-use claims, PHI-handling guidance, or clinical benchmarks in the inspected file.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9`
- Routes: `/v1/models/potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9/inference-routes`
- Regional deployment: `/v1/models/potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9/regional-deployment`
- Serverless handoff: `/v1/models/potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/potsu-potsu-medembed-small-biomedical-matryoshka-v2-tei-cuda-1-9/SKILL.md
