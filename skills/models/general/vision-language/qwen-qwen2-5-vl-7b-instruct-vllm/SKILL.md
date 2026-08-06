---
name: use-forge-qwen-qwen2-5-vl-7b-instruct-vllm
description: Use exact Forge model qwen-qwen2-5-vl-7b-instruct-vllm for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen2.5-VL 7B Instruct

- Model slug: `qwen-qwen2-5-vl-7b-instruct-vllm`
- Family: `qwen-qwen2-5-vl-7b-instruct`
- Version: `vllm-0.21.0` (`vllm-0-21-0`)
- Hierarchy: `models / general / vision-language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen2.5-VL 7B Instruct is an Apache-2.0 vision-language chat model for OCR, document and chart understanding, visual question answering, and structured extraction.

## Use this exact model when

- Use this exact `qwen-qwen2-5-vl-7b-instruct-vllm` version when the task supplies text, image and needs text.
- Qwen2.5-VL 7B Instruct is an Apache-2.0 vision-language chat model for OCR, document and chart understanding, visual question answering, and structured extraction.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Describe this image and transcribe any visible text. If no text is visible, say so before summarizing the layout in two bullets.'): Prompt
- `image_url` (text; optional; default 'https://raw.githubusercontent.com/github/explore/main/topics/pytorch/pytorch.png'): Image URL or data URL
- `temperature` (number; optional; bounds 0..2; default 0.1): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": [
        {
          "text": "{{prompt}}",
          "type": "text"
        },
        {
          "image_url": {
            "url": "{{image_url}}"
          },
          "type": "image_url"
        }
      ],
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": false,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen2-5-vl-7b-instruct-vllm` with version key `vllm-0-21-0`.
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
- Research key: `huggingface-co-qwen-qwen2-5-vl-7b-instruct-557edb1d63`
- Recommended: General multimodal question answering and scene understanding (text+image/video to text) — The Hugging Face model page and repository README provide an inference example using the processor.apply_chat_template and model.generate code path and report multimodal benchmark scores indicating multimodal QA/video capabilities for the exact Qwen2.5-VL-7B-Instruct checkpoint.
- Recommended: Long-form video/multimodal temporal understanding (research/evaluation) — The Hugging Face model page/README for Qwen2.5-VL-7B-Instruct reports LongVideoBench and other video-related benchmark scores and the preprocessor/config indicate temporal_patch_size and video token IDs for video inputs, supporting evaluation-oriented long-video understanding use under the reported evaluation conditions.
- Avoid: Clinical, medical, or other safety‑critical decision-making — Evidence gap: no primary evidence in the inspected checkpoint repository files or technical report documents any clinical validation, regulatory evaluation, or explicit clinical‑use safeguards for Qwen2.5-VL-7B-Instruct. The model README and config do not document clinical datasets, certifications, or instructions for safety‑critical deployment.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen2-5-vl-7b-instruct-vllm`
- Routes: `/v1/models/qwen-qwen2-5-vl-7b-instruct-vllm/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen2-5-vl-7b-instruct-vllm/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen2-5-vl-7b-instruct-vllm/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/qwen-qwen2-5-vl-7b-instruct-vllm/SKILL.md
