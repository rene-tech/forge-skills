---
name: use-forge-nvidia-nemotron-nano-12b-v2-vl-nim
description: Use exact Forge model nvidia-nemotron-nano-12b-v2-vl-nim for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Nemotron Nano 12B V2 VL

- Model slug: `nvidia-nemotron-nano-12b-v2-vl-nim`
- Family: `nvidia-nemotron-nano-12b-v2-vl`
- Version: `1.5.0` (`nim-1-5-0`)
- Hierarchy: `models / general / vision-language`
- Stability: `testing`
- Default eligible: `false`
- License: `nvidia-open-model-license; nvidia-nim-container-terms`
- Research status: `source-linked`

## Purpose

NVIDIA Nemotron Nano 12B V2 VL is a commercial-ready vision-language reasoning model for document intelligence, visual question answering, OCR-style extraction, image summarization, and multimodal chat.

## Use this exact model when

- Use this exact `nvidia-nemotron-nano-12b-v2-vl-nim` version when the task supplies text, image and needs text.
- NVIDIA Nemotron Nano 12B V2 VL is a commercial-ready vision-language reasoning model for document intelligence, visual question answering, OCR-style extraction, image summarization, and multimodal chat.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Describe the image and identify any visible text or layout details in two concise bullets.'): Prompt
- `image_url` (text; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAJ0lEQVR42mN4pqCFFSlX3MGKGEY10ESD1pYorOjrJRusaFQDTTQAAD//eJDqUy8IAAAAAElFTkSuQmCC'): Image URL or data URL
- `reasoning_mode` (select; optional; choices /no_think, /think; default '/no_think'): Reasoning Mode
- `temperature` (number; optional; bounds 0..2; default 0.1): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 512): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "{{reasoning_mode}}",
      "role": "system"
    },
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

1. Load this skill and pin model slug `nvidia-nemotron-nano-12b-v2-vl-nim` with version key `nim-1-5-0`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/chat/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 131072.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-nemotron-nano-12b-v2-vl-nim`
- Routes: `/v1/models/nvidia-nemotron-nano-12b-v2-vl-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-nemotron-nano-12b-v2-vl-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-nemotron-nano-12b-v2-vl-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/nvidia-nemotron-nano-12b-v2-vl-nim/SKILL.md
