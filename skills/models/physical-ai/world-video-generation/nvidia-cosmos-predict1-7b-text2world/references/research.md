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

- Research key: `docs-nvidia-com-nim-cosmos-latest-quickstart-guide-html-nvidia-cosmos-predict1-7b-text2world-c88f94644e`
- Independent audit: `revised`
- Researched: `2026-07-23T22:32:29.404770+00:00`

Primary authoritative sources (Hugging Face model pages, NIM reference, Predict1 model matrix, and NGC catalog) support the checkpoint name Cosmos-Predict1-7B-Text2World, parameter scale 7B, diffusion-transformer latent-space video denoising architecture, text-conditioning via cross-attention, adaptive layer normalization for time embedding, temporal concatenation of conditional latents, and that outputs are video clips. Primary findings do not report an immutable upstream checkpoint identifier that maps NGC/NIM/container artfacts to a specific upstream artifact. Runtime-serving numeric precision for the NIM/container is not specified in the provided primary findings. Canonical numeric benchmark table rows for many common metrics (e.g., PSNR, SSIM, LPIPS, FID, FVD, TAE-*) are not present in the NIM/docs/NGC/Hugging Face/GitHub sources supplied, though an arXiv preprint (v2) in the findings reports multiview/trajectory-conditioned numeric metrics for sample variants; mapping between those reported upstream benchmark rows and the specific NIM-served artifact is not established by the supplied primary findings. Repository examples and model pages include multiview/trajectory-conditioned inference examples and request-format examples. Guardrail functionality and license consequences for bypassing guardrails are described in NIM/docs, but an exhaustive blocklist file or explicit blocklist policy locator is not published in the supplied primary findings.

## Identity

- Upstream name: Cosmos-Predict1-7B-Text2World
- Checkpoint/version: Cosmos-Predict1-7B-Text2World
- Immutable revision: Evidence gap: immutable upstream checkpoint identifier (commit hash, release tag, or artifact ID) for Cosmos-Predict1-7B-Text2World is not reported in the provided primary findings (checked model card, Hugging Face page, GitHub releases, and NGC container listing).
- Parameter scale: 7B
- Architecture/head: Diffusion transformer for latent-space video denoising composed of interleaved self-attention, cross-attention, and feed-forward layers; cross-attention conditions on input text during denoising; adaptive layer normalization embeds time information before each layer; when image/video conditioning is used, conditional latent frames are concatenated with generated frames along the temporal dimension; augment noise is added to conditional latent frames to bridge the training/inference gap.
- License: NVIDIA Open Model License
- Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

## Selection

### Recommended

- **Text-to-world video generation (short physics-aware simulation clips) using the 7B Text2World diffusion checkpoint** — Official model pages, the Predict1 model matrix, NGC container listing, and repository examples describe the checkpoint as producing dynamic videos from text and optional visual conditioning and provide inference/deployment guidance for Text2World workflows.
  Scope: Cosmos-Predict1-7B-Text2World (upstream-checkpoint evidence and NIM/NGC deployment artifacts)
  Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md
- **Multi-view/trajectory-conditioned generation for research workflows (requires downstream revalidation on target datasets)** — Repository contains a multiview inference example demonstrating inference format and conditioning patterns; Hugging Face model pages and repo describe multiview/trajectory-conditioned sample variants.
  Scope: Cosmos-Predict1-7B-Text2World (upstream-checkpoint evidence in repo/model pages)
  Evidence: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World
- **Deploying the NIM/container for GPU-accelerated inference of Text2World workflows** — NGC container listing, Predict1 model matrix, and NIM release notes identify an NIM container image and provide deployment/runtime guidance for the 7B Text2World variant.
  Scope: nvidia/cosmos-predict1-7b-text2world (NIM container and NGC image)
  Evidence: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html

### Conditional

- **Using upstream-reported multiview numeric metrics (geometry/temporal quality) to validate production deployments** — Requires locating canonical benchmark table/figure rows in the upstream paper/preprint that explicitly name the evaluated checkpoint and verifying that the evaluated upstream checkpoint is the identical artifact served by the NIM/container; perform downstream validation on target datasets before trusting numeric values.
  Scope: Upstream sample variants reported in arXiv preprint (Cosmos-Predict1-7B-Text2World sample/multiview variants) — treat as upstream-checkpoint evidence until mapping to NIM-served artifact is proven.
  Evidence: https://arxiv.org/html/2501.03575v2, https://github.com/nvidia-cosmos/cosmos-predict1/releases, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

