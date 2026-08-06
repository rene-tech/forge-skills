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

- Research key: `build-nvidia-com-nvidia-llama-3-2-nemoretriever-300m-embed-v2-f53275e56f`
- Independent audit: `revised`
- Researched: `2026-07-23T22:19:09.850664+00:00`

This dossier is scoped to the NIM-served checkpoint nvidia/llama-3.2-nemoretriever-300m-embed-v2 as documented by NVIDIA primary pages. Primary NVIDIA documentation identifies this serving variant as a 9-layer transformer encoder distilled/pruned from a larger Llama 3.2 retriever checkpoint, exposing a bi-encoder embedding head with embedding dimensionality 2048 and model-reported parameter counts of 307M (excluding embeddings) and 569M (including embeddings) (support matrices). The NIM exposes a REST embeddings endpoint with request fields including model, input, input_type (query|passage), encoding_format, embedding_type, and truncate controls (inference reference and NeMo REST reference). The NeMo support matrices and model pages document a model-supported maximum context length of 8192 tokens for the 300M model while the inference API reference includes a request-level maximum input-length statement (documented divergence noted). Primary evidence gaps remain for an immutable upstream checkpoint revision identifier or direct downloadable upstream checkpoint path for this exact v2 checkpoint, explicit tokenizer implementation artifacts for this exact v2 checkpoint (vocab/SP/merges and tokenizer name/version), and explicit PHI/clinical usage guidance.

## Identity

- Upstream name: nvidia/llama-3.2-nemoretriever-300m-embed-v2
- Checkpoint/version: nvidia/llama-3.2-nemoretriever-300m-embed-v2
- Immutable revision: not reported
- Parameter scale: 307M non-embedding parameters; 569M total parameters (including embeddings)
- Architecture/head: Transformer encoder (9 layers); bi-encoder retrieval embedding head; embedding dimensionality 2048
- License: NVIDIA Community Model License; Llama 3.2 Community License
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-

## Selection

### Recommended

- **Multilingual / cross-lingual dense retrieval for question-answering over large text corpora** — The official NIM model reference and NGC catalog describe the v2 NeMo Retriever embedding model as optimized for multilingual and cross-lingual QA retrieval and list evaluation on 26 languages; the model is published as a retrieval embedding NIM suitable for extracting per-input embeddings.
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-
- **Long-document retrieval via chunking/truncation up to the model-supported context length** — NeMo support matrices and the model reference document model support for inputs up to 8192 tokens for the 300M model and the NIM inference API exposes truncate controls enabling chunking/truncation workflows.
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2
- **Extracting per-input embedding vectors (float or supported encodings) for downstream retrieval pipelines** — NeMo Retriever REST reference documents an embeddings endpoint returning an array of embedding objects with embedding_type and encoding_format options; support matrices list embedding dimension 2048 and supported embedding types.
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html

### Conditional

- **Commercial production deployment of the NIM container** — Requires NGC catalog license/subscription acceptance and following the NeMo getting-started Docker/run guidance; validate environment variables and model-download-provider settings prior to deployment.
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2 (NGC container referenced in deploy docs)
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy
- **Using non-float embedding encodings (int8/uint8/binary/ubinary) for storage/performance** — Downstream consumers must expect and correctly decode the chosen embedding_type and encoding_format; validate similarity metric and storage/decoding pipeline for non-float encodings.
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### Avoid

- **Submitting inputs with the wrong input_type (mismatched 'query' vs 'passage') for retrieval** — The inference API reference documents that input_type must be set (query|passage) and that using the wrong type reduces retrieval accuracy (mode-sensitive bi-encoder semantics).
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2
- **Running the 300M embedding NIM on GPU clusters configured with Multi-instance GPU (MIG) mode** — NeMo getting-started and support documentation state that GPU clusters with GPUs in MIG mode are not supported for this NIM (MIG unsupported guidance).
  Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

## Input preparation

### Semantic inputs

