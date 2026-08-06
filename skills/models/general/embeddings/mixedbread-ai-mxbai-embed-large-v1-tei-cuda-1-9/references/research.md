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

- Research key: `huggingface-co-mixedbread-ai-mxbai-embed-large-v1-593ef8cf28`
- Independent audit: `revised`
- Researched: `2026-08-06T12:49:05.421946+00:00`

Upstream checkpoint mixedbread-ai/mxbai-embed-large-v1 (checkpoint name: mxbai-embed-large-v1) is an embeddings encoder based on a BertModel architecture with hidden_size=1024, 24 layers, and 16 attention heads as specified in the upstream config.json. The Hugging Face model page reports an aggregate MTEB average score of 64.68 and several task-level MTEB averages (classification, clustering, retrieval, STS, reranking, summarization) for this checkpoint. The repository LICENSE declares Apache-2.0. Primary sources do not document tokenizer/tokenization specifics, a formal input JSON schema, or per-dataset MTEB breakdowns; these gaps are recorded. Where the model card and config.json provide configuration values (embedding dimension, architecture, default torch dtype), runtime-serving behaviors (normalization defaults, Forge/NIM-specific runtime dtype or normalization) are not described in the verified primary checkpoint artifacts and are therefore treated as evidence gaps.

## Identity

- Upstream name: mixedbread-ai/mxbai-embed-large-v1
- Checkpoint/version: mxbai-embed-large-v1
- Immutable revision: not reported
- Parameter scale: 0.34 B parameters
- Architecture/head: BertModel encoder; hidden_size=1024; num_hidden_layers=24; num_attention_heads=16
- License: Apache-2.0
- Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1, https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json, https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/LICENSE

## Selection

### Recommended

- **Dense retrieval and semantic search using text embeddings** — The upstream model card reports embedding outputs and MTEB evaluation coverage indicating suitability for embedding-based retrieval tasks; config.json specifies a 1024-d embedding dimension supporting dense-retrieval vector sizes.
  Scope: mixedbread-ai/mxbai-embed-large-v1
  Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1, https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json
- **Retrieval-augmented generation (RAG) workflows where a separate retriever uses the checkpoint's embeddings** — The model is presented by the authors as an embedding encoder with MTEB benchmark results, indicating intended use as a retriever embedding source; the checkpoint exposes embeddings appropriate for retrieval components.
  Scope: mixedbread-ai/mxbai-embed-large-v1
  Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1, https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json
- **Clustering and reranking in embedding space** — Upstream MTEB task-level averages reported on the model page include clustering and reranking scores, supporting suitability for clustering and reranking experiments using the checkpoint embeddings.
  Scope: mixedbread-ai/mxbai-embed-large-v1
  Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- **Using embeddings as features for downstream classifiers (classification embeddings)** — The model page reports MTEB classification average scores for the checkpoint, indicating embeddings have been evaluated for classification tasks.
  Scope: mixedbread-ai/mxbai-embed-large-v1
  Evidence: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Conditional


### Avoid

- **Use for clinical, medical, or other safety-critical decision-making without expert validation** — Evidence gap: primary sources (model card, config.json, README, LICENSE, and the arXiv paper) do not provide clinical- or safety-critical validation, nor do they provide domain-specific safety assessments required for high-stakes decision-making.
  Scope: mixedbread-ai/mxbai-embed-large-v1
  Evidence: documented evidence gap

## Input preparation

### Semantic inputs

- Inputs are text strings intended to be encoded as embeddings (queries, sentences, or short passages). Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Accepted formats

- The upstream model card documents access via the MixedbreadAI Python client with encoding formats and a dimensions parameter; inputs are provided as text (single string or list of strings is implied by client usage examples on the model page). Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Preprocessing

- Evidence gap: the upstream primary artifacts do not specify tokenizer name, tokenizer version, vocabulary, normalization rules, or exact tokenization pipeline for this checkpoint.

### Pre-submit validation

- Evidence gap: explicit input-validation rules (allowed character sets, maximum token limits as enforced by tokenizer, or error behaviors) are not documented in the verified primary sources for this checkpoint.

### Task-specific formatting

- Evidence gap: no canonical prompt template or retrieval prompt convention is documented in the upstream model card or config.json for this checkpoint.

## Output interpretation

### Outputs

- The upstream checkpoint produces an embedding vector with dimension 1024 (embedding size derived from model hidden_size in config.json and documented on the model card); the config.json also records default torch dtype=float16. Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json, https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Interpretation

- Embeddings emitted by the checkpoint are presented as semantic vectors suitable for similarity comparisons and downstream retrieval/clustering/classification tasks; numeric interpretation (similarity thresholds, score calibration) is not provided upstream. Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Post-inference validation

- Evidence gap: no post-inference calibration, score-threshold guidance, or recommended sanity checks are documented in upstream primary sources for this checkpoint.

## Public benchmarks

### Embedding-based tasks (aggregate MTEB)

- Dataset/split: MTEB / all
- Metric/value: average / 64.68 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Upstream model card reports an aggregated average across MTEB datasets; this is upstream-checkpoint evidence (not a Forge runtime claim). Per-dataset breakdown is not provided in the verified upstream model card.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section
- Caveat: Aggregate MTEB result; per-dataset numbers or per-dataset splits are not provided in the upstream model card.

### MTEB - classification (task-level average)

- Dataset/split: MTEB (classification average) / not reported
- Metric/value: average / 75.64 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; treated as upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section
- Caveat: Per-dataset classification breakdown not provided on the upstream model card.

