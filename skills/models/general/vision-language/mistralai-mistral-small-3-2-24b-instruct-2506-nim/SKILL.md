---
name: use-forge-mistralai-mistral-small-3-2-24b-instruct-2506-nim
description: Use exact Forge model mistralai-mistral-small-3-2-24b-instruct-2506-nim for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Mistral Small 3.2 24B Instruct 2506

- Model slug: `mistralai-mistral-small-3-2-24b-instruct-2506-nim`
- Family: `mistralai-mistral-small-3-2-24b-instruct-2506`
- Version: `1.3.1` (`nim-1-3-1`)
- Hierarchy: `models / general / vision-language`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Mistral Small 3.2 24B Instruct 2506 packaged as NVIDIA's VLM NIM.

## Use this exact model when

- Use this exact `mistralai-mistral-small-3-2-24b-instruct-2506-nim` version when the task supplies text, image and needs text.
- Mistral Small 3.2 24B Instruct 2506 packaged as NVIDIA's VLM NIM.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Describe the image and identify the visible colors and layout in two concise bullets.'): Prompt
- `image_url` (text; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAJ0lEQVR42mN4pqCFFSlX3MGKGEY10ESD1pYorOjrJRusaFQDTTQAAD//eJDqUy8IAAAAAElFTkSuQmCC'): Image URL or data URL
- `temperature` (number; optional; bounds 0..2; default 0.15): Temperature
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
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `mistralai-mistral-small-3-2-24b-instruct-2506-nim` with version key `nim-1-3-1`.
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

- Model: `/v1/models/mistralai-mistral-small-3-2-24b-instruct-2506-nim`
- Routes: `/v1/models/mistralai-mistral-small-3-2-24b-instruct-2506-nim/inference-routes`
- Regional deployment: `/v1/models/mistralai-mistral-small-3-2-24b-instruct-2506-nim/regional-deployment`
- Serverless handoff: `/v1/models/mistralai-mistral-small-3-2-24b-instruct-2506-nim/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/mistralai-mistral-small-3-2-24b-instruct-2506-nim/SKILL.md
