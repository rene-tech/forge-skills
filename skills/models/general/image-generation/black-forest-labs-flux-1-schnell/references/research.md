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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-schnel-145d8ced5b`
- Independent audit: `revised`
- Researched: `2026-07-23T22:33:47.166051+00:00`

Checkpoint-scoped primary evidence available in the inspected authoritative sources (NVIDIA NIM docs and API pages, NVIDIA-hosted Black Forest Labs model card, the Hugging Face repository for the exact checkpoint, and the upstream GitHub repository and license file) documents FLUX.1-schnell as a Black Forest Labs text-to-image checkpoint served via NVIDIA NIM/NGC. Primary evidence consistently reports a 12 billion parameter scale and that the model produces RGB images from text prompts with a distilled architecture optimized for few-step generation (1–4 diffusion steps). Primary sources present overlapping but not fully reconcilable architecture descriptors (see identity.architecture). The model weights license is documented as Apache-2.0 in upstream sources; NIM/NGC packaging is governed by NVIDIA licensing for containers. Primary sources inspected do not publish checkpoint-scoped benchmark tables or protocol-matched peer comparisons, do not specify tokenizer identity or explicit tokenization/truncation bounds, and do not report an immutable upstream revision identifier (commit hash or artifact digest) for this exact checkpoint. See evidenceGaps for exact checked locators.

## Identity

- Upstream name: FLUX.1-schnell
- Checkpoint/version: FLUX.1-schnell; NVIDIA NIM container tag nvcr.io/nim/black-forest-labs/flux.1-schnell:1.1.4 (as listed on the NVIDIA getting-started latest page)
- Immutable revision: not reported
- Parameter scale: 12 billion parameters
- Architecture/head: Conflicting primary-source descriptors for this exact checkpoint: (A) "rectified flow transformer" (Black Forest Labs model card hosted by NVIDIA: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard); (B) implementation-level modular description from the upstream GitHub model.py (https://github.com/black-forest-labs/flux/blob/main/src/flux/model.py) showing transformer-like blocks, embedding layers, and convolutional-style in/out channels; also described in product/overview documentation as a distilled architecture optimized for few-step generation (https://docs.nvidia.com/nim/visual-genai/latest/overview.html). These primary sources present overlapping but not fully reconciled architecture descriptors for the exact checkpoint.
- License: Model weights license: Apache-2.0 (as stated in the upstream Hugging Face repository and the GitHub repository license file). NVIDIA container/catalog pages also reference that the model is available under Apache License, Version 2.0 but the NIM/NGC packaging is governed by NVIDIA Software License Agreement / Product-Specific Terms.
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html, https://docs.nvidia.com/nim/visual-genai/1.5.1/api/flux.1-schnell.html, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-schnell

## Selection

### Recommended

- **Text-to-image generation from plain-text prompts** — Primary NVIDIA-hosted Black Forest Labs model card and the Hugging Face repository describe FLUX.1-schnell as a text-to-image model that generates images from text descriptions and provide sampling/reference implementations.
  Scope: Exact upstream checkpoint FLUX.1-schnell (as documented in the NVIDIA-hosted model card and the upstream Hugging Face repository)
  Evidence: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux
- **Fast, low-step exploratory image generation (few diffusion steps for prompt exploration)** — The NVIDIA-hosted model card and NVIDIA product overview indicate the checkpoint is a distilled model optimized to produce high-quality images in 1–4 diffusion steps suitable for fast local experimentation.
  Scope: Exact upstream checkpoint FLUX.1-schnell and its NVIDIA-served packaging
  Evidence: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://docs.nvidia.com/nim/visual-genai/latest/overview.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell

### Conditional

- **Commercial deployment of FLUX.1-schnell via NVIDIA NIM/NGC** — Deploy only after confirming and accepting NVIDIA container and product license/acceptable-use terms referenced by the NIM/NGC pages and after ensuring any required NVIDIA account/subscription access controls are satisfied.
  Scope: NVIDIA-served container image and NIM packaging for FLUX.1-schnell
  Evidence: https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

### Avoid

- **Treating NVIDIA NIM/NGC packaging or NIM container metadata as checkpoint-quality benchmark evidence** — The NVIDIA NIM/NGC pages and the NVIDIA-hosted model card provide container identity, packaging, and qualitative capability descriptions but do not provide checkpoint-scoped benchmark tables with dataset/split/metric/value entries or protocol-matched quantitative quality metrics for this exact checkpoint.
  Scope: NVIDIA NIM FLUX.1-schnell documentation and NGC container metadata
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html

## Input preparation

### Semantic inputs

- Semantic input is a text prompt (plain-text prompt) used to produce an image from the checkpoint. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell

### Accepted formats

- Primary documentation and upstream repository indicate the model consumes textual prompts (plain-text strings) as the input modality for generation. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell
- Upstream Hugging Face repository provides reference implementation and sampling code demonstrating programmatic loading and invocation patterns for the checkpoint. Sources: https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux

### Preprocessing

- Primary sources document that FLUX.1-schnell is a distilled image-generation model optimized for few-step sampling and that sampling step counts (1–4) are a documented property of the checkpoint's distilled design. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://docs.nvidia.com/nim/visual-genai/latest/overview.html
- NVIDIA NIM getting-started and packaging documentation describe NIM container packaging and variant selection (serving/runtime packaging) used to invoke the model in NVIDIA contexts. Sources: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html

### Pre-submit validation

- Primary sources inspected do not specify tokenizer identity, vocabulary, tokenization/truncation rules, or explicit prompt-length bounds for FLUX.1-schnell. Sources: https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html
- Access to the NVIDIA-served container and NIM endpoints requires acceptance of the container/model license and acceptable-use terms as documented by NVIDIA; confirm account/subscription requirements before attempting to access the NVIDIA-served checkpoint. Sources: https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell

### Task-specific formatting

- The upstream Hugging Face repository reports a reference implementation and sampling code (a dedicated GitHub repository) for programmatic invocation patterns; users should follow the upstream repository's provided code for exact input-field names and pipeline usage. Sources: https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux

## Output interpretation

### Outputs

- The model produces synthesized 2D RGB images from text prompts (text-to-image generation outputs). Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell

### Interpretation

- Primary sources characterize output quality qualitatively (high-quality images, distilled few-step generation) but do not provide calibrated confidence scores or quantitative per-image quality metrics for the checkpoint. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://docs.nvidia.com/nim/visual-genai/latest/overview.html

### Post-inference validation

- Primary sources inspected do not specify post-inference calibration procedures, per-image confidence semantics, nor automated quantitative output-validation checks for FLUX.1-schnell. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Conflicting architecture descriptors across primary sources: the NVIDIA-hosted model card explicitly calls the checkpoint a "rectified flow transformer" while the upstream GitHub implementation exposes transformer-like blocks, embedding layers, and convolutional-style input/output channel handling; product overview also emphasizes a distilled architecture optimized for few-step generation. These descriptions overlap but are not fully reconciled by the inspected primary sources. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://github.com/black-forest-labs/flux, https://docs.nvidia.com/nim/visual-genai/latest/overview.html
- Training dataset and detailed evaluation datasets/splits are not disclosed in the inspected primary sources for this checkpoint. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux
- No checkpoint-scoped public benchmark rows (dataset, split, metric, value) were found in the inspected primary sources for FLUX.1-schnell. Sources: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://huggingface.co/black-forest-labs/FLUX.1-schnell, https://github.com/black-forest-labs/flux, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html
- Separation of responsibilities: FLUX.1-schnell is developed/upstreamed by Black Forest Labs (upstream repository and Hugging Face), while NVIDIA provides packaging/serving via NIM/NGC; NIM/NGC documentation governs container usage and packaging but does not assert upstream model development ownership. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard, https://github.com/black-forest-labs/flux

### Safety

- Use of the NVIDIA-served container and NIM endpoints requires reading and acceptance of the model/container license agreements and acceptable-use policy prior to access; NIM getting-started and NGC catalog entries document access/license controls. Sources: https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- The NGC/container packaging and use of certain packaged models within the container are governed by NVIDIA-specific license terms (NVIDIA Software License Agreement, Product-Specific Terms) and the NVIDIA Open Model License Agreement as referenced on NGC/NIM pages; upstream model weights are separately licensed under Apache-2.0 per the upstream repository license file. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-schnell, https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard
- Evidence gap: The inspected primary sources do not enumerate domain-specific safety validation (for example, healthcare/clinical/regulatory suitability) for FLUX.1-schnell; do not infer suitability for regulated domains without additional documented validation.

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM Visual GenAI Getting Started (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA documentation for the NIM model entry and container metadata in scope (lists container image identity and supported variants).
- Scope: NVIDIA NIM packaging and container metadata for FLUX.1-schnell
- Supports: identity.checkpoint
- Supports: conditionalUseCases
- Supports: inputPreparation.preprocessings
- Supports: safety

### NVIDIA NIM Getting Started v1.1.1

- URL: https://docs.nvidia.com/nim/visual-genai/1.1.1/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned NVIDIA documentation that documents license/acceptable-use acceptance and variant selection environment variables for NIM containers.
- Scope: NVIDIA NIM access and variant selection controls for FLUX.1-schnell
- Supports: inputPreparation.validation
- Supports: safety

### NVIDIA NIM Visual GenAI API Page: FLUX.1-schnell (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Canonical NVIDIA API/model reference for the served checkpoint in Visual GenAI docs.
- Scope: NVIDIA-served API reference for FLUX.1-schnell
- Supports: identity.architecture
- Supports: inputPreparation.acceptedFormats
- Supports: outputInterpretation.outputs
- Supports: limitations

### NVIDIA NIM Visual GenAI API Page: FLUX.1-schnell (v1.5.1)

- URL: https://docs.nvidia.com/nim/visual-genai/1.5.1/api/flux.1-schnell.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned NVIDIA API reference page included among inspected primary sources for revision/update metadata.
- Scope: Versioned NVIDIA-served API page for FLUX.1-schnell
- Supports: identity.architecture
- Supports: identity.evidenceUrls

### NVIDIA NIM Visual GenAI Overview (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Product overview describing distilled architecture and few-step generation properties for FLUX.1-schnell in the Visual GenAI product docs.
- Scope: Product overview statements about distilled design and few-step optimization
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: limitations

### NVIDIA NGC catalog entry for FLUX.1-schnell container

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NGC catalog entry describing distributed container image, packaging, and NVIDIA-specific license/terms references.
- Scope: NGC container metadata and packaging for FLUX.1-schnell
- Supports: identity.checkpoint
- Supports: identity.license
- Supports: conditionalUseCases
- Supports: safety

### Black Forest Labs FLUX.1-schnell Model Card (NVIDIA-hosted)

- URL: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard
- Publisher: Black Forest Labs (hosted by NVIDIA)
- Type: `model-card`
- Primary because: Official upstream model card for the exact checkpoint hosted on NVIDIA Build; contains parameter scale, distilled architecture descriptor, few-step sampling claim, and commercial-use statement.
- Scope: Upstream checkpoint FLUX.1-schnell model card (NVIDIA-hosted)
- Supports: identity.parameterScale
- Supports: identity.architecture
- Supports: recommendedUseCases
- Supports: limitations
- Supports: outputInterpretation.outputs

### Hugging Face: black-forest-labs/FLUX.1-schnell (repository root)

- URL: https://huggingface.co/black-forest-labs/FLUX.1-schnell
- Publisher: Black Forest Labs (Hugging Face repository)
- Type: `repository`
- Primary because: Official upstream Hugging Face repository root for the exact checkpoint; lists parameter scale and license and references a reference implementation.
- Scope: Upstream checkpoint FLUX.1-schnell repository
- Supports: identity.parameterScale
- Supports: identity.license
- Supports: inputPreparation.taskSpecificFormatting
- Supports: recommendedUseCases

### Black Forest Labs GitHub repository (FLUX family)

- URL: https://github.com/black-forest-labs/flux
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Official upstream GitHub repository containing model implementation files and the checkpoint-specific license file; used to verify implementation-level architecture descriptors and license file presence.
- Scope: Upstream FLUX family repository including FLUX.1-schnell
- Supports: identity.architecture
- Supports: identity.license
- Supports: inputPreparation.taskSpecificFormatting

### GitHub license file for FLUX.1-schnell (LICENSE-FLUX1-schnell)

- URL: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-schnell
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Explicit upstream license file for this exact checkpoint in the official repository tree.
- Scope: Exact checkpoint license file
- Supports: identity.license

## Evidence gaps

- Benchmarks: Checked primary sources for checkpoint-scoped benchmark tables/rows for FLUX.1-schnell and found none. Checked the following primary URLs and locators for explicit checkpoint-scoped benchmark tables/rows: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card page and its headings/sections), https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository root and README), https://github.com/black-forest-labs/flux (repository root and README/benchmarks paths), https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell (NGC catalog page), and https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (NIM API reference page). No dataset/split/metric/value checkpoint-scoped benchmark rows were located in those primary-source locators.
- Comparisons: No protocol-matched, checkpoint-scoped primary-source comparisons for FLUX.1-schnell versus named peer models were found in the inspected primary-source locators. Checked: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card sections), https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository), https://github.com/black-forest-labs/flux (repository), https://catalog.ngc.nvidia.com/orgs/nim/teams/black-forest-labs/containers/flux.1-schnell (NGC catalog), and https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (API reference). No protocol-matched peer-comparison tables or rows were located.
- Tokenizer and tokenization bounds: The inspected primary sources do not specify tokenizer identity, vocabulary, tokenization rules, or explicit prompt-length/truncation behavior for FLUX.1-schnell. Checked: https://huggingface.co/black-forest-labs/FLUX.1-schnell (repo root and README), https://github.com/black-forest-labs/flux (repository code paths, including src/flux/model.py), https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card), and https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (API reference).
- Post-inference calibration and confidence semantics: The inspected primary sources do not document post-inference calibration procedures, per-image confidence scores, or automated output-validation semantics for generated images from FLUX.1-schnell. Checked: https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card sections), https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository), and https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (API reference).
- Supported output resolutions and exact output-shape parameters: The inspected primary sources do not list an explicit enumeration of supported output resolutions or exact output-shape parameter table for the checkpoint. Checked: https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (API reference), https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card), and https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository).
- Seed semantics and reproducibility controls: The inspected primary sources do not provide an explicit, checkpoint-scoped specification of the 'seed' field semantics for reproducibility (e.g., whether a fixed seed yields bit-for-bit identical images across runtimes and packaging). Checked: https://docs.nvidia.com/nim/visual-genai/latest/api/flux.1-schnell.html (API reference), https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card), and https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository).
- Immutable revision identifier: The inspected primary sources do not report an immutable upstream revision identifier (for example, a commit hash or model artifact digest) for FLUX.1-schnell. Checked: https://github.com/black-forest-labs/flux (repository root and commits), https://huggingface.co/black-forest-labs/FLUX.1-schnell (repository), and https://build.nvidia.com/black-forest-labs/flux_1-schnell/modelcard (model card).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 7 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[9].primary must be true: $.sources[9].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses forbidden secondary URL https: $.sources[10] uses forbidden secondary URL https://huggingface.co/black-forest-labs/FLUX.1-schnell/discussions/55 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].primary must be true: $.sources[11].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary URL https: $.sources[17] uses forbidden secondary URL https://huggingface.co/black-forest-labs/FLUX.1-schnell/discussions/147 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
