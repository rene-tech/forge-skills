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

- Research key: `huggingface-co-qwen-qwen3-embedding-4b-5fc440f4b7`
- Independent audit: `revised`
- Researched: `2026-08-06T10:16:49.925642+00:00`

Primary publisher-owned artifacts (Hugging Face model repository files and the Qwen3 embedding GitHub repo) identify Qwen3-Embedding-4B as the 4B-parameter member of the Qwen3 embedding series. The checkpoint config.json lists architectures:["Qwen3ForCausalLM"], model_type "qwen3", hidden_size 2560, num_hidden_layers 36, num_attention_heads 32, intermediate_size 9728, max_position_embeddings 40960, hidden_act "silu", and torch_dtype "bfloat16" (see config.json). The Hugging Face README for the checkpoint documents MTEB-style benchmark rows (checkpoint-scoped numeric results) and describes the series as a text-only embedding model with default embedding dimensionality 2560 and support for variable embedding dimensions (MRL) per family/discussion materials. The repository listing for the checkpoint contains tokenizer artifacts (tokenizer.model, tokenizer.json, tokenizer_config.json, special_tokens_map.json, vocab.json) per the repo tree listing. Family-level docs (Qwen3 family page) and the checkpoint config.json present differing context-length indicators (family page documents native 32,768-token support while config.json contains max_position_embeddings=40960); both primary locators were checked and the discrepancy is unresolved by the checked primary files. Publisher-authored checkpoint-scoped separation of model-weight versus code license text, canonical exporter/ONNX parity guidance tied specifically to this checkpoint, and explicit tokenizer-specific truncation/padding semantics or per-embedding calibration guidance were not found in the checked publisher-owned checkpoint artifacts; those are reported as targeted evidence gaps below.

## Identity

- Upstream name: Qwen3 Embedding
- Checkpoint/version: Qwen3-Embedding-4B
- Immutable revision: not reported
- Parameter scale: 4B
- Architecture/head: Qwen3ForCausalLM
- License: not reported
- Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://github.com/QwenLM/Qwen3-Embedding, https://huggingface.co/Qwen/Qwen3-4B

## Selection

### Recommended

- **Multilingual semantic search / text retrieval** — The Hugging Face model page and the checkpoint README present Qwen3-Embedding-4B as a text embedding model intended for retrieval and multilingual use; README includes retrieval-oriented examples and MTEB-style benchmark results for the checkpoint.
  Scope: Qwen3-Embedding-4B (checkpoint-level model card / README and config.json)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- **Embedding-based code search / code retrieval (programming-language text)** — Primary checkpoint-level materials list natural-language and programming-language text among intended inputs and retrieval-oriented examples applicable to code contexts.
  Scope: Qwen3-Embedding-4B (checkpoint-level model card / README)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- **Text clustering and unsupervised organization** — The checkpoint is published as a text embedding model intended for similarity, retrieval, clustering, and related downstream uses as shown on the Hugging Face model page and README benchmark summaries.
  Scope: Qwen3-Embedding-4B (checkpoint-level model card / README)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

### Conditional

- **Instruction-conditioned / instruction-aware embeddings (MRL)** — Treat MRL/instruction-conditioned usage as family-level functionality: validate downstream for this exact checkpoint and serving stack prior to production. The checkpoint README and family-level repository document MRL/instruction-aware capabilities at the family/discussion level; the checkpoint repo provides example usage but does not publish a canonical, benchmarked per-dimension parity table tied specifically to the checkpoint in the checked artifacts.
  Scope: Qwen3 embedding family / checkpoint README and Qwen3 embedding family repo (family-level MRL documentation plus checkpoint README examples)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md, https://github.com/QwenLM/Qwen3-Embedding
- **Custom-dimension (Matryoshka) embeddings (reduced output dimensions)** — Publisher materials document selectable dimensions (MRL) at family/discussion level but do not publish per-dimension parity benchmarks or a canonical checkpoint-scoped protocol for reduced-dimension selection in the checked checkpoint artifacts; downstream performance and calibration validation required.
  Scope: Qwen3 embedding family / checkpoint README (family-level MRL docs mentioned alongside checkpoint README)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md, https://github.com/QwenLM/Qwen3-Embedding
- **Long-context serving with rope-scaling variants** — Resolve the context-length discrepancy and validate runtime rope-scaling flags and effective context limits for the chosen serving stack. The checkpoint config.json reports max_position_embeddings=40960 while the Qwen3 family page documents native 32,768-token support and family-level YaRN RoPE scaling examples; both primary locators were checked and do not resolve the discrepancy.
  Scope: Qwen3 family documentation and checkpoint config.json (family-level rope-scaling docs plus checkpoint config; runtime validation required)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B

### Avoid

