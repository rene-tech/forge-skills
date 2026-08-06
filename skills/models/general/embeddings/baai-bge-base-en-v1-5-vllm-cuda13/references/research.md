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

- Research key: `huggingface-co-baai-bge-base-en-v1-5-57a31c3243`
- Independent audit: `revised`
- Researched: `2026-07-23T23:31:23.613113+00:00`

BAAI/bge-base-en-v1.5 is an embedding checkpoint in the BGE family implemented as a BERT-style encoder (model_type: bert) with 12 layers, 12 attention heads, hidden size 768, intermediate size 3072, and an embedding/output dimension 768. The upstream repository config.json reports vocab_size 30522, pad_token_id 0, type_vocab_size 2, and max_position_embeddings 512. A repository commit (08e3d2c2...) is present in the model history. The model README/performance table reports aggregated MTEB-style scores (average 63.55 across 56 tasks and per-category aggregated scores). Tokenizer artifacts (tokenizer.json and special_tokens_map.json) are present, with special token strings defined; explicit numeric ids for special tokens beyond pad_token_id are not provided in the inspected files. Several operational details are not specified in the inspected sources (exact tokenizer class entry, full special-token id map beyond pad_token_id, per-dataset MTEB protocol details such as seeds and splits, and explicit postprocessing/normalization instructions for embeddings).

## Identity

- Upstream name: BAAI/bge-base-en-v1.5
- Checkpoint/version: BAAI/bge-base-en-v1.5
- Immutable revision: 08e3d2c28e3886dfbcd98caebb447d9e23614bc0
- Parameter scale: 109 million parameters
- Architecture/head: BERT encoder (model_type: bert) — num_hidden_layers: 12, num_attention_heads: 12, hidden_size: 768, intermediate_size: 3072, vocab_size: 30522, pad_token_id: 0, type_vocab_size: 2, max_position_embeddings: 512
- License: MIT
- Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/special_tokens_map.json, https://huggingface.co/BAAI/bge-base-en-v1.5/commit/08e3d2c28e3886dfbcd98caebb447d9e23614bc0, https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md

## Selection

### Recommended

- **General text embeddings for semantic tasks (retrieval, semantic textual similarity, pair classification, clustering, reranking)** — The model README/performance table reports aggregated embedding-task evaluation (average and per-category aggregated scores) for BAAI/bge-base-en-v1.5, indicating the checkpoint is evaluated and positioned for embedding tasks.
  Scope: BAAI/bge-base-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md

### Conditional


### Avoid

- **Sequences longer than 512 tokens without pre-splitting or truncation** — The checkpoint configuration sets max_position_embeddings to 512 (absolute positional embeddings); the upstream configuration therefore does not natively support longer sequences.
  Scope: BAAI/bge-base-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- **Clinical/PHI processing and clinical decision-making without expert validation** — No upstream model card or README guidance, tests, or validations for clinical or PHI-sensitive workflows were found in the inspected repository files and README; upstream documentation does not provide clinical validation or PHI-handling guidance.
  Scope: BAAI/bge-base-en-v1.5
  Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md

## Input preparation

### Semantic inputs

- Text strings (English) as the input modality for embedding. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md

### Accepted formats

- Upstream accepts tokenized text up to a maximum sequence length of 512 tokens (absolute position embeddings configured for 512). Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md

### Preprocessing

- Transformers version is declared as 4.30.0 in the config metadata. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json
- Canonical preprocessing must produce token sequences not exceeding 512 tokens (truncate or pre-split upstream text to meet this bound). Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json
- Tokenizer artifact (tokenizer.json) and special_tokens_map.json are present in the repository and should be used for tokenization when available. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/tokenizer.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/special_tokens_map.json

### Pre-submit validation

- Inputs should be validated to ensure tokenized length ≤ 512 tokens; pad token id is specified as 0 in config.json and type vocab size is 2 (useful for padding/type-id checks). Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json

### Task-specific formatting

- No upstream prompt templates or embedding-specific prompt formatting were found in the inspected README and repository files; the model is presented as a base embedding encoder. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json

## Output interpretation

### Outputs

- The model emits a fixed-size dense embedding vector with dimension 768 (embedding dimension reported as 768 in the README performance table and hidden size 768 in config.json). Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md

### Interpretation

- Embeddings are dense vectors for semantic tasks; upstream sources provide evaluation metrics (aggregated scores) but do not provide calibrated score semantics or units for embedding magnitudes. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md

### Post-inference validation

- No upstream postprocessing instructions (e.g., L2 normalization, whitening, quantization) were found in inspected repository files; downstream users must validate embedding similarity behavior (e.g., choice of cosine similarity or dot product, any normalization) against labeled data before production usage. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json

