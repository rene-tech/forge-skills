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

- Research key: `build-nvidia-com-nvidia-llama-nemotron-rerank-1b-v2-modelcard-906e6e6687`
- Independent audit: `revised`
- Researched: `2026-07-23T22:20:48.027736+00:00`

Verified primary upstream and serving artifacts describe nvidia/llama-nemotron-rerank-1b-v2 as a ~1B-parameter cross-encoder reranker (sequence-classification head, avg pooling) that emits per-passage scalar relevance scores (logits). The Hugging Face repository (model page, README, committed config/tokenizer/LICENSE blobs) and NVIDIA serving artifacts (NIM reference, Build.NVIDIA modelcard, NGC container listing, NeMo documentation and NIM support matrices) form the primary evidence set. NVIDIA-published numeric retrieval results in the available artifacts are reported as pipeline-level evaluations that combine an embedding model + reranker (embedding+rerank pipelines) rather than isolating reranker-only metrics; where numeric values are reported the modelScope is a pipeline. Primary artifacts contain conflicting sequence-length fields: the NeMo rerank README documents a 512-token concatenated query+passage maximum for the base recipe, while committed upstream config blobs and NVIDIA support matrices/build.nvidia modelcard record max_position_embeddings/optimized support of up to 8192 tokens; the runtime-serving token limit for the named NIM container must be confirmed before deployment. Tokenizer implementation name/version and detailed preprocessing (Unicode normalization, punctuation handling, exact tokenization pipeline) are not specified in the available primary artifacts. No immutable upstream checkpoint revision/hash is reported in the available primary artifacts. Primary sources for container/packaging licensing differ from model-weight license blobs and are recorded separately.

## Identity

- Upstream name: nvidia/llama-nemotron-rerank-1b-v2
- Checkpoint/version: nvidia/llama-nemotron-rerank-1b-v2
- Immutable revision: Revision: not reported
- Parameter scale: approximately 1 billion parameters
- Architecture/head: Transformer cross-encoder (sequence-classification / bidirectional cross-attention) with average (mean) pooling and a sequence-classification / binary ranking head (LlamaBidirectionalForSequenceClassification / cross-encoder)
- License: Model weights: NVIDIA Open Model License (model weights blob); repository/source-code files: Apache-2.0 (per committed LICENSE). Container and packaging: NVIDIA container/NGC product terms (NVIDIA Software License / NGC catalog terms).
- Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/d896ceda696c5c6fe0abf65f63a77c691bbf4548/LICENSE, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blame/main/config.json, https://docs.nvidia.com/nemotron/nightly/nemotron/rerank/README.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

## Selection

### Recommended

- **Second-stage reranking in retrieval (RAG) pipelines** — Primary NVIDIA repository README and the NIM reference describe the checkpoint as a reranker that scores question/passage pairs and is evaluated as the reranking component in embedding+reranker pipelines.
  Scope: nvidia/llama-nemotron-rerank-1b-v2 (upstream checkpoint) and the nvidia-llama-nemotron-rerank-1b-v2 NIM packaging (serving variant)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2
- **Multilingual / cross-lingual question-answering retrieval reranking (as a reranker component in pipelines)** — Hugging Face model page and Build.NVIDIA modelcard report multilingual evaluation coverage across 26 languages and position the model as fine-tuned for multilingual/cross-lingual QA retrieval; reported numeric evaluations are pipeline-level (embedding+reranker).
  Scope: nvidia/llama-nemotron-rerank-1b-v2 (upstream checkpoint and model card statements)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Conditional

- **Reranking very long passages or long-document retrieval without chunking** — Confirm deployed serving-runtime token limits prior to use. Primary artifacts contain inconsistent sequence-length statements: NeMo docs state a 512-token concatenated query+passage maximum (NeMo rerank fine-tuning recipe), while committed upstream config blobs and NVIDIA support matrices/build.nvidia modelcard report support and optimized configurations for up to 8192 tokens. Deployment must verify the NIM container runtime contract (actual accepted sequence length) and, if necessary, implement chunking/truncation or pipeline-level document splitting.
  Scope: nvidia/llama-nemotron-rerank-1b-v2 (NeMo docs, upstream config.json, NIM support matrix, Build.NVIDIA modelcard)
  Evidence: https://docs.nvidia.com/nemotron/nightly/nemotron/rerank/README.html, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Avoid

