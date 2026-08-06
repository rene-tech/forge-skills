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

- Research key: `docs-nvidia-com-nim-cosmos-embed1-latest-quickstart-guide-html-9090228f0f`
- Independent audit: `revised`
- Researched: `2026-07-23T23:37:44.870042+00:00`

Cosmos‑Embed1 NIM v1.1.0 is an NVIDIA Inference Microservice that serves aligned video and text embeddings via an OpenAI‑Embeddings‑compatible HTTP endpoint (POST /v1/embeddings). NIM v1.1.0 release notes document added support for video_frames input (8 frames per item) and an updated video decoding dependency. The NIM performance page provides GPU‑specific latency and bulk throughput microbenchmark tables (NIM‑serving runtime evidence). Upstream publisher artifacts (Hugging Face config.json and model pages, TAO and VSS docs, NGC catalog, and Cosmos Lab research page) report per‑variant checkpoint configuration (embed_dim, resolution, num_video_frames) and upstream retrieval/classification metrics; these upstream results are explicitly upstream‑checkpoint evidence and are distinct from NIM‑serving runtime behavior. Primary evidence gaps identified in the inspected sources include immutable NIM container/checkpoint digests, NVIDIA‑published parameter counts per variant, tokenizer/tokenization implementation details in NIM/TAO/VSS docs, and an explicit recommended distance metric or canonical embedding normalization in the inspected NIM/TAO/VSS documentation.

## Identity

- Upstream name: Cosmos-Embed1
- Checkpoint/version: Cosmos-Embed1 NIM v1.1.0
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: Joint video–text dual-encoder: EVA‑ViT‑G visual encoder + Q‑Former aggregator + BERT‑style text encoder with contrastive alignment (CLIP/SigLIP‑style) as described in VSS/TAO documentation (upstream architecture description).
- License: NVIDIA Open Model License
- Evidence: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html

## Selection

### Recommended

- **Text-to-video retrieval (semantic search) using embeddings** — NIM introduction, VSS model doc, NGC/TAO listings and the NIM API reference describe Cosmos‑Embed1 as producing aligned embeddings for text and short‑form videos enabling text‑to‑video retrieval and semantic search. The NIM serves embeddings via POST /v1/embeddings.
  Scope: Cosmos-Embed1 NIM v1.1.0 (NIM-served embeddings via POST /v1/embeddings)
  Evidence: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html
- **Video-to-video retrieval and similarity matching** — NGC TAO model listing and VSS documentation list inverse video search and video‑to‑video search as intended applications, describing a unified embedding space for videos and text.
  Scope: Cosmos-Embed1 NIM v1.1.0 (NIM-served embeddings)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html
- **Semantic deduplication, content clustering, and k‑NN downstream tasks** — NGC catalog, NIM introduction and TAO documentation list semantic deduplication, clustering, and k‑NN style downstream usage as supported downstream applications for embeddings.
  Scope: Cosmos-Embed1 NIM v1.1.0 (NIM-served embeddings)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

### Conditional

- **High‑throughput production embedding inference via Real‑Time Embedding microservice or NIM container** — Follow Real‑Time Embedding microservice deployment guidance and NIM performance guidance (environment variables, validated GPU list, bulk request‑size guidance). Validate throughput/latency against the published NIM performance microbenchmarks for target hardware.
  Scope: Cosmos-Embed1 NIM v1.1.0 deployed via Real‑Time Embedding microservice or NIM container
  Evidence: https://docs.nvidia.com/vss/3.2.0/real-time-embedding.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/quickstart-guide.html
- **Use of upstream fine‑tuned variants or LoRA adapters in production (only after provenance verification)** — Confirm provenance and required fine‑tuning artifacts; treat Hugging Face fine‑tuned artifacts as upstream‑checkpoint evidence unless NVIDIA publishes canonical provenance linking them to an NGC/TAO or NIM immutable release.
  Scope: Upstream‑checkpoint variants (Hugging Face publisher artifacts)
  Evidence: https://huggingface.co/nvidia/Cosmos-Embed1-448p, https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html

### Avoid

