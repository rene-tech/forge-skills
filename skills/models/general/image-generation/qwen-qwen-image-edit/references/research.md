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

- Research key: `docs-nvidia-com-nim-visual-genai-latest-getting-started-html-qwen-qwen-image-edit-8b48716485`
- Independent audit: `revised`
- Researched: `2026-07-23T23:16:00.850064+00:00`

Qwen-Image-Edit is an image-editing checkpoint family packaged and served by NVIDIA as a Visual GenAI NIM. NVIDIA Build and the NGC catalog state the family is built upon a ~20B-parameter Qwen-Image model and that the NIM exposes OpenAI-compatible image-generation and image-editing endpoints. NVIDIA Build publishes a fine-tuned nvpcb variant (qwen-image-edit-nvpcb-ovsl2sl) and documents released diffusers-style artifact directories and fine-tune metadata for that artifact. The canonical Qwen-Image technical report (arXiv:2508.02324) contains family-level evaluations including an ImgEdit table (Table 12). However, no auditable, checkpoint-scoped numeric benchmark rows explicitly tied to the exact NIM-served container tags (qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511, qwen-image-edit-nvpcb-ovsl2sl) were found in the reviewed primary sources.

## Identity

- Upstream name: Qwen-Image-Edit
- Checkpoint/version: qwen-image-edit (container tags referenced: qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511, qwen-image-edit-nvpcb-ovsl2sl)
- Immutable revision: not reported
- Parameter scale: ≈20B
- Architecture/head: Diffusers-style image-editing pipeline built atop Qwen-Image: pipeline includes Qwen2.5-VL visual-language encoder and a VAE encoder/decoder; released diffusers-style artifact directories (transformer/, text_encoder/, vae/, tokenizer/, processor/, scheduler/, model_index.json) are documented for the nvpcb artifact.
- License: Upstream repository artifacts: Apache License 2.0 (Qwen-Image GitHub LICENSE). NIM/container distribution governed by NVIDIA container/NGC catalog licensing terms (NVIDIA Software License Agreement / product-specific NGC terms) as stated on the NGC catalog and NVIDIA Build pages.
- Evidence: https://build.nvidia.com/qwen/qwen-image-edit, https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit, https://github.com/QwenLM/Qwen-Image, https://arxiv.org/abs/2508.02324

## Selection

### Recommended

- **Prompt-driven image editing (semantic edits and appearance/style adjustments) via the NIM OpenAI-compatible image-editing endpoint** — NVIDIA NIM API and NVIDIA Build model page describe Qwen-Image-Edit as an image editing model where a natural-language 'prompt' instructs the edit and input image(s) are processed by the pipeline (Qwen2.5-VL for semantic control and a VAE encoder for appearance control).
  Scope: qwen-image-edit (container tags selectable via NIM_MODEL_VERSION: qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511)
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html, https://build.nvidia.com/qwen/qwen-image-edit, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit
- **Use tag-specific variants for workflows where per-tag release notes indicate variant behavior; validate empirically on target data before production use** — NVIDIA Build and NGC list supported variant tags selectable via NIM_MODEL_VERSION and the nvpcb artifact documents a targeted fine-tuning for PCB-style transfer; tag-specific variants can be selected and validated.
  Scope: qwen-image-edit-2509, qwen-image-edit-2511, qwen-image-edit-nvpcb-ovsl2sl (selectable via NIM_MODEL_VERSION)
  Evidence: https://build.nvidia.com/qwen/qwen-image-edit, https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit

### Conditional

- **Industrial PCB-style domain transfer using the nvpcb fine-tuned variant** — Require validation on representative PCB images because the nvpcb artifact documents a small, targeted fine-tuning run (1500 steps) that updated ≈170M parameters; evaluate downstream detection/performance empirically before production use.
  Scope: qwen-image-edit-nvpcb-ovsl2sl (nvpcb fine-tuned variant)
  Evidence: https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl, https://build.nvidia.com/qwen/qwen-image-edit