- **Using the reranker as a first-stage retriever that exhaustively scores every document in a large knowledge base** — Primary repository README and NVIDIA serving artifacts describe the model as a reranker intended to score candidate passages (second-stage) rather than exhaustively scoring an entire document collection; exhaustive application is computationally infeasible.
  Scope: nvidia/llama-nemotron-rerank-1b-v2 (upstream checkpoint and NIM packaging)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

## Input preparation

### Semantic inputs

- The model consumes paired texts: a query (question) and one or more candidate passages to be scored for relevance (query first, passage second). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Accepted formats

- Serving accepts JSON-style payloads or lists of text pairs (query/passage pairs) as input parameters for the reranker microservice (JSON list of pairs or equivalent structured payload). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Preprocessing

- Primary artifacts document conflicting maximum sequence-length values: the NeMo rerank fine-tuning recipe lists a 512-token concatenated query+passage maximum, while upstream committed config fields and NVIDIA support matrices/build.nvidia modelcard record large max_position_embeddings / optimized sequence-length support (8192). Confirm the serving-runtime token limit before choosing a truncation or chunking strategy. Sources: https://docs.nvidia.com/nemotron/nightly/nemotron/rerank/README.html, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Tokenizer artifact (tokenizer.json) is present in the upstream repository, but the committed artifacts do not document the tokenizer package name/version or full preprocessing/tokenization pipeline (Unicode normalization, punctuation handling, special-token mapping). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/ec7eaa100882cdca3a671776ed4401ec81f54d18/tokenizer.json, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2

### Pre-submit validation

- Validate that inputs are formatted as query/passage pairs and that the total sequence length does not exceed the serving runtime's supported limit (the runtime limit must be confirmed via the NIM support matrix / NIM reference / Build.NVIDIA modelcard). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Task-specific formatting

- The upstream checkpoint and NIM packaging expect pairwise question/passage input format for scoring; query and passage ordering matters (query first, passage second) in the input contract. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2

## Output interpretation

### Outputs

- The model emits per-passage scalar floats (logits) representing relevance scores for each supplied passage in the request. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### Interpretation

- Higher float/logit indicates greater estimated relevance; some artifacts note users may apply a sigmoid activation if probability-like scores are required, but no primary calibration protocol (how to convert logits to calibrated probabilities or thresholds) is provided in the available artifacts. Sources: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

### Post-inference validation

- Treat reported scores as relative ranking signals and validate ranking behavior against held-out retrieval evaluations; available NVIDIA benchmark numbers are reported at the pipeline level (embedding + reranker), so validate reranker contribution within the intended pipeline. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

## Public benchmarks

### TextQA retrieval (BEIR/TextQA subsets: NQ, HotpotQA, FiQA, TechQA)

- Dataset/split: NQ / HotpotQA / FiQA / TechQA (BEIR/TextQA subsets) / not reported
- Metric/value: Recall@5 (average across listed subsets) / 73.64 % (`higher-is-better`)
- Model scope: llama-3.2-nv-embedqa-1b-v2 + llama-3.2-nv-rerankqa-1b-v2 (pipeline-level result reported by NVIDIA)
- Conditions: Reported as a pipeline (embedding model + reranker). The reported number is a pipeline result; reranker-only contribution is not isolated in the cited artifact.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- Locator: NIM reference benchmarks section
- Caveat: Pipeline-level result: dependent on the specified embedding model + reranker combination; reranker-only contribution is not isolated in the cited location.
- Caveat: Per-split/per-language breakdowns and exact evaluation script/version are not provided in the cited primary artifact.

### Multilingual retrieval (MIRACL)

