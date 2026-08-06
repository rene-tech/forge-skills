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

- Research key: `build-nvidia-com-nvidia-llama-nemotron-rerank-vl-1b-v2-b32f924aa4`
- Independent audit: `revised`
- Researched: `2026-07-23T22:25:11.247555+00:00`

Upstream checkpoint llama-nemotron-rerank-vl-1b-v2 is documented by NVIDIA as a multimodal cross-encoder reranker (architecture: LlamaNemotronVLForSequenceClassification / model_type: llama_nemotron_vl_rerank) that accepts a text query and passages that may include text and/or images, aggregates final embeddings via mean pooling, and produces one float score per passage (relative relevance). Config-defined hyperparameters present in the upstream repository config.json include q_max_length=512, p_max_length=10240, force_image_size=512, dynamic_image_size=true, pooling='avg', query_prefix='query:', passage_prefix='passage:', prompt_template 'v1', tokenizer vocabulary size 128267, and torch_dtype bfloat16. The primary NVIDIA NIM/API and Build pages document the model as NIM-served for NeMo Retriever reranking and reference licensing under NVIDIA Nemotron Open Model License and a Llama 3.2 Community License. Benchmarks reported in primary artifacts are presented as pipeline-level results for the embedding+reranker pipeline (llama-nemotron-embed-vl-1b-v2 + llama-nemotron-rerank-vl-1b-v2) with an average reported value 73.98% (see benchmarks entry). Important evidence gaps include: no immutable checkpoint revision identifier located in inspected primary artifacts; no prescriptive logits-to-probability calibration procedure located in inspected primary artifacts; ViDoRe Recall@5 numeric rows for the exact checkpoint were not located in the inspected primary artifacts (see evidenceGaps).

## Identity

- Upstream name: llama-nemotron-rerank-vl-1b-v2
- Checkpoint/version: llama-nemotron-rerank-vl-1b-v2
- Immutable revision: Evidence gap: No immutable checkpoint revision identifier (commit hash or immutable artifact ID) was found in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json ; https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 )
- Parameter scale: approximately 1.7B
- Architecture/head: LlamaNemotronVLForSequenceClassification (model_type: llama_nemotron_vl_rerank); vision encoder + LLM composition declared upstream as SigLIP-2 400M vision encoder + Llama 3.2 1B language model (upstream-checkpoint evidence)
- License: Governing terms referenced in primary sources: NVIDIA Nemotron Open Model License (NVIDIA-hosted), and Llama 3.2 Community License referenced by NVIDIA primary artifacts. Primary artifacts reference licensing but do not present a single canonical weight-vs-code disambiguation (see evidenceUrls).
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/0dff00ba958ae46b0fb9c931fa2a4e3bf308404b/config.json, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2, https://nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license

## Selection

### Recommended

- **Multimodal document reranking in retrieval pipelines (text query vs passages that may contain text and/or images)** — Primary NVIDIA model card and NIM API docs describe this checkpoint as a VLM reranker intended to score text queries against text-only, image-only, or text+image passages and produce per-passage relevance scores.
  Scope: llama-nemotron-rerank-vl-1b-v2 (upstream-checkpoint evidence)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html

### Conditional

- **Deploy as the reranking component inside a larger NeMo/RAG multimodal retrieval pipeline** — Requires enabling rag-server/NIM multimodal reranker image-input flags (e.g., ENABLE_VLM_RERANKER_IMAGE_INPUT) and configuring APP_RANKING_MODELNAME to the VLM reranker; requires aligning runtime container image version and GPU resources per NIM support matrix. This is NIM-served runtime evidence (mapping shown in the rag-server docs where APP_RANKING_MODELNAME must be set to the upstream checkpoint name).
  Scope: llama-nemotron-rerank-vl-1b-v2 when deployed via the NeMo Retriever NIM container (NIM-served runtime evidence)
  Evidence: https://docs.nvidia.com/rag/2.6.0/multimodal-retriever.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/release-notes.html

### Avoid

- **Free-form text generation or instruction-following tasks** — Upstream config.json and model type identify the checkpoint as a sequence-classification / reranker model (binary classification head) rather than an instruction-following generative model; the repository and NIM docs describe scoring/ranking outputs, not generative text APIs.
  Scope: llama-nemotron-rerank-vl-1b-v2 (upstream-checkpoint evidence)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2

## Input preparation

### Semantic inputs

- Query (text) and passage (text and/or image) pairs: the query is text; each passage may include text and/or an attached image for VLM reranking (images are provided on passages for VLM reranking). Sources: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2

### Accepted formats

- API input format: JSON list of text pairs for text-only requests; when VLM image input is enabled, rag-server fetches and attaches base64-encoded image data to passage payloads for the reranker. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://docs.nvidia.com/rag/2.6.0/multimodal-retriever.html

