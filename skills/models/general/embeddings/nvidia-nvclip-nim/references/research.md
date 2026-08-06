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

- Research key: `build-nvidia-com-nvidia-nvclip-99e2d86333`
- Independent audit: `revised`
- Researched: `2026-07-23T22:16:09.756180+00:00`

Primary NVIDIA sources verify NV-CLIP NIM is a packaged NVIDIA multimodal embeddings NIM (Docker container image named nvidia/nvclip-vit-h-14) exposing an embeddings inference surface and health endpoint, with documented zero-shot ImageNet evaluation results (ViT-H-224 listed) and GPU/FP16 TensorRT-optimized runtime accuracy and performance numbers across multiple NVIDIA GPUs. NVIDIA documents the offering as a commercial NVIDIA version of OpenAI's CLIP lineage but does not publish an immutable upstream revision or a protocol-matched parity study. Many runtime and API operational details required for precise input/output contracts (tokenization, resize/crop/normalization, embedding dimensionality, explicit request/response field definitions beyond endpoint paths and OpenAPI schema presence) are not specified in the available primary findings and are recorded as evidence gaps.

## Identity

- Upstream name: OpenAI CLIP
- Checkpoint/version: nvclip-vit-h-14
- Immutable revision: not reported
- Parameter scale: not reported
- Architecture/head: CLIP-style multimodal text/image embedding model; NVIDIA documents a ViT-H-224 (ViT-H) variant in accuracy results and the release notes name the served model variant nvclip-vit-h-14.
- License: Model use: AI Foundation Models Community License Agreement; NIM container/software: NVIDIA Software License Agreement and Product Specific Terms for AI Product.
- Evidence: https://docs.nvidia.com/nim/nvclip/latest/release-notes.html, https://docs.nvidia.com/nim/nvclip/latest/accuracy.html, https://docs.nvidia.com/nim/nvclip/latest/EULA.html, https://developer.nvidia.com/downloads/ai-foundation-models-license, https://github.com/openai/clip/blob/main/model-card.md

## Selection

### Recommended

- **Multimodal semantic search and embedding-based retrieval over text and image data** — NVIDIA documents NV-CLIP NIM as providing state-of-the-art embedding capabilities usable for semantic search and Retrieval Augmented Generation (RAG).
  Scope: nvidia-nvclip-nim / NV-CLIP NIM
  Evidence: https://docs.nvidia.com/nim/nvclip/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip
- **Zero-shot image classification (as a validated evaluation mode)** — NVIDIA reports zero-shot ImageNet top-1 accuracy for a ViT-H-224 NV-CLIP model variant and lists zero-shot image classification as an application.
  Scope: nvidia-nvclip-nim / ViT-H-224 (ViT-H) model variant
  Evidence: https://docs.nvidia.com/nim/nvclip/latest/accuracy.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip

### Conditional

- **High-throughput multimodal embedding serving at scale** — Deployment and throughput claims are conditioned on execution on NVIDIA GPUs with documented optimized TensorRT engines; performance measurements are reported for specific GPUs (H100, A100, L40S, L4, A10G, A6000 Ada, RTX 4090, RTX 5080-WSL, RTX 5090-WSL, GH200) using FP16 and specified image input/ batch settings.
  Scope: nvidia-nvclip-nim runtime deployment
  Evidence: https://docs.nvidia.com/nim/nvclip/latest/performance.html, https://docs.nvidia.com/nim/nvclip/latest/introduction.html, https://docs.nvidia.com/nim/nvclip/latest/release-notes.html
- **Retrieval/embedding stage for RAG or multimodal retrieval** — Use is supported for embedding generation; NVIDIA documents the NIM for semantic search and RAG but does not publish downstream RAG evaluation or end-to-end calibration guidance within the provided findings.
  Scope: nvidia-nvclip-nim embedding service
  Evidence: https://docs.nvidia.com/nim/nvclip/latest/introduction.html

### Avoid

- **Clinical or healthcare decision support** — Primary NVIDIA and upstream OpenAI sources do not provide NV-CLIP-specific clinical validation, PHI handling, or healthcare safety guidance for this exact model/runtime scope; OpenAI's CLIP model card explicitly states the model was not developed for general deployment.
  Scope: nvidia-nvclip-nim / upstream CLIP lineage
  Evidence: https://github.com/openai/clip/blob/main/model-card.md
- **Selecting this model for object detection as a directly exposed Forge/NIM output** — Although NVIDIA documents downstream computer vision tasks in broad terms, the verified NV-CLIP NIM API evidence in scope documents only an embeddings endpoint; there is no primary-source documentation of a direct object-detection output head exposed by the NV-CLIP NIM API.
  Scope: nvidia-nvclip-nim API surface
  Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip, https://docs.nvidia.com/nim/nvclip/latest/api-reference.html

