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

- Research key: `huggingface-co-qwen-qwen3-reranker-4b-6a9281a2d2`
- Independent audit: `revised`
- Researched: `2026-08-06T09:48:07.498656+00:00`

The Qwen3-Reranker-4B upstream checkpoint is documented in the Hugging Face model card for Qwen3-Reranker-4B and evaluated in the QwenLM Qwen3-Embedding repository and the Qwen3 embedding/reranker technical report. Primary evidence indicates the checkpoint is a 4B-parameter member of the Qwen3 embedding/reranker family, evaluated for multilingual retrieval and code-retrieval tasks, and reported to support long contexts (~32,000 tokens) in the Qwen3 family reporting. The QwenLM repository evaluation tables list retrieval and reranking benchmark scores (MTEB variants, MTEB-Code, MLDR, FollowIR) for Qwen3-Reranker-4B; however, the primary sources do not fully enumerate dataset split identifiers, downstream scoring-head architecture, exact preprocessing steps, or immutable checkpoint file hashes. Those missing protocol and provenance details are recorded as evidence gaps throughout this dossier.

## Identity

- Upstream name: Qwen3-Reranker-4B
- Checkpoint/version: Evidence gap: Exact upstream checkpoint file-level revision identifier (commit, blob, or artifact hash) not reported in the available primary sources.
- Immutable revision: Evidence gap: Exact release tag or immutable artifact revision for the named checkpoint not reported in the available primary sources.
- Parameter scale: 4 billion
- Architecture/head: Evidence gap: The primary sources do not provide an explicit architecture label for this checkpoint beyond being a Qwen3-series transformer-based reranker; layer count (reported in repository) is 36 transformer layers but a formal architecture class string is not stated.
- License: Apache-2.0
- Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/pdf/2505.09388, https://arxiv.org/pdf/2506.05176, https://arxiv.org/abs/2104.08663

## Selection

### Recommended

- **Text document and web-page reranking for retrieval systems** — The Hugging Face model card and the Qwen3 embedding/reranker technical report describe Qwen3-Reranker-4B as a text reranker intended for retrieval/ranking tasks; the QwenLM repository evaluation tables report retrieval-oriented benchmark scores for Qwen3-Reranker-4B supporting this usage.
  Scope: Qwen3-Reranker-4B upstream
  Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/pdf/2506.05176
- **Code retrieval and reranking (code search workflows)** — The QwenLM repository evaluation tables and the Qwen3 embedding/reranker technical report list MTEB-Code evaluation metrics for Qwen3-Reranker-4B, indicating evaluation on code-oriented reranking benchmarks.
  Scope: Qwen3-Reranker-4B upstream
  Evidence: https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/pdf/2506.05176
- **Multilingual cross-lingual search and enterprise retrieval** — The Hugging Face model card and Qwen3 technical report describe the Qwen3 reranker/embedding family as multilingual with long-context capabilities, supporting multilingual retrieval applications for the family and reported in the embedding/reranker evaluation materials.
  Scope: Qwen3-Reranker-4B upstream
  Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://arxiv.org/pdf/2505.09388

### Conditional


### Avoid

- **Medical or clinical retrieval that handles Protected Health Information (PHI)** — Primary sources (model card and technical reports) do not provide clinical safety, PHI-handling, or deployment-specific governance guidance; domain-specific validation, compliance checks, and governance are required before use.
  Scope: Qwen3-Reranker-4B upstream
  Evidence: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://arxiv.org/pdf/2505.09388

## Input preparation

### Semantic inputs

- Input consists of text query and candidate/document text pairs intended for reranking (query-document pair). Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B

### Accepted formats

- Text inputs (queries and candidate texts) are the accepted input modality for the upstream reranker checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B

### Preprocessing

- Evidence gap: Exact preprocessing pipeline (tokenization vocabulary, special-token mappings, canonical prompt wrappers, pooling/normalization) for the upstream Qwen3-Reranker-4B checkpoint is not fully specified in the available primary sources. Sources: https://github.com/QwenLM/Qwen3-Embedding

### Pre-submit validation

- Evidence gap: Pre-submission validation rules (bounds on token lengths per input pair, forbidden character handling, canonical input sanitation) are not explicitly documented in the cited primary sources for the named upstream checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://github.com/QwenLM/Qwen3-Embedding

### Task-specific formatting