### Preprocessing

- Prompt and prefix fields: config.json defines query_prefix as 'query:' and passage_prefix as 'passage:' and a prompt_template identified as 'v1'. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json
- Image sizing behavior: config.json sets force_image_size to 512 and dynamic_image_size to true (model supports variable image sizes and a forced 512px setting). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json
- Pooling: the config specifies average pooling (pooling: 'avg') to aggregate the final embedding before the classification head. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json

### Pre-submit validation

- Maximum token lengths: config.json lists q_max_length=512 and p_max_length=10240; inputs exceeding these limits must be chunked or truncated by implementers. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json
- NIM/runtime token limits and optimized configurations: NIM support and optimized configurations document a maximum token limit of 8192 for related reranker artifacts in runtime-optimized modes; implementers must reconcile which artifact/config is in use when selecting tokenization/truncation strategies. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html

### Task-specific formatting

- Task-formatting for API requests: supply a text query and one or more passages; when using rag-server multimodal mode, enable the VLM reranker image flag so rag-server attaches base64-encoded images to passage payloads. Sources: https://docs.nvidia.com/rag/2.6.0/multimodal-retriever.html, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html

## Output interpretation

### Outputs

- Model output is a one-dimensional list of float logits/scores, one score per passage, representing relative relevance. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2

### Interpretation

- Treat outputs as relative relevance scores (higher indicates higher estimated relevance); absolute calibration is not specified in the inspected primary artifacts and implementers should validate ranking thresholds downstream. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2

### Post-inference validation

- Post-inference checks: sanity-check extreme logits and validate end-to-end retrieval quality in downstream pipelines; primary artifacts provide no prescriptive calibration procedure. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2
- Evidence gap: No prescriptive logits-to-probability calibration or trained probability-mapping guidance was located in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2

## Public benchmarks

### multimodal retrieval pipeline evaluation (embedding + reranker)

- Dataset/split: BEIR retrieval + TechQA (pipeline components: embedding + reranker) / not reported
- Metric/value: average score / 73.98% (`higher-is-better`)
- Model scope: Pipeline: llama-nemotron-embed-vl-1b-v2 + llama-nemotron-rerank-vl-1b-v2 (pipeline-level result per primary artifacts)
- Conditions: Pipeline evaluation as reported in primary NIM/Hugging Face artifacts; the reported value is an aggregate across listed datasets (BEIR+TechQA/MIRACL/MLQA/MLDR) and depends on both the embedding and reranker components.
- Source: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Locator: Benchmark results section (pipeline-level benchmark rows) in the NIM reference for nvidia-llama-nemotron-rerank-vl-1b-v2
- Caveat: This numeric value is a pipeline-level aggregate requiring both an embedding checkpoint and the reranker checkpoint; the primary artifact attributes the numbers to the embedding+reranker pipeline rather than the reranker alone.
- Caveat: Exact dataset splits and table/figure numbering are not specified in the inspected primary artifacts; implementers should consult the cited primary artifact for dataset list and aggregation method.

## Comparisons

### nvidia/llama-3_2-nv-rerankqa-1b-v2 — `insufficient-evidence`

- Task: multimodal/document reranking (NVIDIA sibling reranker)
- Criteria: No protocol-matched numeric cross-comparison table for ViDoRe/Recall@5 between these exact checkpoints was located in the inspected primary artifacts; differing supported modalities and sequence-length notes are present across NIM references.
- Rationale: Both are NVIDIA reranker checkpoints documented in NIM references but primary artifacts do not present a single matched-protocol numeric table comparing these exact checkpoints under identical evaluation conditions.
- Comparison conditions: Checked NIM reference docs for both checkpoints; no shared numeric table located in the inspected primary artifacts.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2

### nvidia/llama-nemotron-rerank-1b-v2 — `insufficient-evidence`

- Task: text-only vs VLM reranking (NVIDIA related reranker variants)
- Criteria: Although both are NVIDIA rerankers, primary artifacts do not present a protocol-matched numeric table that directly compares these exact checkpoints under identical evaluation conditions.
- Rationale: Text-only and VLM NIM references document different supported max sequence lengths and modality handling; no protocol-matched numeric cross-eval table was found in the inspected primary artifacts.
- Comparison conditions: Checked the NIM reference for both checkpoints; no matched numeric cross-eval table found in the inspected primary artifacts.
- Evidence: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2

## Limitations and safety

### Limitations

