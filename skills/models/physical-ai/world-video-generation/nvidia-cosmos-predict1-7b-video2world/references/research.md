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

- Research key: `docs-nvidia-com-nim-cosmos-latest-quickstart-guide-html-nvidia-cosmos-predict1-7b-video2worl-c266df85c8`
- Independent audit: `revised`
- Researched: `2026-07-23T22:18:02.844100+00:00`

Using only inspected primary sources, the named upstream checkpoint nvidia/cosmos-predict1-7b-video2world is documented in the NGC container catalog and the upstream repository/model card. Primary checkpoint-scoped evidence supports: (1) the checkpoint name and approximate scale (7B via the model name), (2) architecture described as a diffusion transformer latent denoiser in the API reference, (3) accepted input modalities (text, image, video) and API field names (image, video), (4) NIM runtime behavior for input URL vs base64 controlled by NIM_ALLOW_URL_INPUT, (5) input codec/container support and documented input frame-count bounds, and (6) output delivered in a base64-encoded MP4 in the b64_video field and MP4+VP9 encoding. Primary sources do not publish immutable checkpoint revision/hash, tokenizer implementation metadata (name/version/vocab size), per-output tensor/logit shapes or numeric confidence scores from the callable API, or any checkpoint-scoped numeric benchmark tables; those items are recorded as explicit evidence gaps with the exact inspected pages listed in evidenceGaps.

## Identity

- Upstream name: nvidia/cosmos-predict1-7b-video2world
- Checkpoint/version: nvidia/cosmos-predict1-7b-video2world
- Immutable revision: not reported
- Parameter scale: 7 billion parameters
- Architecture/head: Diffusion transformer latent denoiser composed of interleaved self-attention, cross-attention, and feed-forward layers with adaptive layer normalization for time embedding (checkpoint-scoped description)
- License: NVIDIA Open Model License
- Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://github.com/nvidia-cosmos/cosmos-predict1, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html

## Selection

### Recommended

- **Generate synthetic video sequences for training robotics and autonomous-vehicle perception/simulation pipelines** — NVIDIA documents Cosmos world foundation models and Predict1 variants as intended to produce physically realistic synthetic video data for Physical AI and simulation training workflows.
  Scope: nvidia/cosmos-predict1-7b-video2world (upstream checkpoint) and NIM container nvcr.io/nim/nvidia/cosmos-predict1-7b-video2world
  Evidence: https://arxiv.org/html/2501.03575v2, https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world
- **Image- or video-conditioned future-frame prediction (video continuation) with optional textual conditioning** — Repository examples and the Hugging Face model card describe Video2World variants that accept image or video conditioning concatenated in latent frames and optionally condition on text during denoising.
  Scope: nvidia/cosmos-predict1-7b-video2world (upstream checkpoint and NIM serving runtime)
  Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_video2world.md

### Conditional

- **Commercial production deployment for simulation training pipelines (subject to system-level validation)** — Operators must validate model outputs for the target domain, enforce NIM input/output validation and guardrails, and follow license terms; NIM may choose best model version for available hardware at deployment time.
  Scope: nvidia/cosmos-predict1-7b-video2world (NIM container nvcr.io/nim/nvidia/cosmos-predict1-7b-video2world)
  Evidence: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world, https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html
- **High-resolution or high-FPS generation for simulation (requires empirical validation before use)** — Predict1-7B-Video2World does not publish checkpoint-scoped default resolution/FPS in the inspected sources; other family/checkpoint types (e.g., Transfer2.5-2B) publish specific resolution/FPS settings and therefore those cannot be assumed for this checkpoint without validation.
  Scope: nvidia/cosmos-predict1-7b-video2world
  Evidence: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://docs.nvidia.com/nim/cosmos/latest/introduction.html

### Avoid

- **Using outputs as the sole basis for life-critical or safety-critical decisions** — No primary-source statement certifies this checkpoint for life-critical use; primary sources and model card require system-level validation rather than model-only certification.
  Scope: nvidia/cosmos-predict1-7b-video2world
  Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://arxiv.org/html/2501.03575v2
- **Bypassing documented guardrails to generate disallowed or unsafe content** — NIM documentation and Predict1 diffusion reference describe pre- and post-guard safety mechanisms (including face-blurring for human faces) and warn about guardrail behavior; disabling or bypassing guardrails is not supported as a safe practice per the documented guardrail statements.
  Scope: nvidia/cosmos-predict1-7b-video2world (NIM runtime)
  Evidence: https://docs.nvidia.com/cosmos/latest/predict1/diffusion/reference.html, https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html