- **Prefer a named tag (e.g., qwen-image-edit-2511 or qwen-image-edit-2509) for workflows where release notes indicate tag-specific behavior** — Validate on representative target distribution because tag-specific release notes or variant descriptions do not provide auditable, checkpoint-scoped numeric benchmarks for the NIM-served tag.
  Scope: qwen-image-edit-2509, qwen-image-edit-2511
  Evidence: https://build.nvidia.com/qwen/qwen-image-edit, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit

### Avoid

- **Assuming auditable, checkpoint-scoped numeric benchmark performance for NIM tags without additional provenance** — No primary-source, checkpoint-scoped numeric benchmark rows (dataset, split, metric, numeric value) explicitly tied to the exact Qwen-Image-Edit NIM tags were found in the reviewed primary sources; family-level results in the technical report do not substitute for checkpoint-scoped evidence.
  Scope: Qwen-Image-Edit (all container tags referenced)
  Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://build.nvidia.com/qwen/qwen-image-edit, https://arxiv.org/abs/2508.02324, https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl
- **Relying on NIM offloading policies (disk/system_ram/none) for Qwen-Image-Edit** — NVIDIA documentation explicitly states that offloading policies are not supported by Qwen-Image and Qwen-Image-Edit NIMs.
  Scope: Qwen-Image-Edit NIM
  Evidence: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/configuration.html

## Input preparation

### Semantic inputs

- Natural-language edit instruction is provided via the API 'prompt' parameter describing the desired edit. Sources: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html, https://docs.nvidia.com/nim/visual-genai/1.4.0/api/index.html
- Input image(s) are supplied via the API 'image' parameter and processed by the pipeline (Qwen2.5-VL for semantic control and a VAE encoder for appearance control). Sources: https://build.nvidia.com/qwen/qwen-image-edit, https://github.com/QwenLM/Qwen-Image, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit

### Accepted formats

- NIM exposes OpenAI-compatible image-editing endpoints and lists 'image' as the input/output modality for image-editing endpoints. Sources: https://docs.nvidia.com/nim/visual-genai/1.4.0/api/index.html, https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html

### Preprocessing

- Text is tokenized/processed by the Qwen tokenizer/processor and encoded by Qwen2.5-VL; released diffusers-style artifacts and the Qwen-Image repository include tokenizer/processor and text_encoder artifacts for the family. Sources: https://github.com/QwenLM/Qwen-Image, https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl
- Input images are passed through a VAE encoder as part of the pipeline for appearance control; the nvpcb artifact documents presence of a vae/ directory in released artifacts. Sources: https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl, https://build.nvidia.com/qwen/qwen-image-edit

### Pre-submit validation

- Operational prerequisite: pulling the NIM container requires an NGC API key and Docker/registry authentication as documented on NVIDIA Build deployment pages. Sources: https://build.nvidia.com/qwen/qwen-image-edit/deploy, https://build.nvidia.com/qwen/qwen-image-edit
- Set NIM_MODEL_VERSION to select the desired served tag (example values include qwen-image-edit-2509; if omitted the container may load a default version). Validate the selected tag in test workloads before production. Sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html, https://build.nvidia.com/qwen/qwen-image-edit/deploy
- Evidence gap: precise tokenization limits (max tokens) and explicit text truncation rules for prompts passed to Qwen2.5-VL within Qwen-Image-Edit were not specified in the reviewed primary sources (checked Qwen GitHub and NIM API pages). Sources: https://github.com/QwenLM/Qwen-Image, https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html

### Task-specific formatting

- API expects an OpenAI-compatible image-editing request shape: include 'prompt' describing the edit and 'image' containing the input image(s); select model-specific tags via NIM_MODEL_VERSION when deploying the NIM container. Sources: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

## Output interpretation

### Outputs

- Edited image(s) are the primary output from the OpenAI-compatible image-editing endpoint. Sources: https://docs.nvidia.com/nim/visual-genai/1.4.0/api/index.html, https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html

### Interpretation

- Evidence gap: No documentation in the reviewed sources states that the API returns numeric confidence scores, logits, or calibrated likelihoods for Qwen-Image-Edit responses. Sources: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html, https://build.nvidia.com/qwen/qwen-image-edit

### Post-inference validation

