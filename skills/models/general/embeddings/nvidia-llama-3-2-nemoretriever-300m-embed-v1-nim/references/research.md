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

- Research key: `build-nvidia-com-nvidia-llama-3-2-nemoretriever-300m-embed-v1-a557c043fc`
- Independent audit: `revised`
- Researched: `2026-07-23T21:36:57.906812+00:00`

The exact NIM nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) is documented in NVIDIA primary documentation as a Transformer-encoder embedding model (9 layers) producing 2048-dimensional embeddings. The support matrix (1.10.0) lists the model ID nvidia/llama-3.2-nemoretriever-300m-embed-v1, embedding dimension 2048, and parameter counts 307M (excluding embedding) and 569M total. NVIDIA documentation states the model was pruned and distilled from Llama 3.2-nv-embedqa-1b-v1. The NIM is packaged as a NeMo Retriever Text Embedding NIM intended for multilingual retrieval tasks (26 languages listed). Primary NVIDIA sources document inference-time controls (an 'input_type' parameter and passage/query modes) and list model max-token entries that conflict between support-matrix (8192 tokens) and the model-specific inference page (32k tokens). Primary sources do not publish checkpoint-scoped numeric retrieval benchmarks (recall@k, MRR, nDCG) for this exact v1 checkpoint, do not specify tokenizer identity/vocabulary/normalization details for the exact v1 NIM, and do not document embedding post-normalization semantics; those are recorded as evidence gaps and require runtime validation.

## Identity

- Upstream name: Llama 3.2 NeMo Retriever Embedding 300M v1
- Checkpoint/version: nvidia/llama-3.2-nemoretriever-300m-embed-v1
- Immutable revision: not reported
- Parameter scale: 307 million parameters (excluding embeddings); 569 million total parameters
- Architecture/head: Transformer encoder, 9 layers, embedding dimension 2048
- License: NVIDIA Community Model License (model weights/use); NeMo Retriever code license: not reported
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1, https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/NVIDIA-Models-Community-License-2025-04-15-FINAL.pdf, https://nvidia.com/es-la/agreements/enterprise-software/nvidia-community-models-license

## Selection

### Recommended

- **Multilingual dense retrieval and long-document question-answering retrieval** — NVIDIA documents the model and Build.NVIDIA entry as optimized for multilingual and cross-lingual text question-and-answer retrieval and lists evaluation across 26 languages.
  Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) served via the NeMo Retriever Text Embedding NIM
  Evidence: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v1/-
- **Embedding production component for semantic search and RAG pipelines** — NGC catalog and NVIDIA NIM documentation list semantic search and Retrieval-Augmented Generation (RAG) among intended use cases for the Text Embedding NIMs and describe the NIM as a production-ready microservice.
  Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) NIM/NGC container
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v1/-, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

### Conditional

- **Embedding long documents near implementation token limits** — Primary sources contain conflicting token-limit statements (support-matrix 1.10.0 lists max tokens 8192; the model-specific inference page states 32k). Empirically validate truncation/segmentation and confirm which limit applies to your deployed NIM runtime/manifest before using for very long documents.
  Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) NIM
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1-infer
- **Porting workflows that rely on explicit 'input_type' or passage/query mode semantics** — The inference page documents an 'input_type' parameter and passage/query modes; ensure the deployed NIM/NGC container and pipeline expect and expose the same inference contract before migrating workflows that depend on those fields.
  Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 inference API
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

### Avoid

- **Treating this package as a general text-generation (LM) service** — Primary-source NIM documentation and the NeMo Retriever Embedding NIM references describe embedding endpoints and retrieval-oriented inference controls; they do not document generative-text endpoints for this NIM.
  Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) NIM
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

## Input preparation

### Semantic inputs

- Text strings provided to the embeddings endpoint for embedding generation (queries or passages). Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1

### Accepted formats

- Text inputs consumed via the NeMo Retriever Embedding NIM HTTP API; the NeMo Retriever documentation indicates an OpenAI-compatible embeddings API is available for NeMo Retriever embedding NIMs. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/use-the-api-openai.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

### Preprocessing

- Evidence gap: tokenizer identity (name), tokenizer vocabulary file path, tokenization algorithm, and byte/character normalization steps for this exact v1 NIM are not specified in the inspected primary NVIDIA documentation. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- The model produces fixed-length 2048-dimensional embeddings as documented in the support matrix and NIM reference. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Training methodology references: NVIDIA documents typical embedding-model training as bi-encoder/contrastive learning for retrieval tasks (query and passage encoded independently). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1

