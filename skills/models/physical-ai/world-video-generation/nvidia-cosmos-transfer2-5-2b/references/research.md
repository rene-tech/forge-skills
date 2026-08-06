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

- Research key: `build-nvidia-com-nvidia-cosmos-transfer2-5-2b-modelcard-e510edc819`
- Independent audit: `revised`
- Researched: `2026-07-23T21:29:56.002951+00:00`

Cosmos-Transfer2.5-2B is an NVIDIA latent-space diffusion-transformer for video/world-state generation conditioned by text plus structured video control modalities (edges, depth, segmentation, blur). Primary NVIDIA sources (model card, product docs, research lab, and repository) describe the model family, intended Physical AI use cases (robotics, autonomous vehicles), support for JSON controlnet_specs and multi-video/multi-view conditioning (examples include seven-camera multi-view scenarios), and NIM/container packaging with TensorRT and FP8 optimizations. The examined primary sources do not publish an immutable upstream checkpoint artifact identifier or revision for the named Cosmos-Transfer2.5-2B checkpoint. Measured hardware requirements (minimum GPU and GPU VRAM) and repository-level inference timing snippets are present in primary docs/repository; however, numeric end-to-end generation times for the exact named checkpoint on the NIM/container quickstart tables were not found in the provided findings. Multiple provenance, dataset-split, tokenizer, and output-encoding details are not specified in the available primary sources and are reported below as evidence gaps where appropriate.

## Identity

- Upstream name: Cosmos-Transfer2.5-2B
- Checkpoint/version: not reported
- Immutable revision: not reported
- Parameter scale: 2 billion parameters
- Architecture/head: Diffusion-transformer latent-space video denoiser conditioned by multiple control branches (edges, depth, segmentation, blur) with adaptive layer normalization and temporal/multi-view attention mechanisms
- License: NVIDIA Open Model License (model weights); Apache License 2.0 (source code)
- Evidence: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://github.com/nvidia-cosmos/cosmos-transfer2.5

## Selection

### Recommended

- **Physics-aware video/world-state generation conditioned on text plus multiple structured video control modalities for Physical AI research and synthetic-data generation (robotics, autonomous-vehicle perception)** — Model card, product docs, and the research lab page describe the model as purpose-built for Physical AI and accepting multiple structured video control modalities for generating world-state video/images.
  Scope: Cosmos-Transfer2.5-2B (named checkpoint as published on NVIDIA model card, Hugging Face model page, and research lab pages)
  Evidence: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- **Controlled video-to-video transfer and sim-to-real synthetic-data generation using simulator-derived control maps (depth, segmentation, edges, blur) for data augmentation and training downstream perception models** — Product documentation and research lab examples describe workflows for simulation-to-photorealism and scaling world-state diversity using structured control inputs accepted by Transfer2.5.
  Scope: Cosmos-Transfer2.5-2B (product/documentation and research lab scope)
  Evidence: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- **Multi-view/multi-camera conditional generation producing view-consistent frames per camera in multi-camera world scenarios** — Model card and research examples document multi-view/multi-camera example inputs (seven-camera examples) and show view-consistent generation examples at 1280×720 resolution.
  Scope: Cosmos-Transfer2.5-2B (model card examples and research lab examples)
  Evidence: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5

### Conditional

- **Longer-duration or higher-resolution video generation in production when verifying temporal-consistency and artifact rates (validate before production use)** — Validate temporal consistency, artifact occurrence, and container-optimized precision/quantization behavior on target workloads; verify NIM/container-optimized precisions (TensorRT/FP8) do not change safety/guardrails or downstream accuracy.
  Scope: Cosmos-Transfer2.5-2B (NIM/containerized deployment and published model pages)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b, https://docs.nvidia.com/cosmos/latest/transfer2.5/model_matrix.html, https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html
- **Reference-frame conditioned generation for improved view/temporal consistency (use repository/model-card examples to validate on target inputs)** — Validate reference-frame conditioning behavior on target workloads and follow example JSON controlnet_specs and repository inference examples for reference-frame usage.
  Scope: Cosmos-Transfer2.5-2B (model card and repository examples)
  Evidence: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://github.com/nvidia-cosmos/cosmos-transfer2.5

### Avoid