## Public benchmarks

### Aggregated embedding benchmark (MTEB-style average)

- Dataset/split: MTEB (56 tasks aggregated) / not reported
- Metric/value: average score across 56 tasks / 63.55 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Aggregated score as reported in the repository README performance table; per-dataset splits, seeds, and detailed protocol are not provided in the README performance table.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'average score' (performance table in README)
- Caveat: The README performance table provides aggregated scores but does not expose per-dataset splits, seeds, or detailed evaluation protocol in the inspected file.

### Classification (MTEB category average)

- Dataset/split: MTEB classification category (12 classification tasks aggregated) / not reported
- Metric/value: classification score (category average) / 75.53 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'classification' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### Clustering (MTEB category average)

- Dataset/split: MTEB clustering category (11 clustering tasks aggregated) / not reported
- Metric/value: clustering score (category average) / 45.77 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'clustering' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### Pair classification (MTEB category average)

- Dataset/split: MTEB pair classification category (3 tasks aggregated) / not reported
- Metric/value: pair classification score (category average) / 86.55 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'pair classification' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### Reranking (MTEB category average)

- Dataset/split: MTEB reranking category (4 tasks aggregated) / not reported
- Metric/value: reranking score (category average) / 58.86 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'reranking' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### Retrieval (MTEB category average)

- Dataset/split: MTEB retrieval category (15 tasks aggregated) / not reported
- Metric/value: retrieval score (category average) / 53.25 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'retrieval' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### STS (semantic textual similarity) (MTEB category average)

- Dataset/split: MTEB STS category (10 tasks aggregated) / not reported
- Metric/value: STS score (category average) / 82.40 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'STS' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

### Summary (MTEB category average)

- Dataset/split: MTEB summary category / not reported
- Metric/value: summary score (category average) / 31.07 (`higher-is-better`)
- Model scope: BAAI/bge-base-en-v1.5
- Conditions: Category-aggregated number reported in the README performance table; per-dataset breakdown not present in the inspected file.
- Source: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Locator: README.md — performance table row for 'BAAI/bge-base-en-v1.5' column 'summary' (performance table in README)
- Caveat: README provides category-aggregated numbers without per-dataset metric breakdown in the inspected file.

## Comparisons

### not reported — `insufficient-evidence`

- Task: pairwise model comparisons for embedding tasks
- Criteria: No primary-source per-checkpoint, per-dataset pairwise comparison table or matching-protocol evaluation found in the inspected repository README or config files for BAAI/bge-base-en-v1.5.
- Rationale: The inspected README provides aggregated category and average scores for BAAI/bge-base-en-v1.5 but does not provide protocol-matched pairwise comparison tables with other specific models.
- Comparison conditions: N/A — lacking primary-source pairwise, per-dataset, same-protocol comparisons in the inspected files.
- Evidence: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md

## Limitations and safety

### Limitations

- Maximum sequence length limited to 512 tokens (absolute positional embeddings configured for 512), limiting native support for longer documents. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Architecture is a BERT-style encoder (model_type: bert) with 12 encoder layers and hidden size 768; this encoder-only architecture is intended for embeddings rather than generative/causal modeling. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Ambiguity in reported category scores across inspected README variants: the README performance table entries in different inspected files show close but not identical category numbers (for example, clustering reported as 45.77 in one inspected README entry and as 45.81 in another inspected source collection); these inconsistencies were observed in the inspected repository files and require clarification. Sources: https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- No explicit upstream instructions for postprocessing or embedding normalization (L2 normalization, whitening, quantization) were found in the inspected repository files; downstream normalization choices will affect similarity scores and must be validated. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json
- The repository metadata declares transformers_version as 4.30.0 which may constrain runtime compatibility. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json

### Safety

- No upstream model card or README provides guidance or mandatory restrictions specific to clinical/PHI or regulated-data usage in the inspected files; treat clinical or regulated-data usage as unsupported by upstream documentation and require expert review. Sources: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md, https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Model config (config.json) for BAAI/bge-base-en-v1.5 on Hugging Face

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/config.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Direct model configuration file in the official Hugging Face repository providing architecture hyperparameters and metadata.
- Scope: BAAI/bge-base-en-v1.5 (config.json)
- Supports: model_type: bert
- Supports: num_hidden_layers: 12
- Supports: num_attention_heads: 12
- Supports: hidden_size: 768
- Supports: intermediate_size: 3072
- Supports: max_position_embeddings: 512
- Supports: vocab_size: 30522
- Supports: pad_token_id: 0
- Supports: type_vocab_size: 2
- Supports: transformers_version: 4.30.0

