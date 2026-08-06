---
name: use-forge-huggingfacebio-carbon-3b-vllm-cuda13
description: Use exact Forge model huggingfacebio-carbon-3b-vllm-cuda13 for dna_sequence, text to dna_sequence, text. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Carbon 3B

- Model slug: `huggingfacebio-carbon-3b-vllm-cuda13`
- Family: `huggingfacebio-carbon-3b`
- Version: `hf-fe755cb-vllm-0.22.0-cuda13` (`hf-fe755cb-vllm-0-22-0-cuda13`)
- Hierarchy: `models / life-science / genomics`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Carbon-3B is a public Apache-2.0 generative DNA foundation model from Hugging Face Bio.

## Use this exact model when

- Use this exact `huggingfacebio-carbon-3b-vllm-cuda13` version when the task supplies dna_sequence, text and needs dna_sequence, text.
- Carbon-3B is a public Apache-2.0 generative DNA foundation model from Hugging Face Bio.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['dna_sequence', 'text'] → ['dna_sequence', 'text'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `prompt` (textarea; optional; default '<dna>ATGCGCTAGCTACGATCGATCGTAGCTAGCTAGCTAGCTACGATCGATCGTAGCTA'): DNA prompt
- `temperature` (number; optional; bounds 0..1.3; default 0): Temperature
- `top_p` (number; optional; bounds 0.01..1; default 1): Top P
- `max_tokens` (number; optional; bounds 1..512; default 64): Generated tokens

Route: `POST /v1/completions`

```json
{
  "max_tokens": "{{max_tokens}}",
  "model": "{{model_slug}}",
  "prompt": "{{prompt}}",
  "stream": true,
  "temperature": "{{temperature}}",
  "top_p": "{{top_p}}"
}
```

## Exact output

- `dna_sequence`
- `text`

## Required workflow

1. Load this skill and pin model slug `huggingfacebio-carbon-3b-vllm-cuda13` with version key `hf-fe755cb-vllm-0-22-0-cuda13`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/completions` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-huggingfacebio-carbon-3b-8f075f26ab`
- Recommended: Research generative DNA sequence modelling and long‑context autoregressive generation (exploratory design and evaluation) — Primary sources describe Carbon‑3B as a generative DNA foundation model trained on DNA/RNA corpora with non‑overlapping 6‑mer tokenization and autoregressive generation; the demo and repository examples show generate and score_sequence usage for DNA generation and scoring.
- Recommended: Research fine‑tuning for discriminative tasks (variant‑effect prediction, regression heads) using repository fine‑tuning scripts and reported evaluation protocols — The authors provide fine‑tuning and evaluation scripts in the Carbon repository and report fine‑tuned evaluation results in the preprint/tech‑report; the repository indicates workflows to fine‑tune the base checkpoint with task‑specific heads.
- Recommended: Sequence recovery and motif/perturbation discrimination in research evaluation suites (training‑free and fine‑tuned benchmarks described by the authors) — The preprint and repo describe training‑free evaluation suites and fine‑tuned evaluation tasks including sequence recovery and perturbation discrimination where Carbon‑3B is evaluated.
- Avoid: Unreviewed clinical decision‑making or clinical deployment without expert review — Primary sources do not provide an author declaration of clinical suitability or clinical validation procedures; the materials present research benchmarks and code but not clinical validation.
- Avoid: Feeding DNA payloads without the expected tokenizer tagging/formatting (risking BPE fallback and degraded DNA modelling quality) — The repository tokenizer implementation requires DNA regions to be wrapped in <dna>...</dna> tags to be tokenized as non‑overlapping 6‑mers; without tags the tokenizer will treat input as regular BPE text.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 32768.

## Safety

- Use research, synthetic, public, or explicitly approved non-identifiable data.
- Require qualified domain review for consequential biological or healthcare conclusions; model output is not diagnosis or treatment advice.
- Keep source license, model revision, request, response, and evidence provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/huggingfacebio-carbon-3b-vllm-cuda13`
- Routes: `/v1/models/huggingfacebio-carbon-3b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/huggingfacebio-carbon-3b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/huggingfacebio-carbon-3b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/life-science/genomics/huggingfacebio-carbon-3b-vllm-cuda13/SKILL.md
