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

- Research key: `huggingface-co-qwen-qwen3-embedding-8b-fc4f46b5b3`
- Independent audit: `revised`
- Researched: `2026-08-06T09:44:28.439363+00:00`

This dossier is scoped to the exact upstream checkpoint Qwen3-Embedding-8B and uses only canonical primary URLs found in the reviewed evidence. Primary upstream materials (Hugging Face model page and model files) report an 8B-parameter Qwen3 embedding model with 36 transformer layers, a reported embedding dimensionality of 4096, and an Apache-2.0 model-weight license. Configuration files contain multiple positional/token-length fields that conflict (config.json reports max_position_embeddings=40960 while tokenizer_config.json reports model_max_length=131072), and a public benchmark table (commit) contains numeric columns whose dataset/split mapping is not labeled in the located table; these inconsistencies and missing dataset/licensing metadata are recorded as explicit evidence gaps in the dossier.

## Identity

- Upstream name: Qwen3 Embedding
- Checkpoint/version: Qwen3-Embedding-8B
- Immutable revision: not reported
- Parameter scale: 8B
- Architecture/head: Qwen3 dense transformer backbone for embedding (model_type: qwen3, Qwen3ForCausalLM listed in config.json)
- License: Apache-2.0 (model weights)
- Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/LICENSE

## Selection

### Recommended

- **Multilingual semantic search and retrieval** — The Hugging Face model page and model config identify Qwen3-Embedding-8B as an embedding model intended to map text into dense vectors and support multilingual capability; config.json and the model page list properties and usage context for text embeddings.
  Scope: Qwen3-Embedding-8B (upstream checkpoint)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json
- **Semantic textual similarity and clustering (downstream evaluation required)** — Upstream materials describe the embedding model and its intended downstream uses (retrieval, similarity, ranking); downstream evaluation is required to calibrate thresholds per task and dataset.
  Scope: Qwen3-Embedding-8B (upstream checkpoint)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

### Conditional


### Avoid

- **Healthcare / clinical data processing without expert review** — Primary upstream sources for this checkpoint do not provide explicit statements, validations, or clinical-use endorsements; there is no documented healthcare-specific validation in the located primary materials.
  Scope: Qwen3-Embedding-8B
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

## Input preparation

### Semantic inputs

- Plain text strings to be converted into dense embedding vectors for downstream retrieval, ranking, similarity, and clustering tasks. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B

### Accepted formats

- Text modality inputs (string text) are the accepted input format for the upstream embedding checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B

### Preprocessing

- Tokenizer class and special-token mappings are defined in tokenizer_config.json; the tokenizer class is Qwen2Tokenizer and pad/eos token mappings are present in that file. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json
- Tokenization-related numeric configuration: tokenizer_config.json sets model_max_length to 131072 tokens (documented in the tokenizer file); config.json lists max_position_embeddings as 40960—these values are inconsistent across primary files and should be reconciled before relying on a single numeric context limit. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json
- Vocabulary size and key model config fields (vocab_size = 151665, hidden_size = 4096, num_hidden_layers = 36) are specified in config.json and inform tokenization and model I/O shapes. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

### Pre-submit validation

- Evidence gap: the primary upstream files do not provide an explicit end-to-end input validation checklist (for example, maximum input character length vs token length mapping, disallowed characters, or required normalization); the tokenizer_config.json and config.json were checked but do not supply a full input-validation contract. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B

### Task-specific formatting

- Evidence gap: no explicit upstream prompt templates, pooling, or normalization instructions for embedding tasks are provided in the located model files and model page; implementers must apply their own pooling/normalization consistent with downstream evaluation. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

## Output interpretation

### Outputs

- The upstream checkpoint emits dense embedding vectors; the embedding dimensionality for the 8B embedding model is reported as 4096 in the model page and in config.json (hidden_size 4096). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

### Interpretation

- Evidence gap: primary upstream sources do not provide explicit numerical calibration guidance for interpreting raw embedding similarity scores (e.g., cosine thresholds or normalized score ranges); no calibration tables or example thresholds were located in the reviewed files. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

### Post-inference validation

- Evidence gap: there is no documented post-inference validation or calibration procedure in the located primary materials (no explicit tests, sanity checks, or recommended downstream validation steps were found in the model page or config files). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json

## Public benchmarks

### Embedding / retrieval (upstream reported numeric table)

