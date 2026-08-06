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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-black-forest-labs-flux-1-dev-51a0d62834`
- Independent audit: `revised`
- Researched: `2026-07-24T00:08:06.882166+00:00`

Checked canonical upstream primary sources (Black Forest Labs GitHub model card and docs, and the Hugging Face model repository). Verified checkpoint-scoped facts available in those sources: (1) Upstream descriptions identify FLUX.1 [dev] as a 12 billion-parameter rectified flow transformer for text→image generation (source: Hugging Face model landing; GitHub model card). (2) A SHA-256 checksum string 4610115bb0c89560703c892c59ac2742fa821e60ef5871b33493ba544683abd7 is published in the upstream GitHub docs/text-to-image.md and is attributed there to FLUX.1‑dev. (3) The upstream license text for FLUX.1 [dev] is published as the FLUX.1 [dev] Non‑Commercial License in the repository model_licenses/LICENSE-FLUX1-dev and reiterated in the Hugging Face LICENSE.md. (4) The Hugging Face model repo landing and tree list Diffusers-style artifacts and repository files for FLUX.1-dev. Evidence gaps (items not specified in inspected primary locators): exact tokenizer internals (class, vocab/special-token files, max token length), exact numeric image-preprocessing hyperparameters (resize values, normalization mean/std, channel ordering, crop/pad policy), canonical probabilistic numeric outputs (likelihoods/log-probabilities/calibrated confidences), canonical quantized weight artifacts explicitly tied to flux1-dev.safetensors from the upstream author, and per-checkpoint numeric benchmark rows attributed to the exact flux1-dev.safetensors checkpoint. All claims and gaps above are tied to the exact primary-file locators listed in the sources section.

## Identity

- Upstream name: black-forest-labs/FLUX.1-dev
- Checkpoint/version: flux1-dev.safetensors
- Immutable revision: 4610115bb0c89560703c892c59ac2742fa821e60ef5871b33493ba544683abd7
- Parameter scale: 12 billion parameters
- Architecture/head: rectified flow transformer
- License: FLUX.1 [dev] Non‑Commercial License
- Evidence: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main

## Selection

### Recommended

- **Text-to-image generation (single text prompt → generated image)** — Upstream model card and the Hugging Face model landing describe FLUX.1 [dev] as a generative text→image model and provide usage examples and Diffusers-style runtime guidance.
  Scope: black-forest-labs/FLUX.1-dev (upstream model card and Hugging Face README/tree)
  Evidence: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md
- **Image-conditioned generation/editing using explicitly enumerated FLUX.1 [dev] variants (e.g., Fill, Canny, Depth, Kontext) when those variants are selected upstream** — The upstream model card and repository enumerate dev variants intended for image-conditioned uses and document variant-specific usage.
  Scope: black-forest-labs/FLUX.1-dev variants as enumerated in the upstream model card and Hugging Face repo tree
  Evidence: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main

### Conditional

- **Low-precision / quantized deployment for accelerated inference (conditional)** — Only appropriate if canonical upstream-published quantized weight files explicitly reference the exact flux1-dev.safetensors filename and checksum and upstream documentation validates runtime compatibility; the inspected upstream primary locators do not publish such quantized artifacts tied to flux1-dev.safetensors.
  Scope: canonical upstream flux1-dev.safetensors and any separately published quantized weight files that explicitly reference that file (none found at the checked locators)
  Evidence: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://github.com/black-forest-labs/flux/blob/main/docs/image-editing.md, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md

### Avoid

- **Commercial or production deployment without obtaining a separate commercial license from Black Forest Labs** — The upstream FLUX.1 [dev] license files published in the upstream repository and on the Hugging Face model repo identify the FLUX.1 [dev] Non‑Commercial License and restrict the dev-model weights and inference code to non-commercial/non-production use per the upstream license text.
  Scope: black-forest-labs/FLUX.1-dev (upstream LICENSE files)
  Evidence: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
- **Relying on model-generated calibrated likelihoods/log-probabilities/confidence scores for automated decision-making** — Inspected upstream documentation (model card and README) describes generated image artifacts and usage examples but does not document probabilistic numeric outputs (likelihoods/log-probabilities/calibrated confidence scores) for the checkpoint at those locators.
  Scope: black-forest-labs/FLUX.1-dev (upstream model card and Hugging Face README/tree)
  Evidence: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md

## Input preparation

### Semantic inputs

- Primary input: a single text prompt (one text string) used to condition image generation, as described in upstream usage examples. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md
- Optional image-conditioned inputs: upstream materials enumerate dev variants (e.g., Fill/Canny/Depth/Kontext) that indicate optional RGB image inputs for structural conditioning when those variants are selected upstream. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main

### Accepted formats

- Upstream Hugging Face repository landing and tree list Diffusers-style artifacts and runtime files, indicating availability of model_index.json and safetensors weight files suitable for Diffusers-style runtimes. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main

### Preprocessing

- The Hugging Face repository tree and README list model files (Diffusers-style artifacts) that are expected to be consumed by runtime code; exact numeric preprocessing hyperparameters are not specified at the inspected locators. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md
- Evidence gap: Exact tokenizer/tokenization specifics for FLUX.1-dev (tokenizer class, vocabulary file(s), special tokens, max token length) are not specified at the inspected upstream locators. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md
- Evidence gap: Exact numeric image preprocessing rules for image-conditioned inputs (resize/crop/pad/aspect-ratio policy, numeric resize values, normalization mean/std, channel order) are not documented at the inspected upstream locators. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md

### Pre-submit validation

- Evidence gap: Explicit input validation constraints (exact character/token limits, per-request image-count limits, or exact prompt-length bounds) are not provided at the inspected upstream locators. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main

### Task-specific formatting

- Upstream model card and README provide usage guidance and examples but do not prescribe a single canonical prompt template or enforced prompt-format at the inspected locators. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md

## Output interpretation

### Outputs

- Primary output object: generated images produced by the model from text prompts or image-conditioned variants, as described in the upstream README and model card. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md

### Interpretation

- Evidence gap: The inspected upstream model card and Hugging Face README do not document probabilistic numeric outputs (likelihoods, log-probabilities, or calibrated confidence scores) for the checkpoint; interpret outputs as generated image artifacts without upstream-provided calibrated numeric scores. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md

### Post-inference validation

- Evidence gap: No upstream guidance found at the inspected locators for numeric calibration, probabilistic score validation, or recommended post-processing validation checks for image outputs. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Task-level head-to-head numeric comparisons for image-generation benchmarks tied to flux1-dev.safetensors
- Criteria: No per-dataset numeric benchmark tables or head-to-head comparison rows explicitly attributed to the exact flux1-dev.safetensors checkpoint were found in the inspected primary locators.
- Rationale: Inspected the upstream GitHub model card, docs/text-to-image.md, and the Hugging Face model landing/tree and did not find verifiable benchmark rows or comparison tables for flux1-dev.safetensors.
- Comparison conditions: No comparable primary-side protocol rows present; cannot perform task- and protocol-specific comparison.
- Evidence: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md, https://huggingface.co/black-forest-labs/FLUX.1-dev

## Limitations and safety

### Limitations

- The FLUX.1 [dev] Non‑Commercial License restricts use of dev-model weights and inference code to non-commercial/non-production purposes; commercial deployment requires obtaining a separate commercial license per the upstream license text. Sources: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
- Evidence gap: Per-dataset numeric benchmark tables (dataset name, split, metric, numeric value) explicitly attributed to the exact flux1-dev.safetensors checkpoint were not found at the inspected upstream primary locators. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev, https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md
- Evidence gap: Exact tokenizer/tokenization internals (tokenizer class, vocabulary file(s), special tokens, and max token length) for FLUX.1-dev are not specified at the inspected upstream locators. Sources: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md

### Safety

- Adhere to the upstream FLUX.1 [dev] Non‑Commercial License terms: do not use the dev-model weights for commercial/production purposes without obtaining appropriate commercial licensing from Black Forest Labs. Sources: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
- Evidence gap: No inspected upstream primary source specifies a canonical automated content-filtering implementation, safety pipeline, or enforced moderation controls for FLUX.1-dev at the checked locators; implementers should assume no upstream-provided filter and perform independent safety review and content moderation. Sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Black Forest Labs repository: flux (GitHub)

- URL: https://github.com/black-forest-labs/flux
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Official upstream GitHub repository containing model cards, docs, and license files for FLUX.1 variants.
- Scope: black-forest-labs/flux (repository root)
- Supports: Repository-level listing of model_cards, docs, and model_licenses
- Supports: General repository metadata and links to specific model files

### Black Forest Labs model card: FLUX.1-dev (GitHub)

- URL: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Official model card for FLUX.1-dev describing model identity, variants, and usage guidance at the repository.
- Scope: black-forest-labs/flux (model_cards/FLUX.1-dev.md)
- Supports: Statement that FLUX.1 [dev] is a 12B rectified flow transformer
- Supports: Enumeration of dev variants (Fill/Canny/Depth/Kontext/etc.)
- Supports: Usage guidance and examples as provided upstream

### Black Forest Labs FLUX.1-dev license file (GitHub)

- URL: https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Canonical license file hosted in the official upstream repository enumerating the FLUX.1 [dev] Non‑Commercial license terms.
- Scope: black-forest-labs/flux (model_licenses/LICENSE-FLUX1-dev)
- Supports: Identification of FLUX.1 [dev] Non‑Commercial License and enumerated prohibitions/usage restrictions

### GitHub docs: text-to-image (Black Forest Labs)

- URL: https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Documentation in the upstream repository listing model variants and published SHA-256 checksums attributed to FLUX.1 variants including FLUX.1-dev.
- Scope: black-forest-labs/flux (docs/text-to-image.md)
- Supports: Published SHA-256 checksum for FLUX.1-dev (4610115bb0c89560703c892c59ac2742fa821e60ef5871b33493ba544683abd7)
- Supports: License attribution and model variant listings

### GitHub docs: image-editing (Black Forest Labs)

- URL: https://github.com/black-forest-labs/flux/blob/main/docs/image-editing.md
- Publisher: Black Forest Labs
- Type: `repository`
- Primary because: Upstream documentation referencing FLUX.1 variants and checksums for image-editing variants.
- Scope: black-forest-labs/flux (docs/image-editing.md)
- Supports: Association of FLUX.1 variants with documentation and variant descriptions

### Hugging Face model landing: black-forest-labs/FLUX.1-dev

- URL: https://huggingface.co/black-forest-labs/FLUX.1-dev
- Publisher: Black Forest Labs (Hugging Face model repo)
- Type: `model-card`
- Primary because: Canonical Hugging Face model landing and README for FLUX.1-dev documenting files, README content, and model description.
- Scope: black-forest-labs/FLUX.1-dev (Hugging Face landing)
- Supports: High-level model description stating 12B rectified flow transformer identity
- Supports: Pointer to repository files and usage guidance

### Hugging Face repository tree for FLUX.1-dev (files listing)

- URL: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main
- Publisher: Black Forest Labs (Hugging Face repo)
- Type: `repository`
- Primary because: Direct file listing of the canonical upstream Hugging Face repository for FLUX.1-dev including model files and model_index.json.
- Scope: black-forest-labs/FLUX.1-dev (repo tree)
- Supports: Presence of Diffusers-style artifacts and model files as listed in the repo tree
- Supports: Repository file listing for tokenizer/text_encoder files (if present in the tree)

### Hugging Face README for FLUX.1-dev

- URL: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md
- Publisher: Black Forest Labs (Hugging Face model repo)
- Type: `repository`
- Primary because: Upstream README content on the Hugging Face model landing describing model usage and characteristics.
- Scope: black-forest-labs/FLUX.1-dev (README.md)
- Supports: Model description stating 12B parameter rectified flow transformer identity
- Supports: Usage examples and suggested Diffusers-based runtime usage

### Hugging Face LICENSE.md for FLUX.1-dev

- URL: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
- Publisher: Black Forest Labs (Hugging Face model repo)
- Type: `repository`
- Primary because: Upstream license text hosted on the Hugging Face model repository reiterating the FLUX.1 [dev] Non‑Commercial license.
- Scope: black-forest-labs/FLUX.1-dev (LICENSE.md)
- Supports: Statement that the FLUX.1 [dev] Model is licensed under the FLUX.1 [dev] Non‑Commercial License
- Supports: Additional license disclaimers and risk-mitigation guidance

### NVIDIA NIM Visual GenAI getting-started (FLUX.1-dev entry)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA NIM documentation page that references a packaged NIM container name for FLUX.1-dev and documents supported variants in NVIDIA packaging.
- Scope: NVIDIA NIM packaging and container names referencing FLUX.1-dev
- Supports: NVIDIA NIM container naming and supported variants for FLUX.1-dev (NIM packaging evidence; does not assert it changes upstream checkpoint contents)

### NVIDIA NIM Visual GenAI overview

- URL: https://docs.nvidia.com/nim/visual-genai/latest/overview.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NVIDIA NIM overview pages documenting NIM microservice packaging and variant descriptions for models including flux.1-dev.
- Scope: NVIDIA NIM packaging overview referencing black-forest-labs/flux.1-dev
- Supports: Statements about NVIDIA packaging of NIM microservices tied to specific models and variant support (NIM serving evidence)

## Evidence gaps

- Evidence gap: Exact tokenizer/tokenization specifics for the FLUX.1-dev checkpoint (tokenizer class, vocabulary file(s), special tokens, max token length) are not specified at the inspected upstream primary locators (checked: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md).
- Evidence gap: Exact numeric image preprocessing pipeline rules for image-conditioned inputs (resize/crop/pad/aspect-ratio policy, numeric resize targets, normalization mean/std, and channel order) are not documented at the inspected upstream locators (checked: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md).
- Evidence gap: Probabilistic/scoring outputs (likelihoods, log-probabilities, calibrated confidences) exposed by the upstream checkpoint are not documented at the inspected primary locators (checked: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/README.md).
- Evidence gap: Canonical quantized weight files for the exact FLUX.1-dev checkpoint published by the upstream author were not found at the inspected upstream locators (checked: https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://github.com/black-forest-labs/flux/blob/main/docs/image-editing.md).
- Evidence gap: Per-dataset numeric benchmark tables (dataset name, split, metric, numeric value) explicitly attributed to the exact flux1-dev.safetensors checkpoint were not found at the inspected upstream primary locators (checked: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev, https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main, https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md).
- Evidence gap: Task-level head-to-head numeric comparisons tied to the exact FLUX.1-dev checkpoint with verified protocols and dataset splits were not found at the inspected upstream primary locators (checked: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md, https://huggingface.co/black-forest-labs/FLUX.1-dev).
- Evidence gap: No inspected upstream primary source specifies a canonical automated content-filtering implementation, safety pipeline, or moderation controls for FLUX.1-dev at the checked locators (checked: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md, https://huggingface.co/black-forest-labs/FLUX.1-dev).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 9 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[10].primary must be true: $.sources[10].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses forbidden secondary URL https: $.sources[14] uses forbidden secondary URL https://developer.nvidia.com/blog/optimizing-flux-1-kontext-for-image-editing-with-low-precision-quantization Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary URL https: $.sources[15] uses forbidden secondary URL https://blogs.nvidia.com/blog/rtx-ai-garage-flux-kontext-nim-siggraph Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses forbidden secondary URL https: $.sources[16] uses forbidden secondary URL https://blogs.nvidia.com/blog/rtx-ai-garage-flux-kontext-nim-tensorrt Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://build.nvidia.com/black-forest-labs/flux_1-kontext-dev/modelcard Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.inputPreparation_evidenceGap: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
