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

- Research key: `huggingface-co-alibaba-nlp-gte-reranker-modernbert-base-0ec86b6e00`
- Independent audit: `revised`
- Researched: `2026-07-23T23:41:27.396677+00:00`

Primary upstream evidence is available in the Alibaba-NLP Hugging Face repository blobs and commit history for Alibaba-NLP/gte-reranker-modernbert-base. The repository config.json identifies the architecture class as ModernBertForSequenceClassification (a sequence-classification / reranker head) and records hidden_size and max_position_embeddings = 8192. The repository README blobs present the model as an English text reranker and report checkpoint-scoped aggregate evaluation numbers (MTEB-en 56.19, BEIR 90.68, LoCo 79.99) in a model-list benchmark table. Tokenizer operational metadata (token IDs, model_max_length) and tokenizer truncation/padding/right-side behavior are recorded in the repository tokenizer_config.json blob; however, the located primary blobs do not document tokenizer algorithmic internals beyond configured fields, do not document numeric semantics/calibration of returned relevance scores, do not publish per-dataset evaluation protocol details or evaluation scripts for the reported aggregates, and do not document training-data provenance or explicit safety/mitigation statements. These absent items are recorded as explicit evidence gaps.

## Identity

- Upstream name: Alibaba-NLP/gte-reranker-modernbert-base
- Checkpoint/version: Hugging Face repository blobs and uploaded weight artifacts for Alibaba-NLP/gte-reranker-modernbert-base
- Immutable revision: commit c40156962ee2a34679b0c8399e0d1bb9d68d54ab (config/README association); commit c2c3466f6bb32f168f3df9d76b2aa27023de1336 (artifact uploads)
- Parameter scale: 149 million parameters
- Architecture/head: ModernBertForSequenceClassification (ModernBERT encoder foundation with sequence-classification / reranker head as recorded in the repo config)
- License: Apache-2.0
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commit/c40156962ee2a34679b0c8399e0d1bb9d68d54ab, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commits/c2c3466f6bb32f168f3df9d76b2aa27023de1336, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

## Selection

### Recommended

- **English retrieval reranking (cross-encoder reranker for query + candidate document pairs)** — Repository config.json specifies ModernBertForSequenceClassification (sequence-classification head) and README model-list entries describe gte-reranker-modernbert-base as a text reranker; these checkpoint-scoped artifacts support using the checkpoint as a cross-encoder reranker for query/document pair relevance scoring.
  Scope: Alibaba-NLP/gte-reranker-modernbert-base (config.json and README blobs)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

### Conditional

- **Long-context reranking up to 8192 tokens (query + document pairs where combined token length may approach 8192)** — Config and commit blobs report max_position_embeddings = 8192, but repository blobs do not specify truncation side, per-field token budgets, batching/truncation enforcement, or runtime truncation semantics. Users must validate truncation behavior, batching limits, and confirm that any downstream serving wrapper preserves full 8192-length behavior before production use.
  Scope: Alibaba-NLP/gte-reranker-modernbert-base (config.json and commit c40156962ee2a34679b0c8399e0d1bb9d68d54ab)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commit/c40156962ee2a34679b0c8399e0d1bb9d68d54ab, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

### Avoid

- **Using gte-reranker-modernbert-base as a drop-in embedding generator for vector search without verification** — Config.json records a sequence-classification architecture (ModernBertForSequenceClassification) indicating a cross-encoder reranker head rather than an embedding-only encoder; primary blobs do not provide evidence that this checkpoint is intended or configured as an embeddings-only encoder.
  Scope: Alibaba-NLP/gte-reranker-modernbert-base (config.json and README blobs)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md
- **Assuming numeric calibration or cross-query comparability of any returned "raw_scores" without validation** — Located primary repository blobs (README/config/commits/tokenizer blobs) do not define whether returned relevance fields are logits, probabilities, or calibrated scores; numeric semantics and calibration are not documented in the located blobs.
  Scope: Alibaba-NLP/gte-reranker-modernbert-base (located repository blobs)
  Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json

## Input preparation

### Semantic inputs

- The model is a text reranker intended to accept query + candidate document pairs for pairwise relevance scoring (cross-encoder input semantics). Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json

### Accepted formats