- Post-inference validation should include image decode verification, expected output counts, and empirical visual-fidelity checks because no automated calibration or numeric confidence outputs are documented for Qwen-Image-Edit. Sources: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html, https://build.nvidia.com/qwen/qwen-image-edit

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### black-forest-labs-flux-1-dev — `insufficient-evidence`

- Task: Image editing (prompt-driven image-to-image editing)
- Criteria: No primary-source, checkpoint-scoped numeric comparisons located for Qwen-Image-Edit NIM tags versus the listed alternative on equivalent datasets/protocols.
- Rationale: Reviewed primary sources (NVIDIA NIM docs, NVIDIA Build model pages, NGC catalog entry, and the Qwen-Image technical report) do not contain checkpoint-matched comparative evaluations or numeric benchmarks tying Qwen-Image-Edit NIM tags to peer checkpoints.
- Comparison conditions: Checked NVIDIA NIM docs and Build pages for tag-scoped benchmarks and the upstream technical report (arXiv Table 12) for family-level metrics; none provide auditable, tag-linked head-to-head rows.
- Evidence: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html, https://build.nvidia.com/qwen/qwen-image-edit, https://arxiv.org/abs/2508.02324

## Limitations and safety

### Limitations

- NVIDIA documents that offloading policies (disk, system_ram, none) are not supported by Qwen-Image and Qwen-Image-Edit NIMs; do not assume offloading is available for these NIMs. Sources: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html, https://docs.nvidia.com/nim/visual-genai/latest/configuration.html
- Repository/code license is Apache-2.0 for upstream Qwen-Image repository artifacts while the NIM container and distribution are governed by NVIDIA container/NGC licensing terms; consult both code and container licenses before reuse. Sources: https://github.com/QwenLM/Qwen-Image, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit
- Evidence gap: No auditable, checkpoint-scoped numeric benchmark results (dataset, split, metric, numeric value, and exact checkpoint/tag) were found for the NIM-served tags (qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511, qwen-image-edit-nvpcb-ovsl2sl) in the reviewed primary sources; family-level benchmarks exist in the upstream technical report but are not tied to the specific NIM tags. Sources: https://arxiv.org/abs/2508.02324, https://build.nvidia.com/qwen/qwen-image-edit, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit
- Evidence gap: Operational resource requirements (exact VRAM footprint, validated latency numbers, and max batch sizes) per checkpoint/tag are not specified in the reviewed primary sources; deployments should validate hardware sizing empirically. Sources: https://build.nvidia.com/qwen/qwen-image-edit, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- The nvpcb variant documents a small, targeted fine-tuning (1500 steps; ≈170M parameters updated) and is specialized for PCB-style transfer; do not generalize nvpcb performance to other domains without validation. Sources: https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl

### Safety

- NVIDIA Build model page states that users are responsible for implementing guardrails and safety mechanisms prior to deployment and to report security/AI concerns via the model page. Sources: https://build.nvidia.com/qwen/qwen-image-edit
- Deploying the NIM container requires an NGC API key and is governed by NVIDIA container licensing terms; follow NVIDIA licensing and security guidance when deploying. Sources: https://build.nvidia.com/qwen/qwen-image-edit/deploy, https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit
- Evidence gap: No checkpoint-scoped clinical or PHI-specific handling instructions or approvals for Qwen-Image-Edit were found in the reviewed primary sources; do not assume clinical safety or PHI compliance without additional documented procedures. Sources: https://build.nvidia.com/qwen/qwen-image-edit, https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### NVIDIA NIM Visual GenAI Getting Started (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NVIDIA Visual GenAI NIM documentation describing Qwen-Image-Edit container usage, NIM_MODEL_VERSION selection, defaults, and operational notes used throughout the dossier.
- Scope: Qwen-Image and Qwen-Image-Edit NIM containers and runtime selection
- Supports: NIM_MODEL_VERSION selection behavior and example version names referenced by the dossier.
- Supports: General getting-started and operational notes for Visual GenAI NIMs.

### NVIDIA NIM Visual GenAI Getting Started (v1.6.0)