## Input preparation

### Semantic inputs

- Accepted input modalities for the checkpoint and NIM runtime are text, image, and video (text prompts, image input, or video input may be used for conditioning). Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World
- When image or video is provided as input, repository documentation indicates latent frames are used as conditioning concatenated along the temporal dimension as part of the generation process. Sources: https://github.com/nvidia-cosmos/cosmos-predict1, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World

### Accepted formats

- The NIM accepts either a URL or a base64-encoded image/video for the 'image'/'video' API fields; when the environment variable NIM_ALLOW_URL_INPUT is set to 0 then only base64 is accepted. Sources: https://docs.nvidia.com/nim/cosmos/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html
- Input video containers accepted include any container supported by ffmpeg native demuxers; supported input codecs listed include VP9, VP8, VC1, MPEG-1, MPEG-2, H.264, H.265 (HEVC), AV1, and Raw (uncompressed). Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html

### Preprocessing

- Input image/video dimensions must be multiples of 8; violations are documented to produce 400 Bad Request responses in the NIM API references. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/api-reference.html, https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html
- Input video frame-count bounds for the Predict1-7B-Video2World runtime are documented as requiring between 93 and 480 frames. Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html
- Repository examples document offload strategies and example VRAM/offload footprints for Predict1-7B-Video2World; offload behavior depends on available hardware and chosen offload components. Sources: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_video2world.md, https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html

### Pre-submit validation

- The NIM API returns standard HTTP status codes: 200 OK for success, 400 Bad Request for invalid inputs (including malformed JSON and invalid dimensions), and 500 Internal Server Error for server-side errors. Sources: https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html, https://docs.nvidia.com/nim/cosmos/3.0.0/api-reference.html
- Requests with malformed JSON or invalid parameters are documented to produce error responses; dimension and frame-count violations are explicitly listed as causes for 400 responses. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/api-reference.html, https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html

### Task-specific formatting

- Example inference scripts and CLI examples for Video2World in the upstream repository require an '--input_image_or_video_path' argument and show fields for prompt, negative_prompt, seed, save_path, and disable_guardrail flags in examples. Sources: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_video2world.md, https://github.com/nvidia-cosmos/cosmos-predict1

## Output interpretation

### Outputs

- The API response contains a 'b64_video' field which is a base64-encoded MP4 file. Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html
- NIM support matrix documents that output MP4 containers for Predict1-7B-Video2World use the VP9 codec. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html

### Interpretation

- Primary checkpoint/runtime sources do not publish per-frame tensors, logits, numeric confidences, or calibrated uncertainty scores in the callable API; consumers must decode MP4 and perform downstream analyses to obtain numeric measurements. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://docs.nvidia.com/nim/cosmos/latest/api-reference.html

### Post-inference validation

- Recommended downstream checks include decoding the base64 'b64_video' to an MP4 file, verifying container integrity, and validating frame rate/resolution per task needs because internal numeric confidences are not provided in the documented API. Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World
- Postprocessing guardrails applied by the runtime may blur human faces and/or watermark outputs per the Predict1 diffusion reference; users should detect such modifications as part of output acceptance criteria. Sources: https://docs.nvidia.com/cosmos/latest/predict1/diffusion/reference.html, https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### nvidia-cosmos-predict1-7b-text2world — `insufficient-evidence`

- Task: Video prediction/generation from text and image/video conditioning (family variants)
- Criteria: No primary-source matched-protocol numeric metrics or head-to-head evaluations were found for Predict1-7B-Video2World versus Predict1-7B-Text2World in the inspected canonical sources.
- Rationale: Catalog and model-card entries document both family variants exist and share architecture but do not publish directly comparable checkpoint-scoped numeric evaluation tables for this checkpoint.
- Comparison conditions: Checked Predict1 model matrix, NGC/NGC model catalog entries, and Hugging Face model card for Video2World; no matched-protocol numeric results found for this checkpoint.
- Evidence: https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World

### nvidia-cosmos-transfer2-5-2b — `insufficient-evidence`

- Task: Resolution/FPS and generation-setting comparisons for video-generation checkpoints
- Criteria: Transfer2.5-2B publications describe specific resolution/FPS claims but Predict1-7B-Video2World lacks checkpoint-scoped resolution/FPS numeric claims in inspected sources, preventing direct comparison.
- Rationale: Transfer2.5 documentation includes generation settings; Predict1-7B-Video2World sources do not provide matching numeric defaults or metrics in inspected pages.
- Comparison conditions: Checked Transfer2.5 research pages and Predict1 introduction/model matrix; no matched checkpoint-scoped numeric defaults for Predict1-7B-Video2World were found.
- Evidence: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html

