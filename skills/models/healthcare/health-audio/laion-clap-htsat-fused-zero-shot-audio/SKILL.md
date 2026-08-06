---
name: use-forge-laion-clap-htsat-fused-zero-shot-audio
description: Use exact Forge model laion-clap-htsat-fused-zero-shot-audio for audio, text to classification, embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use LAION CLAP HTSAT Fused Zero-Shot Audio

- Model slug: `laion-clap-htsat-fused-zero-shot-audio`
- Family: `laion-clap-zero-shot-audio`
- Version: `hf365dea6-transformers53-20260706` (`hf365dea6-transformers53-20260706`)
- Hierarchy: `models / healthcare / health-audio`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

LAION CLAP HTSAT Fused is a contrastive language-audio model for audio-text retrieval and zero-shot audio classification.

## Use this exact model when

- Use this exact `laion-clap-htsat-fused-zero-shot-audio` version when the task supplies audio, text and needs classification, embedding, json.
- LAION CLAP HTSAT Fused is a contrastive language-audio model for audio-text retrieval and zero-shot audio classification.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['audio', 'text'] → ['classification', 'embedding', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `audio_data` (file_upload; optional; default 'data:audio/wav;base64,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'): Audio file
- `audio_url` (url; optional; default ''): HTTPS audio URL
- `candidate_labels` (list; required; default ['a person coughing', 'a person sneezing', 'wheezing breath sounds', 'normal breathing', 'human speech', 'music playing', 'silence', 'background noise']): Candidate prompts
- `top_k` (number; optional; bounds 1..16; default 5): Top prompts
- `return_embeddings` (checkbox; optional; default False): Return embeddings

Route: `POST /zero_shot_audio_classification`

```json
{
  "audio_data": "{{audio_data}}",
  "audio_url": "{{audio_url}}",
  "candidate_labels": "{{candidate_labels}}",
  "return_embeddings": "{{return_embeddings}}",
  "top_k": "{{top_k}}"
}
```

## Exact output

- `classification`
- `embedding`
- `json`

## Required workflow

1. Load this skill and pin model slug `laion-clap-htsat-fused-zero-shot-audio` with version key `hf365dea6-transformers53-20260706`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /zero_shot_audio_classification` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-laion-clap-htsat-fused-5b45ac0127`
- Recommended: Using the Hugging Face upload with Transformers pipelines for CLAP model experimentation and prototyping — The official Hugging Face repository explicitly provides instructions to use laion/clap-htsat-fused with Transformers pipelines, and the model card identifies the upload as "Model card for CLAP: Contrastive Language-Audio Pretraining."
- Avoid: Clinical diagnosis or other healthcare decision-making without expert validation — The provided findings do not report clinical evaluation, clinical deployment guidance, or healthcare-specific validation for this exact upload.
- Avoid: Treating repository popularity or file-history metadata as evidence of model quality — The findings report likes, followers, and commit/file-history facts, but they do not report checkpoint-scoped evaluation results establishing quality for this exact upload.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 512.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/laion-clap-htsat-fused-zero-shot-audio`
- Routes: `/v1/models/laion-clap-htsat-fused-zero-shot-audio/inference-routes`
- Regional deployment: `/v1/models/laion-clap-htsat-fused-zero-shot-audio/regional-deployment`
- Serverless handoff: `/v1/models/laion-clap-htsat-fused-zero-shot-audio/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/health-audio/laion-clap-htsat-fused-zero-shot-audio/SKILL.md
