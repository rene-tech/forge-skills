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

- Research key: `huggingface-co-ibm-granite-granite-embedding-small-english-r2-c0cb6b7a27`
- Independent audit: `revised`
- Researched: `2026-08-06T12:17:09.973482+00:00`

This dossier covers the exact checkpoint ibm-granite/granite-embedding-small-english-r2 (Forge family slug huggingface-co-ibm-granite-granite-embedding-small-english-r2-c0cb6b7a27; version tei-cuda-1.9.3 treated as not reported in primary blobs). Primary authoritative locators for checkpoint-specific configuration include the Hugging Face checkpoint model card and the checkpoint config.json blob; they report a ModernBertModel encoder-only bi-encoder with 12 layers, 12 attention heads, hidden_size=384, intermediate_size=1536, vocabulary_size=50368, and max_position_embeddings=8192. The family README and checkpoint model card/paper report retrieval benchmark aggregates and an encoding throughput number; however, per-dataset/per-split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited checkpoint-specific primary locators. Several low-level runtime and implementation details required for strict reproducibility and matched comparisons are not documented in checkpoint-specific primary blobs and are recorded as evidence gaps (notably: checkpoint-specific tokenizer linkage, truncation direction/algorithm, batching determinism, embedding output dtype, pooling-method reconciliation, activation-function reconciliation across blobs, per-dataset/per-metric breakdowns for reported aggregates, low-level throughput protocol metadata, and explicit mapping from Forge suffix c0cb6b7a27 to an upstream commit/blob).

## Identity

- Upstream name: ibm-granite/granite-embedding-small-english-r2
- Checkpoint/version: granite-embedding-small-english-r2
- Immutable revision: not reported
- Parameter scale: 47 million parameters (47M)
- Architecture/head: ModernBertModel (encoder-only ModernBERT bi-encoder). Checkpoint-specific config.json reports: num_hidden_layers=12, num_attention_heads=12, hidden_size=384, intermediate_size=1536, vocabulary_size=50368, max_position_embeddings=8192, classifier_pooling=mean, hidden_act=gelu, classifier_activation=silu, torch_dtype=bfloat16.
- License: Apache-2.0
- Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/blob/c949f235cb63fcbd58b1b9e139ff63c8be764eeb/config.json, https://github.com/ibm-granite/granite-embedding-models, https://arxiv.org/html/2508.21085v1, https://arxiv.org/pdf/2508.21085

## Selection

### Recommended

- **Semantic search and document retrieval (query↔passage bi-encoder embeddings)** — Hugging Face checkpoint model card and the family README/paper describe the checkpoint as a retrieval-oriented bi-encoder producing fixed-length vectors and report retrieval benchmark aggregates supporting retrieval use.
  Scope: granite-embedding-small-english-r2
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- **Retrieval-Augmented Generation (RAG) retrieval stage using dense embeddings (embedding-only retrieval stage)** — Primary model-card and family README describe the checkpoint as producing fixed-length vectors suitable for retrieval stages in RAG pipelines (encoder-only bi-encoder).
  Scope: granite-embedding-small-english-r2
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- **Long-document retrieval using sliding-window chunking (encoding long documents into chunk embeddings)** — Primary README and the paper report a maximum context length of 8192 tokens and describe benchmarking with a sliding-window 512-token chunking protocol for encoding-speed measurement; follow those chunking protocols when reproducing throughput numbers.
  Scope: granite-embedding-small-english-r2
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://arxiv.org/html/2508.21085v1

### Conditional

- **Accelerated inference using Flash Attention 2 (requires user validation)** — Model card/family README indicate optional Flash Attention 2 support; users must install and validate the specified acceleration package and confirm numeric equivalence in their deployment.
  Scope: family-level (granite-embedding-english-r2 family)
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md

### Avoid