- Dataset/split: MIRACL (multilingual benchmark) / not reported
- Metric/value: Recall@5 (average across languages) / 65.80 % (`higher-is-better`)
- Model scope: llama-3.2-nv-embedqa-1b-v2 + llama-3.2-nv-rerankqa-1b-v2 (pipeline-level result reported by NVIDIA)
- Conditions: Reported as a pipeline (embedding model + reranker). The reported number is a pipeline result; reranker-only contribution is not isolated in the cited artifact.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- Locator: NIM reference benchmarks section
- Caveat: Pipeline-level result and aggregated across languages; reranker-only isolated metrics are not provided in the cited primary artifact.
- Caveat: Per-language or per-split breakdowns are not present in the cited location.

### MLDR pipeline retrieval (embed + rerank)

- Dataset/split: MLDR (pipeline evaluation) / not reported
- Metric/value: Recall@5 (pipeline average reported) / 70.69 % (`higher-is-better`)
- Model scope: llama-nemotron-embed-1b-v2 + llama-nemotron-rerank-1b-v2 (pipeline-level result reported on Hugging Face model page)
- Conditions: Pipeline-level metric reported by the upstream model README; reranker-only contribution is not isolated.
- Source: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2
- Locator: Model card / README benchmark table
- Caveat: Reported metric is a pipeline result (embedding + reranker) per upstream README; reranker-only isolated metrics are not provided in the cited artifact.

## Comparisons

### alibaba-nlp-gte-reranker-modernbert-base-tei-cuda-1-9 — `insufficient-evidence`

- Task: Retrieval reranking
- Criteria: No primary-source, checkpoint-scoped matched-protocol comparison between this NVIDIA reranker checkpoint and the listed alternative was found in the available NVIDIA artifacts; the NVIDIA artifacts report pipeline-level metrics and do not include side-by-side cross-vendor matched-protocol tables.
- Rationale: Primary NVIDIA sources do not provide side-by-side matched-protocol benchmarks against this external alternative; direct comparative conclusions require checkpoint-scoped matched evaluations on the same datasets/splits with identical pipeline configurations.
- Comparison conditions: No shared protocol or matched benchmark in the cited NVIDIA materials.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2

### baai-bge-reranker-v2-m3-tei-cuda-1-9 — `insufficient-evidence`

- Task: Retrieval reranking
- Criteria: No primary-source, checkpoint-scoped matched-protocol comparison available in the NVIDIA materials checked.
- Rationale: No checkpoint-scoped comparative benchmark in the NVIDIA artifacts; available NVIDIA results are pipeline-level without cross-vendor matched tables.
- Comparison conditions: No shared protocol or matched benchmark in the cited NVIDIA materials.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

### nvidia-llama-3-2-nv-rerankqa-1b-v2-nim — `tradeoff`

- Task: Clarify identity / naming / provenance
- Criteria: Primary artifacts show an internal config _name_or_path alias and multiple naming conventions across commits and NIM references, indicating naming/alias ambiguity rather than documented performance difference; choose based on the served/packaged NIM identity and provenance requirements.
- Rationale: Repository config.json commit sets _name_or_path to "nvidia/llama-3.2-nv-rerankqa-1b-v2" while Build.NVIDIA and NIM references use llama-nemotron-rerank-1b-v2; no side-by-side performance table is provided to prefer one over the other, so this is a provenance/labeling tradeoff.
- Comparison conditions: Naming/alias evidence found in upstream config.json and NIM references; no matched benchmark protocol differentiating them was provided.
- Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard

### nvidia-llama-nemotron-rerank-vl-1b-v2-nim — `tradeoff`

- Task: Text-only reranking versus multimodal (VL) reranking
- Criteria: Different modality and architecture: the VL variant combines a SigLIP-2 vision encoder + Llama 3.2 language reranker producing a larger multimodal system (~1.7B parameters) and accepts image+text inputs, preventing direct quality-only comparison without a matched multimodal evaluation protocol.
- Rationale: NIM docs and the VL NGC container describe a multimodal architecture (SigLIP-2 vision encoder + Llama 3.2 language model) and different input modalities (image + text), so selection depends on modality requirements (text-only vs. multimodal).
- Comparison conditions: Different input modalities and architecture; a matched multimodal evaluation would be required for direct comparison.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-vl-1b-v2