### Avoid

- **Selecting this checkpoint as a general-purpose text-only LLM for natural-language tasks** — Primary evidence describes the checkpoint and NIM as diffusion-based visual/world-generation models (video/image generation) with a visual/world output head rather than a general-purpose text LLM.
  Scope: Cosmos-Predict1-7B-Text2World
  Evidence: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

## Input preparation

### Semantic inputs

- Primary conditioning input is a text prompt; optional image or video inputs can be supplied for conditioning (single-view and multi-view conditioning supported). Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md

### Accepted formats

- Repository examples and model pages show examples using text prompts and optional image/video conditioning inputs in inference examples; NGC container listing and model pages describe the checkpoint as producing mp4 video outputs. Sources: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

### Preprocessing

- Model operates in latent space: images/videos are converted to latent tokens/frames and conditional latent frames are concatenated with generated frames along the temporal dimension; augment noise is added to conditional latents to bridge training/inference gap (latent-space preprocessing described in model pages and NIM reference). Sources: https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://github.com/nvidia-cosmos/cosmos-predict1

### Pre-submit validation

- Repository examples and container/model pages document typical input usage and some runtime offloading/VRAM requirements for different offload strategies, but explicit runtime input-dimension constraints (for example, multiples-of-8) and exhaustive API field-type schemas are not specified in the supplied primary findings. Sources: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md, https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world
- Evidence gap: authoritative statements of exact input-dimension constraints (e.g., required multiples, maximum pixel dimensions per frame) are not present in the provided primary findings. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

### Task-specific formatting

- A multiview/trajectory-conditioned inference example exists in the repository at examples/inference_diffusion_text2world_multiview.md demonstrating request formatting, required --prompt argument and batch-input JSONL usage. Sources: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md

## Output interpretation

### Outputs

- Official sources describe the model output as generated video objects (short video clips, mp4) produced by the inference pipeline and associated metadata; Predict1 model matrix and NGC catalog indicate outputs are 5-second mp4 clips at 1280x704@24fps in the NGC listing for the cosmos-1.0-diffusion-7b-text2world entry. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World

### Interpretation

- Interpreting outputs should include checks for temporal coherence and geometry-consistency for multiview outputs and alignment with conditioning inputs as discussed in model pages and repository examples; numeric quality metrics reported upstream (arXiv v2) apply to upstream sample variants and require mapping to the exact evaluated checkpoint before being used for calibration. Sources: https://github.com/nvidia-cosmos/cosmos-predict1, https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://arxiv.org/html/2501.03575v2

### Post-inference validation

- Repository examples and container/model pages document typical post-inference handling; however, exact programmatic post-inference validation checks (frame-count enforcement, exact frame-rate handling, exact HTTP status codes for invalid inputs) are not specified in the provided primary findings. Sources: https://github.com/nvidia-cosmos/cosmos-predict1, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

## Public benchmarks

### Multiview/trajectory-conditioned temporal/geometry errors on VideoLDM-MultiView

- Dataset/split: VideoLDM-MultiView / not reported
- Metric/value: TAE-ATE; TAE-RPE-R; TAE-RPE-t / TAE-ATE 0.77; TAE-RPE-R 4.25; TAE-RPE-t 0.29 (Cosmos-Predict1-7B-Text2World-Sample-Multiview); Cosmos-Predict1-7B-Text2World-Sample-Multiview-TrajectoryCond: TAE-ATE 0.54; TAE-RPE-R 4.31; TAE-RPE-t 0.18; Real video reference: TAE-ATE 0.49; TAE-RPE-R 4.60; TAE-RPE-t 0.14 (`lower-is-better`)
- Model scope: Cosmos-Predict1-7B-Text2World sample/multiview variants as reported in arXiv preprint v2
- Conditions: Upstream reported values in arXiv preprint v2 for sample/multiview variants; mapping between these reported upstream sample variants and the NIM-served/container-served named checkpoint is not established by the provided primary findings.
- Source: https://arxiv.org/html/2501.03575v2
- Locator: arXiv preprint v2 — reported numeric results in the paper's results section (arXiv html v2)
- Caveat: The canonical arXiv reported numeric rows are for upstream sample variants; the provided primary findings do not prove the evaluated upstream artifact is identical to the NIM/NGC-served checkpoint.
- Caveat: Exact dataset split used is not reported in the supplied findings.
- Caveat: Protocol details (prompting, multiview conditioning specifics, pre/post processing exact commands) are not fully specified in the arXiv facts provided; downstream revalidation recommended.

