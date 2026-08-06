---
name: use-forge-qwen-qwen3-vl-4b-instruct-vllm-cuda13
description: Use exact Forge model qwen-qwen3-vl-4b-instruct-vllm-cuda13 for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3-VL 4B Instruct

- Model slug: `qwen-qwen3-vl-4b-instruct-vllm-cuda13`
- Family: `qwen-qwen3-vl-4b-instruct`
- Version: `vllm-0.21.0-cuda13-vision-chat` (`vllm-0-21-0-cuda13-vision-chat`)
- Hierarchy: `models / general / vision-language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3-VL 4B Instruct is a public Apache-2.0 vision-language chat model for OCR, visual question answering, document and screenshot understanding, visual coding assistance, and lightweight multimodal reasoning.

## Use this exact model when

- Use this exact `qwen-qwen3-vl-4b-instruct-vllm-cuda13` version when the task supplies text, image and needs text.
- Qwen3-VL 4B Instruct is a public Apache-2.0 vision-language chat model for OCR, visual question answering, document and screenshot understanding, visual coding assistance, and lightweight multimodal reasoning.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Describe this image in one concise sentence, then list any visible text.'): Prompt
- `image_url` (text; optional; default 'https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg'): Image URL
- `temperature` (number; optional; bounds 0..2; default 0.1): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.8): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 256): Max Tokens

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
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-vl-4b-instruct-vllm-cuda13` with version key `vllm-0-21-0-cuda13-vision-chat`.
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
- Research key: `huggingface-co-qwen-qwen3-vl-4b-instruct-2c30792aed`
- Recommended: OCR and visual document understanding — The Hugging Face model card describes expanded OCR and long-document structure parsing and the repository README describes enhanced visual perception and document-related capabilities; config and tokenizer show explicit vision configuration enabling image tokens.
- Recommended: Visual question answering (VQA) and multimodal reasoning — The Hugging Face model card and repository README describe multimodal capabilities, visual reasoning, and enhanced multimodal reasoning; vision+text configuration entries in config.json support image token integration into generation.
- Recommended: Lightweight multimodal/visual-context assistance (e.g., UI description, visual coding hints) — The README describes enhanced agent interaction capabilities and deeper visual perception applicable to visual-context tasks; the model card documents multimodal chat-style interaction and vision configuration.
- Avoid: High-stakes medical, pharmacological, legal, or PHI-sensitive tasks — Primary sources (model card, repository README, config/tokenizer files, and technical-report listing) do not document validated safe-use claims, clinical validation, or PHI-safe guarantees for this checkpoint.
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

- Model: `/v1/models/qwen-qwen3-vl-4b-instruct-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-vl-4b-instruct-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-vl-4b-instruct-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-vl-4b-instruct-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/qwen-qwen3-vl-4b-instruct-vllm-cuda13/SKILL.md
