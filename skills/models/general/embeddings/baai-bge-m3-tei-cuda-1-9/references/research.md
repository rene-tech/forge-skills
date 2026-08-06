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

- Research key: `huggingface-co-baai-bge-m3-2eda4773a3`
- Independent audit: `revised`
- Researched: `2026-07-23T23:43:01.540075+00:00`

Using only the canonical primary sources (Hugging Face model page, the repository blobs and commit pages it exposes, the tokenizer blobs referenced there, and the canonical arXiv preprint), I confirm: the HF config.json declares an XLM-Roberta architecture (model_type="xlm-roberta") with hidden_size=1024, num_hidden_layers=24, num_attention_heads=16, intermediate_size=4096, max_position_embeddings=8194, and torch_dtype="float32" (config.json). The tokenizer_config.json declares tokenizer_class="XLMRobertaTokenizer", model_max_length=8192, and special tokens (bos/eos/pad/unk/mask). The README and model page document embedding-retrieval usage with dense, sparse, and ColBERT-style components and list retrieval score arrays. The repository commit history includes commits that add or remove weight/ONNX artifacts (commits recorded in the repository commit pages). Missing from these canonical primary sources are an explicit canonical parameter-count for the upstream checkpoint, an explicit model-weight or code license file, explicit tokenizer runtime-normalization/OOV/truncation semantics, and numeric benchmark tables that tie the presented retrieval scores to named datasets/splits/metric rows in the paper or model card. All claims below are individually either supported by exact-file locators or explicitly marked as evidence gaps citing the exact primary URLs and paths I inspected.

## Identity

- Upstream name: BAAI/bge-m3
- Checkpoint/version: BAAI/bge-m3
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: XLMRobertaModel; model_type="xlm-roberta"; hidden_size=1024; num_hidden_layers=24; num_attention_heads=16; intermediate_size=4096; max_position_embeddings=8194; torch_dtype="float32" (values from config.json)
- License: not reported
- Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/commits/be9f7f99731dba86ab44550821489908ef3b4baa, https://huggingface.co/BAAI/bge-m3/commits/694b61558aea4ae2512ed8d0e189d5cf8adc2259, https://arxiv.org/abs/2402.03216

## Selection

### Recommended

- **Multilingual dense retrieval (semantic search / vector retrieval)** — Model page and README demonstrate embedding/retrieval usage and show dense retrieval scores; config.json shows hidden_size=1024 which corresponds to the dense vector dimensionality.
  Scope: BAAI/bge-m3 (upstream checkpoint)
  Evidence: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3/blob/main/config.json
- **Hybrid retrieval combining dense + sparse lexical scores** — README and model page show dense and sparse components and list retrieval scores for sparse, dense, and combined sparse+dense.
  Scope: BAAI/bge-m3 (upstream checkpoint)
  Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- **ColBERT-style multi-vector retrieval (multi-vector outputs)** — README and model page indicate ColBERT component outputs and list colbert retrieval scores; examples in README demonstrate 'colbert' in returned scoring dictionaries.
  Scope: BAAI/bge-m3 (upstream checkpoint)
  Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- **Reranking within retrieval pipelines (using reranker checkpoints when required)** — Model card and README recommend hybrid retrieval plus reranking as the recommended retrieval pipeline.
  Scope: BAAI/bge-m3 (upstream checkpoint); separate reranker checkpoints are distinct artifacts
  Evidence: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

### Conditional

- **Long-document retrieval and RAG up to the declared token bound** — tokenizer_config.json sets model_max_length=8192 and config.json sets max_position_embeddings=8194; precise truncation/stride/batching semantics are not documented in the primary blobs so callers must validate tokenized length and implement chunking/aggregation.
  Scope: BAAI/bge-m3 (upstream checkpoint)
  Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3
- **Using use_fp16 to speed encoding** — config.json records torch_dtype="float32" while README includes an example that sets use_fp16=True; the primary sources do not state a single authoritative runtime default dtype, so runtime FP16 behavior must be validated by the caller/serving layer.
  Scope: BAAI/bge-m3 (upstream checkpoint) when invoked with use_fp16 set in client code or a wrapper
  Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

### Avoid

- **Using BAAI/bge-m3 as a standalone generative language model for text generation / LM tasks** — No primary-file evidence documents a generation head, logits/head weights, or a generation/text-LM API for this checkpoint; the provided blobs and README present the model as an embedding/retrieval model.
  Scope: BAAI/bge-m3 (upstream checkpoint)
  Evidence: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

## Input preparation

### Semantic inputs

- Text input (list of strings) is the accepted input format for embedding calls and examples in the README and model page. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- Model is documented as multilingual in the model page and README. Sources: https://huggingface.co/BAAI/bge-m3, https://arxiv.org/abs/2402.03216

### Accepted formats