- Repository README and model listing present the model as a reranker for retrieval/reranking tasks and are the authoritative upstream usage examples located in the repository blobs. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base

### Preprocessing

- Config blobs document vocab_size and special token IDs (e.g., bos_token_id 50281, eos_token_id 50282, pad_token_id 50283, cls_token_id 50281) and other tokenizer-related metadata for the checkpoint. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json
- Tokenizer configuration blob records model_max_length = 8192, tokenizer max length = 512, padding on the right, truncation side = right, and truncation strategy = "longest_first" for the distributed tokenizer configuration. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F5/tokenizer_config.json

### Pre-submit validation

- Model config and commit blobs report maximum position embeddings = 8192; repository blobs do not specify per-field token budgets or runtime truncation enforcement — implementers must validate combined token lengths (query+document) and truncation behavior before production deployment. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commit/c40156962ee2a34679b0c8399e0d1bb9d68d54ab, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

### Task-specific formatting

- Repository README model-list entries present high-level examples and label the model as a reranker for retrieval/reranking tasks; follow the README examples for query+candidate formatting as authoritative upstream examples. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base

## Output interpretation

### Outputs

- Repository README/config/commits do not provide a definitive primary-blob description of returned field numeric semantics (for example, no authoritative blob defines whether a returned relevance field is logits, probabilities, or calibrated scores). Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json

### Interpretation

- Because the located primary blobs do not define numeric semantics or calibration for returned relevance scores, implementers must validate score calibration and cross-query comparability before treating scores as probabilities or calibrated measures. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

### Post-inference validation

- Primary blobs do not document post-inference calibration or validation procedures; implementers should perform downstream calibration and sanity checks for thresholds, cross-query comparisons, and any probabilistic interpretations. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

## Public benchmarks

### Text reranking / retrieval

- Dataset/split: MTEB-en / not reported
- Metric/value: MTEB-en (aggregate) / 56.19 (`higher-is-better`)
- Model scope: gte-reranker-modernbert-base (README model list entry)
- Conditions: Aggregate score reported in repository README model list table; the located README blob does not publish per-dataset protocol, splits, or evaluation script details for the reported aggregate.
- Source: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md
- Locator: README.md model list table showing gte-reranker-modernbert-base performance row
- Caveat: Primary README blob reports an aggregate numeric value but does not include the detailed per-dataset protocol, splits, or evaluation scripts in the located blob.

### Text reranking / retrieval

- Dataset/split: BEIR / not reported
- Metric/value: BEIR (aggregate) / 90.68 (`higher-is-better`)
- Model scope: gte-reranker-modernbert-base (README model list entry)
- Conditions: Aggregate score reported in repository README model list table; the located README blob does not publish per-dataset protocol, splits, or evaluation script details for the reported aggregate.
- Source: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md
- Locator: README.md model list table showing gte-reranker-modernbert-base performance row
- Caveat: Primary README blob reports an aggregate numeric value but does not include the detailed per-dataset protocol, splits, or evaluation scripts in the located blob.

### Long-document retrieval / reranking

- Dataset/split: LoCo / not reported
- Metric/value: LoCo (aggregate) / 79.99 (`higher-is-better`)
- Model scope: gte-reranker-modernbert-base (README model list entry)
- Conditions: Aggregate score reported in repository README model list table; the located README blob does not publish per-dataset protocol, splits, or evaluation script details for the reported aggregate.
- Source: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md
- Locator: README.md model list table showing gte-reranker-modernbert-base performance row
- Caveat: Primary README blob reports an aggregate numeric value but does not include the detailed per-dataset protocol, splits, or evaluation scripts in the located blob.

## Comparisons

### BAAI/bge-reranker-v2-m3 — `insufficient-evidence`

- Task: retrieval-and-reranking
- Criteria: No checkpoint-scoped primary-source side-by-side comparison (same dataset/metric/split/protocol) was found in the located Alibaba-NLP repository blobs for gte-reranker-modernbert-base.
- Rationale: Checked the repository README and config/commit blobs for gte-reranker-modernbert-base and did not find a primary-blob side-by-side numeric comparison that names BAAI/bge-reranker-v2-m3 with matching protocol details.
- Comparison conditions: Peer-side primary evidence for BAAI/bge-reranker-v2-m3 with matching protocol not provided in the located blobs; no protocol-aligned side-by-side found.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json