### nvidia-cosmos3-omni-nano — `insufficient-evidence`

- Task: Architectural and capability context comparisons
- Criteria: Cosmos3-Nano is a distinct family with different published goals; no primary-source numeric head-to-head evaluations against Predict1-7B-Video2World were found in inspected sources.
- Rationale: Technical report and model-card for Cosmos3 family document architecture and capabilities but do not present direct comparative metrics against Predict1-7B-Video2World.
- Comparison conditions: Reviewed Cosmos family technical documentation and Predict1/NIM docs; no matched-protocol numeric comparisons exist in the checked primary sources.
- Evidence: https://huggingface.co/nvidia/Cosmos3-Nano, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html

### nvidia-cosmos3-omni-super — `insufficient-evidence`

- Task: Frontier-scale capability/context comparisons
- Criteria: Cosmos3-Super is a larger-scale omnimodal model family; inspected primary sources do not provide direct benchmark comparisons to Predict1-7B-Video2World.
- Rationale: Technical report and model card document Cosmos3-Super scale but lack direct matched-protocol evaluations against Predict1-7B-Video2World.
- Comparison conditions: Checked Cosmos3 model-card and Predict1 documentation; no checkpoint-scoped numeric comparisons were found.
- Evidence: https://huggingface.co/nvidia/Cosmos3-Super, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html

## Limitations and safety

### Limitations

- Primary sources do not publish checkpoint-level numeric benchmark tables (dataset/split/metric/value/conditions) for nvidia/cosmos-predict1-7b-video2world. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://arxiv.org/html/2501.03575v2, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world
- Primary sources do not publish tokenizer implementation details (tokenizer name/version, vocabulary size, special tokens) for this exact checkpoint. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://github.com/nvidia-cosmos/cosmos-predict1
- Primary sources do not expose per-output tensor shapes, logits, or numeric confidence/calibration scores in the callable API responses for this checkpoint. Sources: https://docs.nvidia.com/nim/cosmos/latest/api-reference.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World
- Primary sources do not publish an immutable checkpoint revision/hash for nvidia/cosmos-predict1-7b-video2world. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World
- Runtime quantization/precision formats shipped per-checkpoint are not exhaustively enumerated in the inspected checkpoint-level sources; support matrix provides GPU/precision guidance but does not enumerate per-checkpoint shipped quantized artifacts. Sources: https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b

### Safety

- Predict1 runtime includes pre-guard and post-guard safety mechanisms; the Predict1 diffusion reference documents built-in guardrails that detect and blur human faces as part of postprocessing. Sources: https://docs.nvidia.com/cosmos/latest/predict1/diffusion/reference.html, https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html
- No primary-source certification for life-critical or safety-critical suitability of this checkpoint was found; system-level validation and additional safeguards are required for safety-critical deployments. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://arxiv.org/html/2501.03575v2
- Users must follow NIM and NGC container licensing and security guidance and enforce input/output validation, guardrails, and legal/licensing compliance in deployments. Sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: Cosmos-Predict1-7B-Video2World

- URL: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World
- Publisher: NVIDIA (Hugging Face model card)
- Type: `model-card`
- Primary because: Upstream checkpoint model card documenting checkpoint name, application category, and license; used for checkpoint-level identity and licensing claims.
- Scope: nvidia/Cosmos-Predict1-7B-Video2World (upstream model card)
- Supports: Checkpoint name and approximate scale implication from name; license statement; application category and access notes

### GitHub: cosmos-predict1 repository (upstream examples and assets)

- URL: https://github.com/nvidia-cosmos/cosmos-predict1
- Publisher: NVIDIA (GitHub repository)
- Type: `repository`
- Primary because: Official upstream repository containing examples, tokenizer/inference artifacts, and inference example guidance for Predict1 variants.
- Scope: nvidia/cosmos-predict1 repository
- Supports: Repository model listings, tokenizer components described, inference examples and offload memory footprints

### Predict1 overview (Cosmos Predict1 documentation index)

- URL: https://docs.nvidia.com/cosmos/latest/predict1/index.html
- Publisher: NVIDIA (official documentation)
- Type: `official-documentation`
- Primary because: Official Predict1 documentation page describing the Predict1 collection purpose and generation modes.
- Scope: Cosmos Predict1 collection (documentation index)
- Supports: High-level description of Predict1 family and generation modes

