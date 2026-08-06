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

- Research key: `build-nvidia-com-nvidia-llama-3-2-nv-rerankqa-1b-v2-3e8a5720eb`
- Independent audit: `revised`
- Researched: `2026-07-23T21:48:28.478654+00:00`

Verified primary NVIDIA documentation identifies the artifact named "llama-3.2-nv-rerankqa-1b-v2" as a 1B-parameter NeMo Retriever reranking checkpoint (transformer encoder cross-encoder reranker) packaged and served as a NIM. NVIDIA NIM reference and Build pages document: query-passage pair input semantics, a numeric relevance logit output produced by a binary-classification head after mean-pooling of the final embedding, multilingual evaluation on 26 languages, and long-context support. Official NIM support matrices (latest and 1.9.0) document a runtime distinction: an optimized configuration supporting up to 8192 tokens and a non-optimized configuration supporting up to 4096 tokens. Primary sources do not publish a stable immutable artifact revision/digest for the served checkpoint, do not expose tokenizer identity/version or detailed truncation strategy for per-side truncation, and do not include checkpoint-scoped numeric benchmark tables or protocol-matched comparisons for this exact reranker runtime; those items are listed as explicit evidence gaps below with the exact canonical URLs checked.

## Identity

- Upstream name: meta-llama/Llama-3.2-1B
- Checkpoint/version: llama-3.2-nv-rerankqa-1b-v2
- Immutable revision: not reported
- Parameter scale: 1B
- Architecture/head: Transformer encoder fine-tuned as a cross-encoder reranker using bi-directional attention, mean-pooling of final embeddings, and a binary-classification head producing a relevance logit
- License: NVIDIA Community Model License and Llama 3.2 community license (model weights/upstream); NIM container/runtime governed by NVIDIA Software License Agreement / Product Specific Terms as published in the NIM EULA
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html

## Selection

### Recommended

- **Reranking candidate passages/documents for a given query in a two-stage retrieval pipeline** — NVIDIA NIM reference and the NVIDIA Build product page describe the checkpoint as intended to improve multilingual retrieval tasks by reranking candidate passages and emitting a relevance logit for each candidate
  Scope: llama-3.2-nv-rerankqa-1b-v2 served via the NeMo Retriever Llama 3.2 reranking NIM
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2

### Conditional

- **Long-document reranking workloads (large context)** — Confirm deployed NIM runtime configuration (optimized vs non-optimized) because official NIM support-matrix documentation documents an optimized configuration supporting 8192 tokens and a non-optimized configuration supporting 4096 tokens; callers must validate which runtime configuration is active for their NIM instance
  Scope: llama-3.2-nv-rerankqa-1b-v2 in NVIDIA NIM optimized vs non-optimized configurations
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- **Enterprise or compliance-sensitive deployments** — Validate applicable license terms, NIM EULA terms, and enterprise/runtime packaging before deployment; confirm entitlement and runtime governance as described in the NIM EULA and NIM reference
  Scope: NIM packaging/runtime for llama-3.2-nv-rerankqa-1b-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2

### Avoid

- **Using this checkpoint as a generative chat or free-form text generation model** — Primary NVIDIA documentation for the exact reranker/runtime describes a reranking model that accepts query-passage pairs and outputs relevance logits; the Build and NIM reference pages do not document generative text outputs for this checkpoint/runtime
  Scope: llama-3.2-nv-rerankqa-1b-v2 reranking checkpoint and NVIDIA NIM service
  Evidence: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- **Using the model beyond its documented evaluated language set without validation** — The NIM reference documents evaluation on 26 listed languages; there is no checkpoint-scoped primary-source evidence that validates broader language coverage for this exact NIM-served reranker
  Scope: llama-3.2-nv-rerankqa-1b-v2 checkpoint
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2

## Input preparation

### Semantic inputs

- The model consumes a text query and one or more candidate passage/document text inputs as paired inputs for reranking (query-passage pairs) Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2/deploy
- Real-world input semantics are a user question/query plus candidate passages/documents to be scored for relevance Sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2

### Accepted formats

- Accepted modality is text; the reranker expects query-passage textual inputs rather than free-form generation prompts Sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- An example API request JSON on the Build deploy page includes fields: "model", "query" with subfield "text", and "passages" array of objects each with a "text" field Sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2/deploy

### Preprocessing

- The reranker is described as a cross-encoder using bi-directional attention over concatenated query-passage tokens with mean-pooling of the final embedding before a binary classification head Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Fine-tuning/training uses cross-entropy loss for sentence-classification-style relevance prediction (positive vs negative passages) Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Pre-submit validation

- Validate total input length against the supported token limit for the deployed NIM configuration (optimized vs non-optimized) using the NIM support-matrix guidance Sources: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/support-matrix.html
- Evidence gap: the primary sources checked do not publish tokenizer identity/version, vocabulary, special-token definitions, or precise per-side truncation rules for this exact checkpoint/runtime; callers must validate tokenization, token counting, and truncation behavior externally before submission Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/reference-grpc.html

### Task-specific formatting