- **Use as a generative language model for token‑level text generation** — Primary NIM docs and API describe Cosmos‑Embed1 as a joint video‑text embedder returning embedding vectors via POST /v1/embeddings; there is no primary‑source evidence in the inspected NIM docs that the model exposes token‑level generation/completion capability.
  Scope: Cosmos-Embed1 NIM v1.1.0
  Evidence: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html

## Input preparation

### Semantic inputs

- Accepted input modalities are text and short‑form video frames; the NIM service accepts text and video inputs and exposes embedding generation endpoints. Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html, https://docs.nvidia.com/vss/3.2.0/real-time-embedding.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/api-reference.html
- Video input can be provided as sampled frames (video_frames); NIM v1.1.0 documents support for video_frames with 8 frames per item. Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

### Accepted formats

- POST /v1/embeddings is the documented inference endpoint and supports request_type modes used for text and video embedding generation. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html
- bulk_text and bulk_video modes are documented for large‑batch processing and the performance page provides example request sizes for throughput testing. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html

### Preprocessing

- Input videos using supported codecs and container formats are handled by the NIM; v1.1.0 release notes indicate an updated video decoding dependency (PyNvVideoCodec==2.0.3). Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html, https://docs.nvidia.com/vss/3.2.0/real-time-embedding.html
- Upstream checkpoint configuration files (upstream‑checkpoint evidence) document num_video_frames=8 and per‑variant spatial resolution fields (resolution) for 224p/336p/448p; these are upstream‑checkpoint preprocessing defaults. Sources: https://huggingface.co/nvidia/Cosmos-Embed1-224p/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-336p/blame/ecf8cbe02f3e3df4d41cb30fbc88232c6826b298/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-448p/blob/f6536214be00bc75b56caa01867d40c4c3633180/config.json, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

### Pre-submit validation

- Validate that request_type is one of the supported modes (query, bulk_text, bulk_video) per the API reference and release notes. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html
- Validate that video_frames items contain exactly 8 sampled frames when using the video_frames input mode (v1.1.0 documents 8 frames per item support). Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html
- Evidence gap: Tokenizer/tokenization implementation details for the text encoder (tokenizer type, vocab, tokenization preprocessing) are not specified in the inspected NIM/TAO/VSS docs. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

### Task-specific formatting

- API request formats reference POST /v1/embeddings and use request_type modes consistent with the NIM API reference (e.g., query, bulk_text, bulk_video); video_frames is documented for v1.1.0. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html

## Output interpretation

### Outputs

- POST /v1/embeddings response returns arrays of floating‑point embedding vectors for text or video inputs (one embedding per input item) as described in the NIM API reference and introduction. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html
- Variant‑specific embedding dimensionalities are reported in upstream config.json files: 224p → embed_dim 256; 336p → embed_dim 768; 448p → embed_dim 768 (these values are upstream‑checkpoint evidence and separate from NIM‑serving runtime metadata). Sources: https://huggingface.co/nvidia/Cosmos-Embed1-224p/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-336p/blame/ecf8cbe02f3e3df4d41cb30fbc88232c6826b298/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-448p/blob/f6536214be00bc75b56caa01867d40c4c3633180/config.json, https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1/v1.0/model-card/safety-and-security
- Evidence gap: An explicit statement in the inspected NIM/TAO/VSS docs that embeddings are L2‑normalized (or another specific normalization) is not present; VSS model doc references normalized embeddings but the exact normalization operation is not specified in the inspected NIM/TAO pages. Sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html

### Interpretation

- Interpret embedding vectors as fixed‑length floating‑point feature vectors for downstream similarity tasks (k‑NN, clustering, zero‑shot classification); similarity comparisons require matching embedding dimensionality. Sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html
- Evidence gap: An explicit recommended distance metric (cosine, euclidean, etc.) for retrieval is not specified in the inspected NIM/Real‑Time Embedding/VSS/TAO sources. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

### Post-inference validation

