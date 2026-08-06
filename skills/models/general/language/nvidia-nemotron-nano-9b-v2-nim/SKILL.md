---
name: use-forge-nvidia-nemotron-nano-9b-v2-nim
description: Use exact Forge model nvidia-nemotron-nano-9b-v2-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use NVIDIA Nemotron Nano 9B v2

- Model slug: `nvidia-nemotron-nano-9b-v2-nim`
- Family: `nvidia-nemotron-nano-9b-v2`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `nvidia-ai-foundation-models-community-license`
- Research status: `source-linked`

## Purpose

NVIDIA Nemotron Nano 9B v2 packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.

## Use this exact model when

- Use this exact `nvidia-nemotron-nano-9b-v2-nim` version when the task supplies text and needs text.
- NVIDIA Nemotron Nano 9B v2 packaged as an NVIDIA NIM and mirrored into Forge regional registries as part of all-accessible NVIDIA NIM wave2.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Explain in two concise bullet points how Forge probes model support across GPU regions.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `max_tokens` (number; optional; bounds 1..4096; default 256): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": "{{messages}}",
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `nvidia-nemotron-nano-9b-v2-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-nvidia-nvidia-nemotron-nano-9b-v2-0a7b913edb`
- Recommended: Unified reasoning and chat (general-purpose reasoning + instruction following) — Official NVIDIA model page and downloadable model card describe Nemotron Nano 9B v2 as a unified model intended for reasoning and non-reasoning tasks and document a reasoning-trace-first response mode that can be enabled or controlled.
- Recommended: High-throughput long-context inference (single-GPU long-context serving up to 128k tokens in bf16 on supported NVIDIA GPUs) — The technical report and Megatron‑Bridge docs state the compressed 9B checkpoint supports inference up to 128k tokens and report throughput/efficiency gains versus a comparator (Qwen3‑8B) and configuration notes for running long contexts in bfloat16 on NVIDIA GPUs.
- Recommended: Commercial deployment via NVIDIA NIM / NGC packaging (server/containerized deployments) — The NGC catalog listing and NIM API reference document official NIM/container packaging and runtime APIs for the named checkpoint and list developer scenarios including agent and RAG-style deployment.
- Avoid: Clinical decision-making or regulated medical advice — Evidence gap: primary sources do not document domain-specific safety validations, clinical approvals, or regulatory compliance for Nemotron Nano 9B v2; do not use for clinical decision-making without expert review and regulatory evidence.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `stable` and default-eligible is `true`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/nvidia-nemotron-nano-9b-v2-nim`
- Routes: `/v1/models/nvidia-nemotron-nano-9b-v2-nim/inference-routes`
- Regional deployment: `/v1/models/nvidia-nemotron-nano-9b-v2-nim/regional-deployment`
- Serverless handoff: `/v1/models/nvidia-nemotron-nano-9b-v2-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/nvidia-nemotron-nano-9b-v2-nim/SKILL.md