- Official task format for this checkpoint is a query-passage pair for reranking as documented in the NIM reference Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- A canonical example request JSON with fields "model", "query.text", and "passages[].text" is provided on the Build deploy page Sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2/deploy
- gRPC reference documents the gRPC input field names and shapes for reranking requests (query and passage fields encoded as BYTES) Sources: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/reference-grpc.html

## Output interpretation

### Outputs

- The model emits a numeric relevance logit score indicating document relevance to the provided query (ranking score) — this is the documented output contract for the reranker Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- The ranking signal is produced by a binary-classification head over the mean-pooled final embedding (a relevance logit) Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Interpretation

- Higher numeric logit values indicate greater relevance according to the NVIDIA NIM reference and Build page; the output is a ranking score and not a generated answer text Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2

### Post-inference validation

- Evidence gap: the primary sources do not publish calibration guidance, score normalization guidance, or recommended operational thresholds for the relevance logit; downstream systems should calibrate thresholds and validate ranking behavior on held-out task data Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- Validate that reranking behavior meets retrieval pipeline requirements and domain/language expectations because the NIM reference documents evaluation on 26 languages but does not provide checkpoint-scoped deployment thresholds Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Evidence gap: primary sources checked do not report an immutable checkpoint revision identifier, artifact digest, or hash for the exact served checkpoint/runtime Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- The provided primary evidence does not specify tokenizer identity/version, vocabulary, or special-token definitions for this exact checkpoint/runtime Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- Sequence length and token limits depend on runtime configuration: official NIM support-matrix documentation documents 8192 tokens for optimized configuration and 4096 tokens for non-optimized configuration; callers must confirm which runtime is active Sources: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/support-matrix.html, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- The model's documented evaluation is limited to the 26 languages listed in the NIM reference; broader language coverage for this checkpoint is not established in the cited primary sources Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- License and runtime governance are layered: model weights/upstream base are subject to Llama 3.2 community licensing and NVIDIA Community Model License terms as cited in the NIM reference, and the NIM container/runtime is governed by NVIDIA Software License/Product Terms (NIM EULA) Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html

### Safety

- Users must ensure compliance with applicable laws and the NVIDIA Community Model License terms and the NIM EULA when using this model Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html
- Evidence gap: the provided primary evidence does not list checkpoint-specific privacy, PHI, clinical-use, or regulated-deployment controls for this exact NIM-served checkpoint/runtime; callers should not assume special-case PHI protections from the cited materials Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM reference: nvidia-llama-3_2-nv-rerankqa-1b-v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM reference page for the exact reranking NIM model/checkpoint documenting architecture, inputs, outputs, evaluation languages, and license statements
- Scope: llama-3.2-nv-rerankqa-1b-v2 checkpoint and NeMo Retriever reranking NIM runtime
- Supports: checkpoint identity
- Supports: architecture description
- Supports: intended reranking use
- Supports: query-passage pair input semantics
- Supports: logit output semantics
- Supports: documented evaluation languages
- Supports: license statements in the NIM reference
- Supports: stated long-context support

### NVIDIA Build page: Llama 3.2 NV-RerankQA 1B v2 (product entry)

- URL: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official Build product page for the named Forge model family and product entry
- Scope: Build entry for llama-3.2-nv-rerankqa-1b-v2 and Forge variant
- Supports: brief product description
- Supports: intended reranking use
- Supports: long-context support claim
- Supports: canonical Build deploy example reference

### NVIDIA Build deploy example for llama-3.2-nv-rerankqa-1b-v2

- URL: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2/deploy
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Build deploy page contains the example API request JSON for the product and explicit field names for query/passage inputs
- Scope: Build deploy example for llama-3.2-nv-rerankqa-1b-v2
- Supports: example API request JSON fields (model, query.text, passages[].text)
- Supports: deployment/deploy field examples

### NVIDIA NIM support matrix for NeMo Retriever text-reranking (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical/latest support matrix documenting optimized vs non-optimized token limits and hardware compatibility for NeMo Retriever reranking models
- Scope: NIM runtime support matrix entries for llama-3.2-nv-rerankqa-1b-v2
- Supports: optimized configuration token limit = 8192 (for supported SKUs/configs)
- Supports: non-optimized configuration token limit = 4096
- Supports: hardware/precision compatibility notes

### NVIDIA NIM support matrix for NeMo Retriever text-reranking 1.9.0

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Historical support matrix documenting model ID mappings and token limits for specific NIM releases (used to verify optimized/non-optimized limits and model IDs)
- Scope: NIM runtime support matrix entries for NeMo Retriever text-reranking 1.9.0
- Supports: model ID mapping for Llama-3.2-NV-RerankQA-1B-v2
- Supports: optimized configuration token limit guidance (8192 documented)
- Supports: non-optimized configuration token limit guidance (4096 documented)
- Supports: compute capability and precision compatibility

### NIM reference gRPC: NeMo Retriever text-reranking (1.9.0) - gRPC field shapes

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/reference-grpc.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: gRPC reference documents the input field names and shapes for reranking requests (query and passage fields encoded as BYTES)
- Scope: gRPC reference for NeMo Retriever text-reranking 1.9.0
- Supports: gRPC input field names and shapes for query and passage
- Supports: model ID mapping to gRPC model name