### MTEB - clustering (task-level average)

- Dataset/split: MTEB (clustering average) / not reported
- Metric/value: average / 46.71 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section
- Caveat: Per-dataset clustering breakdown not provided on the upstream model card.

### MTEB - pair classification (task-level average)

- Dataset/split: MTEB (pair classification average) / not reported
- Metric/value: average / 87.2 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section

### MTEB - reranking (task-level average)

- Dataset/split: MTEB (reranking average) / not reported
- Metric/value: average / 60.11 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section

### MTEB - retrieval (task-level average)

- Dataset/split: MTEB (retrieval average) / not reported
- Metric/value: average / 54.39 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section

### MTEB - STS (semantic textual similarity) (task-level average)

- Dataset/split: MTEB (STS average) / not reported
- Metric/value: average / 85.00 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section

### MTEB - summarization (task-level average)

- Dataset/split: MTEB (summarization average) / not reported
- Metric/value: average / 32.71 (`higher-is-better`)
- Model scope: mixedbread-ai/mxbai-embed-large-v1
- Conditions: Reported as a task-level average on the upstream model card; upstream-checkpoint evidence.
- Source: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Locator: MTEB results section

## Comparisons

### Alibaba-NLP/gte-modernbert-base — `insufficient-evidence`

- Task: embedding-based semantic similarity
- Criteria: No verified checkpoint-to-checkpoint, same-protocol primary evidence exists for the alternative within the curated top-level sources; direct protocol-matched comparison cannot be validated from the available primary artifacts.
- Rationale: The draft previously referenced a Hugging Face page for the alternative but that page was not included as a verified primary source in the curated top-level sources; therefore a direct, checkpoint-scoped comparison is unsupported by the verified primary evidence set.
- Comparison conditions: Alternative model primary source for the stated checkpoint is not present in this dossier's primary sources; protocols (dataset splits, prompt/pooling, normalization) cannot be confirmed as matched.
- Evidence:

## Limitations and safety

### Limitations

- Evidence gap: tokenizer name, tokenizer version, vocabulary, and exact tokenization/normalization pipeline are not specified in the upstream model card or config.json.
- Evidence gap: per-dataset MTEB breakdowns (exact dataset rows and splits) are not provided in the upstream model card; only aggregate and task-level averages are reported upstream. Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1

### Safety

- Model weights and repository code are licensed under the Apache License 2.0 according to the upstream LICENSE file; preserve license obligations when redistributing or using the model. Sources: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/LICENSE
- Evidence gap: the upstream primary artifacts do not provide explicit safety, privacy, or domain-specific dual‑use guidance (for example, clinical use, biosecurity, or highly regulated domains).

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### MixedBread AI mxbai-embed-large-v1 model page

- URL: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
- Publisher: Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model card for the checkpoint; contains model description and reported MTEB results and size.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: embedding-output
- Supports: input-modality=text
- Supports: license
- Supports: MTEB-aggregate
- Supports: task-level-MTEB-averages
- Supports: client-access-notes

### mxbai-embed-large-v1 config.json

- URL: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository config describing exact architecture fields (hidden_size, num_hidden_layers, num_attention_heads, default torch dtype).
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: architecture
- Supports: hidden-size
- Supports: layers
- Supports: heads
- Supports: dtype
- Supports: max-position-embeddings

### License for mxbai-embed-large-v1

- URL: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/LICENSE
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Canonical LICENSE file for the repository establishing license for code and model weights as published upstream.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: license
- Supports: usage-constraints

### mxbai-embed-large-v1 README.md

- URL: https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/README.md
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository README accompanying the upstream checkpoint; supports usage notes and high-level model family description.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: model-family-description
- Supports: usage-notes

### arXiv: Mixedbread AI mxbai-embed-large-v1 paper

- URL: https://arxiv.org/pdf/2403.10446
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing model design and training approach referenced by the authors.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: model-description
- Supports: training-approach

### Mixedbread AI Python SDK README

- URL: https://github.com/mixedbread-ai/python-sdk/blob/main/README.md
- Publisher: GitHub
- Type: `repository`
- Primary because: Author-maintained client repository referenced by the upstream model page for programmatic access to the checkpoint.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: client-access
- Supports: usage-examples

### Binary embeddings repository

- URL: https://github.com/mixedbread-ai/binary-embeddings
- Publisher: GitHub
- Type: `repository`
- Primary because: Author-maintained repository referenced by the upstream project; supports binary embedding usage discussions included in the upstream project scope.
- Scope: mixedbread-ai/mxbai-embed-large-v1
- Supports: binary-embeddings
- Supports: quantization-discussions

## Evidence gaps

- Parameter-count reporting: while the model card reports 0.34 B parameters, the upstream artifacts do not provide an explicit exact parameter-count breakdown or immutable revision that documents the exact parameter count; revision hash is not reported in the verified primary sources.
- Exact tokenizer details (tokenizer name, tokenizer version, vocab files, normalization rules, tokenization pipeline) are not provided in the upstream model card or config.json.
- Per-dataset MTEB breakdowns (exact dataset-level rows and splits) are not provided in the upstream model card; only aggregate and task-level averages are published upstream.
- No canonical input JSON schema or formal API request/response schema is documented in the verified upstream sources for this checkpoint.
- No upstream primary-source guidance is provided for post-inference calibration, similarity-threshold selection, or domain-specific safety validation; downstream calibration and threshold guidance are absent.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 5 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property limitsAndRisks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