- Evidence gap: Official prompt templates, paired-input order, or exact paired-input formatting for query-document scoring are not provided for this upstream checkpoint in the cited primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B

## Output interpretation

### Outputs

- The upstream model is a text reranker that produces a relevance/ranking score for a query-candidate pair (a scalar score per pair) intended to be used to order candidate lists. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://github.com/QwenLM/Qwen3-Embedding

### Interpretation

- Higher scores correspond to higher predicted relevance in ranking evaluations; primary sources do not provide detailed calibration guidance for converting raw scores to application-specific thresholds. Sources: https://arxiv.org/pdf/2506.05176, https://huggingface.co/Qwen/Qwen3-Reranker-4B

### Post-inference validation

- Evidence gap: Post-inference validation procedures (sanity checks, score-distribution diagnostics, calibrated threshold recommendations) are not explicitly documented in the available primary sources for this upstream checkpoint. Sources: https://github.com/QwenLM/Qwen3-Embedding

## Public benchmarks

### Code ranking/retrieval

- Dataset/split: MTEB-Code / not reported
- Metric/value: MTEB-Code score / 81.20 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables and the Qwen3 embedding/reranker technical report; the primary sources list the numeric score but do not fully specify exact dataset split identifiers, downstream scoring-head architecture, or preprocessing details required for strict protocol parity.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits, downstream scoring head, and preprocessing) are not fully specified in the cited repository table; comparability to other reported numbers may vary.

### Retrieval ranking

- Dataset/split: MTEB-R / not reported
- Metric/value: MTEB-R score / 69.76 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables; primary sources do not fully enumerate split and preprocessing details.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits and preprocessing) are incompletely specified in the primary sources.

### Retrieval ranking

- Dataset/split: CMTEB-R / not reported
- Metric/value: CMTEB-R score / 75.94 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables; primary sources do not fully enumerate split and preprocessing details.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits and preprocessing) are incompletely specified in the primary sources.

### Retrieval ranking

- Dataset/split: MMTEB-R / not reported
- Metric/value: MMTEB-R score / 72.74 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables; primary sources do not fully enumerate split and preprocessing details.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits and preprocessing) are incompletely specified in the primary sources.

### MLDR

- Dataset/split: MLDR / not reported
- Metric/value: MLDR score / 69.97 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables; primary sources do not fully enumerate split and preprocessing details.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits and preprocessing) are incompletely specified in the primary sources.

### FollowIR

- Dataset/split: FollowIR / not reported
- Metric/value: FollowIR score / 14.84 (`higher-is-better`)
- Model scope: Qwen3-Reranker-4B upstream
- Conditions: Reported in the QwenLM Qwen3-Embedding repository evaluation tables; primary sources do not fully enumerate split and preprocessing details.
- Source: https://github.com/QwenLM/Qwen3-Embedding
- Locator: evaluation table (Qwen3-Reranker-4B row) in repository
- Caveat: Protocol-level details (exact splits and preprocessing) are incompletely specified in the primary sources.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Retrieval and code reranking
- Criteria: Direct checkpoint-scoped, identical-protocol comparison is not supported by the available primary sources in this dossier; the alternative-model primary source required for parity is not present in the verified primary-source set.
- Rationale: No identical-protocol primary evidence pairing (exact checkpoint rows, identical splits, and identical downstream head/harness) exists in the verified primary sources to conclude a head-to-head result between Qwen3-Reranker-4B and any specific alternative checkpoint within the dossier's primary-source set.
- Comparison conditions: Evidence gap: Missing primary-source benchmark tables for the alternative checkpoint under identical evaluation protocol (exact splits, preprocessing, and downstream head) prevent a direct comparison.
- Evidence: https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/pdf/2506.05176

## Limitations and safety

### Limitations

- Context-length claim and numeric ambiguity: primary Qwen3 family sources report long-context capability (32K tokens) for the Qwen3 embedding/reranker family and the Qwen3 technical report discusses long-context design, but exact numeric token-budget wording differs across family-level reporting; the precise canonical maximum token length claim for this exact named checkpoint is 32,000 tokens as reported in the QwenLM repository but the primary sources do not provide an explicit singular normative token-budget specification for every artifact. Sources: https://github.com/QwenLM/Qwen3-Embedding, https://arxiv.org/pdf/2505.09388
- Evidence gap: Exact tokenizer configuration (tokenizer class, vocabulary size, and explicit special-token mappings) for the upstream Qwen3-Reranker-4B checkpoint is not fully specified in the available primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://github.com/QwenLM/Qwen3-Embedding
- Evidence gap: Exact checkpoint revision and file-level provenance (commit/revision identifiers or artifact hashes for the named model weights) are not reported in the Hugging Face model card or the cited technical reports; thus binary-level provenance cannot be established from the available primary sources. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B, https://arxiv.org/pdf/2506.05176