### NIM using-reranking documentation (using-reranking / API behavior)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/using-reranking.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Documentation describing request parameters (query, passages, truncate) and API semantics for reranking
- Scope: NeMo Retriever reranking API usage documentation (latest)
- Supports: request includes query, list of passages, optional truncate parameter
- Supports: truncate parameter semantics (NONE or END)
- Supports: ranking based only on query and passages text

### NVIDIA NIM release notes: NeMo Retriever text-reranking (latest release notes)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes document supported SKUs, default precision behavior, and model artifact download providers
- Scope: NeMo Retriever text-reranking release notes (latest)
- Supports: supported optimized SKUs and precision guidance
- Supports: default precision is FP16 when supported
- Supports: model artifact download providers (HF/NGC) guidance

### NVIDIA NIM EULA for NeMo Retriever text-reranking 1.12.0

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM EULA and product-specific licensing/governance documentation for the NIM container/runtime packaging
- Scope: NIM runtime license and EULA terms applicable to packaged reranking NIMs
- Supports: runtime/container license governance
- Supports: statement that model use is governed by NVIDIA Community Model License and Llama 3.2 community license in NIM packaging

### NIM speech resources EULA (enterprise software license locator)

- URL: https://docs.nvidia.com/nim/speech/latest/resources/eula.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA agreements and license locator confirming NIM container governance by NVIDIA Software License Agreement and community model license references
- Scope: NIM EULA / license locator
- Supports: NIM container governed by NVIDIA Software License Agreement and Product Specific Terms
- Supports: ai-foundation-models community license referenced

### NVIDIA NGC catalog: Llama-3.2-nv-rerankqa-1b-v2 production branch

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nv-rerankqa-1b-v2-pb6/-
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NGC catalog entry for the NIM production branch, documenting availability and supported branch lifecycle
- Scope: NIM production branch metadata for llama-3.2-nv-rerankqa-1b-v2
- Supports: production branch availability description
- Supports: confirmation that the NIM provides a relevance logit for reranking

### Build model card: llama-nemotron-rerank-1b-v2 model card

- URL: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Model card entry associated with the reranking model describing architecture lineage and parameter count
- Scope: Build model card for the reranking checkpoint
- Supports: statement that network architecture is fine-tuned meta-llama/Llama-3.2-1B
- Supports: parameter count = 1.0 × 10^9 (1B)
- Supports: maximum sequence length claim (8192 tokens)

### Meta Llama 3.2 model card (upstream-checkpoint evidence)

- URL: https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md
- Publisher: Meta
- Type: `repository`
- Primary because: Upstream model-family card documenting Llama 3.2 base-family properties referenced by NVIDIA
- Scope: meta-llama/Llama-3.2-1B upstream model-family card
- Supports: upstream architecture lineage to meta-llama/Llama-3.2
- Supports: description of upstream Llama 3.2 family and available sizes (1B mentioned in upstream family)

## Evidence gaps

- Evidence gap: No checkpoint-scoped numeric benchmark rows or tables found for llama-3.2-nv-rerankqa-1b-v2 at the NIM reference page (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2).
- Evidence gap: No checkpoint-scoped numeric benchmark rows or tables found for llama-3.2-nv-rerankqa-1b-v2 on the Build product page (checked https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2 and https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard).
- Evidence gap: No checkpoint-scoped numeric benchmark rows or tables found in the upstream Llama 3.2 model card for metrics tied to the NVIDIA-served reranker (checked https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md).
- Evidence gap: No immutable checkpoint revision identifier, artifact digest, or published hash for the exact served artifact found in the NIM reference or Build pages (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2 and https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2).
- Evidence gap: Tokenizer identity/version, vocabulary, and special-token definitions for this exact checkpoint/runtime are not specified in the NIM reference or Build pages (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2 and https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2).
- Evidence gap: Precise per-side truncation rules, token counting behavior, and tokenizer truncation strategy are not published for this exact NIM-served checkpoint/runtime (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, and https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.9.0/reference-grpc.html).
- Evidence gap: No calibration guidance, score-normalization procedures, or recommended operational thresholds for the relevance logit are published in the primary sources checked (https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2 and https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2).
- Evidence gap: No checkpoint-specific privacy, PHI, clinical-use, or regulated-deployment controls published for this exact NIM-served checkpoint/runtime in primary sources (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2 and https://docs.nvidia.com/nim/nemo-retriever/text-reranking/1.12.0/eula.html).
- Evidence gap: No task- and protocol-matched primary-source comparisons verified for this exact checkpoint/runtime at the checked canonical NVIDIA and upstream URLs (checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, and https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md).
- Evidence gap: Benchmarks section is empty because no checkpoint-scoped numeric benchmark rows were found in the canonical NVIDIA or upstream sources (checked URLs: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2, https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md).
- Evidence gap: Comparisons section is empty because no protocol-matched primary-source comparisons for this exact NIM-served reranker were found at the canonical NVIDIA or upstream locations (checked URLs: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2, https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 4 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