- The model accepts textual inputs intended for embedding extraction; accepted request-level input types include 'query' and 'passage'. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Input is provided as a string or array of strings in the embeddings POST request. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy

### Accepted formats

- Official REST request schema fields documented include model, input (string or array), input_type (query|passage), encoding_format (float or base64), embedding_type (float, int8, uint8, binary, ubinary), truncate (START, END, NONE), and optional user/dimensions fields. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy

### Preprocessing

- The REST inference API and NeMo reference expose a 'truncate' request field with allowed values START, END, and NONE to control truncation behavior. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Documented divergence in token limits: the inference API reference includes a request-level maximum input length statement (32,000 tokens) while the NeMo Retriever support matrix and model pages document model support up to 8192 tokens for the 300M model; both statements are present in primary sources and constitute a documented scope divergence. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html
- Docker deployment and getting-started guidance reference required environment variables/credentials for model download and runtime configuration (examples include HF_TOKEN, NGC_API_KEY, and NIM_MODEL_DOWNLOAD_PROVIDER) and Docker/shared-memory guidance. Sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html

### Pre-submit validation

- Callers should validate non-empty input strings and allowed enum values before submission; the REST reference documents required fields and response error behavior for invalid inputs. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Validate NGC license/subscription acceptance prior to pulling the container image as part of deployment validation. Sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html
- Ensure input_type aligns with intended query/passage semantics because incorrect mode reduces retrieval accuracy (recommended pre-check). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer

### Task-specific formatting

- Sample REST requests in the deploy docs use fields and values such as {"model": "nvidia/llama-3.2-nemoretriever-300m-embed-v2", "input": "...", "input_type": "query", "encoding_format": "float", "truncate": "NONE"}. Sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy
- The NeMo Retriever reference documents the response schema semantics: top-level 'object' as 'list', 'data' as an array with one embedding object per input, and each embedding object containing 'object' ('embedding'), 'index', and 'embedding' (array of values). Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer

## Output interpretation

### Outputs

- NeMo Retriever REST response contains top-level 'object' ("list"), 'data' (array of embedding objects), 'model' (served model ID), and a 'usage' object; each embedding object includes 'object' ("embedding"), 'index', and 'embedding' (array of numeric values). Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer
- Embedding dimensionality reported for the 300M model is 2048 in the NeMo support matrices and model reference; output embeddings should match this dimensionality when the model is configured accordingly. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2
- Embedding outputs are returned as numeric arrays by default (float default) and supported embedding_type values include float, int8, uint8, binary, and ubinary; encoding_format options include float and base64, as documented in the NeMo reference and support matrices. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### Interpretation

- The documentation does not specify whether embeddings are normalized by default for this exact v2 checkpoint; callers should perform downstream validation and consider caller-side normalization (e.g., L2) when normalization semantics are required. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Callers must align similarity metric choice with the chosen embedding_type/encoding_format and encoding (e.g., integer encodings require appropriate decoding/metric handling). Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### Post-inference validation

- Post-inference checks should verify returned embedding dimensionality matches the configured/model-supported dimension and that encoding_format/embedding_type align with downstream consumers. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- The response includes a 'usage' object with token usage information that callers can inspect to validate token counts and truncation effects. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nvidia-llama-3_2-nemoretriever-300m-embed-v1 — `insufficient-evidence`

- Task: embeddings / retrieval
- Criteria: Direct numeric preference requires matched primary-source benchmark rows (dataset, split, metric, numeric values, and protocol) for both v1 and v2; such matched v2 numeric rows were not found in the inspected v2 pages.
- Rationale: Support matrices and references describe families and capabilities, but primary-source matched-protocol numeric benchmark rows for exact v2 vs v1 were not located for v2 in the inspected facts.
- Comparison conditions: Requires identical dataset/split/metric/protocol numeric rows in primary docs for both checkpoints to prefer one over the other.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html

### nvidia-llama-3_2-nv-embedqa-1b-v1 — `insufficient-evidence`