- List of strings / text sequences as shown in README encode examples and model page. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- Declared tokenizer model_max_length is 8192 (tokenizer_config.json) and config.json lists max_position_embeddings=8194; these are the documented numeric bounds present in repository blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/config.json

### Preprocessing

- Tokenizer class is declared as XLMRobertaTokenizer in tokenizer_config.json; tokenizer special tokens (bos/cls/eos/pad/unk/mask) are declared in tokenizer_config.json. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json
- tokenizer.json artifact is present in the repository blobs; .gitattributes marks tokenizer.json as an LFS pointer and a commit added tokenizer.json to the repo. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer.json, https://huggingface.co/BAAI/bge-m3/blob/main/.gitattributes, https://huggingface.co/BAAI/bge-m3/commit/3069def033ce91d907258f9a830e442610dbfe0b
- Evidence gap: canonical tokenizer runtime behaviors (Unicode normalization, OOV handling, whitespace/punctuation normalization, sentence-splitting rules) are not documented in the checked primary blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer.json, https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

### Pre-submit validation

- Callers should validate tokenized length against model_max_length because precise truncation/stride/batching semantics are not specified in the primary blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/config.json
- Evidence gap: No explicit upstream rules for invalid inputs (e.g., empty strings, binary payloads) were found in the checked primary blobs; client-side validation is required. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3

### Task-specific formatting

- README examples call model.encode with text-only inputs and show returned dense/sparse/colbert components; there are no special prompt templates required for embedding usage in the checked blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3

## Output interpretation

### Outputs

- Dense embedding vectors are 1024-dimensional per hidden_size=1024 in config.json; README and model page present dense embedding usage. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- README demonstrates returning a 'sparse' lexical component and shows examples of computing lexical matching scores. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3
- README demonstrates optional ColBERT-style multi-vector outputs and shows 'colbert' component in returned scoring dictionaries. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3

### Interpretation

- Evidence gap: No explicit primary-blob statement that embeddings returned are normalized by default was found in the checked README, config.json, tokenizer blobs, or model page. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3
- The README presents combined scoring components (dense/sparse/colbert) as returned parts of scoring dictionaries; exact downstream interpretation and thresholds require tuning. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md

### Post-inference validation

- No upstream calibration, confidence intervals, or numeric thresholds for decision-making are provided in the checked primary sources; downstream validation on labeled data is required. Sources: https://huggingface.co/BAAI/bge-m3, https://arxiv.org/abs/2402.03216, https://huggingface.co/BAAI/bge-m3/blob/main/README.md
- If using hybrid weighted scoring, tune component weights on validation data; the README provides component outputs but no universal thresholds in the checked blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Task-level numeric comparison
- Criteria: No named dataset/split/metric table rows in the checked primary sources to support direct, protocol-matched comparisons for retrieval benchmarks.
- Rationale: The model page lists numeric arrays but does not identify dataset names, splits, or metric labels in the checked primary blobs or the arXiv preprint; therefore direct comparisons to other checkpoints cannot be validated from these primary sources alone.
- Comparison conditions: I inspected https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, and https://arxiv.org/abs/2402.03216 and found no comparable table rows.
- Evidence: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://arxiv.org/abs/2402.03216

### insufficient-evidence — `insufficient-evidence`

- Task: Family-level benchmark attribution
- Criteria: Paper-level family benchmarks (if present in the arXiv preprint) are not explicitly attributed in the checked primary blobs to this exact upstream checkpoint without noting downstream heads or evaluation scripts; therefore benchmarks cannot be attributed directly to the checkpoint without additional primary evidence.
- Rationale: I inspected the arXiv preprint and the model page but did not find checkpoint-matched numeric tables tying family-level results to this exact upstream checkpoint in the checked locations.
- Comparison conditions: Checked https://arxiv.org/abs/2402.03216 and https://huggingface.co/BAAI/bge-m3/blob/main/README.md for explicit per-checkpoint tables; none were present in the checked primary locations.
- Evidence: https://arxiv.org/abs/2402.03216, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

## Limitations and safety

### Limitations