- **Applications requiring provable, formal physical‑law guarantees or certified multi-agent-dynamics correctness without downstream validation** — Evidence gap: primary NVIDIA model card, product docs, and research lab page describe physics-aware world-state generation but do not provide proofs, formal guarantees, or evaluation protocols certifying provable physics-grounding or multi-agent dynamics correctness for the named checkpoint.
  Scope: Cosmos-Transfer2.5-2B (upstream checkpoint and published materials)
  Evidence: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- **Production deployment on non-Linux operating systems without vendor validation** — Evidence gap: available primary documentation includes Docker/NIM container usage and runtime flags but does not publish explicit cross-platform (non-Linux) support claims or validated runtime matrices for non-Linux OSes.
  Scope: Cosmos-Transfer2.5-2B (NIM/container)
  Evidence: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b
- **Assuming upstream-checkpoint parity with NIM/container TensorRT/FP8 quantized performance/precision without explicit validation** — Evidence gap / NIM-only: NGC container listing documents container-level optimizations (TensorRT, FP8) but primary model pages do not publish the exact precisions tested/supported for the upstream checkpoint itself; treat container optimizations as NIM-level evidence.
  Scope: Cosmos-Transfer2.5-2B (distinguish upstream checkpoint vs NIM/container)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard

## Input preparation

### Semantic inputs

- Text prompts (free-text) are accepted as conditioning inputs together with structured video control inputs. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html
- Structured video control modalities accepted include RGB video, depth maps, segmentation maps, edge maps, and blur control modalities. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Multi-view/multi-camera world-scenario inputs (examples document seven camera streams used as control inputs) are supported in examples. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5

### Accepted formats

- Generation and control configuration is provided via JSON-based controlnet_specs (repository and product docs describe JSON configuration/spec patterns). Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://github.com/nvidia-cosmos/cosmos-transfer2.5
- Input video modalities are provided as standard video assets; documented examples use 1280×720 (720P) inputs in examples. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html

### Preprocessing

- Inputs are featurized and processed in a compressed latent space as part of the latent-space denoising pipeline. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Adaptive Layer Normalization is applied to embed temporal information into denoising layers as described in product/repository materials. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://github.com/nvidia-cosmos/cosmos-transfer2.5
- The NIM/container quickstart documents Docker runtime and environment flags required to run the NIM, indicating containerized preprocessing and runtime expectations. Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b

### Pre-submit validation

- Validate that JSON controlnet_specs conform to the documented schema and required fields per the Transfer2.5 docs before invocation. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html
- Check that input videos match expected resolution and frame-rate conventions for reported examples (documented examples use 1280×720 at 16 FPS in product materials). Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- When using multi-chunk inputs, validate chunk boundaries and reference-frame alignment as discussed in repository/quickstart examples. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html, https://github.com/nvidia-cosmos/cosmos-transfer2.5

### Task-specific formatting

- Typical generation invocation pairs a free-text prompt with structured JSON controlnet_specs plus one or more control input videos; repository and product docs illustrate example JSON specifications. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://github.com/nvidia-cosmos/cosmos-transfer2.5
- The NIM/container quickstart documents CLI/container invocation patterns and environment flags to run the NIM and retrieve encoded output from the server response. Sources: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html
- The repository documents example inference modes (single-video inference, auto/multiview examples, and autoregressive sliding-window mode for longer videos) that affect input formatting and chunking behavior. Sources: https://github.com/nvidia-cosmos/cosmos-transfer2.5

## Output interpretation

### Outputs

- Generated outputs are video sequences typically reported in examples at 1280×720 (720P) and example documentation shows 16 FPS usage; example generation lengths include 5-second examples illustrated in materials. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html
- Multi-view examples report generation of view-consistent frames per camera (seven-camera examples at 1280×720 are shown in published examples). Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Evidence gap: Exact output codec/container/bitrate/frame-encoding parameters for generated videos are not published in the examined primary sources.

### Interpretation

- Model outputs are stochastic conditional generative video frames; NVIDIA publishes control-type quality metrics at an aggregated level in research materials, but primary sources do not provide per-instance calibrated confidences. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- Evidence gap: Per-frame calibrated confidence or uncertainty outputs are not documented in the examined primary sources.

### Post-inference validation

- Perform post-inference checks for temporal consistency (no object disappearance/morphing across frames), view-consistency across camera outputs, and alignment between segmentation/depth outputs and input control maps as recommended in documentation/repository examples. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html
- Apply documented post-processing safety steps (e.g., face blurring) when outputs contain sensitive personal data per model card and product documentation. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html
- When using generated data as synthetic training data, validate distributional shift, artifact rates, and downstream model robustness per documentation guidance. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5

## Public benchmarks

