---
name: use-forge-microsoft-phi-4-mini-reasoning-vllm-cuda13
description: Use exact Forge model microsoft-phi-4-mini-reasoning-vllm-cuda13 for text to text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Microsoft Phi-4 Mini Reasoning

- Model slug: `microsoft-phi-4-mini-reasoning-vllm-cuda13`
- Family: `microsoft-phi-4-mini-reasoning`
- Version: `vllm-0.21.0-cuda13` (`vllm-0-21-0-cuda13`)
- Hierarchy: `models / general / language`
- Stability: `testing`
- Default eligible: `false`
- License: `mit`
- Research status: `source-linked`

## Purpose

Microsoft Phi-4 Mini Reasoning is a public MIT-licensed 3.8B-parameter dense text-generation model for multi-step mathematical reasoning, symbolic problem solving, formal proof-style prompts, and compact reasoning use cases where latency and GPU footprint matter.

## Use this exact model when

- Use this exact `microsoft-phi-4-mini-reasoning-vllm-cuda13` version when the task supplies text and needs text.
- Microsoft Phi-4 Mini Reasoning is a public MIT-licensed 3.8B-parameter dense text-generation model for multi-step mathematical reasoning, symbolic problem solving, formal proof-style prompts, and compact reasoning use cases where latency and GPU footprint matter.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text'] → ['text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default 'Solve this step by step and return the final answer clearly: A factory makes 18 valves per hour on line A and 24 valves per hour on line B. If line B runs for 2 fewer hours than line A and together they make 300 valves, how many hours did line A run?'): Prompt
- `temperature` (number; optional; bounds 0..2; default 0.2): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 0.95): Top P
- `max_tokens` (number; optional; bounds 1..8192; default 1024): Max Tokens

Route: `POST /v1/chat/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "messages": [
    {
      "content": "You are Phi, a compact reasoning assistant. Show concise reasoning and put the final answer at the end.",
      "role": "system"
    },
    {
      "content": "{{prompt}}",
      "role": "user"
    }
  ],
  "model": "{{model_slug}}",
  "stream": false,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `text`

## Required workflow

1. Load this skill and pin model slug `microsoft-phi-4-mini-reasoning-vllm-cuda13` with version key `vllm-0-21-0-cuda13`.
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
- Research key: `huggingface-co-microsoft-phi-4-mini-reasoning-511de4e658`
- Recommended: Compact/math reasoning and lightweight deployment scenarios (embedded tutoring, edge/mobile inference) as suggested by the model card's stated potential use cases. — The Hugging Face model page lists Phi-4-mini-reasoning as optimized for mathematical reasoning and as suitable for constrained-compute or latency-sensitive environments; potential use cases include educational applications, embedded tutoring, and lightweight edge or mobile deployment.
- Avoid: Evidence gap: No primary-source evidence in the repository explicitly documents avoid-use boundaries tied to this exact checkpoint (for example, explicit prohibitions on high-stakes clinical, legal, or safety-critical uses). — Evidence gap: The Hugging Face model page and repository blobs inspected do not contain explicit avoid-use or forbidden-application statements for this checkpoint.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/microsoft-phi-4-mini-reasoning-vllm-cuda13`
- Routes: `/v1/models/microsoft-phi-4-mini-reasoning-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/microsoft-phi-4-mini-reasoning-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/microsoft-phi-4-mini-reasoning-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/language/microsoft-phi-4-mini-reasoning-vllm-cuda13/SKILL.md