## Comparisons

### Cosmos-Predict1-7B-Video2World — `insufficient-evidence`

- Task: Text2World vs Video2World variant comparisons
- Criteria: Protocol- and dataset-matched numeric comparison required; canonical matched-protocol numeric table rows with explicit dataset/split and checkpoint identifier are not present in the supplied primary findings for both variants.
- Rationale: Release notes and container/model listings identify multiple Predict1 variants, but the supplied primary findings do not provide shared benchmark protocol or canonical numeric table rows enabling direct numeric comparison for the exact 7B Text2World artifact vs Video2World.
- Comparison conditions: Requires canonical benchmark table rows with explicit dataset/split and checkpoint identifier for both variants.
- Evidence: https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://github.com/nvidia-cosmos/cosmos-predict1

### Cosmos-Transfer2.5-2B — `insufficient-evidence`

- Task: Transfer-family vs Predict1 diffusion-family comparisons
- Criteria: Different model families and no matched-protocol evidence present in the supplied primary findings.
- Rationale: The provided primary findings do not include canonical matched-benchmark rows or protocol details that tie Transfer-family numeric claims directly to the 7B Text2World checkpoint.
- Comparison conditions: Requires canonical benchmark artifact with dataset/split and identical evaluation protocol for both families.
- Evidence: https://github.com/nvidia-cosmos/cosmos-predict1, https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html

### Cosmos-Reason1 — `insufficient-evidence`

- Task: Reasoning/backbone vs world-generation comparisons
- Criteria: Different task families; comparisons need a common evaluation protocol that is not present in the supplied findings.
- Rationale: Primary findings do not provide a shared protocol or numeric benchmark rows that would enable direct numeric comparisons between Reason-family and Predict1 diffusion-family artifacts.
- Comparison conditions: Requires matched tasks, dataset/split, and evaluation metrics in canonical primary sources.
- Evidence: https://github.com/nvidia-cosmos/cosmos-predict1, https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html

## Limitations and safety

### Limitations

- Evidence gap: The immutable upstream checkpoint revision (commit hash, release tag, or artifact ID) that would map the NIM/container artifact to a specific upstream checkpoint is not present in the provided primary findings. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://github.com/nvidia-cosmos/cosmos-predict1/releases, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world
- Evidence gap: Canonical numeric benchmark values (PSNR, SSIM, LPIPS, FID, FVD, Sampson error, TAE-*, success rate, etc.) for the 7B Text2World variant are not verifiable in the supplied primary findings except for the arXiv v2 reported multiview/trajectory metrics; other common vision/video metrics are not present in the NIM/docs/NGC/Hugging Face/GitHub sources supplied. Sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://github.com/nvidia-cosmos/cosmos-predict1/releases, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://arxiv.org/html/2501.03575v2
- Evidence gap: Runtime numeric precision (fp16, bf16, int8, or FP8/quantized variants) served by the NIM/container for the named NGC image is not specified in the supplied primary findings; some support/compatibility notes (e.g., inference tested with BF16 in NGC listing and support-matrix notes about FP8 support on specific hardware) are present but do not definitively document the runtime precision of the published NIM container image. Sources: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world, https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html, https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html
- Evidence gap: Guardrail/blocklist exact-locus gap — an exhaustive blocklist file or explicit blocklist policy file locator is not present in the supplied primary findings; docs and guardrail model listing describe guardrail components and blocklist keyword checker behavior but do not publish an exhaustive blocklist file in the supplied sources. Sources: https://docs.nvidia.com/cosmos/2.0.0/guardrail.html, https://huggingface.co/nvidia/Cosmos-1.0-Guardrail, https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world

### Safety

- The NIM reference states that bypassing, disabling, or circumventing any safety guardrail, encryption, DRM, or authentication mechanism terminates rights under the NVIDIA Open Model License. Sources: https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b
- Cosmos Guardrail is integrated into diffusion and autoregressive world-generation pipelines and includes a Blocklist keyword checker, a Video Content Safety Filter, and a Face Blur Filter; the guardrail components are intended for prompt moderation for world generation but an exhaustive blocklist file/policy locator is not published in the supplied primary findings. Sources: https://huggingface.co/nvidia/Cosmos-1.0-Guardrail, https://docs.nvidia.com/cosmos/2.0.0/guardrail.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face official NVIDIA model page - Cosmos-Predict1-7B-Text2World

