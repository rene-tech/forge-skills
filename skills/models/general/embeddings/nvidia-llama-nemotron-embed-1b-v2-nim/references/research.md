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

- Research key: `build-nvidia-com-nvidia-llama-nemotron-embed-1b-v2-e33887bdd4`
- Independent audit: `revised`
- Researched: `2026-07-23T21:42:48.263795+00:00`

The Forge variant corresponds to NVIDIA's text-only checkpoint llama-nemotron-embed-1b-v2 (default name nvidia/llama-nemotron-embed-1b-v2). Primary NVIDIA sources (Build.NVIDIA model card, NIM reference, Hugging Face model card, Nemo microservices customizer) report the checkpoint as a fine-tuned Llama 3.2 1B retriever (transformer-encoder, bi-encoder trained with contrastive learning) producing 2048-dimensional embeddings for multilingual dense retrieval across 26 languages and supporting input contexts up to 8192 tokens. The model entity configuration lists parameter count 1,000,000,000 and precision bf16-mixed; the NIM container image tag is nvcr.io/nim/nvidia/llama-nemotron-embed-1b-v2:1.13.0. Official NIM performance documentation provides latency and throughput measurements for the Nemo Retriever text-embedding NIM under specified batch and concurrency settings. Primary sources do not publish retrieval-metric numeric benchmarks (e.g., NDCG/Recall) tied to this text-only checkpoint's model card or NIM reference; tokenizer identifier, explicit pooling method, and packaging provenance (whether the NIM is an unchanged wrapper around an upstream binary) are not specified in the checked primary sources and are recorded as evidence gaps.

## Identity

- Upstream name: nvidia/llama-nemotron-embed-1b-v2
- Checkpoint/version: llama-nemotron-embed-1b-v2
- Immutable revision: not reported
- Parameter scale: 1,000,000,000
- Architecture/head: Fine-tuned Llama 3.2 1B retriever; Transformer encoder; bi-encoder trained with contrastive learning
- License: Model weights: NVIDIA Open Model License; Code/tooling: Llama 3.2 Community Model License (distinction reported in customizer documentation)
- Evidence: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/embedding.html, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2

## Selection

### Recommended

- **Multilingual semantic/dense retrieval for question-answering over large text corpora** — Build.NVIDIA model card and the NIM reference describe intended use for multilingual dense retrieval and long-document QA support across 26 languages using 2048-dimensional embeddings produced by a bi-encoder.
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- **Embedding generation for retrieval-augmented generation (RAG) backends and multilingual/cross-lingual retrieval pipelines** — Primary sources state the model is a bi-encoder trained with contrastive learning producing 2048-dimensional embeddings intended for indexing and similarity search; Hugging Face and Build.NVIDIA list RAG/retrieval scenarios as intended uses.
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard

### Conditional

- **Domain adaptation or fine-tuning for specialized retrieval domains** — Primary Hugging Face model card states the model can be customized for domain-specific use cases but does not publish the fine-tuning protocol or artifacts; obtain, validate, and test any customization artifacts and procedures before production use.
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2
- **Using NIM-provided runtimes for high-throughput serving with latency constraints** — Use only under the documented NIM deployment and performance conditions (GPU configuration, batch sizes, concurrency) and validate under your target hardware; NIM performance page provides example latency/throughput but you must reproduce under your environment.
  Scope: nvidia-llama-nemotron-embed-1b-v2 (NIM serving/runtime)
  Evidence: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/embedding.html, https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html

### Avoid

- **Using the text-only checkpoint for image or multimodal embedding tasks** — Primary sources document multimodal image support on separate NeMo Retriever/embedded VL variants and the text-only checkpoint is described as text-only; do not assume image inputs are supported by this text-only checkpoint.
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard
- **Treating embeddings as calibrated probabilistic confidences or final decision outputs without downstream validation** — Primary sources describe embeddings as retrieval features produced by a contrastive-trained bi-encoder and do not provide calibration semantics or recommended decision thresholds.
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- **Clinical or PHI-sensitive decision making without documented PHI handling or clinical validation** — Primary sources do not publish PHI handling or clinical/regulatory validation guidance tied to this checkpoint (see safety evidence gap).
  Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
  Evidence: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2

