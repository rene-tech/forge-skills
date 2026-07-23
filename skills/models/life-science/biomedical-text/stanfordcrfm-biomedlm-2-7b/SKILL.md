---
name: use-forge-stanfordcrfm-biomedlm-2-7b
description: Use exact Forge model stanfordcrfm-biomedlm-2-7b for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BioMedLM 2.7B

- Model slug: `stanfordcrfm-biomedlm-2-7b`
- Family: `stanfordcrfm-biomedlm`
- Version: `2.7b` (`2-7b`)
- Hierarchy: `models / life-science / biomedical-text`
- Stability: `stable`
- Default eligible: `false`
- License: `bigscience-bloom-rail-1.0`
- Research status: `source-linked`

## Purpose

Stanford CRFM BioMedLM 2.7B biomedical text generation wrapper.

## Use this exact model when

- Use this exact `stanfordcrfm-biomedlm-2-7b` version when the task supplies text and needs text.
- Stanford CRFM BioMedLM 2.7B biomedical text generation wrapper.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Summarize why protein sequence embeddings are useful in drug discovery.'): Prompt
- `max_new_tokens` (number; optional; bounds 1..512; default 96): Max new tokens
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature

Route: `POST /v1/inference/stanfordcrfm-biomedlm-2-7b`

```json
{
  "max_new_tokens": "{{max_new_tokens}}",
  "prompt": "{{prompt}}",
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `stanfordcrfm-biomedlm-2-7b` with version key `2-7b`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/stanfordcrfm-biomedlm-2-7b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `stable` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/stanfordcrfm-biomedlm-2-7b`
- Routes: `/v1/models/stanfordcrfm-biomedlm-2-7b/inference-routes`
- Regional deployment: `/v1/models/stanfordcrfm-biomedlm-2-7b/regional-deployment`
- Serverless handoff: `/v1/models/stanfordcrfm-biomedlm-2-7b/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/biomedical-text/stanfordcrfm-biomedlm-2-7b/SKILL.md