- URL: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World
- Publisher: Hugging Face / NVIDIA
- Type: `model-card`
- Primary because: Official Hugging Face model card published by NVIDIA providing checkpoint identity, architecture summary, license label, and README content used by the checkpoint.
- Scope: Cosmos-Predict1-7B-Text2World
- Supports: identity
- Supports: architecture
- Supports: license
- Supports: examples

### Hugging Face legacy model page - Cosmos-1.0-Diffusion-7B-Text2World

- URL: https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World
- Publisher: Hugging Face / NVIDIA
- Type: `model-card`
- Primary because: Legacy/alternate Hugging Face model card documenting the same checkpoint identity and architecture descriptions used as upstream-checkpoint evidence.
- Scope: Cosmos-1.0-Diffusion-7B-Text2World
- Supports: identity
- Supports: architecture

### NIM reference - nvidia-cosmos-1_0-diffusion-7b

- URL: https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b
- Publisher: NVIDIA (NIM API docs)
- Type: `official-documentation`
- Primary because: NIM API/reference entry describing the checkpoint identity, architecture notes, memory/offload runtimes, and license/legal guardrail implications.
- Scope: Cosmos-Predict1-7B-Text2World (NIM reference serving metadata)
- Supports: identity
- Supports: architecture
- Supports: runtime-offload-memory
- Supports: safety

### NGC container listing - cosmos-1.0-diffusion-7b-text2world

- URL: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world
- Publisher: NVIDIA NGC (container/catalog)
- Type: `official-documentation`
- Primary because: Official NGC catalog entry for the model/container describing output format, tested precision notes, and deployment metadata.
- Scope: nvidia/cosmos-predict1-7b-text2world (NGC container/model listing)
- Supports: outputs
- Supports: deployment
- Supports: parameterScale
- Supports: runtime-tested-precision

### Predict1 model matrix (docs.nvidia.com)

- URL: https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Official Predict1 model matrix used in Predict1 documentation that records parameter scale and multiview/deployment notes referenced in the dossier.
- Scope: Cosmos-Predict1 family (model matrix)
- Supports: parameterScale
- Supports: deployment-notes
- Supports: multiview-support

### NIM Predict1 release notes (NIM) - 3.0.0

- URL: https://docs.nvidia.com/nim/cosmos/3.0.0/release-notes.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Release notes referencing Predict1 NIM identifiers and GA release metadata used to tie serving artifacts to Predict1 family names.
- Scope: Predict1 NIM release notes
- Supports: release-notes
- Supports: container-identity

### Predict1 support matrix (docs.nvidia.com) — runtime/hardware/precision notes

- URL: https://docs.nvidia.com/nim/cosmos/2.0.0/support-matrix.html
- Publisher: NVIDIA Documentation
- Type: `official-documentation`
- Primary because: Support matrix listing hardware compatibility and precision/FP8/BF16 notes included in the supplied findings.
- Scope: Predict1 support matrix
- Supports: hardware-support
- Supports: precision-compatibility
- Supports: multi-gpu-support

### nvidia-cosmos/cosmos-predict1 (GitHub repository)

- URL: https://github.com/nvidia-cosmos/cosmos-predict1
- Publisher: GitHub / NVIDIA
- Type: `repository`
- Primary because: Official repository containing examples, inference scripts, Dockerfile and example request bodies used as upstream-checkpoint/example evidence.
- Scope: Cosmos-Predict1 repository
- Supports: examples
- Supports: inference-format
- Supports: repository-code
- Supports: dockerfile

### nvidia-cosmos/cosmos-predict1 — releases page

- URL: https://github.com/nvidia-cosmos/cosmos-predict1/releases
- Publisher: GitHub / NVIDIA
- Type: `repository`
- Primary because: Repository releases page included in the supplied findings (used to identify release announcements and commit identifiers referenced in findings).
- Scope: cosmos-predict1 releases
- Supports: releases
- Supports: commit-records

### Multiview inference example file — inference_diffusion_text2world_multiview.md