## Input preparation

### Semantic inputs

- Text queries and passages (text-only inputs) are the accepted semantic input for the text-only checkpoint, supporting long documents up to 8192 tokens. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2

### Accepted formats

- Plain text strings representing queries or passages (text inputs) up to 8192 tokens; the text-only checkpoint is documented to accept text inputs only. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard

### Preprocessing

- Primary sources do not publish tokenizer identifier, vocabulary, or tokenization algorithm for the text-only checkpoint; the modelcard and NIM reference state token-length limits but omit tokenizer implementation details. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- Model entity configuration lists precision as bf16-mixed in the Nemo microservices customizer documentation; use this as the documented default precision for deployments unless overridden. Sources: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/embedding.html

### Pre-submit validation

- Primary sources specify input format limits (e.g., max 8192 tokens for text) but do not document additional formal input-validation steps or health-check procedures specific to this checkpoint in the model card or NIM reference. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard

### Task-specific formatting

- Primary sources do not publish canonical prompt templates, prefixing conventions, or exact pooling/prompt formatting instructions for the text-only checkpoint; these details are absent from the checked model card and NIM reference. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2

## Output interpretation

### Outputs

- The checkpoint emits dense embedding vectors (arrays of floats) with embedding dimensionality 2048 (supports Matryoshka/dynamic embedding sizing features). Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2

### Interpretation

- Primary sources describe embeddings as retrieval features produced by a bi-encoder trained with contrastive learning; they do not provide probabilistic or calibrated score semantics for embedding magnitudes. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2

### Post-inference validation

- Primary sources do not publish post-inference calibration procedures, recommended numeric similarity thresholds, or standardized downstream validation protocols for embeddings produced by the text-only checkpoint. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2

## Public benchmarks

### Serving performance (passage embedding latency)

- Dataset/split: not applicable (serving/runtime measurement) / not reported
- Metric/value: average latency (ms) / 188.4 ms (passage inputs of 300 tokens, batch size 64, concurrency 1) (`lower-is-better`)
- Model scope: nemo-retriever text-embedding NIM (serving/runtime measurements reported in NIM performance docs)
- Conditions: Passage inputs of 300 tokens; batch size 64; concurrency 1 (as reported on NIM performance page).
- Source: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Locator: Performance page (reported latency/throughput measurements)
- Caveat: These are NIM serving/runtime measurements as reported on the Nemo Retriever performance page; primary sources do not explicitly tie these rows to a specific model-card evaluation table for retrieval metrics.
- Caveat: Hardware, exact image, container tag, and deployment configuration affect reproducibility; reproduce under target environment.

### Serving performance (passage embedding throughput)

- Dataset/split: not applicable (serving/runtime measurement) / not reported
- Metric/value: throughput (inputs/s) / 338.7 inputs/s (passage inputs of 300 tokens, batch size 64, concurrency 1) (`higher-is-better`)
- Model scope: nemo-retriever text-embedding NIM (serving/runtime measurements reported in NIM performance docs)
- Conditions: Passage inputs of 300 tokens; batch size 64; concurrency 1.
- Source: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Locator: Performance page (reported latency/throughput measurements)
- Caveat: These performance numbers are runtime measurements from the NIM performance documentation and may depend on the NIM runtime version, GPU SKU, and container configuration.
- Caveat: Primary sources do not provide a benchmark table of retrieval effectiveness (e.g., NDCG) tied to this text-only model card.

### Serving performance (query latency example)