### Repository-reported average diffusion times (distilled vs base) on RTX PRO 6000 Blackwell SE (inference timing snippet)

- Dataset/split: not applicable / not applicable
- Metric/value: Average diffusion time (seconds) for distilled and base models on RTX PRO 6000 Blackwell SE; distilled speedup factor / Average distilled model diffusion time = 1 second; Average base diffusion time = 605.7 seconds; Distilled improvement = 7.7× (values reported in repository docs/inference.md) (`lower-is-better`)
- Model scope: Cosmos-Transfer2.5-2B (repository inference notes — distilled vs base variants)
- Conditions: Repository inference.md variant/measurement notes for RTX PRO 6000 Blackwell SE (see exact repo path and statements).
- Source: https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/inference.md
- Locator: GitHub repository — docs/inference.md — lines stating: 'Average distilled model diffusion time on an RTX PRO 6000 Blackwell SE GPU is 1 second.' and 'Average base diffusion time on an RTX PRO 6000 Blackwell SE GPU is 605.7 seconds.'
- Caveat: These timings are provided in the repository inference documentation and refer to distilled vs base variants; they are repository-measured values and not an independent benchmark report.
- Caveat: The repository timings are for a specific GPU (RTX PRO 6000 Blackwell SE) and variant; they should not be generalized to other hardware or NIM/container-optimized configurations without validation.

### Minimum GPU and GPU VRAM requirement

- Dataset/split: not applicable / not applicable
- Metric/value: Minimum GPU count and single-GPU VRAM required for inference / Minimum 1 GPU; single-GPU GPU VRAM requirement 65.4 GB; 'Auto' specialized checkpoint requires minimum 8 GPUs (values reported on the Transfer2.5 model_matrix page) (`context-only`)
- Model scope: Cosmos-Transfer2.5-2B (model_matrix page)
- Conditions: Model matrix hardware/requirements section on the product documentation
- Source: https://docs.nvidia.com/cosmos/latest/transfer2.5/model_matrix.html
- Locator: Transfer2.5 model matrix — 'Minimum GPU/VRAM requirements' row/section on model_matrix.html
- Caveat: These requirements are reported on the product model_matrix page and reflect NVIDIA's documented minimums for the named Transfer2.5-2B model; NIM/container runtime profiles may provide additional optimized or alternative profiles.

## Comparisons

### nvidia-cosmos-predict1-7b-text2world — `insufficient-evidence`

- Task: World/video generation (text-conditioned)
- Criteria: No checkpoint-scoped primary-source evaluation using an identical task protocol (same resolution, FPS, control type, dataset/split, and measurement definition) for the alternative was found in the provided primary findings.
- Rationale: Provided primary findings include checkpoint-scoped metrics for Transfer2.5-2B but do not include a matching Predict1-7B checkpoint evaluation under the same protocol needed for direct comparison.
- Comparison conditions: Comparison would require identical evaluation protocol, datasets/splits, control modalities, and measurement definitions on both checkpoints; those matching protocol elements were not found for the alternative in the provided sources.
- Evidence: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html, https://github.com/nvidia-cosmos/cosmos-transfer2.5

### nvidia-cosmos-predict1-7b-video2world — `insufficient-evidence`

- Task: World/video generation (video-conditioned)
- Criteria: No checkpoint-scoped primary-source metrics for Predict1-7B under an identical evaluation protocol were available in the provided findings.
- Rationale: No matched evaluation protocol and checkpoint-scoped metrics for the alternative were found in the provided primary sources; thus direct evidence-backed comparisons are unsupported.
- Comparison conditions: Identical task protocol and dataset required; missing for the alternative in provided sources.
- Evidence: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html, https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html

### nvidia-cosmos3-omni-nano — `insufficient-evidence`

- Task: World/video generation (omni family, Nano)
- Criteria: No checkpoint-scoped primary-source evaluation for Cosmos3 Omni (Nano) matching the Transfer2.5-2B control-type protocols was found in the provided findings.
- Rationale: Provided findings did not include matched evaluation protocol and checkpoint-scoped metrics for the alternative.
- Comparison conditions: Identical dataset/split, resolution, FPS, control types, and measurement definitions required but not present.
- Evidence: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html

### nvidia-cosmos3-omni-super — `insufficient-evidence`