- Task: embeddings / retrieval
- Criteria: Direct numeric comparison requires primary-source benchmark data for both exact v2 and the alternative on the same dataset/protocol; such matched primary rows were not found for exact v2 in the inspected facts.
- Rationale: The nv-embedqa-1b-v1 upstream and combination results are reported in NVIDIA model cards, but direct matched numeric rows for the v2 single-call embedding NIM were not located in the inspected v2 primary pages.
- Comparison conditions: Requires identical dataset/split/metric/protocol primary tables/figures for both sides.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v1

### insufficient-evidence — `insufficient-evidence`

- Task: embeddings / retrieval
- Criteria: For any other candidate comparison a matched primary-source benchmark for both sides on the same protocol is required and was not present for exact v2 in the inspected facts.
- Rationale: No matched primary-source numeric benchmark data for exact v2 and arbitrary alternatives on identical protocols was found in the inspected facts.
- Comparison conditions: Requires identical dataset/split/metric/protocol primary tables/figures for both sides.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2

## Limitations and safety

### Limitations

- Maximum context length for the 300M model is reported as 8192 tokens in the NeMo Retriever support matrix; callers must chunk or truncate longer texts. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html
- Documented scope divergence: the inference API documents a request-level maximum input length statement (32,000 tokens) while the NeMo support matrix and model pages report a model-enforced maximum of 8192 tokens for the 300M model; callers must treat the smaller model-supported limit as the effective per-request model context limit unless the deployment documentation states otherwise. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- GPU clusters with GPUs in MIG mode are not supported for the NeMo Retriever embedding NIM per getting-started/support docs; multi-GPU deployment is not included in the noted release guidance for some versions. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- Evidence gap: The inspected primary sources do not report an immutable revision identifier, commit hash, or downloadable upstream checkpoint path for the exact nvidia/llama-3.2-nemoretriever-300m-embed-v2 checkpoint. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-
- Evidence gap: Tokenizer implementation files (vocab, merges or SentencePiece model), tokenizer name/version, and exact tokenization/normalization rules for the exact nvidia/llama-3.2-nemoretriever-300m-embed-v2 checkpoint were not found in the inspected primary pages. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy

### Safety

- Use and distribution are governed by NVIDIA license terms and NGC catalog license/subscription acceptance; model use is noted as governed by the NVIDIA Community Model License and Llama 3.2 Community License where applicable. Sources: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-, https://developer.nvidia.com/downloads/assets/ace/model_card/llama-3.2-3b_for_Nv_IGI_SDK.pdf
- Evidence gap: The inspected primary NVIDIA pages do not provide explicit healthcare/clinical or PHI-specific authorization or prohibition statements for this checkpoint; no PHI-specific guidance was located in the checked canonical pages. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-
- The model is described as production-ready in NVIDIA documentation, but commercial use remains subject to the license terms and NGC acceptance flow. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NIM reference: nvidia-llama-3_2-nemoretriever-300m-embed-v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM model reference for the llama-3.2-nemoretriever-300m-embed-v2 serving variant; contains model identity, embedding dimension, multilingual evaluation claim, training/architecture notes, and readiness statements used in this dossier.
- Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2
- Supports: Checkpoint name and high-level description
- Supports: Transformer encoder architecture (9 layers) and embedding size 2048
- Supports: Multilingual evaluation claim and supported languages listing
- Supports: Model readiness and deployment statements
- Supports: Embedding output format description

### NIM inference API reference: nvidia-llama-3_2-nemoretriever-300m-embed-v2 (infer)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2-infer
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Inference API reference describing request fields (input_type, truncate), request-level token length statements, and mode-sensitivity used in this dossier.
- Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2 (infer schema)
- Supports: Request fields including input_type and truncate
- Supports: Request-level maximum input length statement
- Supports: Warning that wrong input_type reduces retrieval accuracy
- Supports: Sample response schema fields

### Deployment docs / sample API request for the v2 NIM (Build)

