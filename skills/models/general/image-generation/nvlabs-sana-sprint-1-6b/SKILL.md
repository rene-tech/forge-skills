---
name: use-forge-nvlabs-sana-sprint-1-6b
description: Use exact Forge model nvlabs-sana-sprint-1-6b for text to image. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use SANA Sprint 1.6B

- Model slug: `nvlabs-sana-sprint-1-6b`
- Family: `nvlabs-sana-sprint`
- Version: `1.6b-1024px-diffusers` (`1-6b-1024px-diffusers`)
- Hierarchy: `models / general / image-generation`
- Stability: `experimental`
- Default eligible: `true`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

SANA Sprint 1.6B text-to-image generation through a reusable Diffusers wrapper.

## Use this exact model when

- Use this exact `nvlabs-sana-sprint-1-6b` version when the task supplies text and needs image.
- SANA Sprint 1.6B text-to-image generation through a reusable Diffusers wrapper.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['image'] contract.
- Do not hide its `experimental` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'A clean product render of an AI image generation workstation, crisp typography, realistic materials, studio lighting'): Prompt
- `seed` (number; optional; bounds 0..999999; default 7): Seed
- `steps` (number; optional; bounds 1..8; default 2): Steps
- `guidance_scale` (number; optional; bounds 0..10; default 4.5): Guidance

Route: `POST /v1/inference/nvlabs-sana-sprint-1-6b`

```json
{
  "guidance_scale": "{{guidance_scale}}",
  "prompt": "{{prompt}}",
  "seed": "{{seed}}",
  "steps": "{{steps}}"
}
```

## Exact output

- `image`

## Required workflow

1. Load this skill and pin model slug `nvlabs-sana-sprint-1-6b` with version key `1-6b-1024px-diffusers`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/nvlabs-sana-sprint-1-6b` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `github-com-nvlabs-sana-c4c236c402`
- Recommended: High-throughput text-to-image generation at 1024×1024 using the NVlabs-provided 1.6B Sana‑Sprint checkpoint packaged for Diffusers. — NVlabs model_zoo and asset/docs present a Sana‑Sprint 1.6B 1024px checkpoint and NVlabs conversion/examples show conversion to a Diffusers pipeline with dtype bf16 and usage examples for 1024×1024 variants; repository performance tables report throughput/latency operating points for 1024×1024 Sana variants.
- Recommended: Image-to-image (img2img) workflows using the SanaSprint img2img Diffusers packaging as provided in NVlabs conversion examples and docs. — NVlabs repository includes a ComfyUI/packaging JSON and model_zoo/conversion examples referencing img2img-capable variants and Diffusers packaging; repository and docs show example configs and precision variants used for image-conditioning workflows.
- Avoid: Treating NVlabs-reported numeric benchmarks (FID/CLIP/GenEval) as protocol-matched equivalents to other models without verifying dataset split identifiers, RNG/seed, and full preprocessing/evaluation protocol. — NVlabs repository performance tables include numeric operating-point summaries (for example a 2-step row with FID=6.50 in asset/docs/sana_sprint.md and a repository-root reported FID=5.92 for 1024×1024), but the inspected NVlabs primary materials do not publish canonical checkpoint-scoped dataset split identifiers or RNG/seed policy required for matched-protocol numeric comparison. Treat numeric rows as upstream-reported summaries unless full protocol metadata is published upstream.
- Avoid: Clinical or PHI-bearing production deployment assuming upstream clinical validation or PHI-handling guidance. — Inspected NVlabs repository and docs do not publish checkpoint-scoped clinical validation, PHI handling procedures, or domain-specific safety approvals for this checkpoint; do not assume the checkpoint is validated for clinical use without separate domain-specific evaluation and approvals.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `experimental` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvlabs-sana-sprint-1-6b`
- Routes: `/v1/models/nvlabs-sana-sprint-1-6b/inference-routes`
- Regional deployment: `/v1/models/nvlabs-sana-sprint-1-6b/regional-deployment`
- Serverless handoff: `/v1/models/nvlabs-sana-sprint-1-6b/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/image-generation/nvlabs-sana-sprint-1-6b/SKILL.md