- Evidence gap: No canonical parameter-count (total number of parameters) for this exact upstream checkpoint was found in the checked primary Hugging Face blobs or the arXiv preprint. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://arxiv.org/abs/2402.03216, https://huggingface.co/BAAI/bge-m3
- Evidence gap: No model-weight license file or explicit license text for model weights or code was found in the checked primary blobs; identity.license is not reported from the primary sources. Sources: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://arxiv.org/abs/2402.03216
- Repository history shows commits that add and remove model artifacts (ONNX uploads, deletion of model.safetensors, addition of pytorch_model.bin) — callers must verify exact files present at the revision they intend to use. Sources: https://huggingface.co/BAAI/bge-m3/commits/be9f7f99731dba86ab44550821489908ef3b4baa, https://huggingface.co/BAAI/bge-m3/commit/6a3fd5fa10d7c4e4fabeace29e36b2bfa76d45d5, https://huggingface.co/BAAI/bge-m3/commit/3069def033ce91d907258f9a830e442610dbfe0b
- Evidence gap: Numeric benchmark tables with dataset names, splits, metric names, and per-checkpoint numeric values for standard retrieval benchmarks are not present in the checked primary sources; numeric benchmark claims cannot be recorded without those primary entries. Sources: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://arxiv.org/abs/2402.03216
- Evidence gap: Tokenizer/full preprocessing behavior necessary for strict comparability (detailed OOV handling, Unicode normalization, whitespace/punctuation rules, truncation/stride semantics) is not specified in the checked primary blobs. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md

### Safety

- Evidence gap: No checkpoint-specific PHI, clinical suitability, regulated-use, or data-retention statements were found in the checked primary Hugging Face blobs or the arXiv preprint; expert review is required for clinical deployments. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3, https://arxiv.org/abs/2402.03216
- Evidence gap: No checkpoint-specific upstream safety mitigations or human-review mandates are documented in the checked primary blobs; implementers must apply standard organizational safety review processes. Sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3, https://arxiv.org/abs/2402.03216

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card — BAAI/bge-m3

- URL: https://huggingface.co/BAAI/bge-m3
- Publisher: BAAI / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page and model card for the checkpoint 'BAAI/bge-m3'.
- Scope: BAAI/bge-m3 (upstream checkpoint)
- Supports: model described as embedding/retrieval model
- Supports: lists numeric retrieval score arrays (colbert, sparse, dense, hybrid combinations)
- Supports: documents recommended hybrid retrieval plus reranking pipeline

### Hugging Face model config.json for BGE-M3 (main blob)

- URL: https://huggingface.co/BAAI/bge-m3/blob/main/config.json
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Repository config.json blob contains architecture hyperparameters and dtype declarations.
- Scope: BAAI/bge-m3 config.json (main blob)
- Supports: architecture: XLMRobertaModel; model_type='xlm-roberta'
- Supports: hidden_size=1024
- Supports: num_hidden_layers=24
- Supports: num_attention_heads=16
- Supports: intermediate_size=4096
- Supports: max_position_embeddings=8194
- Supports: torch_dtype="float32"

### Hugging Face tokenizer_config.json for BGE-M3 (main blob)

- URL: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Repository tokenizer_config.json blob declares tokenizer class, special tokens, and model_max_length.
- Scope: BAAI/bge-m3 tokenizer_config.json (main blob)
- Supports: tokenizer_class='XLMRobertaTokenizer'
- Supports: model_max_length=8192
- Supports: special tokens declarations (bos/eos/pad/unk/mask)

### BGE-M3 README (Hugging Face repository blob)

- URL: https://huggingface.co/BAAI/bge-m3/blob/main/README.md
- Publisher: BAAI / Hugging Face
- Type: `official-documentation`
- Primary because: Repository README demonstrates API usage, example encode calls, and example returned outputs (dense/sparse/colbert) and shows an example use_fp16 option.
- Scope: BAAI/bge-m3 README (main blob)
- Supports: example model.encode usage returning dense/sparse/colbert components
- Supports: example setting use_fp16=True in examples
- Supports: compute_lexical_matching_score examples and demonstration of returned scoring dict keys

### Hugging Face tokenizer.json blob (tokenizer artifact pointer)

- URL: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer.json
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Repository tokenizer artifact blob present (tokenization data/behaviour stored as blob); blob is present and referenced by .gitattributes.
- Scope: BAAI/bge-m3 tokenizer.json (main blob)
- Supports: presence of tokenizer.json artifact (tokenization data/behaviour)

### Hugging Face .gitattributes (marks tokenizer.json as LFS pointer)

- URL: https://huggingface.co/BAAI/bge-m3/blob/main/.gitattributes
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: .gitattributes marks tokenizer.json as a Git LFS pointer, confirming tokenizer.json is stored as an LFS artifact.
- Scope: BAAI/bge-m3 .gitattributes (main blob)
- Supports: tokenizer.json is stored via Git LFS pointer

### Hugging Face commit listing (commits/main)

- URL: https://huggingface.co/BAAI/bge-m3/commits/main
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Commit listing shows repository activity and SHAs referencing file additions and README updates.
- Scope: BAAI/bge-m3 commit listing (main)
- Supports: multiple README updates and other commits in repository history

### Hugging Face commit (SHA 694b61558aea4ae2512ed8d0e189d5cf8adc2259) view

- URL: https://huggingface.co/BAAI/bge-m3/commits/694b61558aea4ae2512ed8d0e189d5cf8adc2259
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Commit view used to validate specific README/config/tokenizer uploads in history.
- Scope: BAAI/bge-m3 commit 694b61558... (commit view)
- Supports: commit that updated README.md; records of commits that updated config.json and uploaded tokenizer.json

