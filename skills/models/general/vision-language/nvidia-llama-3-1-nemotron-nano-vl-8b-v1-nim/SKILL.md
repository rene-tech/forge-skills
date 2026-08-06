---
name: use-forge-nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim
description: Use exact Forge model nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim for text, image to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Nvidia Llama 3 1 Nemotron Nano VL 8b V1

- Model slug: `nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim`
- Family: `nvidia-llama-3-1-nemotron-nano-vl-8b-v1`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / vision-language`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-nim; third-party model license`
- Research status: `source-linked`

## Purpose

Nvidia Llama 3 1 Nemotron Nano VL 8b V1 NIM for vision-language chat; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.

## Use this exact model when

- Use this exact `nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim` version when the task supplies text, image and needs text.
- Nvidia Llama 3 1 Nemotron Nano VL 8b V1 NIM for vision-language chat; mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave7.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Describe this image briefly.'): Prompt
- `image_url` (text; optional; default 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII='): Image URL or data URL

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": 128,
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
  "stream": false
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-llama-3-1-nemotron-nano-vl-8b-v1-8525423fc4`
- Recommended: Interactive visual question answering and multimodal chat over images — Primary NVIDIA NIM API reference, Build model card, NGC container listing, and NVIDIA-authored Hugging Face model card describe the model as a vision-language model accepting image and text inputs and list interactive image Q&A and multimodal chat among supported use cases.
- Recommended: Document and image summarization — NVIDIA primary sources for the checkpoint list image summarization and document-image summarization among intended uses.
- Recommended: OCR and document understanding from image inputs — Primary NVIDIA sources explicitly list optical character recognition and document‑intelligence use cases for this VL checkpoint.
- Avoid: Clinical diagnostic or regulated medical use — Primary sources inspected for this checkpoint do not report clinical validation, regulatory approval, or medical‑use evaluation for the exact Forge-served artifact.
- Avoid: Any task requiring documented calibrated confidence scores or probability-calibrated outputs — Primary sources describe text-string outputs but do not report calibrated confidence semantics or probability-calibration procedures for this checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim`
- Routes: `/v1/models/nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/vision-language/nvidia-llama-3-1-nemotron-nano-vl-8b-v1-nim/SKILL.md