- Evidence gap: ViDoRe Recall@5 numeric rows for llama-nemotron-rerank-vl-1b-v2 were not present in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Evidence gap: No immutable checkpoint revision identifier (commit hash or immutable artifact ID) was found in the inspected primary artifacts (checked: Hugging Face model page and config.json, Build model page, NIM API reference). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Configuration divergence: NIM/runtime documentation for related text-only reranker artifacts reports max-sequence-length notes (8192) that differ from the upstream config.json p_max_length=10240; implementers must reconcile which artifact/config is authoritative for their deployment. Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2, https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html
- Evidence gap: No prescriptive logits-to-probability calibration procedure or trained probability-mapping guidance was located in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Evidence gap: Full tokenizer end-to-end specification with examples for all multimodal input permutations (text-only, image-only, image+text) is not exhaustively enumerated in the inspected primary artifacts (checked: repository config.json and model README). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json, https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2

### Safety

- Evidence gap: Primary source artifacts inspected do not provide scoped PHI/clinical-use prohibitions or detailed data-handling restrictions for this checkpoint; no primary-source clinical/PHI guidance located in the inspected artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ). Sources: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Forge policy: Treat the model as unsuitable for unreviewed clinical decision-making or PHI processing without appropriate legal/compliance review and expert validation (conservative Forge policy requirement).

## Related upstream agent skills

### `exact-model`

NVIDIA's public Nemotron retrieval recipe skill distinguishes first-stage embedding from second-stage reranking and documents data preparation, evaluation, export, and deployment for the named Llama Nemotron retrieval families. Keep its recipe artifacts separate from the exact Forge NIM request and runtime contract.
- [nemotron-retrieval-recipes](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-retrieval-recipes)

## Primary sources

### NIM reference: nvidia-llama-nemotron-rerank-vl-1b-v2 (API docs)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM/API reference documenting the NIM-served checkpoint, benchmark rows (pipeline-level), input/output semantics, and licensing pointers for this exact checkpoint.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: checkpoint identity
- Supports: multimodal capability statement
- Supports: output semantics
- Supports: benchmark pipeline results (embed+rerank)
- Supports: licensing pointers

### Hugging Face model page: nvidia/llama-nemotron-rerank-vl-1b-v2

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2
- Publisher: Hugging Face (model owner: NVIDIA)
- Type: `model-card`
- Primary because: Official upstream model repository and model card maintained by NVIDIA for the exact checkpoint; documents multimodal capability, architecture summary, and benchmark statements.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: checkpoint identity
- Supports: multimodal capability
- Supports: architecture composition
- Supports: pipeline benchmark rows (embed+rerank)

### config.json (nvidia/llama-nemotron-rerank-vl-1b-v2) — cited blob (commit path)

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json
- Publisher: Hugging Face (repository contents maintained by NVIDIA)
- Type: `repository`
- Primary because: Repository configuration file providing exact config fields (model_type, q_max_length, p_max_length, image_size, dynamic_image_size, force_image_size, pooling, query_prefix, passage_prefix, tokenizer vocabulary size, torch_dtype).
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: model_type
- Supports: q_max_length
- Supports: p_max_length
- Supports: image_size
- Supports: dynamic_image_size
- Supports: force_image_size
- Supports: pooling
- Supports: query_prefix
- Supports: passage_prefix
- Supports: tokenizer vocabulary size
- Supports: torch_dtype

### Repository README (nvidia/llama-nemotron-rerank-vl-1b-v2) — cited blob

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/0dff00ba958ae46b0fb9c931fa2a4e3bf308404b/README.md
- Publisher: Hugging Face (model owner: NVIDIA)
- Type: `repository`
- Primary because: Model README providing accepted input modalities, output semantics, and usage notes for this exact checkpoint.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: input modalities
- Supports: output semantics
- Supports: model parameter scale
- Supports: pooling and loss details

### NeMo Retriever Text Reranking Overview (NVIDIA Docs)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Describes the NeMo Retriever reranking NIM packaging, supported multimodal reranking behavior, and input modality expectations for the VLM reranker.
- Scope: llama-nemotron-rerank-vl-1b-v2 (NIM packaging/runtime mapping)
- Supports: multimodal reranking behavior
- Supports: query/passage modality rules
- Supports: NIM Docker image and service mapping

### RAG multimodal retriever integration docs (NVIDIA)

- URL: https://docs.nvidia.com/rag/2.6.0/multimodal-retriever.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Describes rag-server integration flags, service names, container image, and runtime conditions for enabling VLM reranker image input and mapping APP_RANKING_MODELNAME to the upstream checkpoint name.
- Scope: llama-nemotron-rerank-vl-1b-v2 (NIM-served runtime mapping)
- Supports: ENABLE_VLM_RERANKER_IMAGE_INPUT usage
- Supports: APP_RANKING_MODELNAME mapping to upstream checkpoint
- Supports: runtime container image name

### NVIDIA Nemotron Open Model License (NVIDIA-hosted)