- **Non-English inputs or multilingual retrieval** — Primary artifacts identify this checkpoint as English-targeted; authors label the checkpoint and family artifacts as English models and training provenance notes indicate English-targeted data.
  Scope: granite-embedding-small-english-r2
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://github.com/ibm-granite/granite-embedding-models
- **Code retrieval tasks** — Primary repository and model-card artifacts document English checkpoints targeted at text retrieval and do not claim code-specialized training; authors recommend code-specific models for code retrieval in family-level notes.
  Scope: granite-embedding-small-english-r2
  Evidence: https://github.com/ibm-granite/granite-embedding-models, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- **Clinical decision-making or medical diagnostics** — Primary artifacts do not report evaluation on medical/clinical datasets and authors do not claim clinical validation for this checkpoint.
  Scope: granite-embedding-small-english-r2
  Evidence: https://github.com/ibm-granite/granite-embedding-models, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- **Downstream tasks requiring fine-grained per-token representations (token-level tasks)** — Primary model-card and repository documentation describe the checkpoint as a bi-encoder that produces a single fixed-length vector per input rather than per-token outputs.
  Scope: granite-embedding-small-english-r2
  Evidence: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md

## Input preparation

### Semantic inputs

- Plain English text (queries, passages, documents) as single text inputs to be encoded into a single vector. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://github.com/ibm-granite/granite-embedding-models

### Accepted formats

- Raw UTF-8 text strings provided to the model-card usage examples for encoding. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2

### Preprocessing

- Tokenizer artifacts (tokenizer.json and special_tokens_map.json) are provided at the Granite English R2 family repository and describe the family-level tokenizer configuration and special tokens. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/tokenizer.json, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/special_tokens_map.json
- Maximum context length is reported as 8192 tokens; authors benchmark long-document encoding with a sliding-window of 512-token chunks in the paper and README. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://arxiv.org/html/2508.21085v1

### Pre-submit validation

- Inputs longer than the reported maximum context length (8192 tokens) will be truncated per primary documentation; primary artifacts do not document truncation direction (left/right) or the exact token-dropping algorithm at checkpoint-specific blobs. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- Tokenizer special tokens are defined in the family tokenizer blobs and should be validated against tokenizer.json and special_tokens_map.json prior to encoding. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/tokenizer.json, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/special_tokens_map.json

### Task-specific formatting

- No special prompt or instruction template is required for embedding use; examples show encoding raw text as a single input to the bi-encoder. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- For long documents authors benchmark using a sliding-window with 512-token chunks; implementers should follow that chunking protocol when reproducing throughput numbers. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://arxiv.org/html/2508.21085v1

## Output interpretation

### Outputs

- Produces a single fixed-length embedding vector of dimension 384 per input text; no per-token outputs are reported in checkpoint-specific primary artifacts. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md

### Interpretation

- Embeddings are intended as dense semantic representations for retrieval and are typically compared with cosine similarity; primary artifacts describe retrieval usage but do not provide per-vector numeric calibration. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- Primary artifacts report vector dimensionality (384) but do not provide an explicit statement of the numeric dtype (float32 vs float16) of the produced embedding vectors at the checkpoint-specific primary locators; implementers should validate dtype at runtime. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/blob/c949f235cb63fcbd58b1b9e139ff63c8be764eeb/config.json

### Post-inference validation

- Post-inference sanity checks: verify embedding dimensionality (384) and expected normalization behavior in the chosen runtime; primary artifacts do not provide a numeric calibration or explicit dtype guarantee. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://github.com/ibm-granite/granite-embedding-models

## Public benchmarks

### BEIR (aggregate retrieval)