- URL: https://docs.nvidia.com/nim/visual-genai/1.6.0/getting-started.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Versioned NVIDIA NIM Getting Started page cited for NIM_MODEL_VERSION usage examples and default selections referenced by the dossier.
- Scope: Qwen-Image and Qwen-Image-Edit NIM containers and version selection behavior (v1.6.0)
- Supports: Use `-e NIM_MODEL_VERSION=<version>` to select a model version for Qwen-Image-Edit.
- Supports: Example model version values including `qwen-image-edit-2509` and `qwen-image-edit-2511`.
- Supports: Statement that offloading policies are not supported by Qwen-Image-Edit NIMs.

### NVIDIA NIM API: Qwen-Image-Edit (latest)

- URL: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: API reference specific to the Qwen-Image-Edit NIM used to verify API parameter semantics and OpenAI-compatible editing contract.
- Scope: Qwen-Image-Edit API specification and parameter semantics
- Supports: API parameter semantics for prompt and image used by Qwen-Image-Edit NIM.
- Supports: Indication that the NIM exposes an OpenAI-compatible image-editing API shape.

### NVIDIA NIM API Index (OpenAI-compatible endpoints)

- URL: https://docs.nvidia.com/nim/visual-genai/1.4.0/api/index.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM API index page establishing that the NIM exposes OpenAI-compatible image generation and image editing endpoints.
- Scope: NIM OpenAI-compatible API endpoints (image generation and editing)
- Supports: The NIM provides OpenAI-compatible endpoints for generating images from text prompts and for editing images with text prompts.

### NVIDIA Build: Qwen-Image-Edit model page

- URL: https://build.nvidia.com/qwen/qwen-image-edit
- Publisher: NVIDIA Build
- Type: `official-documentation`
- Primary because: Official NVIDIA Build model overview page describing capabilities, supported variant tags, and deployment responsibilities used for multiple dossier claims.
- Scope: Qwen-Image-Edit model overview and deployment responsibilities
- Supports: Qwen-Image-Edit described as an image editing model with multilingual text editing and subject consistency.
- Supports: Qwen-Image-Edit is built upon the 20B Qwen-Image model.
- Supports: Pipeline description: input image fed into Qwen2.5-VL and a VAE encoder for appearance control.
- Supports: User responsibility guidance for guardrails and safety prior to deployment.
- Supports: Lists supported variant tags selectable via NIM_MODEL_VERSION (qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511).

### NVIDIA Build: qwen-image-edit-nvpcb-ovsl2sl artifact page

- URL: https://build.nvidia.com/nvidia/qwen-image-edit-nvpcb-ovsl2sl
- Publisher: NVIDIA Build (Qwen team)
- Type: `repository`
- Primary because: Official NVIDIA Build artifact page documenting the nvpcb fine-tuned variant, reported parameter counts, fine-tuning steps, cumulative compute, and released diffusers-style pipeline artifact contents.
- Scope: qwen-image-edit-nvpcb-ovsl2sl (nvpcb fine-tuned variant)
- Supports: nvpcb variant metadata: v1.0.0 release, trained for 1500 steps.
- Supports: Total parameters approximately 2.0 × 10^10 (≈20B).
- Supports: Approximately 1.7 × 10^8 (≈170M) diffusion-transformer parameters were updated during fine-tuning.
- Supports: Cumulative compute reported ≈0.6 GPU-hour total.
- Supports: Released artifact includes transformer/, text_encoder/, vae/, tokenizer/, processor/, scheduler/, and model_index.json directories/files.
- Supports: Output resolution and output format notes for nvpcb variant.

### NVIDIA Build: Qwen-Image-Edit deploy/self-hosted

- URL: https://build.nvidia.com/qwen/qwen-image-edit/deploy
- Publisher: NVIDIA Build
- Type: `official-documentation`
- Primary because: Official NVIDIA deployment/self-hosting documentation for the Qwen-Image-Edit NIM used to verify operational prerequisites (NGC API key requirement, Docker invocation notes).
- Scope: Deployment and self-hosted instructions for Qwen-Image-Edit NIM
- Supports: An NGC API key is required to pull NIM containers from the NVIDIA NGC registry.
- Supports: Deployment instructions for running the Qwen-Image-Edit NIM container and selecting NIM_MODEL_VERSION.

