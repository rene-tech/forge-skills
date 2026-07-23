---
name: use-forge-stanfordcrfm-biomedlm-2-7b-safety-review
description: Use exact Forge model stanfordcrfm-biomedlm-2-7b-safety-review for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BioMedLM 2.7B

- Model slug: `stanfordcrfm-biomedlm-2-7b-safety-review`
- Family: `stanfordcrfm-biomedlm`
- Version: `hf-3e1a0ab-wrapper-20260426-fix2` (`hf-3e1a0ab-life-science-20260426-fix2`)
- Hierarchy: `models / healthcare / biomedical-text`
- Stability: `testing`
- Default eligible: `false`
- License: `bigscience-bloom-rail-1.0`
- Research status: `source-linked`

## Purpose

BioMedLM 2.7B is a Stanford CRFM and MosaicML biomedical GPT-style language model trained on PubMed abstracts and full-text data from The Pile.

## Use this exact model when

- Use this exact `stanfordcrfm-biomedlm-2-7b-safety-review` version when the task supplies text and needs text.
- BioMedLM 2.7B is a Stanford CRFM and MosaicML biomedical GPT-style language model trained on PubMed abstracts and full-text data from The Pile.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; required; default 'Summarize why biomedical language models can help literature triage, and list two limitations.'): Prompt
- `max_new_tokens` (number; optional; bounds 1..512; default 96): Max new tokens
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `research_use_acknowledgement` (checkbox; required; default True): Research-only use acknowledged

Route: `POST /v1/inference/stanfordcrfm-biomedlm-2-7b-safety-review`

```json
{
  "max_new_tokens": "{{max_new_tokens}}",
  "prompt": "{{prompt}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `stanfordcrfm-biomedlm-2-7b-safety-review` with version key `hf-3e1a0ab-life-science-20260426-fix2`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/stanfordcrfm-biomedlm-2-7b-safety-review` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/stanfordcrfm-biomedlm-2-7b-safety-review`
- Routes: `/v1/models/stanfordcrfm-biomedlm-2-7b-safety-review/inference-routes`
- Regional deployment: `/v1/models/stanfordcrfm-biomedlm-2-7b-safety-review/regional-deployment`
- Serverless handoff: `/v1/models/stanfordcrfm-biomedlm-2-7b-safety-review/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-text/stanfordcrfm-biomedlm-2-7b-safety-review/SKILL.md