### Special tokens map (special_tokens_map.json) for BAAI/bge-base-en-v1.5 on Hugging Face

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/main/special_tokens_map.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository file defining special token string labels for the checkpoint.
- Scope: BAAI/bge-base-en-v1.5 (special_tokens_map.json)
- Supports: Defines CLS token as "[CLS]"
- Supports: Defines MASK token as "[MASK]"
- Supports: Defines PAD token as "[PAD]"
- Supports: Defines SEP token as "[SEP]"
- Supports: Defines UNK token as "[UNK]"

### Repository commit for BAAI/bge-base-en-v1.5 (commit 08e3d2c2)

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/commit/08e3d2c28e3886dfbcd98caebb447d9e23614bc0
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Immutable repository commit referenced in the model's repository history.
- Scope: BAAI/bge-base-en-v1.5 (commit 08e3d2c2)
- Supports: Repository commit with changes to model file hash and size
- Supports: Historical edits to config.json (removal of some previous keys)

### Repository commits index for BAAI/bge-base-en-v1.5 (commits/main)

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/commits/main
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Repository commits index showing commit history and commit messages for the checkpoint.
- Scope: BAAI/bge-base-en-v1.5 (commits/main)
- Supports: Commit history entries including 'Onnx Support' (a5beb1e) and other repository updates

### README performance table for BAAI/bge-base-en-v1.5 (README.md at commit dd9f4294)

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/README.md
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Model README in the official Hugging Face repository containing the performance table used for aggregated scores and descriptive model information.
- Scope: BAAI/bge-base-en-v1.5 (README.md at specific commit)
- Supports: Embedding/output dimension 768 in performance table
- Supports: Maximum sequence length 512 in performance table
- Supports: Aggregated performance numbers (average 63.55 and per-category aggregated scores) reported in the performance table

### Tokenizer artifact (tokenizer.json) for BAAI/bge-base-en-v1.5

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5/blob/dd9f42942e0729b6c53632f3c23b0e801f236569/tokenizer.json
- Publisher: Hugging Face
- Type: `repository`
- Primary because: Tokenizer artifact present in the official Hugging Face repository for the checkpoint.
- Scope: BAAI/bge-base-en-v1.5 (tokenizer.json)
- Supports: Presence of tokenizer.json artifact for the checkpoint

### Mirror of README/performance table (hugging-face.cn mirror of README.md)

- URL: https://hugging-face.cn/BAAI/bge-base-en-v1.5/blob/main/README.md
- Publisher: hugging-face.cn (mirror)
- Type: `repository`
- Primary because: Inspected mirror copy included in the evidence set that contains performance-table statements and license citation used in the findings.
- Scope: BAAI/bge-base-en-v1.5 (README mirror)
- Supports: Statement that the model is MIT licensed
- Supports: Performance table entries including average and per-category aggregated scores
- Supports: Model dimension 768 and sequence length 512 reported in the performance table
- Supports: Parameter count reported as 109 million in the mirrored README performance table

### Exact official starting source declared by Forge

- URL: https://huggingface.co/BAAI/bge-base-en-v1.5
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: baai-bge-base-en-v1-5
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Tokenizer class name (tokenizer_class entry) is not specified in the inspected repository files: checked tokenizer.json and special_tokens_map.json in the repository — no explicit tokenizer_class string was found in the inspected files.
- Numeric ids for special tokens other than pad_token_id are not specified in the inspected files: special_tokens_map.json defines special token strings but does not provide explicit numeric ids for CLS, SEP, UNK, MASK; config.json provides pad_token_id = 0 but not the others.
- Per-dataset, per-split MTEB metric breakdowns, seeds, and exact evaluation protocol are not present in the inspected README performance table: the README provides aggregated and category averages but not the per-dataset rows, random seeds, or full protocol details.
- No explicit upstream instructions for embedding postprocessing (normalization, whitening, quantization) were found in the inspected repository files: checked README.md, config.json, and tokenizer artifacts — no postprocessing guidance present.
- Batching behavior, recommended batch sizes, memory/latency measurements, and operational performance numbers are not provided in the inspected repository files: checked config.json and README.md — no performance benchmarks or batching guidance present.
- A small inconsistency/ambiguity in reported category numbers across inspected README variants was observed (e.g., clustering reported as 45.77 in one inspected source and 45.81 in another set of inspected facts); the repository files inspected do not explain the discrepancy and require clarification.
- No explicit upstream statement was found in the inspected files confirming or denying the claim that the pre-trained checkpoint 'cannot be used for similarity calculation directly and needs to be fine-tuned'; that external claim is not corroborated by the inspected repository files and requires creator clarification.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[2].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[3].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[4].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[5].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[6].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[7].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/BAAI/bge-base-en-v1.5: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
