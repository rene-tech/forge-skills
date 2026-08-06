---
name: use-forge-qwen-qwen3-vl-reranker-2b-vllm-cuda13
description: Use exact Forge model qwen-qwen3-vl-reranker-2b-vllm-cuda13 for text, image to ranking. Load when selecting, calling, comparing, interpreting, or deploying this specific version.
---

# Use Qwen3-VL Reranker 2B

- Model slug: `qwen-qwen3-vl-reranker-2b-vllm-cuda13`
- Family: `qwen-qwen3-vl-reranker-2b`
- Version: `vllm-0.21.0-cuda13-vision-rerank-onboarding` (`vllm-0-21-0-cuda13-vision-rerank-onboarding`)
- Hierarchy: `models / general / retrieval-and-reranking`
- Stability: `testing`
- Default eligible: `false`
- License: `apache-2.0`
- Research status: `source-linked`

## Purpose

Qwen3-VL Reranker 2B is an Apache-2.0 multimodal reranker for text, image, screenshot, and visual-document retrieval workflows.

## Use this exact model when

- Use this exact `qwen-qwen3-vl-reranker-2b-vllm-cuda13` version when the task supplies text, image and needs ranking.
- Qwen3-VL Reranker 2B is an Apache-2.0 multimodal reranker for text, image, screenshot, and visual-document retrieval workflows.
- Select this version only after explicitly accepting its experimental/non-default status.

## Do not use it when

- Do not use it when the task's input or required output differs from the declared ['text', 'image'] → ['ranking'] contract.
- Do not hide its `testing` stability or default-eligible=false status from the user.
- Do not make quality, safety, efficacy, or suitability claims beyond the reviewed evidence attached to this exact skill.

## Exact request contract

- `query` (textarea; optional; default 'A woman playing with her dog on a beach at sunset.'): Query
- `documents` (json_editor; optional; default ['A woman shares a joyful moment with her golden retriever on a sun-drenched beach at sunset.', {'content': [{'type': 'image_url', 'image_url': {'url': 'https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg'}}]}, {'content': [{'text': 'A golden retriever offers its paw while sitting with a woman on the beach.', 'type': 'text'}, {'type': 'image_url', 'image_url': {'url': 'https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg'}}]}]): Candidate documents
- `top_n` (number; optional; default 3): Top N

Route: `POST /v1/inference/qwen-qwen3-vl-reranker-2b-vllm-cuda13`

```json
{
  "documents": "{{documents}}",
  "model": "{{model_slug}}",
  "query": "{{query}}",
  "top_n": "{{top_n}}"
}
```

## Exact output

- `ranking`

## Required workflow

1. Load this skill and pin model slug `qwen-qwen3-vl-reranker-2b-vllm-cuda13` with version key `vllm-0-21-0-cuda13-vision-rerank-onboarding`.
2. Fetch the live model detail and inference-routes endpoints before every run.
3. Validate the exact required fields and parameter bounds listed below; do not silently coerce, truncate, or omit inputs.
4. Call `POST /v1/inference/qwen-qwen3-vl-reranker-2b-vllm-cuda13` using the declared request template.
5. Validate the returned fields/modalities and preserve the exact model slug, version, region, accelerator, cold-start, and latency metadata.
6. Use the public-evidence section only within its stated scope; use Forge probe history only for runtime placement and performance.

## Evidence

Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
Read `references/evidence.md` and the linked primary source before making a model-quality comparison.

## Audited model guidance

- Audited research: `revised`
- Research key: `huggingface-co-qwen-qwen3-vl-reranker-2b-03d6241fb5`
- Recommended: Multimodal reranking for query-document pairs where fine-grained relevance scoring is required — Upstream model card and repository describe the Qwen3-VL-Reranker model series as a reranker that refines retrieval results and operates on query-document pairs, intended for multimodal information retrieval and cross-modal understanding.
- Recommended: Image–text retrieval reranking (multimodal candidate reranking) — The upstream model card and repository state the model suite accepts text and images and that the reranker refines retrieval results in a multimodal retrieval pipeline.
- Recommended: Video–text matching reranking within a multimodal retrieval workflow — The upstream model card indicates the suite accepts video as an input modality and positions the reranker as the component to refine retrieval results.
- Avoid: Using the reranker checkpoint as an embedding model that outputs vector embeddings for ANN retrieval — Upstream materials separate the embedding model and the reranker: the embedding model is described as generating high-dimensional vectors while the reranker is described as refining retrieval results with pairwise relevance scoring; this indicates the reranker is not the embedding-producing checkpoint.
- Avoid: Relying on reranker outputs as calibrated probabilities or fixed thresholds for automated high-stakes decisions — Upstream files do not provide score-range semantics, calibration guidance, or thresholding instructions for this checkpoint; no calibration or probability semantics are documented in the checked primary files.
- Avoid: Assuming undocumented preprocessing, truncation, batching, or multimodal packing contracts in production-critical pipelines — Upstream README and config.json do not specify exact tokenization, image/video preprocessing, cropping, resizing, padding, multimodal packing, or batching behavior for this checkpoint; these are gaps that require local validation.
- Before selecting against another model, transforming user data, interpreting outputs, or citing quality, read `references/research.md`.

## Limitations

- Catalog stability is `testing` and default-eligible is `false`.
- Forge has linked the exact model's primary source, but has not attached an independently reviewed public benchmark claim to this exact skill. Do not invent one, transfer a neighboring checkpoint's result, or treat Forge latency/GPU probes as model-quality evidence.
- Declared context/sequence window: 4096.

## Safety

- Do not send credentials, secrets, personal data, or confidential content without an approved processing basis.
- Require human review before consequential, safety-critical, legal, financial, or high-impact decisions.
- Keep source license, model revision, request, response, and evaluation provenance with derived artifacts.

## Live Forge and Serverless

- Model: `/v1/models/qwen-qwen3-vl-reranker-2b-vllm-cuda13`
- Routes: `/v1/models/qwen-qwen3-vl-reranker-2b-vllm-cuda13/inference-routes`
- Regional deployment: `/v1/models/qwen-qwen3-vl-reranker-2b-vllm-cuda13/regional-deployment`
- Serverless handoff: `/v1/models/qwen-qwen3-vl-reranker-2b-vllm-cuda13/deploy`
- Load `$use-nebius` and `$nebius-forge-model-deployment` for a user-owned endpoint.

## Progressive references

- `../research.md` — audited task-group selection and comparability rules.
- `../research.json` — machine-readable task-group dossier.
- `references/evidence.md` — benchmark/source scope.
- `references/research.md` — full audited model-use dossier.
- `references/research.json` — machine-readable audited dossier.
- `references/forge-model.json` — complete public Forge model snapshot.
- `references/forge-skill.json` — complete exact-skill API snapshot.
- Repository file: https://github.com/rene-tech/forge-skills/blob/main/skills/models/general/retrieval-and-reranking/qwen-qwen3-vl-reranker-2b-vllm-cuda13/SKILL.md