### Pre-submit validation

- Validate input token lengths in deployment: the support matrix (1.10.0) lists max tokens 8192 for the 300M v1 entry, while the model inference page lists a maximum input length of 32k tokens; reconcile which applies to your deployed runtime and empirically validate truncation/segmentation behavior. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1-infer
- Evidence gap: the inspected primary documentation does not fully specify per-request batching parameter names, request-size limits, or exact truncation/cropping policies for over-length inputs for this exact v1 NIM; validate these behaviors at runtime or via the deployed NIM manifest. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Validate target hardware meets documented platform requirements in the NeMo Retriever support matrix before production deployment. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### Task-specific formatting

- Evidence gap: the inspected primary documentation does not enumerate an exhaustive per-field request contract for POST /v1/embeddings for this exact v1 NIM (specific field names and per-field semantics not fully documented in the checked pages). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

## Output interpretation

### Outputs

- Embedding dimensionality for this NIM is 2048 as stated in the support matrix and NIM reference. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Evidence gap: the exact API response JSON schema fields (e.g., top-level 'object', 'data' array items with 'object','index','embedding', 'model', and 'usage') are not specified with that exact schema in the inspected primary NVIDIA pages for this exact v1 NIM; verify the response shape against the deployed NIM's API reference/manifest at runtime. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

### Interpretation

- Do not assume embeddings are L2-normalized: the inspected primary documentation does not specify L2 normalization or other post-scaling for v1; perform runtime validation before relying on implicit normalization. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Use inference-time 'usage' or runtime telemetry (when available) for operational accounting and token counts per request as documented in NeMo Retriever references. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

### Post-inference validation

- Post-inference checks: verify each returned embedding vector length equals 2048 for the v1 NIM and verify presence of any declared per-item metadata fields in the deployed API contract. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Evidence gap: embedding normalization (e.g., L2) and any scaling applied to vectors are not documented in the inspected primary sources; include explicit normalization and magnitude checks in validation pipelines. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nvidia-llama-3-2-nemoretriever-300m-embed-v2 — `insufficient-evidence`

- Task: embeddings for semantic search / retrieval
- Criteria: No protocol-matched, checkpoint-scoped numeric benchmarks for v1 versus v2 are present in the inspected primary NVIDIA sources; a valid comparison requires matched datasets, splits, metrics, and evaluation protocol explicitly attributed to each exact checkpoint.
- Rationale: Inspected NVIDIA primary documentation documents v1 NIM properties but does not include matched numeric comparisons between v1 and v2; therefore protocol-matched selection is not possible from primary sources.
- Comparison conditions: Would require matched benchmark datasets, splits, metrics, and exact checkpoint attribution for both v1 and v2 in primary NVIDIA docs.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### alibaba-nlp-gte-modernbert-base — `insufficient-evidence`

- Task: embeddings for semantic search / retrieval
- Criteria: No primary-source, protocol-matched benchmark data in the inspected NVIDIA sources compares this exact v1 NIM to the external alternative; protocols and checkpoints differ and are not documented in a comparable way in the checked NVIDIA primary docs.
- Rationale: The inspected NVIDIA primary documentation does not include numeric benchmarks that would support a direct, protocol-matched comparison to external models.
- Comparison conditions: Require explicit benchmark tables with dataset, split, metric, and value attributed to the exact v1 NIM and to the external model using an identical evaluation protocol.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1

## Limitations and safety

### Limitations

- License and deployment constraints: model weights/use are governed by the NVIDIA Community Model License as provided in the canonical NVIDIA license PDF and web landing page; specific code-license attribution for NeMo Retriever code is not reported in the inspected primary NVIDIA pages. Sources: https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/NVIDIA-Models-Community-License-2025-04-15-FINAL.pdf, https://nvidia.com/es-la/agreements/enterprise-software/nvidia-community-models-license, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Operational/hardware constraints: the NeMo Retriever support matrix lists platform/device profiles, embedding precision support, and approximate parameter counts; ensure target hardware meets documented platform requirements before production deployment. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- Evaluation limits: inspected primary sources do not provide checkpoint-scoped numeric retrieval benchmarks for this v1 NIM, limiting evidence-backed claims about relative retrieval quality. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1
- Evidence gap: tokenizer name, tokenizer vocabulary, tokenization algorithm, and byte/character normalization procedures for this v1 NIM are not specified in the inspected primary NVIDIA documentation. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### Safety