- Post‑inference validation: ensure embedding dimensionality from the served variant matches downstream index dimensionality; if dimensions differ, the embeddings are not directly compatible. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/configuration.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html
- Post‑inference sanity checks: verify non‑NaN, finite float values and expected vector length per variant before indexing or similarity computation. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html
- Evidence gap: Explicit NVIDIA guidance in NIM/NGC docs instructing operators to re‑index vector stores after switching model variants is not present in the inspected sources. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/configuration.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html

## Public benchmarks

### Inference latency (per-item embedding generation) for request_type "query" (NIM‑serving operational microbenchmark)

- Dataset/split: not applicable (inference microbenchmark) / not reported
- Metric/value: Latency (seconds per video / seconds per text input) / Examples from NIM performance page: A100‑SXM4‑40GB: video 0.0672 s, text 0.0074 s; A100‑PCIE‑40GB: video 0.0683 s, text 0.0093 s; H100‑80GB‑HBM3: video 0.0431 s, text 0.0058 s; L4: video 0.1096 s, text 0.0085 s; RTX 6000 Ada: video 0.0527 s, text 0.0067 s. (`lower-is-better`)
- Model scope: Cosmos-Embed1 NIM v1.1.0 (NIM-serving latency microbenchmarks)
- Conditions: NIM request_type "query" inference microbenchmarks as published on the NIM performance page; rows tied to specific GPU models and test conditions. Exact runtime configuration (precision, TensorRT settings) per row is not fully enumerated in the source and is an evidence gap.
- Source: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html
- Locator: Performance page — latency table rows for specific GPUs
- Caveat: These are NIM‑serving runtime microbenchmarks tied to specific GPU hardware and test conditions; do not conflate with upstream model‑quality benchmarks.
- Caveat: Exact runtime configuration (precision, TensorRT settings) and full system tuning for each row are not fully enumerated in the source; treat missing details as evidence gaps.

### Bulk_video throughput (videos/second) (NIM‑serving operational microbenchmark)

- Dataset/split: not applicable (inference microbenchmark) / not reported
- Metric/value: Throughput (videos/second) / Examples from NIM performance page: A100: 16 videos/second for 15s 1080p video with request size 64; H100: 28.57 videos/second (same test conditions). (`higher-is-better`)
- Model scope: Cosmos-Embed1 NIM v1.1.0 (bulk_video throughput)
- Conditions: Published bulk_video throughput numbers on the NIM performance page for specified GPUs (test conditions such as 15‑second 1080p video and request size 64). Exact precision/TensorRT/runtime flags per row are not enumerated and are evidence gaps.
- Source: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html
- Locator: Performance page — throughput table rows for specific GPUs
- Caveat: Throughput depends on hardware, batch composition, and request_type; published values correspond to specific test conditions listed on the performance page and may not generalize.
- Caveat: The performance page does not enumerate all configuration knobs (precision, TensorRT settings) that could affect throughput in every row.

### Upstream retrieval and classification benchmarks (upstream‑checkpoint evidence)

- Dataset/split: Kinetics-400 validation; Robotics benchmark; AV benchmark; Kinetics-600; Kinetics-700 / validation (as reported in upstream model card)
- Metric/value: Reported retrieval/recall and F1 metrics (as published in upstream model card) / Upstream model‑card reported numbers (examples): Kinetics‑400 F1: 224p 83.06, 336p 87.66, 448p 88.21; Robotics T2V‑R@1: 224p 4.26, 336p 7.04, 448p 7.18; AV T2V‑R@1: 224p 30.11, 336p 34.42, 448p 34.66. (`higher-is-better`)
- Model scope: Upstream‑checkpoint metrics reported on Hugging Face model card pages for Cosmos‑Embed1 variants (224p/336p/448p) — upstream‑checkpoint evidence
- Conditions: Reported by upstream Hugging Face model cards / README; these are upstream‑checkpoint evaluation results and are not NIM‑serving microbenchmarks. Exact evaluation protocol details are those provided by the upstream model card.
- Source: https://huggingface.co/nvidia/Cosmos-Embed1-224p
- Locator: Model card / README sections listing reported metrics
- Caveat: These are upstream‑checkpoint evaluation numbers reported on Hugging Face model cards and are not NIM‑serving runtime measurements.
- Caveat: If the NIM serves a different variant/resolution or applies runtime changes, those upstream numbers do not directly transfer to NIM‑serving quality.

