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

- Research key: `huggingface-co-baai-bge-reranker-v2-m3-3891d3dadf`
- Independent audit: `revised`
- Researched: `2026-07-23T23:57:27.860071+00:00`

Verified primary repository files show that the checkpoint BAAI/bge-reranker-v2-m3 is configured as a sequence-classification cross-encoder reranker (config.json lists architectures = ["XLMRobertaForSequenceClassification"] and model_type = "xlm-roberta"). The tokenizer_config.json declares tokenizer_class = "XLMRobertaTokenizer" and model_max_length = 8192. config.json declares max_position_embeddings = 8194 and other model hyperparameters (hidden_size=1024, num_hidden_layers=24, num_attention_heads=16, intermediate_size=4096). The repository README documents that the model accepts a question + document pair and outputs a single scalar relevance score that can be mapped to [0,1] via a sigmoid. Primary-source evidence for parameter count, an explicit license text in the upstream repo, training-time maximum sequence length, numeric benchmarks for BioASQ for this exact checkpoint, runtime wrapper/truncation policies, and post-inference calibration procedures were not found in the inspected primary repository files (config.json, tokenizer_config.json, README at the checked locator).

## Identity

- Upstream name: BAAI/bge-reranker-v2-m3
- Checkpoint/version: baai-bge-reranker-v2-m3
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: XLMRobertaForSequenceClassification
- License: not reported
- Evidence: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json

## Selection

### Recommended

- **Reranking top-k retrieval candidates (query, passage pairs) in multilingual retrieval and open-domain QA pipelines** — Upstream README documents that the model accepts a query (question) and a document (passage) and directly outputs a similarity/relevance score; config.json shows a sequence-classification head appropriate for cross-encoder reranking.
  Scope: BAAI/bge-reranker-v2-m3
  Evidence: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

### Conditional

- **Reranking with long combined query+passage inputs subject to tokenizer/model max-length bounds** — Validate that the tokenized combined length of query+passage fits within tokenizer model_max_length (8192) and model positional limits (config.json max_position_embeddings = 8194); perform end-to-end latency and memory testing in target runtime to ensure the combined length is supported in practice.
  Scope: BAAI/bge-reranker-v2-m3
  Evidence: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

### Avoid

- **Using this reranker checkpoint as an embedding model (embedding-model substitute)** — Upstream README and config identify the artifact as a cross-encoder reranker with a sequence-classification head that directly outputs a single scalar relevance score per query–document pair rather than producing fixed vector embeddings for each input.
  Scope: BAAI/bge-reranker-v2-m3
  Evidence: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

## Input preparation

### Semantic inputs

- The model consumes plain-text pairs consisting of a query (question) and a passage/document. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md

### Accepted formats

- Accepted modality: plain text pairs (query, passage) as documented in the repository README. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md

### Preprocessing

- Tokenizer class declared as XLMRobertaTokenizer in tokenizer_config.json. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json
- Tokenizer special tokens declared (bos_token '<s>', cls_token '<s>', eos_token '</s>', pad_token '<pad>', sep_token '</s>', mask_token '<mask>', unk_token '<unk>'). Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json
- Declared tokenizer model_max_length is 8192 (tokenizer_config.json); config.json lists max_position_embeddings = 8194. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

### Pre-submit validation

- Evidence gap: explicit runtime wrapper truncation/concatenation rules, per-field token limits, and canonical input validation checks are not documented in the inspected repository files (no runtime truncation policy or per-field limits present in README, config.json, or tokenizer_config.json). Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json

### Task-specific formatting

- Input ordering expected by the reranker is a query followed by a candidate passage (pair [query, passage]); no upstream prompt template or separator convention beyond tokenizer special tokens is prescribed in the README or config. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

## Output interpretation

### Outputs

- The upstream model produces a single scalar similarity/relevance score for each query–passage pair (sequence-classification output). Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

### Interpretation

- Higher scores indicate greater predicted relevance; the README states the produced score can be mapped to [0,1] using a sigmoid function. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md

### Post-inference validation

- Evidence gap: upstream repository files do not provide explicit post-inference calibration procedures, recommended numeric thresholds, or operating points; downstream users must validate calibration for their tasks. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Reranking on BioASQ / QA reranking tasks
- Criteria: No verifiable numeric, like-for-like benchmark rows for this exact checkpoint were found in the inspected primary repository files; no checkpoint-specific numeric rows are present in the checked README or config files.
- Rationale: The repository README and config identify the model and head but do not publish explicit numeric benchmark rows (dataset split, metric, numeric value) for BioASQ or comparable reranking evaluations for this exact checkpoint at the checked locators.
- Comparison conditions: Checked primary-locator materials do not contain evaluation tables or rows that report dataset, split, metric, value, and explicit checkpoint identifier together; therefore like-for-like comparisons against peers cannot be established from these sources alone.
- Evidence: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json