- Evidence gap: primary-source documentation inspected does not specify PHI-specific safeguards, clinical validation, or explicit suitability for clinical decision-making for this v1 NIM; treat use involving PHI or clinical decisions as requiring additional organizational controls and expert review. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- NVIDIA documents that core models were trained using responsibly selected, auditable data sources, but the inspected primary documentation does not provide provenance details sufficient to assert PHI-safe training or deployment practices for clinical use. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NIM Reference: nvidia-llama-3_2-nemoretriever-300m-embed-v1

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM reference page for the exact named serving variant (v1); provides model description, architecture statements, pruning/distillation provenance, evaluation-language listing, and license pointers.
- Scope: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (v1) NIM reference
- Supports: Model name and description as Llama 3.2 NeMo Retriever Embedding 300M v1
- Supports: Transformer encoder, 9 layers, embedding dimension 2048
- Supports: Pruned and distilled provenance statement
- Supports: Training-methodology statements (bi-encoder/contrastive)
- Supports: Statements about suitability for multilingual retrieval

### NIM Inference Reference: nvidia-llama-3_2-nemoretriever-300m-embed-v1 (infer page)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1-infer
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Model-specific inference page that documents inference-time parameters including 'input_type', passage/query modes, and a stated maximum input text length for embedding inference.
- Scope: Inference-specific details for nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Supports: Inference-time 'input_type' parameter and passage/query modes
- Supports: Model-specific stated maximum input text length (32k tokens on inference page)

### NeMo Retriever Text Embedding Support Matrix (1.10.0)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Support matrix entry listing model ID, max tokens, parameter counts, embedding dimension, device/precision profiles for NeMo Retriever embedding NIMs including the v1 entry.
- Scope: Support matrix entries applicable to nvidia-llama-3_2-nemoretriever-300m-embed-v1
- Supports: Model ID nvidia/llama-3.2-nemoretriever-300m-embed-v1
- Supports: Max tokens entry 8192 for the 300M v1 row
- Supports: Parameter counts (307M excluding embeddings; 569M total)
- Supports: Embedding dimensionality (2048)
- Supports: Device/precision support table rows

### NeMo Retriever Text Embedding API Reference (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical NeMo Retriever Embedding API reference describing the HTTP API surface for embedding NIMs and runtime fields like truncate and usage.
- Scope: NeMo Retriever Text Embedding NIM API reference (applies to embedding endpoints and response schema areas)
- Supports: HTTP API reference for NeMo Retriever Embedding NIMs
- Supports: Model-level max token length entries and the 'truncate' runtime control
- Supports: General API and operational endpoints (health/metrics/version)

### NeMo Retriever Text Embedding Performance

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official performance page listing latency and throughput measurements for passage and query inputs under specific microbenchmarks.
- Scope: Performance measurements for NeMo Retriever Embedding NIMs (passage/query latency and throughput examples)
- Supports: Passage and query latency/throughput microbenchmark examples

### NeMo Retriever Text Embedding Release Notes (1.9.0)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.9.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes documenting addition of support for the llama-3.2-nemoretriever-300m-embed-v1 NIM and quantization support notes.
- Scope: Release notes (1.9.0) documenting added support for the v1 NIM
- Supports: Release 1.9.0 added support for llama-3.2-nemoretriever-300m-embed-v1
- Supports: Quantization support additions documented

### Build.NVIDIA model page: llama-3_2-nemoretriever-300m-embed-v1

- URL: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1
- Publisher: NVIDIA Build
- Type: `official-documentation`
- Primary because: Canonical Build.NVIDIA model/packaging page for the exact serving variant; documents multilingual support and high-level model description.
- Scope: Build.NVIDIA release/packaging page for the v1 NIM
- Supports: Multilingual support claim (26 languages listed)
- Supports: High-level model description and packaging/availability

### NVIDIA Models Community License (PDF)

- URL: https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/NVIDIA-Models-Community-License-2025-04-15-FINAL.pdf
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical PDF of the NVIDIA Community Model License referenced by NVIDIA for model weight/use governance.
- Scope: License governing NVIDIA Models distributed under the NVIDIA Community Model License
- Supports: NVIDIA Community Model License terms and usage restrictions applicable to NVIDIA Models

### NVIDIA Community Models License (web)