- URL: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy
- Publisher: NVIDIA Build (NIM deploy docs)
- Type: `official-documentation`
- Primary because: Official deployment page providing sample REST request, Docker run guidance, and example container image string used in this dossier.
- Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2 (deploy/sample)
- Supports: Sample REST request fields and example values
- Supports: Docker run guidance and sample docker run flags
- Supports: Example container image and runtime guidance

### NGC catalog container entry: llama-3.2-nemoretriever-300m-embed-v2

- URL: https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-
- Publisher: NVIDIA NGC catalog
- Type: `official-documentation`
- Primary because: Official NGC catalog listing for the v2 container; confirms availability, subscription/license flow, and production-readiness metadata.
- Scope: nvidia/llama-3.2-nemoretriever-300m-embed-v2 (NGC container)
- Supports: Production-readiness and subscription/licensing metadata
- Supports: High-level model description and suggested use-cases
- Supports: NGC license/subscription metadata and license governance statements

### NeMo Retriever text-embedding latest reference (REST response schema)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Official NeMo Retriever REST reference documenting endpoints, request/response schemas, embedding_type and encoding_format enumerations used in this dossier.
- Scope: NeMo Retriever text-embedding (latest reference)
- Supports: POST /v1/embeddings request fields and optional parameters
- Supports: Response schema: object, data[], model, usage, and embedding object fields
- Supports: Supported embedding_type and encoding_format enumerations
- Supports: Modality and input_type enumerations

### NeMo Retriever text-embedding getting-started

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Getting-started guide documenting Docker run examples, environment variables for model download, and NGC license acceptance requirements used in this dossier.
- Scope: NeMo Retriever text-embedding (getting-started)
- Supports: Environment variables HF_TOKEN and NGC_API_KEY and NIM_MODEL_DOWNLOAD_PROVIDER guidance
- Supports: MIG unsupported statement and Docker/shared memory guidance
- Supports: License acceptance requirement prior to pulling container

### NeMo Retriever text-embedding latest environment variables

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/environment-variables.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Environment-variable reference used to verify download-provider and runtime environment variables and defaults.
- Scope: NeMo Retriever text-embedding (environment variables)
- Supports: Environment variable NIM_PIPELINE_MAX_BATCH_TOKENS and other NIM env var semantics
- Supports: NIM_MAX_SEQ_LEN override behavior
- Supports: NIM_MODEL_DOWNLOAD_PROVIDER selection (hf/ngc) and other runtime flags

### NeMo Retriever text-embedding latest release notes

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Release notes documenting environment-variable behaviors and model download-provider guidance referenced in this dossier.
- Scope: NeMo Retriever text-embedding (release notes)
- Supports: Model artifact download-provider options and environment variable guidance
- Supports: Environment variable renames and runtime notes

### NeMo Retriever text-embedding 1.10.0 support matrix

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/1.10.0/support-matrix.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Support matrix version 1.10.0 lists the model and per-model metadata used in this dossier.
- Scope: NeMo Retriever text-embedding 1.10.0 support matrix
- Supports: Model ID listing for nvidia/llama-3.2-nemoretriever-300m-embed-v2
- Supports: Maximum tokens supported listed as 8192 for the 300M model
- Supports: Parameter counts and embedding dimension entries for the 300M model
- Supports: Supported embedding types enumerated

### NeMo Retriever text-embedding 2.2.0 support matrix

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/2.2.0/support-matrix.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Support matrix version 2.2.0 lists parameter counts and embedding dimension metadata referenced in this dossier.
- Scope: NeMo Retriever text-embedding 2.2.0 support matrix
- Supports: 307M parameters (excluding embeddings) and 569M total parameters for 300M model
- Supports: Embedding dimension 2048 for 300M model
- Supports: Supported embedding type enumerations