## Input preparation

### Semantic inputs

- The NV-CLIP NIM consumes text and image inputs for a multimodal embeddings model. Sources: https://docs.nvidia.com/nim/nvclip/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip

### Accepted formats

- The official NV-CLIP NIM API provides an embeddings endpoint at /v1/embeddings. Sources: https://docs.nvidia.com/nim/nvclip/latest/api-reference.html
- NVIDIA documents the NV-CLIP NIM programming model as OpenAI API-compatible with custom NVIDIA extensions. Sources: https://docs.nvidia.com/nim/nvclip/latest/introduction.html

### Preprocessing

- Evidence gap: The available primary findings do not specify tokenization, image resizing/cropping policy, normalization constants, batching rules, or detailed preprocessing steps required before submission to the embeddings endpoint.

### Pre-submit validation

- The NV-CLIP NIM provides a readiness health endpoint at /v1/health/ready for service availability checks before calling embeddings. Sources: https://docs.nvidia.com/nim/nvclip/latest/api-reference.html
- Evidence gap: The available primary findings do not specify maximum text length, maximum image size, request payload-size limits, invalid-modality handling, or field-level validation error details for NV-CLIP NIM.

### Task-specific formatting

- The documented inference task endpoint for NV-CLIP NIM is /v1/embeddings. Sources: https://docs.nvidia.com/nim/nvclip/latest/api-reference.html
- Evidence gap: The available primary findings do not specify a zero-shot prompt template, label-formatting rule, or paired text-image ordering convention for classification or retrieval tasks.

## Output interpretation

### Outputs

- The NV-CLIP NIM inference surface is an embeddings endpoint; outputs are embedding-oriented rather than direct classifier or detector outputs. Sources: https://docs.nvidia.com/nim/nvclip/latest/api-reference.html, https://docs.nvidia.com/nim/nvclip/latest/introduction.html
- Evidence gap: The available primary findings do not report the embedding vector dimensionality, response field names, normalization state (e.g., unit-normalized), or score units for this exact NV-CLIP NIM scope.

### Interpretation

- Embeddings from NV-CLIP NIM are documented for semantic search, retrieval, and multimodal search; outputs should be interpreted as representation vectors for similarity/retrieval workflows rather than as standalone factual judgments. Sources: https://docs.nvidia.com/nim/nvclip/latest/introduction.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip
- Evidence gap: The available primary findings do not define similarity-score semantics, calibrated thresholds, or recommended interpretation thresholds for this NV-CLIP NIM scope.

### Post-inference validation

- NVIDIA validates NV-CLIP NIM zero-shot performance on the ImageNet validation dataset of 50,000 images and reports top-1 accuracy; downstream users should perform their own validation on target datasets for classification-style uses. Sources: https://docs.nvidia.com/nim/nvclip/latest/accuracy.html
- Evidence gap: The available primary findings do not provide post-inference quality checks, drift-detection thresholds, or embedding sanity-validation procedures for this exact NV-CLIP NIM scope.

## Public benchmarks

### Zero-shot image classification

- Dataset/split: ImageNet validation dataset / validation
- Metric/value: top-1 accuracy / 0.7786 (`higher-is-better`)
- Model scope: nvidia-nvclip-nim / ViT-H-224 (ViT-H) model variant
- Conditions: NVIDIA-reported NV-CLIP NIM zero-shot evaluation on the ImageNet validation dataset of 50,000 images.
- Source: https://docs.nvidia.com/nim/nvclip/latest/accuracy.html
- Locator: Accuracy page; zero-shot ImageNet evaluation statements for the ViT-H-224 model variant.
- Caveat: The accuracy page lists a ViT-H-224 zero-shot numeric entry (0.7786) and the release notes name a served variant nvclip-vit-h-14; the findings do not explicitly reconcile whether ViT-H-224 and nvclip-vit-h-14 are identical aliases within the provided primary documentation.
- Caveat: This is a documented NVIDIA runtime/model evaluation; upstream checkpoint parity is not established by a protocol-matched published study in the provided sources.

### Zero-shot image classification (TensorRT-optimized runtime)