- URL: https://nvidia.com/es-la/agreements/enterprise-software/nvidia-community-models-license
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Web landing page for the NVIDIA Community Model License with usage and runtime notes referenced by NVIDIA documentation.
- Scope: License and runtime requirements pointers
- Supports: License overview and statements about governance of NVIDIA AI Foundation Models

### NGC catalog: llama-3.2-nemoretriever-300m-embed-v1

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v1/-
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC container catalog entry for the exact NIM packaging; documents intended use cases and platform stack.
- Scope: NGC container/catalog entry for the v1 NIM
- Supports: Packaging as a Text Embedding NIM
- Supports: Intended use cases: semantic search, RAG, multilingual retrieval

### NeMo Retriever Helm values (repository)

- URL: https://github.com/NVIDIA/NeMo-Retriever/blob/main/nemo_retriever/helm/values.yaml
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Helm chart values for NeMo Retriever; documents default resource and probe settings used by the official NIM helm deployment.
- Scope: Helm deployment configuration for NeMo Retriever NIMs
- Supports: Liveness/readiness probe patterns (GET /v1/health) and default CPU/memory request/limit examples

### NeMo Retriever Helm README (repository)

- URL: https://github.com/NVIDIA/NeMo-Retriever/blob/main/nemo_retriever/helm/README.md
- Publisher: NVIDIA
- Type: `repository`
- Primary because: Helm README documenting deployment ports, worker defaults, and maximum upload size settings for the official helm chart.
- Scope: Helm deployment README for NeMo Retriever
- Supports: Default service port and worker/batch defaults and maximum upload size

### NeMo Retriever Text Embedding Release Notes (1.14.0)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.14.0/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes documenting later support branches, quantization and production-branch changes related to NeMo Retriever NIMs.
- Scope: Release notes covering newer NeMo Retriever releases and production branches
- Supports: Release history entries relevant to NeMo Retriever NIM families (production branches, quantization support notes)

### NeMo Retriever Text Embedding Support Matrix (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Latest support-matrix documentation with runtime token-budget and recommended NIM pipeline max-seq-len settings for specific hardware.
- Scope: Latest support matrix entries and recommended max-seq-len settings
- Supports: Token-budget and recommended NIM_PIPELINE_MAX_SEQ_LEN settings for certain hardware profiles

### NeMo Retriever Embedding NIM: OpenAI-compatible API guidance

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/use-the-api-openai.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Documentation stating that NeMo Retriever embedding NIMs provide an OpenAI-compatible API surface.
- Scope: OpenAI-compatible API guidance for NeMo Retriever Embedding NIMs
- Supports: Statement that NeMo Retriever Embedding NIMs expose an OpenAI-compatible API

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric retrieval benchmarks (recall@k, MRR, nDCG, or embedding-quality scores) for nvidia-llama-3_2-nemoretriever-300m-embed-v1 were found in the inspected primary sources (checked: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1 — model reference; https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html — support matrix; https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v1 — Build.NVIDIA page; https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v1-infer — inference page; https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.9.0/release-notes.html — release notes).
- Evidence gap: Tokenizer name, tokenizer vocabulary file path, tokenization algorithm, and exact byte/character normalization steps for this exact v1 NIM are not specified in the inspected primary NVIDIA documentation (checked: NIM reference, support matrix 1.10.0, inference page).
- Evidence gap: Embedding output normalization (e.g., L2 normalization) and any scaling applied to vectors are not specified in the inspected primary documentation (checked: NIM reference and latest API reference).
- Evidence gap: Exact API request parameter names and per-field request contract for POST /v1/embeddings (batching parameter names, truncation controls, explicit request field names) are not fully documented for this exact v1 NIM in the inspected primary references (checked: NIM reference, latest API reference, inference page).
- Evidence gap: Batching behavior, request size limits per request, and how over-length inputs are handled (truncation, rejection, segmentation) for this v1 NIM are not specified in the inspected primary sources (checked: API reference, support matrix, inference page).
- Evidence gap: Numeric latency, throughput, and matched hardware benchmarks for the v1 NIM under specific GPU/hardware configurations are not provided in the inspected primary sources for this exact v1 checkpoint (checked: support matrix, performance page, and release notes).
- Evidence gap: Exact upstream third-party original checkpoint card/repository for the alleged nv-embedqa-1b-v1 origin is not present among the inspected primary NVIDIA sources; NVIDIA documents pruning/distillation provenance but does not provide an upstream canonical checkpoint URL in the checked pages.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 0 deterministic draft defect(s) were supplied to the audit.

- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
