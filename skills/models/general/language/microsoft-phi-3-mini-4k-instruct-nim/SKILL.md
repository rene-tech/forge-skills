---
name: use-forge-microsoft-phi-3-mini-4k-instruct-nim
description: Use exact Forge model microsoft-phi-3-mini-4k-instruct-nim for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Microsoft Phi-3 Mini 4K Instruct

- Model slug: `microsoft-phi-3-mini-4k-instruct-nim`
- Family: `microsoft-phi-3-mini-4k-instruct`
- Version: `v1` (`v1`)
- Hierarchy: `models / general / language`
- Stability: `stable`
- Default eligible: `true`
- License: `mit`
- Research status: `source-linked`

## Purpose

Microsoft Phi-3 Mini 4K Instruct packaged as an NVIDIA NIM and mirrored into Forge regional registries.

## Use this exact model when

- Use this exact `microsoft-phi-3-mini-4k-instruct-nim` version when the task supplies text and needs text.
- Microsoft Phi-3 Mini 4K Instruct packaged as an NVIDIA NIM and mirrored into Forge regional registries.
- Prefer this version for normal Forge routing because it is marked default-eligible.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `stable` stability or default-eligible=true status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `messages` (chat_history; optional; default 'Explain in two concise paragraphs how regional model image mirrors improve cold-start reliability.'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.7): Temperature
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

1. Load this skill and pin model slug `microsoft-phi-3-mini-4k-instruct-nim` with version key `v1`.
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
- Research key: `build-nvidia-com-microsoft-phi-3-mini-4k-instruct-2cea73bbb6`
- Recommended: Instruction-following and general-purpose chat (English) — Upstream model card and README describe Phi-3-mini-4k-instruct as an instruction‑tuned member of the Phi-3 family and the README/NGC entries describe instruction following and chat-style capabilities; the technical report documents SFT + DPO post-training alignment at the family level.
- Recommended: Latency-constrained deployments requiring a compact instruction-tuned model — The upstream README and repository state the Phi-3 Mini (3.8B) is the smallest/tiniest Phi-3 member intended for quality/low-latency tradeoffs relative to larger family members; NGC packaging lists a compressed artifact targeted at RTX/Ada hardware for low-latency inference.
- Avoid: Clinical or regulated decision-making without explicit domain validation and expert review — The technical report and Microsoft Research landing page describe post-training alignment, robustness testing, and family-level safety work (SFT + DPO and red-teaming) but do not provide checkpoint-specific clinical/regulatory validation or PHI/clinical handling procedures for Phi-3-mini-4k-instruct in the provided primary sources.
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

- Model: `/v1/models/microsoft-phi-3-mini-4k-instruct-nim`
- Routes: `/v1/models/microsoft-phi-3-mini-4k-instruct-nim/inference-routes`
- Regional deployment: `/v1/models/microsoft-phi-3-mini-4k-instruct-nim/regional-deployment`
- Serverless handoff: `/v1/models/microsoft-phi-3-mini-4k-instruct-nim/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/microsoft-phi-3-mini-4k-instruct-nim/SKILL.md