- Dataset/split: ImageNet / not reported
- Metric/value: top-1 accuracy / 76.91% (`higher-is-better`)
- Model scope: nvidia-nvclip-nim optimized TensorRT model on H100 SXM GPU, FP16
- Conditions: Optimized TensorRT NV-CLIP measurement on H100 SXM GPU using FP16 precision; NVIDIA reports this per-GPU optimized runtime accuracy in the accuracy documentation.
- Source: https://docs.nvidia.com/nim/nvclip/latest/accuracy.html
- Locator: Accuracy page; H100 SXM GPU FP16 ImageNet top-1 row.
- Caveat: These optimized TensorRT numbers are runtime- and precision-specific (FP16, TensorRT) and should not be interpreted as unconditional upstream checkpoint-only metrics without a published parity protocol.
- Caveat: The accuracy page provides multiple per-GPU FP16 optimized numbers; mapping between the ViT-H-224 zero-shot entry (0.7786) and the per-GPU optimized rows is not explicitly reconciled in the provided findings.

## Comparisons

### OpenAI CLIP upstream checkpoint lineage — `insufficient-evidence`

- Task: Whether the Forge-served NVIDIA NV-CLIP NIM is proven to be an unchanged packaging of a named upstream checkpoint
- Criteria: Identity equivalence, exact checkpoint naming, immutable revision, and protocol-matched numerical parity
- Rationale: NVIDIA primary sources state NV-CLIP is the NVIDIA commercial version of OpenAI's CLIP and name a served variant (nvclip-vit-h-14), but the available findings do not publish an immutable upstream revision or a protocol-matched side-by-side parity study demonstrating unchanged packaging of a specific upstream checkpoint.
- Comparison conditions: NVIDIA container/catalog, release notes, and OpenAI model card statements cited; no protocol-matched parity or immutable revision locator is published in the provided findings.
- Evidence: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip, https://docs.nvidia.com/nim/nvclip/latest/release-notes.html, https://github.com/openai/clip/blob/main/model-card.md

## Limitations and safety

### Limitations

- Evidence gap: The available primary findings do not report an immutable upstream revision or parameter count for the exact served NV-CLIP scope.
- Evidence gap: The available primary findings do not specify exact preprocessing, tokenization, embedding dimensionality, normalization, or detailed output-schema fields for this NV-CLIP NIM scope.
- A known runtime limitation in NV-CLIP NIM release 2.0.0 is that running with -u $(id -u) is not supported due to permission issues when downloading models. Sources: https://docs.nvidia.com/nim/nvclip/latest/release-notes.html
- OpenAI's CLIP model card states the upstream CLIP model was not developed for general deployment and that deployment requires careful study of capabilities. Sources: https://github.com/openai/clip/blob/main/model-card.md

### Safety

- Use of the NV-CLIP model is governed by the AI Foundation Models Community License Agreement; the NIM container/software is governed by the NVIDIA Software License Agreement and Product Specific Terms for AI Product. Deployments should respect both layers of terms. Sources: https://docs.nvidia.com/nim/nvclip/latest/EULA.html, https://developer.nvidia.com/downloads/ai-foundation-models-license
- The AI Foundation Models Community License grants a non-exclusive, revocable, non-transferable, non-sublicensable license permitting installation and use for non-production purposes including test and evaluation; derivative-model distribution for non-production uses is permitted under conditions in the license. Sources: https://developer.nvidia.com/downloads/ai-foundation-models-license
- OpenAI's CLIP model card documents limitations including fairness/bias concerns and notes the model was not developed for general deployment. Sources: https://github.com/openai/clip/blob/main/model-card.md
- Evidence gap: The available primary findings for this exact NV-CLIP NIM scope do not provide explicit PHI handling, clinical safety protocols, or healthcare expert-review guidance.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NGC NV-CLIP container page

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/nvclip
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NGC container/catalog page describing the NV-CLIP NIM packaging, documented applications, and stated lineage.
- Scope: NV-CLIP NIM container/service
- Supports: identity
- Supports: identity lineage claim
- Supports: recommended use cases
- Supports: avoid-use API-scope boundary

### NVIDIA NIM for NV-CLIP Introduction

- URL: https://docs.nvidia.com/nim/nvclip/latest/introduction.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA product documentation describing the NV-CLIP NIM service, programming model, and suggested applications (semantic search, RAG).
- Scope: NV-CLIP NIM service/runtime introduction
- Supports: recommended use cases
- Supports: conditional deployment use
- Supports: input semantics
- Supports: accepted formats
- Supports: output interpretation

### NVIDIA NIM for NV-CLIP API Reference

- URL: https://docs.nvidia.com/nim/nvclip/latest/api-reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA API reference documenting the embeddings and health endpoints and the OpenAPI schema presence for the service.
- Scope: NV-CLIP NIM API
- Supports: input accepted formats
- Supports: task formatting
- Supports: validation
- Supports: output contract scope

### NVIDIA NIM for NV-CLIP Accuracy