- URL: https://nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Authoritative license text referenced by NVIDIA primary artifacts governing model use.
- Scope: license governing model artifacts as referenced by NVIDIA
- Supports: license terms referenced by modelcard and NIM docs

### NeMo Retriever Text Reranking - Release Notes

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Release notes describing NIM runtime versions and supported modalities for the VLM reranker and runtime improvements.
- Scope: nemo-retriever text-reranking NIM (llama-nemotron-rerank-vl-1b-v2)
- Supports: NIM version notes
- Supports: supported modalities
- Supports: runtime improvements

### NeMo Retriever Text Reranking - Support Matrix

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-reranking/latest/support-matrix.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Support matrix documenting optimized configurations, precision options, and maximum token limits for reranker NIM artifacts.
- Scope: nemo-retriever text-reranking
- Supports: supported precisions and token limits
- Supports: optimized configuration notes

### Build: llama-nemotron-rerank-vl-1b-v2 model page

- URL: https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official product/build page mapping the NIM/serving artifact to the upstream checkpoint and summarizing intended use and license references.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: checkpoint identity
- Supports: intended use
- Supports: licensing references

### NVIDIA Open Model License Agreement (developer download PDF)

- URL: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical license PDF referenced by NVIDIA Build and NIM pages.
- Scope: license governing model artifacts as referenced by NVIDIA
- Supports: license terms referenced by modelcard and NIM docs

### config.json (nvidia/llama-nemotron-rerank-vl-1b-v2) — blame/cited blob

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blame/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json
- Publisher: Hugging Face (repository contents maintained by NVIDIA)
- Type: `repository`
- Primary because: Repository configuration blob (blame view) enumerating config fields and values used by this checkpoint.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: detailed config fields (pooling, prefixes, lengths, vocabulary size, model_type, architecture mapping)

### Hugging Face model page: nvidia/llama-nemotron-rerank-vl-1b-v2 — cited revision/file

- URL: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/0dff00ba958ae46b0fb9c931fa2a4e3bf308404b/config.json
- Publisher: Hugging Face (model owner: NVIDIA)
- Type: `model-card`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: llama-nemotron-rerank-vl-1b-v2
- Supports: Exact audited claim citation

### Cited official first-party source

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2
- Publisher: docs.api.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-llama-nemotron-rerank-vl-1b-v2
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2
- Publisher: docs.api.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-llama-nemotron-rerank-vl-1b-v2
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: ViDoRe Recall@5 numeric rows for llama-nemotron-rerank-vl-1b-v2 were not located in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ).
- Evidence gap: No immutable checkpoint revision identifier (commit hash or immutable artifact ID) was found in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json ; https://build.nvidia.com/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ).
- Evidence gap: No prescriptive logits-to-probability calibration procedure or trained probability-mapping guidance was located in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ; https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-vl-1b-v2 ).
- Evidence gap: Full tokenizer end-to-end specification with examples for all multimodal input permutations (text-only, image-only, image+text) is not exhaustively enumerated in the inspected primary artifacts (checked: https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/316ffa2170b7a2ffba32ebc1c32b2fbef0740ed3/config.json ; https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2 ).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 45 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: unexpected property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1]: $.inputPreparation.preprocessing[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1]: $.outputInterpretation.outputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[1]: $.outputInterpretation.validation[1]: expected object, got str Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0]: $.limitations[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1]: $.limitations[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2]: $.limitations[2]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3]: $.limitations[3]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4]: $.limitations[4]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.evidenceGaps[0]: $.evidenceGaps[0]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.evidenceGaps[1]: $.evidenceGaps[1]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.evidenceGaps[2]: $.evidenceGaps[2]: expected string, got dict Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.family must equal research key 'build-nvidia-com-nvidia-llama-nemotron-rerank-vl-1b-v2-b32f924aa4', got 'build-n Nvidia-com-nvidia-llama-nemotron-rerank-vl-1b-v2-b32f924aa4': $.family must equal research key 'build-nvidia-com-nvidia-llama-nemotron-rerank-vl-1b-v2-b32f924aa4', got 'build-n Nvidia-com-nvidia-llama-nemotron-rerank-vl-1b-v2-b32f924aa4' Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/BAAI/bge-reranker-v2-m3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/nvidia/llama-3_2-nv-rerankqa-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-Reranker-0.6B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Qwen/Qwen3-VL-Reranker-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[2] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[3] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap: $.limitations[4] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/nvidia/llama-nemotron-rerank-vl-1b-v2/blob/0dff00ba958ae46b0fb9c931fa2a4e3bf308404b/config.json: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.api.nvidia.com/nim/reference/nvidia-llama-3_2-nv-rerankqa-1b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-rerank-1b-v2: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