- Dataset/split: not applicable (serving/runtime measurement) / not reported
- Metric/value: average latency (ms) / 6.6 ms (query inputs of 20 tokens, concurrency 1) (`lower-is-better`)
- Model scope: nemo-retriever text-embedding NIM (serving/runtime measurements reported in NIM performance docs)
- Conditions: Query inputs of 20 tokens; concurrency 1.
- Source: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Locator: Performance page (reported latency/throughput measurements)
- Caveat: Runtime measurements depend on deployment configuration; reproduce under target environment.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Head-to-head retrieval-effectiveness comparisons with other Forge-listed embedding models
- Criteria: No protocol-matched numeric head-to-head comparisons for retrieval-effectiveness (dataset/split/metric) naming this exact checkpoint were published in the checked primary sources.
- Rationale: Primary sources (Build.NVIDIA model card, NIM reference, Hugging Face model card) do not publish protocol-matched numeric comparisons for retrieval effectiveness tied to this exact text-only checkpoint; only NIM runtime performance (latency/throughput) is reported.
- Comparison conditions: Checked the model card and NIM reference for explicit numeric comparisons and found none; runtime performance measurements are present but do not constitute retrieval-effectiveness head-to-head comparisons.
- Evidence: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2

## Limitations and safety

### Limitations

- No numeric retrieval-effectiveness benchmark values (dataset, split, metric, numeric value) for the text-only checkpoint are published on the official model card or NIM reference pages. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- Tokenizer identifier, vocabulary, and tokenization algorithm are not specified in the checked primary sources for the text-only checkpoint. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.nvidia.com/nemo/microservices/latest/customizer/models/embedding.html
- The exact packaging/provenance relationship between the NIM/container and any underlying upstream checkpoint binary (whether the NIM is an unchanged wrapper around an upstream model-file) is not declared in the checked primary sources. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-embed-1b-v2, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- Multimodal evaluation results referenced for sibling VL variants are described without full numeric disclosure in the checked primary sources, limiting external comparability. Sources: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard

### Safety

- Primary sources label the model as ready for commercial use. Sources: https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2, https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard
- Evidence gap: Primary NVIDIA sources checked (Build.NVIDIA model card, NIM reference, Hugging Face model card) do not publish PHI handling guidance, clinical validation, or regulated-use approvals for this text-only checkpoint. Sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2

## Related upstream agent skills

### `exact-model`

NVIDIA's public Nemotron retrieval recipe skill distinguishes first-stage embedding from second-stage reranking and documents data preparation, evaluation, export, and deployment for the named Llama Nemotron retrieval families. Keep its recipe artifacts separate from the exact Forge NIM request and runtime contract.
- [nemotron-retrieval-recipes](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/nemotron-retrieval-recipes)

## Primary sources

### Build.NVIDIA modelcard for Llama Nemotron Embed 1B v2

- URL: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard
- Publisher: NVIDIA Build (official modelcard)
- Type: `model-card`
- Primary because: Official Build.NVIDIA model card providing checkpoint identity, intended use, architecture, parameter count, embedding dimension, and max sequence length for the text-only checkpoint.
- Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
- Supports: identity fields (checkpoint name, architecture type, parameter count, embedding dimension)
- Supports: intended use statements (multilingual dense retrieval, QA)
- Supports: maximum sequence length (8192 tokens)
- Supports: supported languages and long-document support

### Build.NVIDIA model page for Llama Nemotron Embed 1B v2 (canonical Build landing)

- URL: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Canonical Build.NVIDIA landing page declared by Forge as the official starting source for the serving variant.
- Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
- Supports: high-level model identity and multilingual retrieval claims
- Supports: release date and copyright notice

### NIM reference: nvidia-llama-nemotron-embed-1b-v2

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM reference documenting the NIM packaging, architecture description, and input length limits for the text-only checkpoint.
- Scope: nvidia-llama-nemotron-embed-1b-v2 (text-only NIM reference)
- Supports: architecture description (Fine-tuned Llama 3.2 1B retriever)
- Supports: max sequence length (8192 tokens) and input acceptance statements
- Supports: embedding dimension (2048) and intended retrieval use
- Supports: bi-encoder/contrastive training description

### NVIDIA Llama Nemotron Embed 1B v2 — Hugging Face model card

- URL: https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2
- Publisher: NVIDIA (Hugging Face model listing)
- Type: `model-card`
- Primary because: Official NVIDIA-hosted Hugging Face model card describing the checkpoint identity, architecture, parameter count, licensing references, and intended uses.
- Scope: llama-nemotron-embed-1b-v2 (text-only checkpoint)
- Supports: identity fields (architecture, parameter count, embedding dimension)
- Supports: license references (NVIDIA Open Model License and Llama 3.2 Community Model License)
- Supports: statements of intended commercial readiness and developer customization
- Supports: bi-encoder and contrastive training description