- Dataset/split: BEIR (aggregate reported by authors) / not specified in primary sources
- Metric/value: BEIR average score (author-reported aggregate) / 50.9 (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Author-reported aggregate present in the arXiv paper benchmarking table/section; per-dataset/split/metric-variant breakdown not provided at the cited locator.
- Source: https://arxiv.org/html/2508.21085v1
- Locator: Paper benchmarking table / experiments section reporting BEIR average for granite-embedding-small-english-r2
- Caveat: Per-dataset/split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited location.

### MTEB-v2 Retrieval (aggregate reported by authors)

- Dataset/split: MTEB-v2 (aggregate reported by authors) / not specified in primary sources
- Metric/value: MTEB-v2 Retrieval average score (author-reported aggregate) / 55.6 (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Author-reported aggregate reported on the checkpoint model card; per-dataset/split/metric-variant breakdown not provided at the cited locator.
- Source: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Locator: Checkpoint model card benchmarking table/metrics
- Caveat: Per-dataset/split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited location.

### CoIR (aggregate reported by authors)

- Dataset/split: CoIR (aggregate reported by authors) / not specified in primary sources
- Metric/value: CoIR (10) score (author-reported aggregate) / 53.9 (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Author-reported aggregate reported on the checkpoint model card; per-dataset/split/metric-variant breakdown not provided at the cited locator.
- Source: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Locator: Checkpoint model card benchmarking table/metrics
- Caveat: Per-dataset/split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited location.

### MLDR (English) (aggregate reported by authors)

- Dataset/split: MLDR (English) (aggregate reported by authors) / not specified in primary sources
- Metric/value: MLDR (English) score (author-reported aggregate) / 40.1 (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Author-reported aggregate appears in both the checkpoint model card and the paper; per-dataset/split/metric-variant breakdown not provided at the cited locators.
- Source: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Locator: Checkpoint model card benchmarking table; paper benchmarking table reports MLDR (English) = 40.1
- Caveat: Per-dataset/split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited locations.

### LongEmbed (long-document retrieval) (aggregate reported by authors)

- Dataset/split: LongEmbed (aggregate reported by authors) / not specified in primary sources
- Metric/value: LongEmbed aggregate score (author-reported) / 61.9 (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Author-reported aggregate reported on the checkpoint model card; per-dataset/split/metric-variant breakdown not provided at the cited locator.
- Source: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Locator: Checkpoint model card benchmarking table/metrics
- Caveat: Per-dataset/split/metric-variant breakdowns required for protocol-matched comparisons are not present at the cited location.

### Encoding throughput (documents per second)

- Dataset/split: not applicable / not applicable
- Metric/value: documents per second (throughput) / 199 documents per second (author-reported) (`higher-is-better`)
- Model scope: granite-embedding-small-english-r2
- Conditions: Throughput reported by authors using a sliding-window chunking protocol (512-token chunks) under their benchmarking setup; low-level protocol details (batch size, precision/mixed-precision, other runtime parameters) are not provided at the cited locators.
- Source: https://arxiv.org/html/2508.21085v1
- Locator: Paper benchmarking/experiments section reporting encoding speed for granite-embedding-small-english-r2
- Caveat: The paper and checkpoint model card do not provide full low-level protocol details (batch size, precision/mixed-precision, exact hardware configuration) required for strict hardware/protocol comparability.

## Comparisons

### Qwen3 (embedding paper: arXiv 2506.05176) — `insufficient-evidence`

- Task: General embedding evaluation and MTEB-style comparisons
- Criteria: Per-dataset and protocol-matched metric breakdowns (tokenization, chunking, metric variant, splits) required to compare MTEB-style aggregates are not present for granite at the checkpoint-specific primary locators; the Qwen3 arXiv preprint is present as a primary locator but protocol-matched per-dataset breakdowns needed for direct comparison are absent on one or both sides.
- Rationale: Granite primary artifacts report MTEB-style aggregates but do not provide per-dataset/per-metric breakdowns at the checkpoint-specific primary locators. The canonical Qwen3 paper is available as a primary locator but a protocol-matched per-dataset breakdown for both sides is not present at the cited primary locators, preventing a verified numeric comparison.
- Comparison conditions: Protocol-matched per-dataset/split/metric-variant tables required; absent at granite checkpoint-specific locators.
- Evidence: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://arxiv.org/pdf/2506.05176

## Limitations and safety

### Limitations

- Model trained for English only; primary artifacts state English models were trained on English texts and label the checkpoint as English. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://github.com/ibm-granite/granite-embedding-models
- Not intended for code retrieval or token-level tasks; primary artifacts identify the checkpoint as a bi-encoder producing fixed-length vectors rather than per-token outputs. Sources: https://github.com/ibm-granite/granite-embedding-models, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Evidence gap: activation function ambiguity — primary locators contain conflicting or non-reconciled indicators (config.json reports hidden activation as gelu and classifier activation as silu while family README lists GeGLU); primary sources do not provide a single reconciled locator for the activation function used in the released checkpoint. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/blob/c949f235cb63fcbd58b1b9e139ff63c8be764eeb/config.json
- Evidence gap: pooling strategy ambiguity — config.json lists classifier_pooling as mean while other family-level artifacts contain indicators of CLS-style pooling; no single checkpoint-specific primary locator definitively states which pooling method the official inference pipeline uses. Sources: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/blob/c949f235cb63fcbd58b1b9e139ff63c8be764eeb/config.json, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- Evidence gap: tokenizer implementation and linkage — tokenizer.json and special_tokens_map.json are present at the family-level repository blob but an explicit checkpoint-specific tokenizer implementation file path or an explicit tokenizer.json blob tied to the exact checkpoint revision is not present in checkpoint-specific primary locators. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/tokenizer.json, https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/special_tokens_map.json
- Evidence gap: per-dataset and per-metric breakdowns for reported aggregate benchmarks (BEIR, MTEB-v2, CoIR, MLDR, LongEmbed) — the family README/model card/paper present aggregate scores in tables but do not include per-dataset/per-split/per-metric-variant tables necessary for protocol-matched comparisons. Sources: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2, https://arxiv.org/html/2508.21085v1
- Evidence gap: exact low-level protocol metadata for throughput (batch size, precision settings) — the paper and README report an encoding throughput number using a sliding-window chunking protocol but do not provide explicit batch size, precision/mixed-precision, or other low-level runtime details required for strict comparability. Sources: https://arxiv.org/html/2508.21085v1, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Evidence gap: Forge suffix mapping for c0cb6b7a27 — no primary-source evidence in the cited blobs provides an explicit mapping from the Forge revision suffix c0cb6b7a27 to a specific upstream commit hash, model blob, or tag in the official repository or Hugging Face blob history.

### Safety

- Training data curation notes indicate filtering of hate/abusive/profane text per repository/readme; no explicit automated PHI-handling guidance is provided in the cited primary artifacts. Sources: https://github.com/ibm-granite/granite-embedding-models, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Authors do not claim clinical validation for this checkpoint; the model is not documented as suitable for clinical decision-making in the cited primary artifacts. Sources: https://github.com/ibm-granite/granite-embedding-models, https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Evidence gap: no explicit biosecurity, specialized PHI handling, or privacy controls are documented in the cited primary sources; implementers should apply their own data governance when encoding sensitive data.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### IBM Granite Embedding model card (Hugging Face)

- URL: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2
- Publisher: IBM Granite (hosted on Hugging Face)
- Type: `model-card`
- Primary because: Official checkpoint model card provided by the model authors with model specifications, usage examples, and reported checkpoint-specific benchmarks.
- Scope: granite-embedding-small-english-r2 (Hugging Face model card)
- Supports: Model identifier ibm-granite/granite-embedding-small-english-r2
- Supports: Produces 384-dimensional embeddings (checkpoint-level claim)
- Supports: Parameter scale reported as ~47M for this checkpoint
- Supports: Maximum context length advertised as 8192 tokens (checkpoint-level claim)
- Supports: Reported retrieval benchmark aggregates and encoding speed in checkpoint model card

### Granite family README (Hugging Face blob)

- URL: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/main/README.md
- Publisher: IBM Granite (Hugging Face)
- Type: `model-card`
- Primary because: Official family README maintained by the model authors containing family-level descriptions, tokenizer artifacts pointer, and performance table listing author-reported aggregates for family checkpoints.
- Scope: granite-embedding-english-r2 family README (family-level evidence)
- Supports: Family-level tokenizer and vocabulary size (50368)
- Supports: Family-level notes on Flash Attention 2 optional support
- Supports: Family-level performance table listing author-reported aggregates for family checkpoints (small and full variants)

### Checkpoint config.json (Hugging Face blob)

- URL: https://huggingface.co/ibm-granite/granite-embedding-small-english-r2/blob/c949f235cb63fcbd58b1b9e139ff63c8be764eeb/config.json
- Publisher: IBM Granite (Hugging Face blob)
- Type: `model-card`
- Primary because: Canonical checkpoint configuration blob for this exact checkpoint containing explicit architecture and configuration fields.
- Scope: granite-embedding-small-english-r2 (checkpoint-specific config blob)
- Supports: architecture field: ModernBertModel (model_type "modernbert")
- Supports: num_hidden_layers=12, num_attention_heads=12, hidden_size=384, intermediate_size=1536 (checkpoint-specific)
- Supports: max_position_embeddings=8192 (checkpoint-specific)
- Supports: vocabulary_size=50368 (checkpoint-specific)
- Supports: classifier_pooling="mean" (checkpoint-specific)
- Supports: hidden_act=gelu and classifier_activation=silu (checkpoint-specific)
- Supports: torch_dtype listed as bfloat16 (checkpoint-specific)

### Tokenizer JSON (family blob)

- URL: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/tokenizer.json
- Publisher: IBM Granite (Hugging Face blob)
- Type: `repository`
- Primary because: Official tokenizer artifact blob for the Granite English R2 family providing tokenizer configuration and vocabulary mapping at the family level.
- Scope: granite-embedding-english-r2 family tokenizer (family-level)
- Supports: Presence of tokenizer.json artifact for the family (provides tokenizer mapping and algorithmic artifact when present)

### Tokenizer special_tokens_map.json (family blob)

- URL: https://huggingface.co/ibm-granite/granite-embedding-english-r2/blob/92d727113b781457af4e0d8361e54652ec18b590/special_tokens_map.json
- Publisher: IBM Granite (Hugging Face blob)
- Type: `repository`
- Primary because: Official tokenizer special_tokens_map blob in the Hugging Face family repository; supports tokenizer special-token definitions for the family.
- Scope: granite-embedding-english-r2 family tokenizer special tokens (family-level)
- Supports: Definition of special tokens for the family-level tokenizer

### IBM Granite embedding models repository (GitHub)

- URL: https://github.com/ibm-granite/granite-embedding-models
- Publisher: ibm-granite (GitHub)
- Type: `repository`
- Primary because: Official repository maintained by the authors containing training/data notes, README variants, and license text.
- Scope: granite-embedding-small-english-r2 (family-level repository)
- Supports: Training data curation notes including filtering of hate/abuse/profanity (family-level)
- Supports: English-only training statements for English checkpoints (family-level)
- Supports: Apache-2.0 license statement for repository artifacts (family-level documentation)

### Granite embedding technical paper (arXiv HTML)

- URL: https://arxiv.org/html/2508.21085v1
- Publisher: arXiv
- Type: `paper`
- Primary because: Author technical paper describing architecture, evaluation, and encoding-speed benchmark for the R2 release (contains checkpoint-level benchmark entries in the paper tables/sections).
- Scope: granite-embedding-small-english-r2 (paper-level evidence for R2 release)
- Supports: Discussion of long-document benchmarking with sliding-window 512-token chunks
- Supports: Encoding speed 199 documents/sec reported for granite-embedding-small-english-r2 in benchmarking section
- Supports: Paper benchmarking table entries listing BEIR average for the small checkpoint

### Granite embedding technical paper (arXiv PDF)

- URL: https://arxiv.org/pdf/2508.21085
- Publisher: arXiv
- Type: `paper`
- Primary because: Official PDF of the technical paper with benchmark and architecture details.
- Scope: granite-embedding-small-english-r2 (paper-level evidence)
- Supports: Benchmarking details and architecture description for the R2 models

### Qwen3 Embedding paper (arXiv PDF)

- URL: https://arxiv.org/pdf/2506.05176
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing the Qwen3 Embedding series; included as primary evidence only for comparison purposes where cited.
- Scope: Qwen3 embedding family (comparison primary locator)
- Supports: Qwen3 Embedding design and training claims used for cross-checking comparisons

## Evidence gaps

- Tokenizer implementation details: The primary artifacts confirm family-level tokenizer artifacts and a reported vocabulary size (50368) at the family tokenizer blobs, but an explicit checkpoint-specific tokenizer implementation file path or an explicit tokenizer.json blob tied to the exact checkpoint revision and algorithmic tokenization description for granite-embedding-small-english-r2 is not present in checkpoint-specific primary locators (see family tokenizer.json blob URL).
- Exact truncation behavior (direction and token-dropping algorithm): Primary sources report a maximum context length of 8192 tokens but do not document whether truncation is left/right/center or the exact token-dropping algorithm at the checkpoint-specific primary locators.
- Batching determinism: No primary-source evidence in the cited artifacts specifies whether batching changes numeric outputs or provides guidance on batching determinism for identical numeric outputs at the checkpoint-specific blobs.
- Embedding output dtype: Primary artifacts report vector dimensionality (384) but do not provide an explicit statement of the numeric dtype (float32 vs float16) of the produced embedding vectors at checkpoint-specific primary locators.
- Pooling ambiguity resolution: Checkpoint config.json lists classifier_pooling=mean while family-level artifacts contain other pooling indicators; no single checkpoint-specific primary locator definitively reconciles which pooling method the official inference pipeline uses for this checkpoint.
- Activation function ambiguity: Some family-level locators list GeGLU while the checkpoint config.json lists hidden activation=gelu and classifier_activation=silu; these conflicting primary locators are not reconciled by a single authoritative checkpoint-specific primary source.
- Per-dataset and per-metric breakdowns for reported aggregate benchmarks (BEIR, MTEB-v2, CoIR, MLDR, LongEmbed): The family README, checkpoint model card, and paper present aggregate scores but do not include per-dataset/per-split/per-metric-variant tables necessary for protocol-matched comparisons at the checkpoint-specific locators.
- Exact low-level protocol metadata for throughput (batch size, precision settings): The paper and README report an encoding throughput number (199 docs/sec) under a sliding-window 512-token chunking protocol, but do not provide explicit batch size, precision/mixed-precision, or other low-level runtime details required for strict comparability at the cited locators.
- Revision mapping for Forge suffix c0cb6b7a27: No primary-source evidence in the cited artifacts provides an explicit mapping from the Forge revision suffix c0cb6b7a27 to a specific upstream commit hash, model blob, or tag in the official repository or Hugging Face blob history.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 14 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5] uses unapproved repository owner 'teradata' for this exact model scope: $.sources[5] uses unapproved repository owner 'teradata' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8] uses forbidden secondary host ai.azure.com: $.sources[8] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'baai' for this exact model scope: $.sources[11] uses unapproved repository owner 'baai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'snowflake' for this exact model scope: $.sources[14] uses unapproved repository owner 'snowflake' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'mixedbread-ai' for this exact model scope: $.sources[18] uses unapproved repository owner 'mixedbread-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-large-en-v1.5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/154/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.comparisons_meta: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
