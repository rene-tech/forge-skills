---
name: use-forge-mit-ast-finetuned-audioset-10-10-0-4593-wrap-259e5d7b
description: Use exact Forge model mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12 for audio to json, scores. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use MIT AST AudioSet Classifier

- Model slug: `mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12`
- Family: `mit-ast-audioset-classifier`
- Version: `hf-f826b80-wrapper-cuda12-safetensors` (`hf-f826b80-wrapper-cuda12-safetensors`)
- Hierarchy: `models / healthcare / health-audio`
- Stability: `experimental`
- Default eligible: `false`
- License: `bsd-3-clause`
- Research status: `source-linked`

## Purpose

MIT AST AudioSet Classifier serves MIT/ast-finetuned-audioset-10-10-0.4593 through a Forge-owned FastAPI wrapper for short WAV, FLAC, MP3, or OGG clips.

## Use this exact model when

- Use this exact `mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12` version when the task supplies audio and needs json, scores.
- MIT AST AudioSet Classifier serves MIT/ast-finetuned-audioset-10-10-0.4593 through a Forge-owned FastAPI wrapper for short WAV, FLAC, MP3, or OGG clips.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['audio'] → ['json', 'scores'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `audio_data` (file_upload; optional; default 'data:audio/wav;base64,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'): Audio clip
- `top_k` (number; optional; bounds 1..50; default 10): Top labels
- `target_labels` (json_editor; optional; default ['Cough', 'Throat clearing', 'Sneeze', 'Wheeze', 'Breathing']): Target labels
- `return_frame_scores` (checkbox; optional; default False): Return frame scores
- `research_use_acknowledgement` (checkbox; optional; default True): Research-only use acknowledged

Route: `POST /audio_classification`

```json
{
  "audio_data": "{{audio_data}}",
  "model": "{{model_slug}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_frame_scores": "{{return_frame_scores}}",
  "target_labels": "{{target_labels}}",
  "top_k": "{{top_k}}"
}
```

## Exact output

- `json`
- `scores`

## Required workflow

1. Load this skill and pin model slug `mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12` with version key `hf-f826b80-wrapper-cuda12-safetensors`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /audio_classification` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 1024.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12`
- Routes: `/v1/models/mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12/inference-routes`
- Regional deployment: `/v1/models/mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12/regional-deployment`
- Serverless handoff: `/v1/models/mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/health-audio/mit-ast-finetuned-audioset-10-10-0-4593-wrapper-cuda12/SKILL.md