- Dataset/split: not reported (table columns unlabeled in located commit) / not reported
- Metric/value: unspecified table metric column (numeric value reported in commit table) / 70.58 (`higher-is-better`)
- Model scope: Qwen3-Embedding-8B (values appear in a Hugging Face commit table associated with the Qwen repo)
- Conditions: not reported (commit table does not label protocol or dataset/split mapping)
- Source: https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566
- Locator: Hugging Face commit db0a90a6c240a32b407e262e44790b7da31d6566 -> 'Benchmarks' table (first numeric column shows 70.58 for Qwen3-Embedding-8B)
- Caveat: The located table shows numeric columns but does not label which dataset or split each column corresponds to; dataset/split/protocol mapping is not present in the located commit table.

### Embedding / retrieval (upstream reported numeric table alternative column)

- Dataset/split: not reported (table columns unlabeled in located commit) / not reported
- Metric/value: unspecified table metric column (numeric value reported in commit table) / 75.22 (`higher-is-better`)
- Model scope: Qwen3-Embedding-8B (values appear in a Hugging Face commit table associated with the Qwen repo or related summary)
- Conditions: not reported (commit table does not label protocol or dataset/split mapping)
- Source: https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566
- Locator: Hugging Face commit db0a90a6c240a32b407e262e44790b7da31d6566 -> 'Benchmarks' table (additional numeric columns shown; table columns are unlabeled in the located commit)
- Caveat: The located table presents multiple numeric columns but lacks explicit dataset/split labels or a mapping from column to dataset; therefore the dataset and metric name for the numeric values cannot be confirmed from the primary locator.

## Comparisons

### https://huggingface.co/Alibaba-NLP/gte-modernbert-base-tei-cuda-1-9 — `insufficient-evidence`

- Task: Embedding / Retrieval
- Criteria: direct, protocol-matched checkpoint-to-checkpoint benchmark comparison (identical dataset/split/metric and evaluation protocol)
- Rationale: The located upstream materials for Qwen3-Embedding-8B contain a numeric benchmarks table (commit) but do not provide labeled dataset/split mapping or a protocol that matches the alternative's public page; no protocol-matched head-to-head numbers are present in the located Qwen commit or model page to support a direct comparison.
- Comparison conditions: No protocol mapping or dataset/split labels present in the Qwen commit table; alternative model page not provided among the located primary sources for cross-checking.
- Evidence: https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566, https://huggingface.co/Qwen/Qwen3-Embedding-8B

### https://huggingface.co/BAAI/bge-base-en-v1.5 — `insufficient-evidence`

- Task: Embedding / Retrieval
- Criteria: direct, protocol-matched checkpoint-to-checkpoint benchmark comparison (identical dataset/split/metric and evaluation protocol)
- Rationale: The located Qwen upstream materials do not include labeled dataset/split mapping for the numeric table; without explicit protocol matching and the alternative's canonical benchmark numbers in the provided evidence set, a protocol-matched comparison is not supported by the located primary sources.
- Comparison conditions: No protocol mapping or dataset/split labels present in the Qwen commit table; alternative model page not present among the located primary sources in this dossier.
- Evidence: https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566, https://huggingface.co/Qwen/Qwen3-Embedding-8B

## Limitations and safety

### Limitations

- Evidence gap: the primary upstream materials reviewed do not contain an explicit statement of training-data licenses or per-dataset licensing (for example, no clear primary-source statement that MS MARCO or other downstream fine-tuning datasets were used or constrained under a non-commercial license was found in the model page, config.json, tokenizer_config.json, or LICENSE file). Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/LICENSE
- Configuration inconsistency: positional/context-length values differ across primary files (tokenizer_config.json model_max_length = 131072 vs config.json max_position_embeddings = 40960 vs model page statement of 32,000 tokens); this inconsistency is recorded here and requires upstream clarification before assuming a single context-length contract. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-8B

### Safety

- Evidence gap: no explicit safety, privacy, or clinical-use guidance is present in the located primary checkpoint materials; implementers must apply standard data-handling and privacy practices and obtain expert review for sensitive domains. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-8B, https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/LICENSE

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Embedding-8B (Hugging Face model page)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Canonical Hugging Face upstream model page for the Qwen3-Embedding-8B checkpoint; contains summary, files, and links to model artifacts.
- Scope: Qwen3-Embedding-8B
- Supports: checkpoint identity and general embedding usage
- Supports: multilingual support claim
- Supports: high-level model description