- **Direct multimodal (image/video) inputs to this checkpoint** — The checkpoint README and model card describe the Qwen3-Embedding series as a text-only embedding model; multimodal/VL embedding variants are documented at the family/repository level as separate variants, not as this exact checkpoint.
  Scope: Qwen3-Embedding-4B (embedding head, text-only checkpoint)
  Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md, https://github.com/QwenLM/Qwen3-Embedding

## Input preparation

### Semantic inputs

- Plain text inputs (natural language) and programming-language text are intended input modalities for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

### Accepted formats

- Text inputs (UTF-8 strings) are the accepted input format for the embedding checkpoint; README examples use plain text payloads. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

### Preprocessing

- The checkpoint repository tree lists tokenizer artifacts (tokenizer.model, tokenizer.json, tokenizer_config.json, special_tokens_map.json, vocab.json) in the repo root. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main
- Evidence gap: Tokenizer-specific normalization, exact tokenization rules, and canonical truncation/padding semantics required for precise replication are not specified in the checked checkpoint files; implement tokenizer validation tests and confirm truncation/padding semantics before production deployment. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json

### Pre-submit validation

- Check input length against upstream configuration: config.json records max_position_embeddings=40960 while the family page documents native 32,768-token context; this discrepancy is unresolved in the checked primary sources and must be validated for the intended runtime. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B
- Evidence gap: The checkpoint repository does not publish exhaustive tokenizer-specific truncation/padding edge-case rules in the checked files; perform tokenization edge-case tests prior to deployment. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json

### Task-specific formatting

- README examples demonstrate optional instruction-prefixed queries (e.g., an "Instruct:" line) for improved retrieval quality, but no single prescriptive benchmarked prompt template tied to a full checkpoint-level evaluation is published in the checked checkpoint README. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- Evidence gap: Canonical runtime flags or TEI/vLLM serving templates tied to this exact checkpoint are not published in the checked checkpoint artifacts; consult family-level docs and validate runtime behaviour on the target serving stack. Sources: https://github.com/QwenLM/Qwen3-Embedding, https://huggingface.co/Qwen/Qwen3-Embedding-4B

## Output interpretation

### Outputs

- A numeric dense embedding vector; default embedding dimensionality is 2560 as implied by hidden_size in config.json. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

### Interpretation

- Embeddings are unitless vectors intended for similarity, retrieval, clustering, and related tasks; primary sources do not publish per-embedding probabilistic calibration or confidence units for this checkpoint. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

### Post-inference validation

- Evidence gap: Primary sources do not provide standardized per-embedding calibration or confidence metrics for Qwen3-Embedding-4B; downstream validation is required for safety-critical or calibrated-score use cases. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json

## Public benchmarks

### Embedding evaluation (MTEB, English aggregated)

- Dataset/split: MTEB (English) / not reported
- Metric/value: Mean(Task) / 72.27 (`higher-is-better`)
- Model scope: Qwen3-Embedding-4B checkpoint (as reported in the checkpoint README)
- Conditions: Protocol details (dataset split, preprocessing, pooling/aggregation, and explicit evaluation script) are not reported in the checked README table; replicability requires those details.
- Source: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- Locator: README MTEB benchmark table
- Caveat: The README presents numeric MTEB-style rows but the checked artifact does not publish dataset split, preprocessing, pooling, or evaluation script details required for strict protocol-identical comparisons.

### Embedding evaluation (MTEB, English - Retrieval subset)

- Dataset/split: MTEB Retrieval (English) / not reported
- Metric/value: Retrieval / 77.03 (`higher-is-better`)
- Model scope: Qwen3-Embedding-4B checkpoint (as reported in the checkpoint README)
- Conditions: Pooling/aggregation, exact dataset split, and preprocessing not specified in README; reproducing this number requires the missing protocol details.
- Source: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- Locator: README MTEB benchmark table (Retrieval row)
- Caveat: Benchmark row present in README but lacks the protocol-level details (split, pooling, preprocessing) necessary for direct comparability.

## Comparisons

### Qwen3-Embedding-0.6B — `insufficient-evidence`

- Task: General embedding tasks (family-style comparisons such as MTEB-style retrieval / classification / clustering)
- Criteria: Direct numeric comparison requires identical dataset files/split, preprocessing, pooling/aggregation method, and metric definition; those protocol details are not published in the checked checkpoint README table for both checkpoints.
- Rationale: The checkpoint README includes numeric rows for Qwen3-Embedding-4B and describes the 0.6B family member, but the checked README does not include the complete protocol details required to guarantee protocol-identical numeric comparisons between checkpoints.
- Comparison conditions: Missing dataset split, preprocessing, pooling method, and evaluation script in the checkpoint README table prevent protocol-identical comparison.
- Evidence: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md, https://huggingface.co/Qwen/Qwen3-Embedding-4B