### Hugging Face commit group (be9f7f99731dba86ab44550821489908ef3b4baa) view

- URL: https://huggingface.co/BAAI/bge-m3/commits/be9f7f99731dba86ab44550821489908ef3b4baa
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Commit view documents additions/deletions: MIRACL evaluation update, ONNX addition, deletion of model.safetensors, uploads of pytorch_model.bin in history.
- Scope: BAAI/bge-m3 commit group (be9f7f9...)
- Supports: commit that updated MIRACL evaluation results
- Supports: commit that added ONNX file(s)
- Supports: commit that deleted model.safetensors
- Supports: commit that uploaded pytorch_model.bin under a directory

### Hugging Face commit adding tokenizer.json (commit view 3069def033ce91d907258f9a830e442610dbfe0b)

- URL: https://huggingface.co/BAAI/bge-m3/commit/3069def033ce91d907258f9a830e442610dbfe0b
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Commit page records the upload of tokenizer.json to the repository.
- Scope: BAAI/bge-m3 commit 3069def (tokenizer.json added)
- Supports: tokenizer.json upload event

### Hugging Face commit adding ONNX files (commit view 6a3fd5fa10d7c4e4fabeace29e36b2bfa76d45d5)

- URL: https://huggingface.co/BAAI/bge-m3/commit/6a3fd5fa10d7c4e4fabeace29e36b2bfa76d45d5
- Publisher: BAAI / Hugging Face
- Type: `repository`
- Primary because: Commit page records addition of ONNX model files with sizes and token decoder details.
- Scope: BAAI/bge-m3 commit 6a3fd5f (ONNX files added)
- Supports: ONNX files added to repository; token decoder special token definitions recorded

### Hugging Face README blob at specific revision (blob/694b61558.../README.md)

- URL: https://huggingface.co/BAAI/bge-m3/blob/694b61558aea4ae2512ed8d0e189d5cf8adc2259/README.md
- Publisher: BAAI / Hugging Face
- Type: `official-documentation`
- Primary because: Alternate README revision used to corroborate example outputs and API demonstrations.
- Scope: BAAI/bge-m3 README (specific revision blob)
- Supports: demonstrates model.encode returning dense/sparse/ColBERT vectors
- Supports: shows compute_score returning dict with 'colbert', 'sparse', 'dense' keys

### arXiv: M3-Embedding paper (BGE-M3 paper)

- URL: https://arxiv.org/abs/2402.03216
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical preprint describing the M3-Embedding approach; included for family/method context.
- Scope: M3-Embedding / BGE-M3 paper (canonical preprint)
- Supports: paper title and authorship for M3-Embedding
- Supports: context for the model family and methodological claims (no per-checkpoint numeric benchmark tables were found in the checked locations)

## Evidence gaps

- Evidence gap: No canonical parameter-count for the exact upstream checkpoint was found in the inspected primary sources: https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://arxiv.org/abs/2402.03216, https://huggingface.co/BAAI/bge-m3
- Evidence gap: No explicit model-weight license file or model-weight license text was found in the inspected primary sources: https://huggingface.co/BAAI/bge-m3, https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://arxiv.org/abs/2402.03216
- Evidence gap: Tokenizer runtime behaviors necessary for strict comparability (Unicode normalization, OOV handling, whitespace/punctuation normalization, sentence-splitting rules) are not documented in the checked blobs: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer.json, https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md
- Evidence gap: Precise truncation/stride/batching semantics when inputs exceed model_max_length are not specified in the checked primary blobs: https://huggingface.co/BAAI/bge-m3/blob/main/tokenizer_config.json, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3/blob/main/README.md
- Evidence gap: No numeric benchmark tables tying the presented retrieval score arrays to named datasets/splits/metric rows were found in the checked primary sources: https://huggingface.co/BAAI/bge-m3 (model page main), https://huggingface.co/BAAI/bge-m3/blob/main/README.md (README blob), https://arxiv.org/abs/2402.03216 (paper main).
- Evidence gap: No explicit upstream statement that embeddings are normalized by default was found in the checked primary blobs: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3/blob/main/config.json, https://huggingface.co/BAAI/bge-m3
- Evidence gap: No checkpoint-specific PHI/clinical/regulatory/data-retention statements were found in the checked primary sources: https://huggingface.co/BAAI/bge-m3/blob/main/README.md, https://huggingface.co/BAAI/bge-m3, https://arxiv.org/abs/2402.03216

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'flagopen' for this exact model scope: $.sources[11] uses unapproved repository owner 'flagopen' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary host ollama.com: $.sources[12] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.comparisons_evidence_removed: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.removedSecondaryUrls: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[1]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