### NVIDIA Llama rerank variants (NVIDIA Llama 3.2 NV-RerankQA 1B v2; NVIDIA Llama Nemotron Rerank 1B v2; NVIDIA Llama Nemotron Rerank VL 1B v2) — `insufficient-evidence`

- Task: retrieval-and-reranking
- Criteria: No checkpoint-scoped primary-source side-by-side comparison found in the located Alibaba-NLP repository blobs for gte-reranker-modernbert-base.
- Rationale: Repository README/config/commit blobs for gte-reranker-modernbert-base contain no direct numeric comparisons to the listed NVIDIA reranker variants in the located primary blobs.
- Comparison conditions: Peer-side primary comparison entries not found in the located Alibaba-NLP blobs; no direct protocol-aligned comparison evidence present in the research findings.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

### Qwen reranker variants (Qwen3-Reranker-0.6B, Qwen3-Reranker-4B, Qwen3-VL-Reranker-2B) — `insufficient-evidence`

- Task: retrieval-and-reranking
- Criteria: No checkpoint-scoped primary-source side-by-side comparison found in the located Alibaba-NLP repository blobs for gte-reranker-modernbert-base.
- Rationale: The located Alibaba-NLP blobs do not include direct numeric comparisons or references to the listed Qwen reranker variants in the repository README or config/commit blobs reviewed in the research findings.
- Comparison conditions: Peer-side primary comparison entries not present in the located Alibaba-NLP blobs; no direct protocol-aligned comparison evidence present in the research findings.
- Evidence: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

## Limitations and safety

### Limitations

- Apache-2.0 license is declared in repository README blame view. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/2b1862f777a28ed2f938a99b368aa67a8bccd796/README.md
- Evidence gap: The located primary blobs do not document training data sources, data provenance, or bias/mitigation statements for this exact checkpoint.
- The repository records weight artifact uploads (safetensors, ONNX) in commits, but the repository blobs do not include runtime performance (latency, GPU memory, throughput) measurements for this specific checkpoint. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commits/c2c3466f6bb32f168f3df9d76b2aa27023de1336

### Safety

- Evidence gap: The located primary repository blobs do not contain creator-provided statements about safety mitigations, privacy/PHI handling, clinical/regulatory warnings, or explicit dual-use mitigations for this checkpoint.
- Operational artifacts in the repository commits (weights uploads) and README blobs are implementation/deployment evidence rather than documented safety mitigations; users should apply standard data-handling and review controls when deploying rerankers. Sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commits/c2c3466f6bb32f168f3df9d76b2aa27023de1336, https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Exact official starting source declared by Forge (model page)

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: Model page is the repository-level canonical locator for the checkpoint and provides top-level metadata for Alibaba-NLP/gte-reranker-modernbert-base used by this dossier.
- Scope: Alibaba-NLP/gte-reranker-modernbert-base (model page)
- Supports: Model identifier and top-level repository metadata
- Supports: High-level model listing and task tags

### Repository README (refs/pr/4) showing model list and performance rows (README.md)

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F4/README.md
- Publisher: Alibaba-NLP (Hugging Face repository blob)
- Type: `repository`
- Primary because: README blob contains the model-list table rows and reported aggregate benchmark numbers for gte-reranker-modernbert-base used as checkpoint-scoped evidence in this dossier.
- Scope: README model list entries and benchmark table rows for gte-reranker-modernbert-base
- Supports: Reported aggregate performance numbers (MTEB-en 56.19, BEIR 90.68, LoCo 79.99) for gte-reranker-modernbert-base
- Supports: Model listing showing distinction between embedding and reranker variants
- Supports: Model size and max input length statements

### Repository README blame (alternate view) showing model family statements and license (README.md blame)

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/2b1862f777a28ed2f938a99b368aa67a8bccd796/README.md
- Publisher: Alibaba-NLP (Hugging Face repository blob blame)
- Type: `repository`
- Primary because: Blame view of the repository README records model-list entries and metadata used by this dossier including license statements and top-level model facts.
- Scope: README model-list entries and license statements for gte-reranker-modernbert-base
- Supports: Model listing and task/type (Text reranker)
- Supports: Apache-2.0 license declaration in README blame view
- Supports: Model size and max input length statements