- URL: https://docs.nvidia.com/nim/nvclip/latest/accuracy.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA benchmark/accuracy documentation reporting zero-shot ViT-H-224 accuracy and per-GPU FP16 optimized TensorRT top-1 accuracy rows.
- Scope: NV-CLIP NIM evaluated on ImageNet; accuracy and per-GPU optimized runtime metrics
- Supports: benchmarks
- Supports: recommended zero-shot use
- Supports: output validation guidance

### NVIDIA NIM for NV-CLIP Performance

- URL: https://docs.nvidia.com/nim/nvclip/latest/performance.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA runtime performance documentation providing measured latency and throughput for specific GPUs, batch, and image-size conditions.
- Scope: NV-CLIP NIM runtime performance
- Supports: conditional deployment use
- Supports: performance conditions

### NVIDIA NIM for NV-CLIP Release Notes

- URL: https://docs.nvidia.com/nim/nvclip/latest/release-notes.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA release notes naming the served model variant nvclip-vit-h-14 and documenting a known runtime limitation in release 2.0.0.
- Scope: NV-CLIP NIM release history and limitations
- Supports: identity checkpoint
- Supports: conditional deployment use
- Supports: limitations

### NVIDIA NIM for NV-CLIP EULA

- URL: https://docs.nvidia.com/nim/nvclip/latest/EULA.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA licensing EULA page distinguishing NIM container/software terms from model-use licensing and pointing to the AI Foundation Models license.
- Scope: NV-CLIP NIM licensing (container and model-use layers)
- Supports: identity license
- Supports: safety/license handling

### NVIDIA AI Foundation Models Community License

- URL: https://developer.nvidia.com/downloads/ai-foundation-models-license
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA reference to the AI Foundation Models Community License governing model use; provides license terms permitting non-production uses and outlining distribution/derivative conditions.
- Scope: Model license terms referenced for NV-CLIP model use
- Supports: identity license
- Supports: safety/license handling

### OpenAI CLIP model card

- URL: https://github.com/openai/clip/blob/main/model-card.md
- Publisher: OpenAI
- Type: `model-card`
- Primary because: OpenAI's official CLIP model card documenting upstream CLIP's intended research purpose, limitations, and deployment cautions referenced by NVIDIA.
- Scope: Upstream CLIP lineage and upstream deployment cautions
- Supports: identity upstream name
- Supports: architecture lineage
- Supports: safety/deployment caution
- Supports: limitations
- Supports: comparison evidence

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/nvclip
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: nvidia-nvclip
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Checked https://docs.nvidia.com/nim/nvclip/latest/accuracy.html: The accuracy page reports ImageNet zero-shot accuracy and per-GPU optimized TensorRT numbers, but the findings do not provide a protocol-matched upstream-versus-NIM parity study or an immutable upstream revision locator proving identical packaged weights.
- Checked https://github.com/openai/clip/blob/main/model-card.md and https://docs.nvidia.com/nim/nvclip/latest/release-notes.html: The available findings do not report a directly matching upstream checkpoint name/revision and numeric value pair that can be unambiguously mapped to the served nvclip-vit-h-14 runtime.
- Checked https://docs.nvidia.com/nim/nvclip/latest/api-reference.html and https://docs.nvidia.com/nim/nvclip/latest/introduction.html: The available findings do not specify tokenization, image resize/crop policy, normalization constants, batching preprocessing, or explicit example request/response JSON payloads for the embeddings endpoint.
- Checked https://docs.nvidia.com/nim/nvclip/latest/api-reference.html: The available findings do not declare maximum text length, maximum image size, or field-level validation error formats for NV-CLIP NIM.
- Checked https://docs.nvidia.com/nim/nvclip/latest/api-reference.html and https://docs.nvidia.com/nim/nvclip/latest/introduction.html: The available findings do not provide a zero-shot prompt template, label formatting convention, or paired text-image ordering rule for classification/retrieval tasks.
- Checked https://docs.nvidia.com/nim/nvclip/latest/api-reference.html and https://docs.nvidia.com/nim/nvclip/latest/accuracy.html: The available findings do not report the embedding vector dimensionality, response field names, normalization state (unit normalization), or score units for this NV-CLIP NIM scope.
- Checked https://docs.nvidia.com/nim/nvclip/latest/EULA.html and https://developer.nvidia.com/downloads/ai-foundation-models-license: The available findings do not unambiguously state whether all forms of production deployment are permitted under the AI Foundation Models Community License for every use case; the license text documents non-production permissions and other constraints that require user review.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/nvclip Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://build.nvidia.com/nvidia/nvclip: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