- Task: World/video generation (omni family, Super)
- Criteria: No checkpoint-scoped primary-source evaluation for Cosmos3 Omni (Super) matching Transfer2.5-2B control-type protocols was found in the provided findings.
- Rationale: Without matched primary-source evaluation protocol and checkpoint-scoped metrics for the alternative, direct evidence-backed comparisons are not possible from the provided findings.
- Comparison conditions: Identical task protocol and dataset required; missing for the alternative in provided sources.
- Evidence: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html

## Limitations and safety

### Limitations

- Checkpoint immutable identifier (commit hash, S3/NGC artifact ID, or canonical model artifact URL) for Cosmos-Transfer2.5-2B is not published in the examined primary sources. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://github.com/nvidia-cosmos/cosmos-transfer2.5
- Dataset names and exact evaluation splits used to compute the published control-type quality metrics (SSIM, Edge F1, Depth si-RMSE, Mask mIoU, Overall Quality) are not reported in the available primary sources. Sources: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- Tokenizer/tokenization specifics (tokenizer type, vocabulary, tokenization rules, embedding/head details) for the named Cosmos-Transfer2.5-2B checkpoint are not documented in the examined primary sources. Sources: https://github.com/nvidia-cosmos/cosmos-transfer2.5, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- Training data provenance and composition (exact dataset names, licenses, and curation procedures for this exact checkpoint) are not provided in the available primary sources. Sources: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Exact multi-GPU scaling protocol, batch-sizing guidance, and measured latency-vs-GPU-count scaling curves are not published in the provided primary sources. Sources: https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html, https://docs.nvidia.com/cosmos/latest/transfer2.5/model_matrix.html
- Output codec/container/bitrate/frame-encoding parameters for generated videos are not published in the examined primary sources. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html

### Safety

- Model weights are published under the NVIDIA Open Model License and source code under Apache License 2.0; the Hugging Face model page and NVIDIA model card state that bypassing or disabling technical limitations or safety guardrails terminates rights under the NVIDIA Open Model License. Sources: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B, https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- Documentation and model card indicate inference pipeline includes input safety checks and post-processing safety steps (including face blurring) and recommend applying documented post-processing for sensitive personal data. Sources: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard, https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html
- Container/NIM packaging includes inference optimizations (TensorRT, FP8 quantization profiles) that are distinct from upstream-checkpoint semantics; treat container-optimized behavior as NIM-level evidence and validate guardrail behavior after container-level optimizations are applied. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Cosmos-Transfer2.5-2B model card (NVIDIA Build)

- URL: https://build.nvidia.com/nvidia/cosmos-transfer2_5-2b/modelcard
- Publisher: NVIDIA
- Type: `model-card`
- Primary because: Official NVIDIA model card for the named Cosmos-Transfer2.5-2B checkpoint and published examples.
- Scope: Cosmos-Transfer2.5-2B (model card / published examples)
- Supports: Model purpose and recommended uses
- Supports: Multi-view example claims
- Supports: Reference to accepted inputs and control modalities
- Supports: License/guardrail summary statements (as published on the model card)

### Cosmos-Transfer2.5-2B Hugging Face model page

- URL: https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B
- Publisher: NVIDIA (Hugging Face model card)
- Type: `model-card`
- Primary because: Canonical published model card for the named checkpoint hosted by NVIDIA on Hugging Face.
- Scope: Cosmos-Transfer2.5-2B (Hugging Face checkpoint page)
- Supports: Release metadata and license statement
- Supports: Reported example output resolution/FPS metadata

### Cosmos Transfer2.5 index (product documentation)

- URL: https://docs.nvidia.com/cosmos/latest/transfer2.5/index.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Product-family documentation describing accepted modalities, JSON controlnet_specs, and usage workflows.
- Scope: Cosmos-Transfer2.5 family documentation
- Supports: Accepted control modalities and JSON-based controlnet_specs
- Supports: Product-level architecture notes and usage workflows

### Transfer2.5 Quickstart Guide (NVIDIA docs)

- URL: https://docs.nvidia.com/cosmos/latest/transfer2.5/quickstart_guide.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Quickstart guide containing example invocation guidance and runtime notes.
- Scope: Transfer2.5 quickstart and measurement examples (NIM/container usage notes)
- Supports: Example invocation patterns, runtime/container flags and usage notes
- Supports: Example resolution/FPS conventions referenced in examples

### Transfer2.5 model matrix (inference performance and requirements)

- URL: https://docs.nvidia.com/cosmos/latest/transfer2.5/model_matrix.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Model matrix listing measured inference performance and hardware requirements.
- Scope: Transfer2.5 model performance and hardware requirements
- Supports: Minimum GPU/VRAM requirements and notes on specialized 'Auto' checkpoint variants