### Model configuration (config.json) blame for refs/pr/4 showing architecture and hyperparameters

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blame/refs%2Fpr%2F4/config.json
- Publisher: Alibaba-NLP (Hugging Face repository blob blame)
- Type: `repository`
- Primary because: Model config blob documents architecture class, hidden_size, special token IDs, max_position_embeddings and other hyperparameters for the checkpoint.
- Scope: config.json for gte-reranker-modernbert-base (refs/pr/4)
- Supports: Architecture: ModernBertForSequenceClassification
- Supports: Hidden size 768 and other hyperparameters
- Supports: max_position_embeddings = 8192 and tokenizer-related token ID fields

### Commit recording config and README association (commit c40156962ee2a34679b0c8399e0d1bb9d68d54ab)

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commit/c40156962ee2a34679b0c8399e0d1bb9d68d54ab
- Publisher: Alibaba-NLP (Hugging Face repository commit view)
- Type: `repository`
- Primary because: Commit metadata records config.json upload and associated model metadata at a specific revision used to tie hyperparameter values to a concrete revision.
- Scope: Commit c40156962ee2a... (config/README association)
- Supports: Recorded max_position_embeddings = 8192 at this commit
- Supports: Association of config and README blobs at a named revision

### Repository commits view showing weight artifact uploads (commits/c2c3466f6bb32f168f3df9d76b2aa27023de1336)

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/commits/c2c3466f6bb32f168f3df9d76b2aa27023de1336
- Publisher: Alibaba-NLP (Hugging Face repository commits view)
- Type: `repository`
- Primary because: Commits page records ONNX and safetensors uploads in the repository history and is used to verify presence of weight artifacts in the repository history.
- Scope: Weights/artifact upload commits for gte-reranker-modernbert-base
- Supports: ONNX and model.safetensors uploads recorded in commits
- Supports: General commit history for artifact uploads and pipeline tag changes

### Tokenizer configuration blob (tokenizer_config.json) for gte-reranker-modernbert-base

- URL: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/blob/refs%2Fpr%2F5/tokenizer_config.json
- Publisher: Alibaba-NLP (Hugging Face repository blob)
- Type: `repository`
- Primary because: Tokenizer configuration blob records tokenizer settings distributed with the checkpoint (max lengths, pad/truncation behavior, special tokens) used as upstream tokenizer metadata.
- Scope: tokenizer_config.json for gte-reranker-modernbert-base
- Supports: model_max_length = 8192 and tokenizer max_length = 512
- Supports: pad on the right, truncation on the right, truncation strategy = longest_first
- Supports: Special tokens ([CLS], [PAD], [SEP], [MASK], [UNK]) and PreTrainedTokenizerFast class indicator

### ModernBERT canonical arXiv preprint

- URL: https://arxiv.org/pdf/2412.13663
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical ModernBERT preprint provides family-level architecture description and long-context encoder claims referenced by the gte-modernbert series; used only for family-level corroboration.
- Scope: ModernBERT family documentation (family-level corroboration)
- Supports: Family-level ModernBERT claims such as native sequence length 8192, family architectural descriptions, and long-context performance claims

## Evidence gaps

- No primary-blob documentation found for tokenizer algorithmic internals (BPE vs SentencePiece), normalization rules, or lowercasing semantics for the checkpoint; the tokenizer_config.json records configured fields but not algorithmic internals.
- No primary-blob documentation located for per-field token budgets (e.g., explicit query vs document token limits), truncation enforcement at runtime beyond tokenizer default settings, or explicit truncation-side policy tied to inference code in the located repository blobs.
- No primary-blob documentation located for numeric semantics or calibration of any returned relevance score fields (for example, whether returned values are logits, probabilities, or calibrated scores) in the reviewed repository blobs.
- No checkpoint-scoped primary-side-by-side comparisons to the named Forge peers (BAAI/bge-reranker-v2-m3; NVIDIA Llama rerank variants; Qwen reranker variants) were located in the reviewed Alibaba-NLP repository blobs.
- No primary-blob runtime performance measurements (latency, GPU memory footprint, throughput) for this specific checkpoint were found in the located README/config/commit blobs.
- No primary-blob documentation of training data sources, data provenance, or bias/mitigation statements for this exact checkpoint was located in the reviewed repository blobs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base/discussions/15/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