### arXiv: Cosmos World Foundation Model Platform (v2)

- URL: https://arxiv.org/html/2501.03575v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Canonical research preprint describing the Cosmos World Foundation Model Platform and architecture claims referenced by NVIDIA.
- Scope: Cosmos research paper (Predict family overview)
- Supports: High-level family description and architecture claims where present

### NIM Quickstart Guide (Cosmos)

- URL: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Quickstart demonstrating example API usage, base64 encoding instruction, supported codecs, and input frame-count bounds.
- Scope: NIM quickstart guide for Cosmos Predict1 (latest)
- Supports: Example API usage, input base64 requirement example, supported codecs list, documented frame-count bounds (93-480)

### NIM API reference (Cosmos Predict1 latest)

- URL: https://docs.nvidia.com/nim/cosmos/latest/api-reference.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: API reference showing accepted API fields, URL vs base64 acceptance, NIM_ALLOW_URL_INPUT behavior, and IMAGE2VIDEO/VIDEO2WORLD field requirements.
- Scope: Cosmos Predict1 API reference (latest)
- Supports: API field semantics ('video' and 'image'), NIM_ALLOW_URL_INPUT behavior, input acceptance semantics, field requirements for IMAGE2VIDEO and VIDEO2WORLD

### NIM introduction (Cosmos)

- URL: https://docs.nvidia.com/nim/cosmos/latest/introduction.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Introduction page listing generation mode definitions and NIM distribution/usage guidance.
- Scope: NIM Cosmos introduction (latest)
- Supports: Definitions of TEXT2VIDEO and IMAGE2VIDEO generation modes and notes on NIM distribution

### NIM API reference (Cosmos Predict1 1.0.0)

- URL: https://docs.nvidia.com/nim/cosmos/1.0.0/api-reference.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Versioned API reference documenting HTTP status codes and API behavior for Predict1 1.0.0.
- Scope: Cosmos Predict1 API reference (1.0.0)
- Supports: HTTP status code semantics (200/400/500) and generation time guidance

### NIM support matrix (2.0.0)

- URL: https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Support matrix listing accepted input codecs/containers, frame-count bounds, GPU/precision guidance, and Predict1 variant listings including Video2World.
- Scope: NIM support matrix (2.0.0) for Cosmos-Predict1-7B-Video2World
- Supports: Accepted input codecs/containers, documented frame-count bounds, GPU/Memory/Precision table, Predict1 variant listings
- Supports: License guidance for NIM-distributed Cosmos models

### NIM support matrix (3.0.0)

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Later-version support matrix documenting input/output encoding guidance and fallback configuration requirements.
- Scope: NIM support matrix (3.0.0)
- Supports: Confirmed input container support, statement that outputs use MP4+VP9 for Predict1-7B-Video2World, and fallback VRAM requirements

### Predict1 diffusion reference (guardrail documentation)

- URL: https://docs.nvidia.com/cosmos/latest/predict1/diffusion/reference.html
- Publisher: NVIDIA (official documentation)
- Type: `official-documentation`
- Primary because: Predict1 diffusion reference documenting built-in guardrails and postprocessing behaviors such as face blurring.
- Scope: Predict1 diffusion reference (safety/guardrails)
- Supports: Guardrail behavior (face blurring) and statements about built-in safety mechanisms

### NGC Catalog: Cosmos Predict1-7B-Video2World container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NGC container catalog entry identifying the NIM container image that serves the Predict1-7B-Video2World checkpoint and listing licensing and container metadata.
- Scope: nvcr.io/nim/nvidia/cosmos-predict1-7b-video2world (NIM container)
- Supports: Container identity, NIM packaging, licensing statements, container metadata

### Predict1 tokenizer inference guide

- URL: https://docs.nvidia.com/cosmos/latest/predict1/tokenizer/inference_guide.html
- Publisher: NVIDIA (official documentation)
- Type: `official-documentation`
- Primary because: Tokenizer inference guide describing available image and video tokenizers and checkpoint directory contents (encoder/decoder/autoencoder artifacts).
- Scope: Predict1 tokenizer inference guide
- Supports: Tokenizer artifact locations and statement that video tokenizers are temporally causal

### GitHub: Predict1 Video2World inference example (inference_diffusion_video2world.md)

- URL: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_video2world.md
- Publisher: NVIDIA (GitHub repository)
- Type: `repository`
- Primary because: Repository example demonstrating CLI/inference arguments, offload VRAM footprints, and available Predict1-7B-Video2World/14B variants.
- Scope: Predict1 repository example (Video2World inference guidance)
- Supports: Inference script invocation patterns, offload memory footprints, and CLI flags

