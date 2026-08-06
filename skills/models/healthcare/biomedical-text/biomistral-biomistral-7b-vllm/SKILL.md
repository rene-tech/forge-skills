---
name: use-forge-biomistral-biomistral-7b-vllm
description: Use exact Forge model biomistral-biomistral-7b-vllm for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use BioMistral 7B

- Model slug: `biomistral-biomistral-7b-vllm`
- Family: `biomistral-biomistral-7b`
- Version: `9a11e1f` (`hf-9a11e1f-vllm-0-21-0`)
- Hierarchy: `models / healthcare / biomedical-text`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

BioMistral 7B is an Apache-2.0 biomedical language model further pre-trained from Mistral 7B on PubMed Central Open Access text.

## Use this exact model when

- Use this exact `biomistral-biomistral-7b-vllm` version when the task supplies text and needs text.
- BioMistral 7B is an Apache-2.0 biomedical language model further pre-trained from Mistral 7B on PubMed Central Open Access text.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'For nonclinical biomedical literature triage, summarize how protein language model embeddings can support drug discovery research. Include two limitations and avoid diagnosis, treatment, or patient-specific recommendations.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..1024; default 256): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": "{{messages}}",
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `biomistral-biomistral-7b-vllm` with version key `hf-9a11e1f-vllm-0-21-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-biomistral-biomistral-7b-63b81ae75b`
- Recommended: Biomedical question-answering and domain-specific QA evaluation (research/evaluation use only) — The project model pages and the arXiv preprint present BioMistral-7B and its merged variants as further-pretrained models targeted at medical/biomedical domains and publish SFT/evaluation numeric results for domain QA prompts and medical benchmarks.
- Avoid: Direct deployment for clinical care or production medical decision-making — Evidence gap: the inspected canonical repository/model-page materials and inspected config/tokenizer files do not publish a creator-provided clinical-use certification, PHI-handling guidance, or deployment safety certification; the model is presented and evaluated in a research/evaluation context.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 2048.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/biomistral-biomistral-7b-vllm`
- Routes: `/v1/models/biomistral-biomistral-7b-vllm/inference-routes`
- Regional deployment: `/v1/models/biomistral-biomistral-7b-vllm/regional-deployment`
- Serverless handoff: `/v1/models/biomistral-biomistral-7b-vllm/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-text/biomistral-biomistral-7b-vllm/SKILL.md