- URL: https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md
- Publisher: GitHub / NVIDIA
- Type: `repository`
- Primary because: Exact repository example file demonstrating multiview/trajectory-conditioned inference request formatting cited across the dossier.
- Scope: examples/inference_diffusion_text2world_multiview.md (repo file)
- Supports: examples
- Supports: task-formatting
- Supports: inference-arguments

### arXiv preprint (v2) reporting multiview/trajectory numeric metrics

- URL: https://arxiv.org/html/2501.03575v2
- Publisher: arXiv
- Type: `paper`
- Primary because: Upstream preprint included in the supplied findings that reports numeric multiview/trajectory-conditioned metrics for sample variants of the 7B model.
- Scope: Upstream paper reporting sample/multiview variant benchmarks
- Supports: benchmarks
- Supports: architectural-notes (AdaLN-LoRA)
- Supports: numeric-results

### Cited official first-party source

- URL: https://docs.nvidia.com/cosmos/2.0.0/guardrail.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-text2world
- Supports: Exact independently audited claim citation

### Cited official first-party source

- URL: https://huggingface.co/nvidia/Cosmos-1.0-Guardrail
- Publisher: huggingface.co
- Type: `model-card`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-predict1-7b-text2world
- Supports: Exact independently audited claim citation

## Evidence gaps

- Revision/commit gap: The provided primary findings do not include an immutable upstream checkpoint identifier (commit hash, release tag, or immutable artifact ID) that unequivocally maps the NGC/NIM/container image to a specific upstream checkpoint artifact. Locations used to search (from provided findings): Hugging Face model page (https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World), NIM reference (https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b), GitHub releases (https://github.com/nvidia-cosmos/cosmos-predict1/releases), and NGC container listing (https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world).
- Benchmark numeric gap: The provided primary findings do not contain canonical numeric benchmark table/figure rows for common video/image quality metrics (PSNR, SSIM, LPIPS, FID, FVD, Sampson error, etc.) for the Cosmos-Predict1-7B-Text2World checkpoint in the NIM/docs/NGC/Hugging Face/GitHub sources supplied; an arXiv v2 preprint reports several multiview/trajectory metrics for sample variants (see https://arxiv.org/html/2501.03575v2) but mapping to the NIM-served artifact is not established.
- Runtime-precision gap: The provided primary findings do not unambiguously specify the runtime numeric precision (fp16, bf16, int8, FP8, or a quantized variant) of weights served by the NIM/container image; support notes and tested-precision mentions exist but do not definitively document the runtime precision of the published container image (checked NGC, Predict1 model matrix, and NIM support matrix).
- Input-dimension constraint gap: The provided primary findings do not contain an authoritative statement specifying exact input-dimension constraints (for example, multiples-of-8) for image/video inputs; locations checked include the NIM reference (https://docs.api.nvidia.com/nim/reference/nvidia-cosmos-1_0-diffusion-7b), Predict1 model matrix (https://docs.nvidia.com/cosmos/latest/predict1/model_matrix.html), Hugging Face model page (https://huggingface.co/nvidia/Cosmos-Predict1-7B-Text2World), and repository examples (https://github.com/nvidia-cosmos/cosmos-predict1/blob/main/examples/inference_diffusion_text2world_multiview.md).
- Guardrail/blocklist exact-locus gap: The provided primary findings reference guardrail components and keyword/blocklist behavior but do not publish an exhaustive blocklist file or explicit blocklist policy file locator in the supplied primary sources (checked https://docs.nvidia.com/cosmos/2.0.0/guardrail.html, https://huggingface.co/nvidia/Cosmos-1.0-Guardrail, and https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cosmos/models/cosmos-1.0-diffusion-7b-text2world).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 13 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[16]: $.sources[16]: missing required property modelScope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16]: $.sources[16]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[4].primary must be true: $.sources[4].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[8].primary must be true: $.sources[8].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/nvidia/Cosmos-Predict1-7B-Video2World Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.nvidia.com/nim/cosmos/latest/introduction.html Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path: $.benchmarks is empty without an evidence gap naming the exact primary-source URL and checked table/figure/section/page/heading/path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.conditionalUseCases_limitations: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.conditionalUseCases_overrides: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://docs.nvidia.com/cosmos/2.0.0/guardrail.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` https://huggingface.co/nvidia/Cosmos-1.0-Guardrail: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