### Safety

- Evidence gap: Explicit safety guidance, PHI-handling procedures, or domain-specific prohibited-use policies are not provided in the primary model card or the cited technical reports; deployment for high-stakes or regulated domains requires domain-specific governance and expert review. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B
- Forge policy: Treat retrieval/reranker outputs as unverified candidate scores; do not use without downstream human review or domain validation for high-stakes decisions. Sources: https://huggingface.co/Qwen/Qwen3-Reranker-4B

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Reranker-4B model card

- URL: https://huggingface.co/Qwen/Qwen3-Reranker-4B
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Canonical Hugging Face model card for the Qwen3-Reranker-4B upstream checkpoint; authoritative model metadata and high-level usage description.
- Scope: Qwen3-Reranker-4B upstream
- Supports: upstream-origin
- Supports: model-license
- Supports: semanticInputs
- Supports: acceptedFormats
- Supports: general-purpose-description

### Qwen3 embedding / reranker repository (evaluation tables)

- URL: https://github.com/QwenLM/Qwen3-Embedding
- Publisher: QwenLM (GitHub)
- Type: `repository`
- Primary because: Official QwenLM repository containing evaluation tables used to report the listed MTEB and related benchmark scores for Qwen3-Reranker-4B.
- Scope: Qwen3-Reranker-4B upstream
- Supports: benchmarks
- Supports: evaluation-tables
- Supports: parameter-scale
- Supports: model-layer-count
- Supports: context-length-claim

### Qwen3 technical report

- URL: https://arxiv.org/pdf/2505.09388
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical Qwen3 technical report describing the Qwen3 family design, long-context capability, and multilingual scope.
- Scope: Qwen3 family / Qwen3-Reranker design
- Supports: architecture-description
- Supports: context-length-claim
- Supports: family-scope

### Qwen3 embedding and reranker technical report (evaluation including MTEB Code)

- URL: https://arxiv.org/pdf/2506.05176
- Publisher: arXiv
- Type: `paper`
- Primary because: Technical report specifically covering Qwen3 embedding and reranker evaluations, cited by repository tables for MTEB-Code and related scores.
- Scope: Qwen3-Embedding / Qwen3-Reranker evaluation
- Supports: benchmark-results
- Supports: evaluation-protocol-summary

### BEIR benchmark paper (heterogeneous IR benchmark)

- URL: https://arxiv.org/abs/2104.08663
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical BEIR benchmark paper describing the benchmark and metrics (used as a reference for BEIR-style evaluations); included because BEIR is the canonical description of the metric family referenced in prior drafts.
- Scope: BEIR benchmark
- Supports: benchmark-description
- Supports: metric-definition

## Evidence gaps

- Exact upstream checkpoint file-level revision identifiers (commit, blob, or artifact hash) for Qwen3-Reranker-4B are not reported in the available primary sources.
- Exact tokenizer configuration (tokenizer class, vocabulary size, and explicit special-token mappings) for the upstream Qwen3-Reranker-4B checkpoint is not fully specified in the available primary sources.
- Full experimental protocol details for each reported benchmark (exact dataset splits, downstream scoring-head architecture, preprocessing steps, seed, and evaluation harness) are incompletely specified in the available primary sources.
- BEIR nDCG@10 numeric result for Qwen3-Reranker-4B: Evidence gap — no verifiable BEIR nDCG@10 checkpoint-scoped numeric value for Qwen3-Reranker-4B was found among the verified primary sources in this dossier.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 15 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'dengcao' for this exact model scope: $.sources[3] uses unapproved repository owner 'dengcao' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4] uses unapproved repository owner 'tensorblock' for this exact model scope: $.sources[4] uses unapproved repository owner 'tensorblock' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses unapproved repository owner 'vllm-project' for this exact model scope: $.sources[5] uses unapproved repository owner 'vllm-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary host hub.docker.com: $.sources[6] uses forbidden secondary host hub.docker.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-ranker-modernbert-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-reranker-v2-m3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[6]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