### qwen-qwen3-reranker-0-6b-vllm-cuda13 — `insufficient-evidence`

- Task: Retrieval reranking
- Criteria: No checkpoint-scoped primary-source matched-protocol comparisons found in the NVIDIA materials checked.
- Rationale: NVIDIA primary artifacts do not include cross-vendor matched-protocol comparisons to this alternative; direct comparison requires matched evaluation protocols and datasets.
- Comparison conditions: No shared protocol or benchmark in the cited NVIDIA materials.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2

## Limitations and safety

### Limitations

- Applying the reranker exhaustively over a large knowledge base (scoring every document) is computationally infeasible; the model is intended as a second-stage reranker after candidate generation. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2
- Conflicting maximum sequence-length statements exist in primary artifacts (NeMo docs: 512 concatenated tokens; upstream config fields and NIM support matrices/Build.NVIDIA modelcard: max_position_embeddings / optimized support up to 8192). Deployment must confirm serving-runtime token limit prior to use. Sources: https://docs.nvidia.com/nemotron/nightly/nemotron/rerank/README.html, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Model naming/alias ambiguity exists: committed config.json sets _name_or_path to "nvidia/llama-3.2-nv-rerankqa-1b-v2" while other official artifacts use llama-nemotron-rerank-1b-v2; confirm intended labeling for provenance-sensitive workflows. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json, https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Training/data provenance detail is limited in the provided primary artifacts: the README commits a blended training set (800k samples) but does not provide per-dataset license-by-dataset or full preprocessing details. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/refs%2Fpr%2F12/README.md, https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blame/b736e636c7a36513c8b48a1937efb8087620d4e1/README.md

### Safety

- Users must comply with the stated model licensing: model weights are governed by the NVIDIA Open Model License and repository/source files reference Apache-2.0; container usage is governed by NGC/container terms. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/d896ceda696c5c6fe0abf65f63a77c691bbf4548/LICENSE, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-1b-v2
- NIM/NGC container images are governed by NVIDIA Software License Agreement and product-specific terms; users must accept NGC catalog terms and ensure appropriate access rights before pulling images. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-1b-v2
- Evidence gap: Primary artifacts do not provide explicit downstream calibration guidance (how to transform logits into calibrated probabilities or decision thresholds); users should develop and validate calibration for production thresholds using held-out data.

## Related upstream agent skills

### `exact-model`

NVIDIA's public Nemotron retrieval recipe skill distinguishes first-stage embedding from second-stage reranking and documents data preparation, evaluation, export, and deployment for the named Llama Nemotron retrieval families. Keep its recipe artifacts separate from the exact Forge NIM request and runtime contract.
- [nemotron-retrieval-recipes](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-retrieval-recipes)

## Primary sources

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/llama-nemotron-rerank-1b-v2/modelcard
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Forge-declared official modelcard for the covered serving variant; documents serving-level identity, input/output contract, token-limit claim, and model description for the named variant.
- Scope: nvidia-llama-nemotron-rerank-1b-v2
- Supports: Serving-level model identity for the named variant, stated supported token length claim (8192), input format as list of text pairs/JSON, output type as floats, runtime engine (TensorRT), multilingual coverage statement

### NIM reference: nvidia-llama-nemotron-rerank-1b-v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Official NIM runtime/reference documenting the specific NIM packaging for llama-nemotron-rerank-1b-v2, input/output contract and model developer identity.
- Scope: nvidia-llama-nemotron-rerank-1b-v2 (NIM runtime / reference)
- Supports: Input/output JSON contract (query/passage pairs), output as per-passage floats (logits), model developer identity, multilingual coverage statement

### NVIDIA NeMo Retriever (nemotron) rerank README