## Limitations and safety

### Limitations

- Model architecture and declared hyperparameters (from config.json): architectures = ["XLMRobertaForSequenceClassification"]; model_type = "xlm-roberta"; hidden_size = 1024; num_hidden_layers = 24; num_attention_heads = 16; intermediate_size = 4096; max_position_embeddings = 8194. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json
- Declared tokenizer bounds (from tokenizer_config.json): tokenizer_class = "XLMRobertaTokenizer" and model_max_length = 8192; special tokens defined in tokenizer_config.json represent upstream tokenization bounds but do not specify runtime truncation behavior. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json
- Evidence gap: the inspected repository files do not state an explicit training-time maximum sequence length (training truncation length) or provide a full training data composition for this checkpoint at the checked locators. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json

### Safety

- Evidence gap: no explicit upstream privacy, clinical, or dual-use safety disclaimers or operational data-handling rules were present in the inspected primary repository files; apply standard data governance and expert review when using outputs in sensitive domains. Sources: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### README.md (BAAI/bge-reranker-v2-m3) [specific commit blob]

- URL: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md
- Publisher: HuggingFace
- Type: `repository`
- Primary because: Upstream repository README for the exact checkpoint at the checked locator; contains model usage and description statements.
- Scope: BAAI/bge-reranker-v2-m3
- Supports: Describes reranker input as question + document pair
- Supports: States the model outputs a similarity score and that the score can be mapped to [0,1] with a sigmoid
- Supports: Identifies the repository and provides usage instructions

### config.json (BAAI/bge-reranker-v2-m3)

- URL: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/config.json
- Publisher: HuggingFace (repository file)
- Type: `repository`
- Primary because: Model configuration file declaring architecture, model_type, and model hyperparameters for this exact checkpoint.
- Scope: BAAI/bge-reranker-v2-m3
- Supports: architecture: XLMRobertaForSequenceClassification
- Supports: model_type: xlm-roberta
- Supports: hidden_size=1024, num_hidden_layers=24, num_attention_heads=16, intermediate_size=4096
- Supports: max_position_embeddings=8194
- Supports: _name_or_path field value

### tokenizer_config.json (BAAI/bge-reranker-v2-m3)

- URL: https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/main/tokenizer_config.json
- Publisher: HuggingFace (repository file)
- Type: `repository`
- Primary because: Tokenizer configuration file declaring tokenizer class, special tokens, and model_max_length for this exact checkpoint.
- Scope: BAAI/bge-reranker-v2-m3
- Supports: tokenizer_class: XLMRobertaTokenizer
- Supports: model_max_length=8192
- Supports: special tokens declarations (bos_token, eos_token, pad_token, unk_token, mask_token, sep_token, cls_token)

### Exact official starting source declared by Forge

- URL: https://huggingface.co/BAAI/bge-reranker-v2-m3
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: baai-bge-reranker-v2-m3
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No verifiable numeric benchmark row (dataset, split, metric, numeric value) for BioASQ 12b Phase A Batch 1 for this exact checkpoint was found in the inspected primary repository files (checked README at https://huggingface.co/BAAI/bge-reranker-v2-m3/blob/c0abf900d43de6a2652b9acd221bb1b45ab65d6e/README.md).
- Evidence gap: License text for the upstream checkpoint was not found in the inspected repository files (checked README, config.json, tokenizer_config.json at the listed locators).
- Evidence gap: The inspected repository files do not state an explicit training-time maximum sequence length (training truncation length) or full training data composition for this checkpoint (checked README, config.json, tokenizer_config.json).
- Evidence gap: Explicit runtime wrapper behavior, truncation policy, canonical pair concatenation separators, and per-field token limits are not documented in the inspected repository files (checked README, config.json, tokenizer_config.json).
- Evidence gap: No explicit post-inference calibration guidance, recommended numeric thresholds, or operating points are provided in the inspected repository files (checked README, config.json).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 10 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[7]: $.sources[7]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2312.15503 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2312.15503 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/pdf/2312.15503 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/BAAI/bge-reranker-v2-m3: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
