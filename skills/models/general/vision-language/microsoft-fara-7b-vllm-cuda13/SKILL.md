---
name: use-forge-microsoft-fara-7b-vllm-cuda13
description: Use exact Forge model microsoft-fara-7b-vllm-cuda13 for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Fara-7B

- Model slug: `microsoft-fara-7b-vllm-cuda13`
- Family: `microsoft-fara-7b`
- Version: `vllm-0.21.0-cuda13-vision-chat-probe` (`vllm-0-21-0-cuda13-vision-chat-probe`)
- Hierarchy: `models / general / vision-language`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

Microsoft Fara-7B is a public, ungated MIT-licensed 7B vision-language computer-use agent model.

## Use this exact model when

- Use this exact `microsoft-fara-7b-vllm-cuda13` version when the task supplies text, image and needs text.
- Microsoft Fara-7B is a public, ungated MIT-licensed 7B vision-language computer-use agent model.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `task` (textarea; optional; default 'Describe the visible sample image. If there is no browser control or call-to-action, return a safe no-op browser action and explain why no click is needed.'): Task
- `image_url` (text; optional; default 'https://raw.githubusercontent.com/github/explore/main/topics/pytorch/pytorch.png'): Screenshot URL or data URL
- `temperature` (number; optional; bounds 0..2; default 1e-06): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 768): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "You are a web automation agent that performs actions on websites to fulfill user requests by calling tools. Stop before checkout, booking, purchase, calls, email, orders, personal data entry, payment, sign-in, job applications, or any other critical point requiring user permission or sensitive information.",
      "role": "system"
    },
    {
      "content": [
        {
          "text": "{{task}}",
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

1. Load this skill and pin model slug `microsoft-fara-7b-vllm-cuda13` with version key `vllm-0-21-0-cuda13-vision-chat-probe`.
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
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/microsoft-fara-7b-vllm-cuda13`
- Routes: `/v1/models/microsoft-fara-7b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/microsoft-fara-7b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/microsoft-fara-7b-vllm-cuda13/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/microsoft-fara-7b-vllm-cuda13/SKILL.md