## Comparisons

### no-primary-comparator-available — `insufficient-evidence`

- Task: Text-to-video retrieval and retrieval accuracy comparisons
- Criteria: Operational (latency/throughput) vs upstream quality (retrieval R@k) differ in protocol, dataset, and measurement conditions.
- Rationale: VSS/TAO and Hugging Face report upstream checkpoint quality metrics while NIM performance page reports inference latency/throughput. The inspected sources do not contain a direct NIM‑serving head‑to‑head retrieval accuracy comparison under a shared protocol.
- Comparison conditions: No single canonical head‑to‑head benchmark published in the inspected NVIDIA NIM/VSS/TAO docs that applies the exact NIM v1.1.0 serving artifact and matching evaluation protocol for retrieval metrics; operational and quality metrics are measured under different protocols.
- Evidence: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://huggingface.co/nvidia/Cosmos-Embed1-224p

## Limitations and safety

### Limitations

- Evidence gap: Exact immutable NIM container or model checkpoint digest for Cosmos‑Embed1 NIM v1.1.0 is not reported in the inspected NIM/NGC/TAO/VSS pages. Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html
- Evidence gap: NVIDIA‑published parameter counts (total parameters) for Cosmos‑Embed1 variants (224p/336p/448p) are not present in the inspected official NIM/TAO/VSS/NGC pages. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html, https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html, https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1/v1.0/model-card/safety-and-security
- Variant embed_dim differences require downstream index compatibility — 224p outputs 256‑dim while 336p/448p output 768‑dim, so mixing vectors from different variants without re‑indexing will fail dimensionality checks (upstream‑checkpoint config evidence). Sources: https://huggingface.co/nvidia/Cosmos-Embed1-224p/blob/refs%2Fpr%2F1/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-336p/blame/ecf8cbe02f3e3df4d41cb30fbc88232c6826b298/config.json, https://huggingface.co/nvidia/Cosmos-Embed1-448p/blob/f6536214be00bc75b56caa01867d40c4c3633180/config.json
- Evidence gap: Tokenizer/tokenization implementation details for the text encoder (tokenizer type, vocab, preprocessing) are not documented in the inspected NIM/TAO/VSS sources. Sources: https://huggingface.co/nvidia/Cosmos-Embed1-336p, https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html, https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html
- Evidence gap: Complete configuration‑to‑benchmark mapping (full details of precision, TensorRT settings, exact batch sizes and runtime flags used to produce each performance table row) is not fully enumerated in the performance page. Sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html, https://docs.nvidia.com/nim/cosmos-embed1/latest/configuration.html

### Safety

- Model and deployment licensing and export controls: Cosmos‑Embed1 and related VSS models are governed by the NVIDIA Open Model License; users must comply with export, import, trade, and economic sanctions law as stated in the NVIDIA Open Model License documents. Sources: https://docs.nvidia.com/vss/latest/License-Information.html, https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Safety guidance / intended application domains: the model family is documented for Physical‑AI domains (robotics, autonomous vehicles, video understanding) and operators should apply dataset licensing and domain‑appropriate expert review for safety‑critical deployments. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1, https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1
- Evidence gap: explicit NVIDIA NIM/NGC guidance on clinical/biological dual‑use, biosecurity, or healthcare‑specific usage restrictions for Cosmos‑Embed1 is not present in the inspected sources. Sources: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html, https://docs.nvidia.com/vss/latest/License-Information.html

## Related upstream agent skills

### `exact-model`

