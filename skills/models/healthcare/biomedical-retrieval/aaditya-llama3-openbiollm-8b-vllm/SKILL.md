---
name: use-forge-aaditya-llama3-openbiollm-8b-vllm
description: Use exact Forge model aaditya-llama3-openbiollm-8b-vllm for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Llama3 OpenBioLLM 8B

- Model slug: `aaditya-llama3-openbiollm-8b-vllm`
- Family: `aaditya-llama3-openbiollm-8b`
- Version: `70d6bb5` (`hf-70d6bb5-vllm-0-21-0`)
- Hierarchy: `models / healthcare / biomedical-retrieval`
- Stability: `testing`
- Default eligible: `false`
- License: `llama3`
- Research status: `source-linked`

## Purpose

Llama3 OpenBioLLM 8B is a public biomedical instruction-tuned Llama 3 8B derivative intended for biomedical question answering and research workflows.

## Use this exact model when

- Use this exact `aaditya-llama3-openbiollm-8b-vllm` version when the task supplies text and needs text.
- Llama3 OpenBioLLM 8B is a public biomedical instruction-tuned Llama 3 8B derivative intended for biomedical question answering and research workflows.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default '<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are OpenBioLLM running in a Forge onboarding safety gate. Answer only for nonclinical biomedical research, literature triage, and scientific workflow drafting. Do not provide medical advice, diagnosis, treatment, triage, medication recommendations, or patient-specific interpretation.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\nFor nonclinical biomedical literature triage, summarize how large language models can help compare gene-disease association evidence. Include two limitations and avoid diagnosis, treatment, or patient-specific recommendations.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'): Llama 3 Instruct Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..1024; default 256): Max Tokens

Route: `POST /v1/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "stop": [
    "<|eot_id|>",
    "<|end_of_text|>"
  ],
  "stream": true,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `aaditya-llama3-openbiollm-8b-vllm` with version key `hf-70d6bb5-vllm-0-21-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-aaditya-llama3-openbiollm-8b-d788c593a7`
- Recommended: Biomedical question answering and research workflows — Canonical model landing page and repository README describe the checkpoint as an instruction‑tuned biomedical derivative intended for biomedical question answering and research workflows.
- Avoid: Clinical diagnosis, treatment planning, or any clinical decision-making without expert review — Repository README and model card explicitly caution outputs should not replace professional medical advice and advise consulting qualified healthcare providers; repository lacks formal clinical validation and regulatory disclaimers beyond general advisories in the inspected files.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 8192.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/aaditya-llama3-openbiollm-8b-vllm`
- Routes: `/v1/models/aaditya-llama3-openbiollm-8b-vllm/inference-routes`
- Regional deployment: `/v1/models/aaditya-llama3-openbiollm-8b-vllm/regional-deployment`
- Serverless handoff: `/v1/models/aaditya-llama3-openbiollm-8b-vllm/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/biomedical-retrieval/aaditya-llama3-openbiollm-8b-vllm/SKILL.md
