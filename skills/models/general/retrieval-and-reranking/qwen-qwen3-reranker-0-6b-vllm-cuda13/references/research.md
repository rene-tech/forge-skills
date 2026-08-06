# Audited model research

## Contents

- [Identity](#identity)
- [Selection](#selection)
- [Input preparation](#input-preparation)
- [Output interpretation](#output-interpretation)
- [Public benchmarks](#public-benchmarks)
- [Comparisons](#comparisons)
- [Limitations and safety](#limitations-and-safety)
- [Related upstream agent skills](#related-upstream-agent-skills)
- [Primary sources](#primary-sources)
- [Evidence gaps](#evidence-gaps)

- Research key: `huggingface-co-qwen-qwen3-reranker-0-6b-b13594dd7d`
- Independent audit: `revised`
- Researched: `2026-08-06T09:57:30.798372+00:00`

Qwen3-Reranker-0.6B is a checkpoint in the Qwen3 embedding and reranking series documented on the HuggingFace model page. The Qwen3 family is described in the canonical Qwen3 technical report (arXiv:2505.09388) and the model-series documentation as providing embedding and reranking models at sizes including 0.6B, 4B, and 8B, with multilingual capabilities and long-text understanding. The supplied primary sources do not publish immutable checkpoint revision identifiers, apples-to-apples numeric benchmark rows for the exact 0.6B reranker checkpoint, explicit tokenizer blob details in the provided findings, or an explicit API output shape and recommended score transform for the checkpoint; these gaps are recorded in evidenceGaps. Primary evidence used: the HuggingFace model page for Qwen3-Reranker-0.6B and the Qwen3 technical report (arXiv:2505.09388).

## Identity

- Upstream name: Qwen3
- Checkpoint/version: Qwen3-Reranker-0.6B
- Immutable revision: not reported
- Parameter scale: 0.6B
- Architecture/head: Reranker (Qwen3 embedding/reranking series checkpoint)
- License: not reported
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

## Selection

### Recommended

- **Text retrieval / reranking in retrieval pipelines (reranker stage)** — The HuggingFace model page documents this checkpoint as part of the Qwen3 embedding and reranking series, which is specifically designed for text embedding and ranking tasks.
  Scope: Qwen3-Reranker-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
- **Multilingual reranking across many languages (pipeline reranker)** — The Qwen3 technical report documents Qwen3's multilingual capabilities (stated support for many languages) and the HuggingFace model page lists the reranking model as part of that multilingual series.
  Scope: Qwen3-Reranker-0.6B
  Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

### Conditional

- **Evaluation on non-Latin scripts or narrow domain-specific reranking** — Downstream validation and task-specific evaluation required to verify performance on particular non-Latin scripts or narrow domains; the primary sources describe multilingual capability but do not publish checkpoint-level domain- or language-specific evaluation rows for the 0.6B reranker.
  Scope: Qwen3-Reranker-0.6B
  Evidence: https://arxiv.org/pdf/2505.09388, https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

### Avoid

- **Standalone large-scale document retrieval without a separate first-stage retriever** — The HuggingFace model page and family description present embedding and reranking modules that are intended to be combined; the series is described as providing both embedding and reranking models rather than replacing a first-stage retriever alone.
  Scope: Qwen3-Reranker-0.6B
  Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

## Input preparation

### Semantic inputs

- Text query and text document inputs (query–document pairs) intended for embedding and reranking workflows. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

### Accepted formats

- Plain text queries and documents for text embedding and reranking tasks. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

### Preprocessing

- Evidence gap: The supplied primary sources in the findings do not include tokenizer blob paths, tokenizer class names, explicit model_max_length values, or ordered preprocessing/tokenization steps for this exact checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Pre-submit validation

- Evidence gap: The supplied primary sources do not report explicit input bounds, tokenizer maximum token length, pad/eos token IDs, or explicit input-validation checks for the 0.6B reranker checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Task-specific formatting

- Developers can combine embedding and reranking modules from the Qwen3 series; the model page describes both embeddings and rerankers and their intended use together. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
- Evidence gap: No canonical upstream prompt templates, pair-order conventions, or official task-formatting templates for query–document pair inputs for this checkpoint were present in the supplied primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

## Output interpretation

### Outputs

- Evidence gap: The supplied primary sources do not specify the exact output tensor/score shape emitted by the upstream 0.6B reranker checkpoint in the provided findings. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Interpretation

- Evidence gap: No explicit guidance in the supplied primary sources about whether to apply a sigmoid, softmax, or other calibration to the reranker outputs for downstream probability interpretation. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Post-inference validation

- Evidence gap: No post-inference validation or calibration workflows are specified for this checkpoint in the supplied primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### Alibaba-NLP/gte-reranker-modernbert-base — `insufficient-evidence`

- Task: reranking/IR
- Criteria: No apples-to-apples protocol-level benchmark rows in the supplied primary findings for the alternative; cannot verify dataset/split/metric/head comparability from the provided sources.
- Rationale: The research findings do not include primary-source benchmark rows for Alibaba-NLP/gte-reranker-modernbert-base to enable a direct protocol-matched comparison with Qwen3-Reranker-0.6B.
- Comparison conditions: Checked canonical Qwen3 sources for 0.6B but no matching canonical alternative benchmark rows found in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### BAAI/bge-reranker-v2-m3 — `insufficient-evidence`

- Task: reranking/IR
- Criteria: No protocol-matched primary benchmark rows for the alternative are present in the supplied findings to allow apples-to-apples comparison.
- Rationale: The supplied findings contain no primary-source benchmark table for BAAI/bge-reranker-v2-m3.
- Comparison conditions: Checked canonical Qwen3 sources for 0.6B but no matching canonical alternative benchmark rows found in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### NVIDIA llama-3-2-nv-rerankqa-1b-v2 — `insufficient-evidence`

- Task: reranking/IR
- Criteria: No primary-source NVIDIA or vendor canonical benchmark rows for the alternative are present in the supplied findings for protocol-matched comparison.
- Rationale: The supplied findings do not include primary vendor pages or benchmark rows for this NVIDIA alternative.
- Comparison conditions: Checked canonical Qwen3 sources for 0.6B but no matching canonical alternative benchmark rows found in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### NVIDIA llama-nemotron-rerank-1b-v2 — `insufficient-evidence`

- Task: reranking/IR
- Criteria: No primary-source benchmark rows for the alternative in the supplied findings.
- Rationale: The supplied findings do not include canonical vendor model cards or benchmark tables for this NVIDIA alternative.
- Comparison conditions: Checked canonical Qwen3 sources for 0.6B but no matching canonical alternative benchmark rows found in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### NVIDIA llama-nemotron-rerank-vl-1b-v2 — `insufficient-evidence`

- Task: multi-modal reranking/IR
- Criteria: No canonical primary-source benchmark rows for the alternative in the supplied findings; modality differs and protocol-matched comparison cannot be verified from provided sources.
- Rationale: The supplied findings do not include primary-source benchmark rows for this NVIDIA multimodal alternative.
- Comparison conditions: Checked canonical Qwen3 sources for 0.6B but no matching canonical alternative benchmark rows found in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Qwen3-Reranker-4B — `insufficient-evidence`

- Task: cross-encoder reranking (reference larger-scale variant)
- Criteria: Scale differs (4B vs 0.6B); no checkpoint-level apples-to-apples numeric protocol rows for both checkpoints are present in the supplied findings to enable a direct numeric comparison.
- Rationale: The HuggingFace model page and Qwen3 family description list multiple sizes including 4B, but the supplied findings do not include protocol-matched numeric benchmark rows for both 0.6B and 4B checkpoints.
- Comparison conditions: Checked canonical Qwen3 sources for family sizes and high-level claims but no checkpoint-level numeric table for 0.6B that matches any 4B row in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Qwen3-VL-Reranker-2B — `insufficient-evidence`

- Task: visual-language reranking/IR (reference VL variant)
- Criteria: Modality and scale differ; the supplied findings do not contain protocol-matched benchmark rows for the VL 2B variant and the 0.6B text reranker.
- Rationale: The supplied findings reference the Qwen3 family and its variants but do not provide numeric apples-to-apples protocol rows for direct comparison.
- Comparison conditions: Checked canonical Qwen3 sources for family descriptions but no protocol-matched numeric benchmark rows were present in the supplied findings.
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

## Limitations and safety

### Limitations

- Evidence gap: The supplied primary sources do not publish an immutable checkpoint revision identifier (git commit, exact weights filename/sha256, or equivalent) for Qwen3-Reranker-0.6B in the provided findings. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388
- Evidence gap: The supplied primary sources do not include canonical numeric apples-to-apples benchmark rows (dataset/split/metric/value) for the exact 0.6B reranker checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388
- Evidence gap: The supplied primary sources do not document tokenizer blob-level details or explicit tokenization parameters for this checkpoint within the findings provided. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

### Safety

- Evidence gap: The supplied primary sources do not provide an explicit safety policy, usage restrictions, or domain-specific handling guidance for the Qwen3-Reranker-0.6B checkpoint within the findings provided. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Reranker-0.6B model page

- URL: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B
- Publisher: Qwen
- Type: `model-card`
- Primary because: Official HuggingFace model page for the Qwen3-Reranker-0.6B checkpoint; primary evidence for checkpoint identity, family membership, intended use as embedding/reranking model, and available sizes in the series.
- Scope: Qwen3-Reranker-0.6B
- Supports: identity
- Supports: recommendedUseCases
- Supports: avoidUseCases
- Supports: inputPreparation
- Supports: taskSpecificFormatting
- Supports: limitations

### Qwen3 technical report (arXiv 2505.09388)

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: arXiv
- Type: `technical-report`
- Primary because: Canonical technical report for the Qwen3 family describing architecture, multilingual scale, and family-level evaluations; primary evidence for family capabilities and scale listings referenced in the findings.
- Scope: Qwen3 family (dense models)
- Supports: identity
- Supports: recommendedUseCases
- Supports: researchSummary
- Supports: limitations

## Evidence gaps

- Evidence gap: No canonical numeric apples-to-apples benchmark rows (dataset/split/metric/value) for Qwen3-Reranker-0.6B were found in the supplied primary sources (checked: HuggingFace model page and Qwen3 arXiv technical report: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).
- Evidence gap: The upstream checkpoint immutable revision (git commit, exact weights filename/sha256, or other immutable locator) for Qwen3-Reranker-0.6B is not reported in the supplied primary sources (checked: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).
- Evidence gap: Tokenizer implementation details, tokenizer_config.json blob path, tokenizer class name, model_max_length, pad/eos token IDs and tokenization flags for this exact checkpoint were not present in the supplied findings (checked: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).
- Evidence gap: No explicit upstream callable output-contract shape or recommended score transform (sigmoid/softmax) for the 0.6B reranker was found in the supplied primary sources (checked: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).
- Evidence gap: No canonical, upstream-published runtime/serving examples or vLLM GitHub examples for hf_overrides, classifier_from_token, or lm_head extraction for Qwen3-Reranker-0.6B are present in the supplied findings; such runtime guidance is therefore an evidence gap in the provided primary sources (checked: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).
- Evidence gap: No explicit safety, data-privacy, clinical, or dual-use guidance for this exact checkpoint was found in the supplied primary sources (checked: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B, https://arxiv.org/pdf/2505.09388).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 20 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses unapproved repository owner 'onnx-community' for this exact model scope: $.sources[4] uses unapproved repository owner 'onnx-community' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'coreai-community' for this exact model scope: $.sources[6] uses unapproved repository owner 'coreai-community' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses unapproved repository owner 'onnx-community' for this exact model scope: $.sources[8] uses unapproved repository owner 'onnx-community' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9] uses forbidden secondary host ollama.com: $.sources[9] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary host docs.vllm.ai: $.sources[10] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://milvus.io/blog/hands-on-rag-with-qwen3-embedding-and-reranking-models-using-milvus.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-reranker-v2-m3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must not be empty: $.benchmarks[0].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must not be empty: $.benchmarks[1].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must not be empty: $.benchmarks[2].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must not be empty: $.benchmarks[3].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must not be empty: $.benchmarks[4].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must not be empty: $.benchmarks[5].sourceLocator must not be empty Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