NVIDIA's Cosmos-Embed skill covers the named Cosmos-Embed1 checkpoint's video/text input preparation, embedding inference, retrieval use cases, evaluation, export, and fine-tuning. Use its TAO container commands only when that environment is selected; use the Forge skill's own request schema for the deployed Forge runtime.
- [tao-finetune-cosmos-embed](https://github.com/NVIDIA/skills/tree/1ab4676c2ee33326ab11042db2a8e98b4d78a1b8/skills/tao-finetune-cosmos-embed)

## Primary sources

### Cosmos Embed1 NIM — Quickstart Guide (v1.1.0)

- URL: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/quickstart-guide.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Versioned quickstart guide for NIM v1.1.0 with launch and usage examples and health‑check guidance.
- Scope: Cosmos-Embed1 NIM v1.1.0 (serving docs)
- Supports: Quickstart examples, container pull/run guidance, health‑check examples

### Cosmos Embed1 NIM — API Reference (latest)

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Defines NIM API endpoints such as POST /v1/embeddings and describes request/response shapes and request_type modes.
- Scope: Cosmos-Embed1 NIM (serving docs)
- Supports: Existence of POST /v1/embeddings endpoint and response shape for embeddings

### Cosmos Embed1 NIM — Release Notes v1.1.0

- URL: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Versioned release notes explicitly documenting v1.1.0 additions including video_frames input support (8 frames per item) and updated video decoding dependency.
- Scope: Cosmos-Embed1 NIM v1.1.0 (serving docs)
- Supports: v1.1.0 adds video_frames input support (8 frames per item), adds GET /health/metrics, updates PyNvVideoCodec dependency

### NGC Catalog — Cosmos-Embed1 NIM container (nim team)

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1
- Publisher: catalog.ngc.nvidia.com
- Type: `official-documentation`
- Primary because: NGC container listing for the Cosmos‑Embed1 NIM container including pull/run instructions and container tag references.
- Scope: Cosmos-Embed1 NIM container (NGC)
- Supports: Container pull/run examples and NGC metadata

### Cosmos-Embed1 (Hugging Face model page — 448p)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-448p
- Publisher: huggingface.co (nvidia publisher)
- Type: `model-card`
- Primary because: Upstream model page and README providing publisher metadata and reported benchmark metadata for 448p.
- Scope: Upstream variant 448p (Hugging Face model card)
- Supports: Reported retrieval/classification benchmark numbers, license and usage notes, intended domains

### Cosmos-Embed1 (Hugging Face model page — 336p)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-336p
- Publisher: huggingface.co (nvidia publisher)
- Type: `model-card`
- Primary because: Upstream model page and README providing publisher metadata and notes about inference acceleration and test hardware.
- Scope: Upstream variant 336p (Hugging Face model card)
- Supports: Inference acceleration engine notes and test hardware references (H100, A100)

### Cosmos-Embed1 (Hugging Face model page — 224p)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-224p
- Publisher: huggingface.co (nvidia publisher)
- Type: `model-card`
- Primary because: Upstream model card and README providing reported benchmark numbers and publisher metadata for 224p.
- Scope: Upstream variant 224p (Hugging Face model card)
- Supports: Upstream‑reported retrieval/recall and F1 metrics and README claims

### Cosmos Embed1 NIM — Performance (latest)

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: NIM‑served inference latency and throughput microbenchmark tables for multiple GPUs.
- Scope: Cosmos-Embed1 NIM (serving performance)
- Supports: Latency and throughput microbenchmark numbers per GPU for request_type query and bulk_video/bulk_text guidance

### Cosmos Embed1 NIM — Configuration (latest)

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/configuration.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Configuration documentation listing environment variables and runtime configuration defaults.
- Scope: Cosmos-Embed1 NIM (serving docs)
- Supports: Environment variables (NGC_API_KEY, NIM_HTTP_API_PORT, CUDA_VISIBLE_DEVICES, NIM_CACHE_PATH, logging and other runtime settings)

### Cosmos Embed1 NIM — Troubleshooting (latest)

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/troubleshooting.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: Troubleshooting and validation behaviors for the NIM runtime (error codes, bulk limits, video upload guidance).
- Scope: Cosmos-Embed1 NIM (serving docs)
- Supports: Validation error behaviors, supported video formats, resolution limits, authentication error guidance

### VSS — Cosmos-Embed1 model doc

- URL: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: VSS model documentation describing architecture, variant support, and Real‑Time Embedding integration.
- Scope: VSS Cosmos-Embed1 (model doc)
- Supports: Architecture description, normalized embeddings (referenced), variant support and Real‑Time Embedding integration

### TAO Toolkit — Cosmos Embed1 (model documentation)

- URL: https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: TAO Toolkit model documentation stating training/inference defaults and variant metadata.
- Scope: TAO Cosmos-Embed1 (upstream/TAO docs)
- Supports: Training/inference defaults, variant metadata (num_video_frames), LoRA references and model usage guidance

### Hugging Face — Cosmos-Embed1-336p config.json (cited revision/file)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-336p/blame/ecf8cbe02f3e3df4d41cb30fbc88232c6826b298/config.json
- Publisher: huggingface.co (nvidia publisher)
- Type: `repository`
- Primary because: Exact upstream config.json used to verify embed_dim and other config fields for 336p.
- Scope: Upstream variant 336p — config.json
- Supports: embed_dim 768, num_video_frames 8, resolution 336 and other config fields

### Hugging Face — Cosmos-Embed1-224p config.json (cited revision/file)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-224p/blob/refs%2Fpr%2F1/config.json
- Publisher: huggingface.co (nvidia publisher)
- Type: `repository`
- Primary because: Exact upstream config.json used to verify embed_dim and other config fields for 224p.
- Scope: Upstream variant 224p — config.json
- Supports: embed_dim 256, num_video_frames 8, resolution 224 and other config fields

### Hugging Face — Cosmos-Embed1-448p config.json (cited revision/file)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-448p/blob/f6536214be00bc75b56caa01867d40c4c3633180/config.json
- Publisher: huggingface.co (nvidia publisher)
- Type: `repository`
- Primary because: Exact upstream config.json used to verify embed_dim and other config fields for 448p.
- Scope: Upstream variant 448p — config.json
- Supports: embed_dim 768, num_video_frames 8, resolution 448 and other config fields

### NGC Catalog — TAO Cosmos-Embed1 model listing

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1
- Publisher: catalog.ngc.nvidia.com
- Type: `official-documentation`
- Primary because: TAO/NGC model listing describing model availability, config hints, and intended use cases.
- Scope: TAO/NGC Cosmos-Embed1 (model listing)
- Supports: Variant descriptions, example training specs, LoRA support and embed_dim references

### Cosmos-Embed1 upstream research page (Cosmos Lab)

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1
- Publisher: research.nvidia.com
- Type: `official-documentation`
- Primary because: Publisher research page reporting upstream model quality metrics and internal benchmark results.
- Scope: Cosmos-Embed1 upstream research reporting
- Supports: Upstream retrieval and AV Actions benchmark numbers for specific upstream checkpoints

### Hugging Face — Cosmos-Embed1-448p README (cited revision)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-448p/blob/refs%2Fpr%2F1/README.md
- Publisher: huggingface.co (nvidia publisher)
- Type: `repository`
- Primary because: Upstream README used to corroborate architecture, license, intended domains and reported benchmark metadata for 448p.
- Scope: Upstream variant README (448p)
- Supports: License statements, intended application domains, variant claims and benchmark summaries

### Hugging Face — Cosmos-Embed1-224p README (cited revision)

- URL: https://huggingface.co/nvidia/Cosmos-Embed1-224p/blob/refs%2Fpr%2F1/README.md
- Publisher: huggingface.co (nvidia publisher)
- Type: `repository`
- Primary because: Upstream README used to corroborate architecture and reported benchmark metadata for 224p.
- Scope: Upstream variant README (224p)
- Supports: Reported Kinetics F1 scores and upstream benchmarking notes

### GitHub — cosmos-curator reference (video pipelines)

- URL: https://github.com/NVIDIA/cosmos-curator/blob/main/docs/curator/reference/video-pipelines.md
- Publisher: github.com
- Type: `repository`
- Primary because: Repository documentation referencing supported cosmos‑embed1 variants and mapping of variants to output dimensionality.
- Scope: cosmos-curator repository (reference docs)
- Supports: CLI option mapping to cosmos-embed1-224p/336p/448p and notes about output dimensionality per variant

### Cosmos Curator — repository root

- URL: https://github.com/NVIDIA/cosmos-curator
- Publisher: github.com
- Type: `repository`
- Primary because: Main repository for cosmos‑curator, used to corroborate deployment and variant mapping documentation.
- Scope: cosmos-curator repository
- Supports: Video curation system, Responsible Use document, LICENSE/NOTICE

### VSS — License Information

- URL: https://docs.nvidia.com/vss/latest/License-Information.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: VSS license information page referenced for licensing governance.
- Scope: VSS license information
- Supports: License name and governance provisions

### NVIDIA Open Model License Agreement (PDF, June 2024)

- URL: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
- Publisher: developer.download.nvidia.com
- Type: `official-documentation`
- Primary because: Archived PDF of NVIDIA Open Model License used to reference license text.
- Scope: License/terms primary
- Supports: License text describing permitted uses and export/compliance obligations

### NGC Catalog — TAO Cosmos-Embed1 model listing — safety/security

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1/v1.0/model-card/safety-and-security
- Publisher: catalog.ngc.nvidia.com
- Type: `official-documentation`
- Primary because: TAO/NGC model safety/security page used to corroborate safety and usage notes.
- Scope: TAO/NGC Cosmos-Embed1 (model listing/safety)
- Supports: Safety/security notes in TAO/NGC model listing

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/api-reference.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/vss/3.2.0/real-time-embedding.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-embed1
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: Exact immutable NIM container or model checkpoint digest for Cosmos-Embed1 NIM v1.1.0 is not reported in the inspected NIM/NGC/TAO/VSS pages.
- Evidence gap: NVIDIA-published parameter counts (total parameters) for Cosmos-Embed1 variants (224p/336p/448p) are not present in the inspected official sources.
- Evidence gap: Tokenizer/tokenization implementation details for the text encoder (tokenizer type, vocab, tokenization preprocessing) are not specified in the inspected NIM/TAO/VSS docs.
- Evidence gap: Explicit recommended distance metric (cosine vs euclidean) for retrieval is not specified in the inspected NIM/Real-Time Embedding/VSS/TAO sources.
- Evidence gap: Complete configuration-to-benchmark mapping (precision, TensorRT settings, exact batch composition and runtime flags) used to produce each performance table row is not fully enumerated in the performance page.
- Evidence gap: Canonical NVIDIA-hosted provenance statement explicitly connecting specific Hugging Face upstream artifacts to an NGC/TAO or NIM immutable release manifest was not identified in the inspected sources.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 128 deterministic draft defect(s) were supplied to the audit.

- `medium` $: $: missing required property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $: $: missing required property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property benchmarks Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property comparisons Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property evidenceGaps Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property limitations Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property outputInterpretation Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property safety Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation: $.inputPreparation: unexpected property think_sources Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must contain at least one primary source: $.sources must contain at least one primary source Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/License-Information.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/nvidia-open-model-license-agreements-24-10-2025.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/real-time-embedding.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/api-reference.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-336p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-336p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-336p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-336p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/License-Information.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/nvidia-open-model-license-agreements-24-10-2025.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/models/cosmos-embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos-embed1/latest/performance.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/vss/latest/real-time-embedding.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/tao/tao-toolkit/7.0.1/text/embedding/cosmos_embed1.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1/v1.0/model-card/safety-and-security Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://nvidia.com/content/dam/en-zz/Solutions/license-agreements/enterprise-software/nvidia-open-model-license-agreements-24-10-2025.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/tao/models/cosmos-embed1/v1.0/model-card/safety-and-security Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/cosmos-embed1 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without a benchmark-specific evidence gap: $.benchmarks is empty without a benchmark-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.comparisons is empty without a comparison-specific evidence gap: $.comparisons is empty without a comparison-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.limitations must contain at least one scoped item: $.limitations must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.safety must contain at least one scoped item: $.safety must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs is empty without a section-specific evidence gap: $.outputInterpretation.outputs is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation is empty without a section-specific evidence gap: $.outputInterpretation.interpretation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation is empty without a section-specific evidence gap: $.outputInterpretation.validation is empty without a section-specific evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/api-reference.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/1.1.0/introduction.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/latest/introduction.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/latest/quickstart-guide.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/cosmos-embed1/latest/release-notes.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/vss/3.2.0/real-time-embedding.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