- URL: https://docs.nvidia.com/nemotron/nightly/nemotron/rerank/README.html
- Publisher: NVIDIA (NeMo docs)
- Type: `official-documentation`
- Primary because: Official NeMo documentation describing the base rerank model family and the NeMo reranking fine-tuning recipe.
- Scope: nemotron rerank family / upstream fine-tuning recipe
- Supports: Base model architecture description (cross-encoder / sequence classification), parameter-scale note (~1B), pooling method (avg), and a reported 512-token concatenated query+passage max in the NeMo fine-tuning recipe

### NGC catalog: llama-nemotron-rerank-1b-v2 container listing

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-1b-v2
- Publisher: NVIDIA (NGC catalog)
- Type: `official-documentation`
- Primary because: Official NGC container catalog entry for the rerank container describing container-level licensing and governance.
- Scope: nvidia-llama-nemotron-rerank-1b-v2 (NGC container)
- Supports: Container-level license/governance, NGC access/terms, container identity for the serving variant

### NIM support matrix for text reranking (latest)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Runtime/support matrix listing model ID and maximum token length claims for optimized configurations.
- Scope: nvidia-llama-nemotron-rerank-1b-v2 (runtime/support matrix)
- Supports: Support matrix listing maximum token length as 8192 for nvidia/llama-nemotron-rerank-1b-v2 and optimized memory/precision guidance

### NIM reference: llama-3.2-nv-rerankqa-1b-v2 (benchmark reporting)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: NIM reference page used by NVIDIA to report pipeline-level benchmark numbers (MIRACL, BEIR/TextQA subsets) for the embed+rerank pipeline combinations.
- Scope: llama-3.2-nv-rerankqa-1b-v2 (NIM reference / reported pipeline benchmarks)
- Supports: Pipeline-level benchmark numbers (e.g., Recall@5 on MIRACL and BEIR/TextQA subsets) and hardware/runtime notes

### Hugging Face model page: nvidia/llama-nemotron-rerank-1b-v2

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Canonical public model page for the checkpoint containing high-level model description, reported pipeline benchmark numbers, and links to committed repository artifacts.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (upstream repository/model card)
- Supports: Model description (reranker), multilingual evaluation claim, reported pipeline Recall@5 metric (MLDR/embedding+rerank pipeline), links to committed config/tokenizer/LICENSE blobs

### Hugging Face README (committed blob) for llama-nemotron-rerank-1b-v2

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/a1f8c0cc84e0e2c068a41a9b997b63684bea12cf/README.md
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Committed README blob containing model intent, high-level evaluation statements, and usage notes.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (specific README commit)
- Supports: Model intent, multilingual evaluation statements, and usage guidance

### Hugging Face README (blame view) with reported benchmarks

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blame/b736e636c7a36513c8b48a1937efb8087620d4e1/README.md
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Committed README blame view that includes pipeline benchmark statements and dataset coverage notes referenced by NVIDIA.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (README blame commit)
- Supports: Reported MIRACL and BEIR/TextQA pipeline benchmark statements and dataset coverage notes

### Hugging Face committed config.json (example commit)

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/8fd3e5d962d44cfe65d4ba0784eebed44cf136b0/config.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Committed model configuration revealing architecture fields, pooling, max_position_embeddings / rope scaling fields, and internal naming aliases.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (committed config.json)
- Supports: Architecture field (LlamaBidirectionalForSequenceClassification), pooling, rope_scaling/original_max_position_embeddings entries (8192 in this commit), _name_or_path alias in the config

### Hugging Face blamed main config.json (blame/main)

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blame/main/config.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Another committed view of config.json showing configuration fields (noting differing numeric fields in separate commits).
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (blame/main config.json)
- Supports: Committed config.json view (noting fields such as max_position_embeddings set to a large value in this view and vocab_size)

### Hugging Face tokenizer.json (committed artifact)

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/ec7eaa100882cdca3a671776ed4401ec81f54d18/tokenizer.json
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Committed tokenizer artifact present in the official repository; verifies presence of a tokenizer file though tokenizer package name/version and normalization details are not specified within the artifact metadata.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (committed tokenizer.json)
- Supports: Presence of tokenizer.json file in the upstream repository (tokenizer artifact present)

