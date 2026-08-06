---
name: use-forge-stabilityai-stable-video-diffusion-img2vid-xt
description: Use exact Forge model stabilityai-stable-video-diffusion-img2vid-xt for image to video. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Stable Video Diffusion XT

- Model slug: `stabilityai-stable-video-diffusion-img2vid-xt`
- Family: `stabilityai-stable-video-diffusion`
- Version: `img2vid-xt-diffusers` (`img2vid-xt-diffusers`)
- Hierarchy: `models / general / video-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `stability-ai-non-commercial-research-community`
- Research status: `source-linked`

## Purpose

Stable Video Diffusion XT image-to-video generation through the Forge Diffusers media wrapper.

## Use this exact model when

- Use this exact `stabilityai-stable-video-diffusion-img2vid-xt` version when the task supplies image and needs video.
- Stable Video Diffusion XT image-to-video generation through the Forge Diffusers media wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['image'] → ['video'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `image` (file_upload; optional; default 'data:image/x-portable-pixmap;base64,UDYKMTYgMTYKMjU1ChRGvhxGuiRGtixGsjRGrjxGqkRGpkxGolRGnlxGmmRGlmxGknRGjnxGioRGhoxGghROvhxOuiROtixOsjROrjxOqkROpkxOolROnlxOmmROlmxOknROjnxOioROhoxOghRWvhxWuiRWtixWsjRWrjxWqkRWpkxWolRWnlxWmmRWlmxWknRWjnxWioRWhoxWghRevhxeuiRetixesjRerjxeqkRepkxeolRenlxemmRelmxeknRejnxeioRehoxeghRmvhxmuiRmtixmsjRmrjxmqkRmpkxmolRmnlxmmmRmlmxmknRmjnxmioRmhoxmghRuvhxuuiRutixusjRurtzw+tzw+tzw+tzw+tzw+tzw+tzw+nRujnxuioRuhoxughR2vhx2uiR2tix2sjR2rtzw+njmbnjmbnjmbnjmbnjmbtzw+nR2jnx2ioR2hox2ghR+vhx+uiR+tix+sjR+rtzw+njmbnjmbnjmbnjmbnjmbtzw+nR+jnx+ioR+hox+ghSGvhyGuiSGtiyGsjSGrtzw+njmbnjmbnjmbnjmbnjmbtzw+nSGjnyGioSGhoyGghSOvhyOuiSOtiyOsjSOrtzw+njmbnjmbnjmbnjmbnjmbtzw+nSOjnyOioSOhoyOghSWvhyWuiSWtiyWsjSWrtzw+njmbnjmbnjmbnjmbnjmbtzw+nSWjnyWioSWhoyWghSevhyeuiSetiyesjSertzw+tzw+tzw+tzw+tzw+tzw+tzw+nSejnyeioSehoyeghSmvhymuiSmtiymsjSmrjymqkSmpkymolSmnlymmmSmlmymknSmjnymioSmhoymghSuvhyuuiSutiyusjSurjyuqkSupkyuolSunlyummSulmyuknSujnyuioSuhoyughS2vhy2uiS2tiy2sjS2rjy2qkS2pky2olS2nly2mmS2lmy2knS2jny2ioS2hoy2ghS+vhy+uiS+tiy+sjS+rjy+qkS+pky+olS+nly+mmS+lmy+knS+jny+ioS+hoy+gg=='): Input Image
- `prompt` (textarea; optional; default 'Animate the input image with subtle cinematic camera motion'): Prompt
- `seed` (number; optional; bounds 0..999999; default 17): Seed
- `num_inference_steps` (number; optional; bounds 10..60; default 25): Steps
- `guidance_scale` (number; optional; bounds 1..15; default 7.5): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 320..1024; default 576): Height
- `num_frames` (number; optional; bounds 14..25; default 25): Frames

Route: `POST /v1/inference/stabilityai-stable-video-diffusion-img2vid-xt`

```json
{
  "fps": 7,
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "image": "{{image}}",
  "num_frames": "{{num_frames}}",
  "num_inference_steps": "{{num_inference_steps}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "width": "{{width}}"
}
```

## Exact output

- `video`

## Required workflow

1. Load this skill and pin model slug `stabilityai-stable-video-diffusion-img2vid-xt` with version key `img2vid-xt-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/stabilityai-stable-video-diffusion-img2vid-xt` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-stabilityai-stable-video-diffusion-img2vid-xt-d9acf75eb0`
- Recommended: Image-to-video generation (short clips conditioned on a single input image) — The official Hugging Face model page and the repository README describe the released SVD and SVD‑XT checkpoints as image-conditioned img2vid latent diffusion models and explicitly document SVD‑XT as fine‑tuned to produce 25 frames at 576×1024.
- Avoid: Long-duration video generation substantially beyond the checkpoint's fine-tuned frame count (e.g., >>25 frames) — Repository/model-card statements document SVD trained for 14 frames and SVD‑XT fine‑tuned to 25 frames; there is no checkpoint-scoped canonical evidence in the checked primary sources that svd_xt.safetensors supports coherent generation of substantially longer sequences without further fine‑tuning or architectural extension.
- Avoid: Relying on emitted per-frame calibrated confidence/probability scores from the checkpoint or demo pipeline — The checked primary sources (model page and README) do not document emission of calibrated per-frame confidence/probability scores or explicit per-frame metadata fields emitted by the checkpoint or demo code.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/stabilityai-stable-video-diffusion-img2vid-xt`
- Routes: `/v1/models/stabilityai-stable-video-diffusion-img2vid-xt/inference-routes`
- Regional deployment: `/v1/models/stabilityai-stable-video-diffusion-img2vid-xt/regional-deployment`
- Serverless handoff: `/v1/models/stabilityai-stable-video-diffusion-img2vid-xt/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/video-generation/stabilityai-stable-video-diffusion-img2vid-xt/SKILL.md
