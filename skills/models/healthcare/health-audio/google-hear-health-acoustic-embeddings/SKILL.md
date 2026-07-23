---
name: use-forge-google-hear-health-acoustic-embeddings
description: Use exact Forge model google-hear-health-acoustic-embeddings for audio to embedding, json. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Google HeAR Health Acoustic Embeddings

- Model slug: `google-hear-health-acoustic-embeddings`
- Family: `google-hear-health-acoustics`
- Version: `hear-tensorflow-1-0-0-wrapper-20260706` (`hear-tensorflow-1-0-0-wrapper-20260706`)
- Hierarchy: `models / healthcare / health-audio`
- Stability: `experimental`
- Default eligible: `false`
- License: `Health AI Developer Foundations terms of use; code examples under Apache-2.0 where applicable`
- Research status: `source-linked`

## Purpose

Google HeAR (Health Acoustic Representations) is a health-acoustic embedding model from Google Health, exposed here as a research-only representation model rather than a diagnostic model or cough-type classifier.

## Use this exact model when

- Use this exact `google-hear-health-acoustic-embeddings` version when the task supplies audio and needs embedding, json.
- Google HeAR (Health Acoustic Representations) is a health-acoustic embedding model from Google Health, exposed here as a research-only representation model rather than a diagnostic model or cough-type classifier.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['audio'] → ['embedding', 'json'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `audio_data` (file_upload; required; default 'data:audio/wav;base64,UklGRkQDAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YSADAABlAD4Iuw1NBIgP9xCmEvwKrgs9FL8cdxWOG4YZViQPJ8MdLSknGPEl0ybuGG8ivB7hJKEVIRquHiUY1Q9ECdgWkguyEvD/uQnsBhgGRvIj9lPt3vfC7br2Sumq7mbulOD05B/rrOF13ejaTOSj2HjgwN8r4LjY1+P96eHfweG57lvqo+bm4870ku+c9KTziP1RAhn9dvsqEIsR+QJREFAVQRIJG7AhbRxRGgwYgRqmGbwZYhwyKU4jeShgKpMnmhfWJ/EVzSFYIbobexSRCz4JkRHtBtsJlwGR/C/8wAH9+ST1HfSm8irvKes085js/d/g35Tbot2i1RHjxd5d26TkStmk3k7mk9/P4Szee+xW6S7ia+WP7JrtXPBs7Bj3qvztAJT9kQDSBIAIOgqzA5sLBx1GHFUXUx9NFjsZ5x/xJFIYNyKoK/glyy1NG1srJymSF78gziMZF+Yd4B9lHGsSNghIDzcFbQniAGj/VQDkAgQDV/RA6Z31eOpx8H/v6dwd6R3eON0Q3BLfG9iX3N7XfNQw12rgf9kq2LncCNt17ErqXN+J5OHpXO477tXznPs78pH9lvg8A9sBzg5ZE8MXTw83Fo4P8hxtIDMbxRolJTsmOiiTHh8egR4/HTIZ+BqpIVAfTidcG1wVyyI2D0QSVRi3DPEWmQ/XAw4MLwrm/mH0lfAJ/JT6GPPe8sPwOeOV4MXrb+nM3ynbQtb624blF9dO2erTEt+k1ejifOCS4P3ev+GW78vydfFQ6enrxvHT/hQD8PfpAuAAVQUlA1IQQBT5GX8TARUzGxEThyPuIrEZOR7AIIgoyyUQHdEqAyr3J/kfeh7VG1kl8hk9IRQQzgrlEAsJewd3AFj/jwLf+Pz5LP2U88zxZPCd6+LuofBE4OfnEubC607mA92N4j3nvucR5KzX89x+33bdhubF4k7ty9yV7aPiXezN55juZvV7/i7wcPkC938FOf30AOYOgwNqFYEMGRzzDb0PdRgCF4Aeexn0GgEW0ReOFt0eIiaWHxYboxwGIZQhKxJbGkESexusFfsQ7A8fD1gAKwKL+g=='): Audio file
- `audio_url` (url; optional; default ''): Audio URL
- `normalize` (checkbox; optional; default False): Normalize embedding
- `return_metadata` (checkbox; optional; default True): Return metadata
- `research_use_acknowledgement` (checkbox; required; default True): Research-only use acknowledged

Route: `POST /v1/audio_embeddings`

```json
{
  "audio_data": "{{audio_data}}",
  "audio_url": "{{audio_url}}",
  "normalize": "{{normalize}}",
  "research_use_acknowledgement": "{{research_use_acknowledgement}}",
  "return_metadata": "{{return_metadata}}"
}
```

## Exact output

- `embedding`
- `json`

## Required workflow

1. Load this skill and pin model slug `google-hear-health-acoustic-embeddings` with version key `hear-tensorflow-1-0-0-wrapper-20260706`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/audio_embeddings` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 2.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/google-hear-health-acoustic-embeddings`
- Routes: `/v1/models/google-hear-health-acoustic-embeddings/inference-routes`
- Regional deployment: `/v1/models/google-hear-health-acoustic-embeddings/regional-deployment`
- Serverless handoff: `/v1/models/google-hear-health-acoustic-embeddings/deploy`
- Load `$use-nebius` for direct Nebius operations.

## Progressive references

- `references/evidence.md` — benchmark/source scope.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/healthcare/health-audio/google-hear-health-acoustic-embeddings/SKILL.md