### Cosmos Transfer2.5 research lab page

- URL: https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer2.5
- Publisher: NVIDIA Research / Cosmos Lab
- Type: `official-documentation`
- Primary because: Research lab page reporting control-type quality metrics and research examples for Transfer2.5.
- Scope: Research lab description and control-type-quality metrics
- Supports: Control-type quality metrics (SSIM, Edge F1, Depth si-RMSE, Mask mIoU, Overall Quality) described at control-type granularity
- Supports: Research examples and conditioning modality descriptions

### Cosmos-Transfer2.5 GitHub repository

- URL: https://github.com/nvidia-cosmos/cosmos-transfer2.5
- Publisher: NVIDIA (GitHub org)
- Type: `repository`
- Primary because: Canonical repository for Transfer2.5 family with implementation notes, example inference modes, and docs.
- Scope: Transfer2.5 implementation and example recipes
- Supports: Repository-level implementation notes, inference example modes, and variant parameter files
- Supports: Implementation/inference documentation (docs/inference.md) with measured timings for specific hardware/variants

### NGC container listing for cosmos-transfer2.5-2b

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-transfer2.5-2b
- Publisher: NVIDIA NGC Catalog
- Type: `official-documentation`
- Primary because: Official NGC container entry describing NIM/container packaging, image tags, and container-level optimizations.
- Scope: Cosmos-Transfer2.5-2B NIM/container
- Supports: Container packaging details, TensorRT and FP8 quantization/optimization notes
- Supports: Container image tags and NIM packaging terms

### NIM/Cosmos quickstart (NGC/NIM documentation)

- URL: https://docs.nvidia.com/nim/cosmos/latest/quickstart-guide.html
- Publisher: NVIDIA NIM Documentation
- Type: `official-documentation`
- Primary because: NIM quickstart documents container invocation flags, environment variables, and runtime expectations for running NIM containers.
- Scope: NIM/container invocation and runtime flags
- Supports: Docker runtime flags and recommended invocation patterns for the NIM container

### Cosmos-Transfer2.5 repository releases

- URL: https://github.com/nvidia-cosmos/cosmos-transfer2.5/releases
- Publisher: NVIDIA (GitHub org)
- Type: `repository`
- Primary because: Repository releases page providing release tags and commit identifiers for the codebase.
- Scope: Repository release history and commit identifiers (codebase)
- Supports: Release entries and commit hashes for repository code releases (release metadata)

### Cosmos-Transfer2.5 GitHub repository — cited revision/file

- URL: https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/inference.md
- Publisher: NVIDIA (GitHub org)
- Type: `repository`
- Primary because: Exact revision/file URL beneath the independently verified first-party source indexed by this dossier.
- Scope: Transfer2.5 implementation and example recipes
- Supports: Exact audited claim citation

## Evidence gaps

- Evidence gap: Immutable upstream checkpoint identifier (commit hash, S3/NGC artifact ID, or canonical model artifact URL) for Cosmos-Transfer2.5-2B is not published in the examined primary sources.
- Evidence gap: Exact numeric values, dataset names, and splits used to compute the control-type quality metrics (SSIM, Edge F1, Depth si-RMSE, Mask mIoU, Overall Quality) are not present in the research lab page or model card in the provided findings.
- Evidence gap: Tokenizer/tokenization details (tokenizer type, vocabulary, tokenization rules, and embedding/head details) for the named Cosmos-Transfer2.5-2B checkpoint are not documented in the provided primary sources.
- Evidence gap: Training data provenance and composition (exact dataset names, licenses, curation procedures) for this exact checkpoint are not documented in the provided primary sources.
- Evidence gap: Output codec/container/bitrate/frame-encoding parameters for generated videos are not published in the examined primary sources.
- Evidence gap: Per-frame calibrated confidence or uncertainty outputs are not documented in the examined primary sources.
- Evidence gap: Exact multi-GPU scaling protocol, batch-sizing guidance, and measured latency-vs-GPU-count scaling curves are not published in the provided primary sources.
- Evidence gap: The exact input artifact or dataset used to derive any performance timing examples in the quickstart/model_matrix or repository docs is not specified in the provided primary findings.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary URL https: $.sources[11] uses forbidden secondary URL https://spheron.network/blog/deploy-nvidia-cosmos-gpu-cloud-synthetic-data Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://github.com/nvidia-cosmos/cosmos-transfer2.5/blob/main/docs/inference.md: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
