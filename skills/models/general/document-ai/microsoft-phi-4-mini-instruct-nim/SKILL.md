---
name: use-forge-microsoft-phi-4-mini-instruct-nim
description: Use exact Forge model microsoft-phi-4-mini-instruct-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Microsoft Phi-4 Mini Instruct

- Model slug: `microsoft-phi-4-mini-instruct-nim`
- Family: `microsoft-phi-4-mini-instruct`
- Version: `1.12.0` (`nim-1-12-0`)
- Hierarchy: `models / general / document-ai`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

Microsoft Phi-4 Mini Instruct is a public MIT-licensed 3.8B-parameter small language model for instruction following, multilingual chat, code-oriented prompts, and tool/function-calling formats.

## Use this exact model when

- Use this exact `microsoft-phi-4-mini-instruct-nim` version when the task supplies text and needs text.
- Microsoft Phi-4 Mini Instruct is a public MIT-licensed 3.8B-parameter small language model for instruction following, multilingual chat, code-oriented prompts, and tool/function-calling formats.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Explain in two concise paragraphs how regional model image mirrors improve cold-start reliability.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `top_p` (number; optional; bounds 0..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..4096; default 256): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": "{{messages}}",
  "model": "{{model_slug}}",
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `microsoft-phi-4-mini-instruct-nim` with version key `nim-1-12-0`.
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
- Research key: `build-nvidia-com-microsoft-phi-4-mini-instruct-deploy-81bff52c7d`
- Recommended: Instruction-following and general multilingual chat/dialog — NVIDIA NGC catalog describes the Phi‑4‑Mini‑Instruct container as an instruction-tuned model suitable for dialogue and instruction-following use; the NVIDIA Build deploy page identifies the corresponding NIM deploy artifact.
- Recommended: Reasoning, mathematics, and code-generation research / developer experimentation — NVIDIA NGC catalog and the Phi‑4 technical report (arXiv / Microsoft Research PDF) present Phi‑4 family strengths and intended capability areas emphasizing reasoning, math, and code-generation; these are described at family level in the technical report and are represented in the NGC container description for the mini-instruct packaging.
- Avoid: High-stakes clinical decision making or handling protected health information without expert governance — The Phi‑4 technical report documents safety/RAI concerns and recommends governance and post-training safety alignment; the inspected primary sources do not provide clinical-use endorsement or PHI‑handling operational guidance for the specific NIM-wrapped checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 131072.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/microsoft-phi-4-mini-instruct-nim`
- Routes: `/v1/models/microsoft-phi-4-mini-instruct-nim/inference-routes`
- Regional deployment: `/v1/models/microsoft-phi-4-mini-instruct-nim/regional-deployment`
- Serverless handoff: `/v1/models/microsoft-phi-4-mini-instruct-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/document-ai/microsoft-phi-4-mini-instruct-nim/SKILL.md
