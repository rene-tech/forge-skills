---
name: use-forge-black-forest-labs-flux-2-klein-4b-diffusers-9fecbc80
description: Use exact Forge model black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use FLUX.2 Klein 4B

- Model slug: `black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload`
- Family: `black-forest-labs-flux-2-klein-4b`
- Version: `4b-diffusers-pytorch2.5.1-cuda12.4-cpu-offload-v1` (`4b-diffusers-cpu-offload`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

FLUX.2 Klein 4B low-VRAM Diffusers variant based on the shared PyTorch 2.5.1 CUDA 12.4 script.

## Use this exact model when

- Use this exact `black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload` version when the task supplies text and needs image.
- FLUX.2 Klein 4B low-VRAM Diffusers variant based on the shared PyTorch 2.5.1 CUDA 12.4 script.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A photorealistic editorial image of a compact GPU workstation in a clean studio, natural perspective, softbox lighting, realistic materials, sharp details, no text'): Prompt
- `seed` (number; optional; bounds 0..999999; default 0): Seed
- `steps` (number; optional; bounds 1..16; default 4): Steps
- `guidance_scale` (number; optional; bounds 1..8; default 1): Guidance
- `width` (number; optional; bounds 512..1536; default 1024): Width
- `height` (number; optional; bounds 512..1536; default 1024): Height

Route: `POST /v1/inference/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "height": "{{height}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}",
  "width": "{{width}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload` with version key `4b-diffusers-cpu-offload`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-black-forest-labs-flux-2-klein-4b-618d859d80`
- Recommended: Text-to-image generation (text prompts) — The Hugging Face model page lists text-to-image generation as a supported capability for the FLUX.2 Klein 4B checkpoint; NVIDIA provider documentation and build page also describe the checkpoint as intended for image-generation workflows.
- Recommended: Image editing and multi-reference image-conditioned editing — The Hugging Face model page indicates image editing and multi-reference editing capabilities for the Klein 4B checkpoint; NVIDIA provider pages and the NVIDIA build page report unified generation and editing capabilities for the packaged model.
- Avoid: Use for clinical, medical, or other safety‑critical decision‑making — Evidence gap: no primary-source documentation in the inspected canonical sources indicates clinical validation, regulatory approval, or validated clinical performance for this checkpoint. Checked primary locations for checkpoint-level clinical/regulated claims: Hugging Face model page and NVIDIA provider pages (NIM API reference, NGC container entry, NVIDIA build page).
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload`
- Routes: `/v1/models/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload/inference-routes`
- Regional deployment: `/v1/models/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload/regional-deployment`
- Serverless handoff: `/v1/models/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/black-forest-labs-flux-2-klein-4b-diffusers-cpu-offload/SKILL.md