### Hugging Face committed LICENSE for rerank-1b-v2

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/d896ceda696c5c6fe0abf65f63a77c691bbf4548/LICENSE
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Committed LICENSE blob describing model-weight licensing and source-file licensing used by upstream repository.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (LICENSE blob)
- Supports: Model weights licensed under NVIDIA Open Model License; repository/source-code files referenced under Apache-2.0

### NIM getting-started (NGC & pull guidance) for text reranking

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/getting-started.html
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Official NIM getting-started documentation describing how to pull NIM containers, license acceptance, and runtime flags; relevant for container/license/runtime governance.
- Scope: nvidia-llama-nemotron-rerank-1b-v2 (NIM/NGC runtime guidance)
- Supports: Instructions to authenticate/pull NIM containers from NGC, license acceptance and runtime flags guidance

### NGC catalog: llama-nemotron-rerank-vl-1b-v2 container listing (multimodal variant)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-rerank-vl-1b-v2
- Publisher: NVIDIA (NGC catalog)
- Type: `official-documentation`
- Primary because: Official NGC container catalog entry for the multimodal VL rerank container used to document modality/architecture differences.
- Scope: nvidia-llama-nemotron-rerank-vl-1b-v2 (NGC container)
- Supports: Container listing and modality/architecture identification for the VL variant

### NIM reference: nvidia-llama-nemotron-rerank-vl-1b-v2 (multimodal NIM reference)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Publisher: NVIDIA (NIM docs)
- Type: `official-documentation`
- Primary because: Official NIM reference page describing the VL (multimodal) rerank variant, used to document modality/architecture differences relative to the text-only reranker.
- Scope: nvidia-llama-nemotron-rerank-vl-1b-v2 (NIM VL reference)
- Supports: Multimodal VL variant identity, architecture notes (SigLIP-2 vision encoder + Llama 3.2 language model), and modality (image + text) support

### Hugging Face model page: nvidia/llama-nemotron-rerank-vl-1b-v2

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Hugging Face repository for the VL variant documenting architecture and modality for the multimodal reranker.
- Scope: nvidia/llama-nemotron-rerank-vl-1b-v2 (upstream repository)
- Supports: VL variant architecture and modality (image + text) statements and committed README/config blobs

### Hugging Face model page: nvidia/llama-nemotron-rerank-1b-v2 — cited revision/file

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/refs%2Fpr%2F12/README.md
- Publisher: NVIDIA (Hugging Face repository)
- Type: `repository`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: nvidia/llama-nemotron-rerank-1b-v2 (upstream repository/model card)
- Supports: Exact audited claim citation

## Evidence gaps

- Evidence gap: tokenizer implementation package name/version not specified in the available primary artifacts (committed tokenizer.json is present but package name/version not declared).
- Evidence gap: exact Unicode normalization form, punctuation handling, and full preprocessing/tokenization pipeline (normalization, mapping of special tokens) are not specified in the available primary artifacts.
- Evidence gap: explicit example JSON request/response payloads with concrete numeric floats for inputs and outputs are not present in the available primary artifacts.
- Evidence gap: per-language and per-split benchmark breakdowns and exact evaluation script/version are not provided in the cited primary artifacts; reported benchmarks are aggregated pipeline averages.
- Evidence gap: serving-runtime token limit for the named NIM container is not unambiguously declared across primary artifacts; NeMo docs state 512 concatenated tokens while upstream config/support-matrix/build.nvidia list 8192 values — confirm runtime limits before deployment.
- Evidence gap: immutable upstream checkpoint revision/hash or commit-id for the exact served checkpoint is not reported in the available primary artifacts.
- Evidence gap: no primary-source, checkpoint-scoped matched-protocol comparisons to the listed external reranker alternatives were found in the available NVIDIA artifacts; direct comparative conclusions cannot be drawn from the available sources.
- Evidence gap: no primary calibration guidance (protocol to convert logits into calibrated probabilities or recommended thresholds) is provided in the available primary artifacts.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/discussions/6 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/discussions/6/files Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia/llama-nemotron-rerank-1b-v2/blob/refs%2Fpr%2F12/README.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