### NIM API reference (docs.api.nvidia.com reference for Cosmos 1.0 diffusion 7B)

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b
- Publisher: NVIDIA (API reference)
- Type: `official-documentation`
- Primary because: Reference documenting end-to-end inference runtime numbers (reference only) and architectural description for the diffusion 7B model.
- Scope: API reference for Cosmos Predict1 7B diffusion inference
- Supports: Runtime reference numbers, model architecture description, license statement

### Predict1 release notes (3.0.0)

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html
- Publisher: NVIDIA (NIM documentation)
- Type: `official-documentation`
- Primary because: Release notes documenting Predict1-7B-Video2World handling of Image2World and Video2World generations.
- Scope: Predict1 release notes (3.0.0)
- Supports: Notes that Predict1-7B-Video2World handles image-to-world and video-to-world generation

### Research: Cosmos Transfer2.5 technical writeup

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Publisher: NVIDIA Research
- Type: `technical-report`
- Primary because: Technical writeup for Transfer2.5 used as comparative family evidence for resolution/FPS statements.
- Scope: Cosmos Transfer2.5 research writeup
- Supports: Transfer2.5 reported generation settings and architecture context

### Cited official first-party source

- URL: https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-video2world
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/api-reference.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-video2world
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-video2world
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://huggingface.co/nvidia/Cosmos3-Nano
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-video2world
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://huggingface.co/nvidia/Cosmos3-Super
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-video2world
- Supports: Exact independently audited claim citation

## Evidence gaps

- No primary-source numeric benchmark results (dataset, split, metric name, numeric value, and evaluation conditions) were published for the exact checkpoint nvidia/cosmos-predict1-7b-video2world in the inspected sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World (model card sections), https://arxiv.org/html/2501.03575v2 (paper sections/figures), https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world (NGC container page), https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html (model matrix).
- No primary-source tokenizer implementation details (tokenizer name/version, vocabulary size, exact special tokens, algorithm) were found for nvidia/cosmos-predict1-7b-video2world after checking: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://github.com/nvidia-cosmos/cosmos-predict1.
- No primary-source per-output tensor shapes, logits, latent tensor dimensions, or numeric confidence/calibration scores for generated frames were published for the callable API of nvidia/cosmos-predict1-7b-video2world after checking: https://docs.nvidia.com/nim/cosmos/latest/api-reference.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World.
- No primary-source explicit default generation resolution or FPS for nvidia/cosmos-predict1-7b-video2world was published in the inspected Predict1/NIM sources (checked: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world, https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_video2world.md).
- No primary-source detailed evaluation protocol, dataset names/splits, or numeric metrics (e.g., FVD, FID, CLIP-based scores) were published specifically for the Predict1-7B-Video2World checkpoint in the inspected sources: https://arxiv.org/html/2501.03575v2, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world.
- No primary-source runtime per-checkpoint quantized model artifact listings (exact shipped quantization formats) were published for Predict1-7B-Video2World; support matrix gives GPU/precision guidance but does not enumerate per-checkpoint shipped quantized artifacts (checked: https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b).
- No primary-source immutable checkpoint revision/hash was published for nvidia/cosmos-predict1-7b-video2world in the inspected upstream or NGC/container pages (checked: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-predict1-7b-video2world, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World).
- No primary-source per-frame metadata schema (timestamps, bounding boxes, segmentation masks, or confidence fields) in the API response for Predict1-7B-Video2World was found after checking: https://docs.nvidia.com/nim/cosmos/latest/api-reference.html, https://docs.nvidia.com/nim/cosmos/3.0.0/support-matrix.html.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 8 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary URL https: $.sources[17] uses forbidden secondary URL https://developer.nvidia.com/blog/advancing-physical-ai-with-nvidia-cosmos-world-foundation-model-platform Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses forbidden secondary URL https: $.sources[18] uses forbidden secondary URL https://blogs.nvidia.com/blog/cosmos-world-foundation-models Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/kadusoham64/Cosmos3-Nano/blob/main/SAFETY.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos/1.0.0/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/kadusoham64/Cosmos3-Nano/blob/main/SAFETY.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Predict2.5-2B Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.outputInterpretation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.inputPreparation_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://docs.nvidia.com/nim/cosmos/3.0.0/api-reference.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia/Cosmos3-Nano: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia/Cosmos3-Super: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