### NeMo Retriever text-embedding latest support matrix

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Support matrix listing supported hardware and precisions for the embedding NIM referenced in this dossier.
- Scope: NeMo Retriever text-embedding (support matrix latest)
- Supports: Supported hardware SKUs and precision guidance for the embedding NIM

### NeMo Retriever text-embedding performance (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Publisher: NVIDIA NeMo documentation
- Type: `official-documentation`
- Primary because: Performance page providing latency benchmark rows on NVIDIA hardware used as operational test data in the facts.
- Scope: NeMo Retriever text-embedding (performance)
- Supports: Performance benchmark latency rows for passage lengths, batch sizes, and token counts on NVIDIA hardware

### NIM reference: nvidia-llama-3_2-nv-embedqa-1b-v1

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v1
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM model reference for the upstream nv-embedqa-1b-v1 checkpoint referenced as the larger checkpoint distilled/pruned into the 300M model.
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v1 (upstream)
- Supports: Identification of the upstream model used for distillation
- Supports: Architecture and embedding size of the upstream model

### NIM inference API reference: nvidia-llama-3_2-nv-embedqa-1b-v1 (infer)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v1-infer
- Publisher: NVIDIA NeMo / NIM documentation
- Type: `official-documentation`
- Primary because: Inference API reference for the upstream nv-embedqa-1b-v1 model used to support mode-sensitivity claims (input_type consequences).
- Scope: nvidia/llama-3.2-nv-embedqa-1b-v1 (infer)
- Supports: Warning that wrong input_type (query vs passage) reduces retrieval accuracy for the related upstream retriever model

### Modelcard: llama-nemotron-rerank-1b-v2 (Build)

- URL: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Publisher: NVIDIA Build (modelcard)
- Type: `official-documentation`
- Primary because: Modelcard for related reranker/embedding combinations reporting MLDR and other benchmark numbers used to identify where numeric results exist for related pipelines.
- Scope: llama-nemotron-rerank-1b-v2 modelcard
- Supports: MLDR benchmark entries for reranker+embedder combinations and reported Average Recall@5 values for those pipelines

### Llama 3.2 Community License (NVIDIA developer asset)

- URL: https://developer.nvidia.com/downloads/assets/ace/model_card/llama-3.2-3b_for_Nv_IGI_SDK.pdf
- Publisher: NVIDIA developer resources
- Type: `official-documentation`
- Primary because: Publisher document indicating the Llama 3.2 Community License referenced in NVIDIA materials.
- Scope: Llama 3.2 licensing reference
- Supports: License name and association with Llama 3.2 releases

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-llama-3-2-nemoretriever-300m-embed-v2
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- No immutable revision identifier, commit hash, or direct downloadable upstream checkpoint path for the exact nvidia/llama-3.2-nemoretriever-300m-embed-v2 checkpoint was found in the inspected primary NVIDIA pages: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-.
- Tokenizer implementation details (tokenizer name/version; vocabulary files; merges or SentencePiece model; normalization/tokenization rules) for the exact nvidia/llama-3.2-nemoretriever-300m-embed-v2 checkpoint were not present in the inspected primary pages: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html, https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2/deploy.
- No explicit primary-source table/figure/row locator for an Average Recall@5 numeric value on the MLDR benchmark for this exact v2 checkpoint was found in the inspected primary pages; related MLDR numeric rows exist for other combinations/pipelines but not for the single-call v2 embedding NIM: checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2 and related modelcards (e.g., https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard).
- The inspected primary NVIDIA pages do not specify whether embeddings are normalized by default (L2 or otherwise) for this exact v2 checkpoint; callers should perform caller-side normalization if required for downstream metrics: checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2 and https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/reference.html.
- The inspected primary NVIDIA pages do not provide explicit PHI/healthcare/clinical authorization or prohibition statements for this checkpoint: checked https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nemoretriever-300m-embed-v2, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/llama-3.2-nemoretriever-300m-embed-v2/-.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 3 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-embedqa-1b-v1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/llama-3_2-nemoretriever-300m-embed-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