### Nemo Retriever text-embedding NIM release notes

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/release-notes.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM release notes documenting runtime changes and preserved supported modalities and API compatibility for the NeMo Retriever embedding NIMs.
- Scope: nemo-retriever text-embedding NIMs (runtime/release notes)
- Supports: runtime upgrade notes for Nemo Retriever embedding NIMs
- Supports: statement that model, supported modalities, and API are unchanged in the 2.0.0 release

### Nemo Retriever text-embedding performance (NIM docs)

- URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/performance.html
- Publisher: NVIDIA NIM documentation
- Type: `official-documentation`
- Primary because: Official NIM performance page reporting latency and throughput measurements for the Nemo Retriever text-embedding NIM.
- Scope: nemo-retriever text-embedding NIM performance (serving/runtime measurements)
- Supports: latency and throughput measurements for query and passage inputs under specified batch/concurrency conditions

### Nemo microservices customizer: Embedding Models documentation

- URL: https://docs.nvidia.com/nemo/microservices/latest/customizer/models/embedding.html
- Publisher: NVIDIA NIM / Nemo microservices documentation
- Type: `official-documentation`
- Primary because: Official documentation listing model parameter count, default model name, NIM container tag, and model precision as part of the embedding models customizer docs.
- Scope: embedding models (model entity configuration and deployment defaults)
- Supports: model parameter count (1,000,000,000)
- Supports: default model name nvidia/llama-nemotron-embed-1b-v2
- Supports: NIM container image tag nvcr.io/nim/nvidia/llama-nemotron-embed-1b-v2:1.13.0
- Supports: deployment configuration (1 GPU with 80 GB) and model precision (bf16-mixed)

### NGC catalog: llama-nemotron-embed-1b-v2 container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-embed-1b-v2
- Publisher: NVIDIA (NGC catalog)
- Type: `official-documentation`
- Primary because: Official NGC catalog page for the NIM container providing container governance, licensing references, and container metadata.
- Scope: nvidia-llama-nemotron-embed-1b-v2 (NIM container)
- Supports: container licensing and governance references (NVIDIA proprietary container license and NVIDIA Open Model License for model use)
- Supports: container metadata (compressed size, last update timestamp)

## Evidence gaps

- No primary-source tokenizer identifier, vocabulary name, or tokenization algorithm was found for the text-only checkpoint at the checked primary URLs: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard and https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2 (inspected model card and NIM reference pages; tokenizer details not present).
- No explicit statement in the checked primary sources declares whether the NIM/container is an unchanged wrapper over an upstream checkpoint binary or applies packaging-level changes; checked URLs: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/llama-nemotron-embed-1b-v2 and https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2 (no packaging/provenance statement found).
- No numeric retrieval-effectiveness benchmark values (dataset, split, metric, numeric value) tied to the text-only checkpoint were found on the checked primary model pages and NIM reference; checked URLs and locators: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard (model card page root) and https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2 (NIM reference page root); neither page contains a numeric retrieval-effectiveness table for this checkpoint.
- The precise pooling method (mean/CLS/other) used to produce final embeddings for the text-only checkpoint is not specified in the checked primary sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard and https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2 (no pooling description found).
- No primary-source statement was found in the checked NVIDIA pages about recommended post-inference calibration procedures or numeric similarity thresholds for downstream use; checked URLs: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard and https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2.
- No explicit PHI/clinical/regulatory guidance or approved regulated-use statements were present in the checked primary sources for this checkpoint; checked URLs: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2/modelcard, https://docs.api.nvidia.com/nim/reference/nvidia-llama-nemotron-embed-1b-v2, https://huggingface.co/nvidia/llama-nemotron-embed-1b-v2.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/llama-nemotron-embed-1b-v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.sourcesUsed: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.benchmarks[3]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