### Qwen3-Embedding-8B tokenizer_config.json (Hugging Face file blob)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Canonical tokenizer configuration file for the Qwen3-Embedding-8B HF model repo; contains tokenizer class, special-token IDs, and model_max_length.
- Scope: Qwen3-Embedding-8B
- Supports: tokenizer class (Qwen2Tokenizer)
- Supports: special-token ID mappings
- Supports: model_max_length value

### Qwen3-Embedding-8B config.json (Hugging Face file blob)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Canonical model configuration file containing architecture fields, hidden_size, vocab_size, num_hidden_layers, and max_position_embeddings.
- Scope: Qwen3-Embedding-8B
- Supports: hidden_size = 4096 (embedding dimensionality)
- Supports: vocab_size = 151665
- Supports: num_hidden_layers = 36
- Supports: max_position_embeddings = 40960

### Qwen3-Embedding-8B LICENSE (Hugging Face file blob)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/LICENSE
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Canonical license file attached to the upstream model repository indicating the model-weight license.
- Scope: Qwen3-Embedding-8B
- Supports: model-weight license: Apache-2.0

### Qwen3-VL-Embedding-8B commit showing benchmark table (Hugging Face commit blob)

- URL: https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Hugging Face commit blob in the Qwen model repository that contains a numeric benchmarks table where numeric results for the 8B embedding checkpoint are shown.
- Scope: Qwen3-Embedding-8B (benchmarks table shown in commit)
- Supports: numeric benchmark columns for Qwen3-Embedding-8B in a repository commit table

### Qwen3-Embedding-8B commit showing configuration notes (Hugging Face commit blob)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-8B/commit/22e872b8258e3891cf33cac5e39e664a55a89de3
- Publisher: Qwen / Hugging Face
- Type: `model-card`
- Primary because: Hugging Face commit blob that documents configuration values referenced in the model repository (context length statements and embedding-dimension support).
- Scope: Qwen3-Embedding-8B
- Supports: context-length statement and embedding-dimension notes in the upstream commit

## Evidence gaps

- Evidence gap: No explicit primary-source statement of training-data licensing or per-dataset license (for example, MS MARCO non-commercial fine-tuning) was found in the upstream model page, config.json, tokenizer_config.json, or LICENSE file at the listed locators: https://huggingface.co/Qwen/Qwen3-Embedding-8B , https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/config.json , https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/b38b5852de4cd88ace019df596e689bad2de3fe7/tokenizer_config.json , https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/LICENSE
- Evidence gap: The numeric benchmark table located in the commit blob at https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B/commit/db0a90a6c240a32b407e262e44790b7da31d6566 contains unlabeled numeric columns; the mapping from table column to dataset name, dataset split, metric name, and exact protocol is not present at that locator.
- Evidence gap: No explicit upstream guidance on embedding score calibration, recommended pooling/normalization, or example thresholds was found in the inspected primary files (model page and config files at the provided locators).
- Evidence gap: The upstream materials contain conflicting context/position-length values (tokenizer_config.json model_max_length = 131072 vs config.json max_position_embeddings = 40960 vs model-page statement of 32,000 tokens); the authoritative single context-length contract is not present at the located primary URLs.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 44 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: unexpected property interpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: missing required property interpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation: $.outputInterpretation: missing required property validation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12]: $.sources[12]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13]: $.sources[13]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14]: $.sources[14]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15]: $.sources[15]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16]: $.sources[16]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17]: $.sources[17]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18]: $.sources[18]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19]: $.sources[19]: missing required property primaryReason Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3] uses unapproved repository owner 'furiosa-ai' for this exact model scope: $.sources[3] uses unapproved repository owner 'furiosa-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary host docs.vllm.ai: $.sources[5] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses forbidden secondary URL https: $.sources[6] uses forbidden secondary URL https://huggingface.co/Qwen/Qwen3-Embedding-8B/discussions/16/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary host ollama.com: $.sources[10] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://qwen.ai/blog?id=qwen3-vl-embedding Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary host medium.com: $.sources[13] uses forbidden secondary host medium.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'redhatai' for this exact model scope: $.sources[18] uses unapproved repository owner 'redhatai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-modernbert-base-tei-cuda-1-9 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-base-en-v1.5 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[1].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