### NGC Catalog entry: qwen-image-edit

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: Official NGC catalog entry documenting container name, licensing statements, and family-level parameter scale assertions referenced by the dossier.
- Scope: NGC catalog entry for the Qwen-Image-Edit container
- Supports: Container image name and distribution details.
- Supports: Statement that Qwen-Image-Edit is built upon the 20B Qwen-Image model and extends image editing capabilities.
- Supports: Container distribution and licensing statements referencing NGC terms.

### Qwen-Image GitHub repository

- URL: https://github.com/QwenLM/Qwen-Image
- Publisher: QwenLM (GitHub)
- Type: `repository`
- Primary because: Official Qwen-Image repository documenting implementation files, tokenizer/processor, and usage instructions referenced by the dossier.
- Scope: Qwen-Image repository and implementation notes
- Supports: Repository contains diffusers-style pipelines (QwenImageEditPlusPipeline, QwenImageEditPipeline, QwenImagePipeline) and tokenizer/processor artifacts.
- Supports: Example pipeline loading and example inference parameters present in repository.
- Supports: Repository includes LICENSE file and tag-specific markdown files.

### Qwen-Image technical report (arXiv:2508.02324)

- URL: https://arxiv.org/abs/2508.02324
- Publisher: arXiv / Qwen authors
- Type: `technical-report`
- Primary because: Canonical technical report PDF describing the Qwen-Image family and family-level evaluation tables (including ImgEdit Table 12) used as upstream-family evidence.
- Scope: Qwen-Image family technical report and family-level evaluation
- Supports: Contains family-level evaluations for the Qwen-Image family, including the ImgEdit benchmark referenced in Table 12 (family-level evidence).
- Supports: Describes the multi-task training paradigm and family capabilities.

### Cited official first-party source

- URL: https://docs.nvidia.com/nim/visual-genai/latest/configuration.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: qwen-qwen-image-edit
- Supports: Exact independently audited claim citation

## Evidence gaps

- No primary-source, checkpoint-scoped numeric benchmark results (dataset name, split, metric, numeric value, and exact checkpoint/tag) were found for Qwen-Image-Edit tags (qwen-image-edit, qwen-image-edit-2509, qwen-image-edit-2511, qwen-image-edit-nvpcb-ovsl2sl) in the reviewed primary sources (checked sources: https://arxiv.org/abs/2508.02324 Table 12; https://build.nvidia.com/qwen/qwen-image-edit; https://catalog.ngc.nvidia.com/orgs/nim/teams/qwen/containers/qwen-image-edit).
- The reviewed primary sources do not document explicit output tensor shapes, raw logits/confidence/calibration scores, or a documented API exposure for such numeric confidence outputs for the exact Qwen-Image-Edit checkpoints (checked: https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html; https://build.nvidia.com/qwen/qwen-image-edit).
- Precise tokenization limits (max tokens) and explicit text truncation rules for prompts passed to Qwen2.5-VL within Qwen-Image-Edit were not specified in the reviewed primary sources (checked: https://github.com/QwenLM/Qwen-Image; https://docs.nvidia.com/nim/visual-genai/latest/api/qwen-image-edit.html).
- Exact batching behavior (max batch size, server-side batching semantics) and validated per-tag VRAM footprints and latency measurements for the exact Qwen-Image-Edit checkpoint tags are not specified in the reviewed primary sources (checked: https://build.nvidia.com/qwen/qwen-image-edit; https://docs.nvidia.com/nim/visual-genai/latest/getting-started.html).
- No primary-source, checkpoint-scoped head-to-head comparisons (quality metrics on matched datasets/protocols) between Qwen-Image-Edit NIM tags and peer checkpoints were located in the reviewed primary sources (checked: https://build.nvidia.com/qwen/qwen-image-edit; https://arxiv.org/abs/2508.02324).

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` $.benchmarks_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` $.comparisons_evidenceGaps: Provider returned a field outside the published dossier schema. Resolution: The runner removed the unsupported field before validation; no accepted dossier field was replaced.
- `low` https://docs.nvidia.com/nim/visual-genai/latest/configuration.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