## Limitations and safety

### Limitations

- Evidence gap: Publisher-authored, checkpoint-level model-weight versus code license separation text was not found in the checked publisher-owned checkpoint artifacts (model page, repo tree, or config.json); the checked files do not contain an explicit checkpoint-scoped license file or clarifying license statement. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- Evidence gap: Tokenizer-specific end-to-end preprocessing semantics (exact normalization, tokenization edge cases, truncation/padding rules) are not documented in the checked checkpoint artifacts; the repo lists tokenizer files but does not publish canonical, prescriptive tokenizer behavior for every edge case. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- Evidence gap: Publisher-authored ONNX/export parity documentation and publisher-published parity benchmarks for exported/quantized variants of this exact checkpoint were not found in the checked publisher-owned artifacts; exporter guidance and parity tables tied specifically to this checkpoint are not present in the checked files. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://github.com/QwenLM/Qwen3-Embedding, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- There is an unresolved discrepancy in maximum context length between config.json (max_position_embeddings = 40960) and the Qwen3 family page (documents native 32,768-token context length and family-level YaRN RoPE scaling); both primary locators were checked and the discrepancy remains unresolved in the checked publisher-owned artifacts. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B

### Safety

- Primary sources do not publish model-specific clinical, PHI, or privacy-handling guidance for this embedding checkpoint; treat outputs as research-grade embeddings and obtain expert review prior to safety-critical use. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- Evidence gap: Canonical robustness, calibration, and probabilistic-confidence benchmarks for Qwen3-Embedding-4B are not published in the checked publisher-owned artifacts; validate thoroughly for safety-critical or regulated contexts. Sources: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Qwen3-Embedding-4B model card (Hugging Face)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-4B
- Publisher: Qwen (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model page for the exact Qwen3-Embedding-4B checkpoint; authoritative checkpoint identity, README content, and usage examples are documented here.
- Scope: Qwen3-Embedding-4B checkpoint (model card / repo root)
- Supports: Checkpoint identity and model card content (usage examples, general description).
- Supports: Presence of model card README and links to repo files.

### Qwen3-Embedding-4B config.json (Hugging Face repository file)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- Publisher: Qwen (Hugging Face)
- Type: `repository`
- Primary because: Checkpoint configuration file exposed in the official Hugging Face model repo; authoritative source for architecture and hyperparameters for this checkpoint.
- Scope: Qwen3-Embedding-4B checkpoint (config.json)
- Supports: Architecture field (architectures:["Qwen3ForCausalLM"]) and model_type 'qwen3'.
- Supports: Config fields include hidden_size=2560, num_hidden_layers=36, num_attention_heads=32, intermediate_size=9728, and max_position_embeddings=40960.
- Supports: Additional config fields hidden_act and torch_dtype.

### Qwen3-Embedding-4B README (Hugging Face repository README blob)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md
- Publisher: Qwen (Hugging Face)
- Type: `model-card`
- Primary because: Checkpoint README in the official Hugging Face repository contains publisher-authored benchmark tables, example usage, and descriptive text for the checkpoint.
- Scope: Qwen3-Embedding-4B checkpoint (README content and reported benchmark rows)
- Supports: Describes the series as a text-only embedding model and provides example usage (instruction-prefixed examples).
- Supports: Contains checkpoint-level MTEB-style benchmark rows reported for Qwen3-Embedding-4B.

### Qwen3-Embedding-4B repo tree (Hugging Face repo file listing)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main
- Publisher: Qwen (Hugging Face)
- Type: `repository`
- Primary because: Repository file listing showing the checkpoint files present in the model repo root (tokenizer artifacts and vocab).
- Scope: Qwen3-Embedding-4B checkpoint (repo file listing)
- Supports: Lists tokenizer artifacts such as tokenizer.model, tokenizer.json, tokenizer_config.json, special_tokens_map.json, and vocab.json.

### Qwen3-Embedding-4B vocab.json (Hugging Face repository file)

- URL: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/vocab.json
- Publisher: Qwen (Hugging Face)
- Type: `repository`
- Primary because: Publisher-hosted vocabulary file for the checkpoint available in the model repo root.
- Scope: Qwen3-Embedding-4B checkpoint (vocab file)
- Supports: Presence of vocab.json in the checkpoint repository.

### Qwen3-Embedding family repository (QwenLM GitHub)

- URL: https://github.com/QwenLM/Qwen3-Embedding
- Publisher: QwenLM (GitHub)
- Type: `repository`
- Primary because: Official Qwen3 embedding family GitHub repository maintained by the publisher; contains family-level documentation and code referenced by checkpoint-level materials.
- Scope: Qwen3 embedding family (family-level docs, MRL/instruction-aware notes)
- Supports: Family-level documentation of Matryoshka Representation Learning (MRL) and instruction-aware behavior; family-level artifacts separate multimodal variants from the text-only embedding checkpoint.

### Qwen3 family model page (Hugging Face)

- URL: https://huggingface.co/Qwen/Qwen3-4B
- Publisher: Qwen (Hugging Face)
- Type: `model-card`
- Primary because: Official Qwen3 family page documenting native context length and family-level rope-scaling behavior relevant to interpreting checkpoint context limits.
- Scope: Qwen3 family documentation (context/rope-scaling reference)
- Supports: Documents native 32,768-token support and optional YaRN RoPE scaling to larger contexts (family-level guidance).

## Evidence gaps

- Evidence gap: Publisher-authored, checkpoint-level model-weight versus code license separation text was not found in the checked publisher-owned checkpoint artifacts: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- Evidence gap: Tokenizer-specific truncation/padding semantics and exact normalization/tokenization edge-case rules are not documented in the checked checkpoint artifacts: https://huggingface.co/Qwen/Qwen3-Embedding-4B/tree/main, https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json
- Evidence gap: Publisher-authored ONNX/export parity documentation and exporter parity benchmarks tied specifically to this checkpoint were not found in the checked publisher-owned artifacts: https://huggingface.co/Qwen/Qwen3-Embedding-4B, https://github.com/QwenLM/Qwen3-Embedding
- Evidence gap: The primary config.json (max_position_embeddings = 40960) and the Qwen3 family documentation (native 32,768-token context length and family-level YaRN scaling) present conflicting context-length guidance; both primary locators were checked and do not resolve the discrepancy: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/main/config.json, https://huggingface.co/Qwen/Qwen3-4B
- Evidence gap: The checkpoint README contains benchmark rows (MTEB-style) but does not publish protocol-complete details (dataset split, preprocessing, pooling/aggregation method, and canonical evaluation script) required for strict numeric comparability; checked primary location: https://huggingface.co/Qwen/Qwen3-Embedding-4B/blob/af551aabe3b5e18ade93393f15c5e6d26935ccae/README.md

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 23 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[3] uses forbidden secondary host ollama.com: $.sources[3] uses forbidden secondary host ollama.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5] uses forbidden secondary URL https: $.sources[5] uses forbidden secondary URL https://huggingface.co/Qwen/Qwen3-Embedding-4B/discussions/21 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'shawnw3i' for this exact model scope: $.sources[10] uses unapproved repository owner 'shawnw3i' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses unapproved repository owner 'dengcao' for this exact model scope: $.sources[11] uses unapproved repository owner 'dengcao' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'alibaba-nlp' for this exact model scope: $.sources[12] uses unapproved repository owner 'alibaba-nlp' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses unapproved repository owner 'baai' for this exact model scope: $.sources[13] uses unapproved repository owner 'baai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'baai' for this exact model scope: $.sources[14] uses unapproved repository owner 'baai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses unapproved repository owner 'bylaw' for this exact model scope: $.sources[15] uses unapproved repository owner 'bylaw' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses unapproved repository owner 'ibm-granite' for this exact model scope: $.sources[16] uses unapproved repository owner 'ibm-granite' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses unapproved repository owner 'intfloat' for this exact model scope: $.sources[17] uses unapproved repository owner 'intfloat' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses unapproved repository owner 'mixedbread-ai' for this exact model scope: $.sources[18] uses unapproved repository owner 'mixedbread-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19] uses unapproved repository owner 'nomic-ai' for this exact model scope: $.sources[19] uses unapproved repository owner 'nomic-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21] uses forbidden secondary host ai.azure.com: $.sources[21] uses forbidden secondary host ai.azure.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25] uses unapproved repository owner 'snowflake' for this exact model scope: $.sources[25] uses unapproved repository owner 'snowflake' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26] uses unapproved repository owner 'snowflake' for this exact model scope: $.sources[26] uses unapproved repository owner 'snowflake' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[27] uses unapproved repository owner 'baai' for this exact model scope: $.sources[27] uses unapproved repository owner 'baai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[28] uses unapproved repository owner 'hotchpotch' for this exact model scope: $.sources[28] uses unapproved repository owner 'hotchpotch' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[29] uses unapproved repository owner 'baai' for this exact model scope: $.sources[29] uses unapproved repository owner 'baai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[29] uses forbidden secondary URL https: $.sources[29] uses forbidden secondary URL https://huggingface.co/BAAI/bge-m3/discussions/7 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[30] uses unapproved repository owner 'ibm-granite' for this exact model scope: $.sources[30] uses unapproved repository owner 'ibm-granite' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://arxiv.org/html/2508.21085v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
