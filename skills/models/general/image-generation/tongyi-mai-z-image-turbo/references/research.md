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

- Research key: `huggingface-co-docs-diffusers-v0-38-0-en-api-pipelines-z-image-5995c81381`
- Independent audit: `revised`
- Researched: `2026-08-06T11:32:09.435050+00:00`

Checkpoint-scoped dossier for Tongyi-MAI/Z-Image-Turbo assembled from canonical upstream artifacts in the research findings. Primary upstream evidence (Hugging Face model repository files and commit records, the model README, the model_index.json, the text-encoder config, and the canonical arXiv preprint) identifies Z-Image-Turbo as a distilled variant of Z-Image built on the S3-DiT architecture and reported at a scale of 6 billion parameters. Upstream checkpoint metadata and README/commit entries assert performance-oriented descriptive claims (8 NFEs, sub-second inference on enterprise H800, fits within 16 GB VRAM) but do not publish protocolized numeric benchmark tables (dataset/split/metric/protocol) for image-quality or reproducible latency/memory tests for this exact checkpoint. Pipeline-class and component references appear in the model_index.json and commit metadata (pipeline class = ZImagePipeline, VAE/text-encoder/scheduler component names), enabling upstream-scoped input/output and component identification; however, several runtime and preprocessing specifics (detailed input tensor shapes, VAE config numeric fields, and pipeline source-line validation logic) are either absent or only present in repository test/issue fragments in the collected findings and are therefore narrowed or recorded as evidence gaps where Turbo-specific checkpoint support is not explicit.

## Identity

- Upstream name: Tongyi-MAI/Z-Image-Turbo
- Checkpoint/version: Tongyi-MAI/Z-Image-Turbo
- Immutable revision: 8baca7fb567bd13703049f88c470abeb00b8fba0
- Parameter scale: 6 billion parameters
- Architecture/head: Scalable Single-Stream Diffusion Transformer (S3-DiT)
- License: Apache-2.0
- Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/8baca7fb567bd13703049f88c470abeb00b8fba0, https://arxiv.org/abs/2511.22699, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md

## Selection

### Recommended

- **Text-to-image generation (photorealistic outputs)** — Model README and commit metadata describe Z-Image-Turbo as a distilled variant optimized for photorealistic generation and list the pipeline tag as text-to-image; the arXiv paper describes Z-Image as an image-generation foundation model built on S3-DiT.
  Scope: Tongyi-MAI/Z-Image-Turbo (upstream model repository and paper scope)
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/8baca7fb567bd13703049f88c470abeb00b8fba0, https://arxiv.org/abs/2511.22699
- **Image-to-image editing / img2img workflows (where supported by pipeline instantiation)** — Model README and model_index.json enumerate multiple Z-Image pipeline classes and the model repository describes generation and editing task scope; the model_index.json declares a pipeline of class "ZImagePipeline" and the model README describes generation and editing capabilities for the family.
  Scope: Tongyi-MAI/Z-Image-Turbo (pipeline and model-index scope)
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json
- **Inpainting / mask-guided editing (pipeline variants within the Z-Image family)** — The README and model-index describe inpainting/editing variants in the Z-Image family and the model repository exposes pipeline classes tied to editing tasks.
  Scope: Tongyi-MAI/Z-Image-Turbo (Z-Image pipeline family as declared in the repository)
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json

### Conditional

- **Low-latency generation (sub-second inference)** — Descriptive upstream claims tie sub-second latency to the distilled Turbo variant and enterprise-grade H800 hardware; any low-latency production use must be validated on the target hardware/runtime configuration because the upstream artifacts provide descriptive claims but no reproducible latency protocol.
  Scope: Tongyi-MAI/Z-Image-Turbo (Turbo distilled variant as referenced in README/commit entries)
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6
- **Bilingual text rendering (English & Chinese)** — Repository README and commit notes claim strong bilingual text rendering for the model family; users must validate on representative prompts and the target runtime because no standardized numeric evaluation protocol or dataset-driven bilingual text-rendering table for the Turbo checkpoint is present in the inspected sources.
  Scope: Tongyi-MAI/Z-Image-Turbo
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6

### Avoid

- **Clinical or medical diagnostic use** — No primary-source clinical validation, regulatory claims, or PHI-handling guidance for this checkpoint are present in the inspected upstream artifacts; the model repository and paper do not provide documented clinical validation materials for Turbo.
  Scope: Tongyi-MAI/Z-Image-Turbo
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699
- **Safety-/compliance-critical use requiring built-in NSFW flags or calibrated safety/confidence outputs** — The examined primary upstream artifacts do not document emitted NSFW scores, calibrated confidence outputs, or built-in safety flags for the checkpoint; no upstream evidence shows the checkpoint provides such signals.
  Scope: Tongyi-MAI/Z-Image-Turbo
  Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md

## Input preparation

### Semantic inputs

- Text prompt(s) are the primary conditioning input for generation pipelines in the Z-Image family. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json
- The model-index and README indicate support for editing pipelines (img2img/inpaint variants) which accept image inputs when those pipeline variants are used. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json

### Accepted formats

- The model repository declares the pipeline tag as text-to-image and exposes pipeline classes for generation and editing; concrete accepted input Python types (PIL, NumPy, torch.Tensor) are not enumerated in the inspected upstream files. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json

### Preprocessing

- The text encoder configuration records torch_dtype = bfloat16 for the tokenizer/text-encoder components in the checkpoint metadata (implying upstream use of bfloat16 for text-encoding components); explicit image_preprocessor code paths and step-by-step preprocessing instructions for image inputs are not present in the inspected upstream artifacts. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/text_encoder/config.json, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo

### Pre-submit validation

- Evidence gap: The inspected upstream artifacts do not include a canonical, Turbo-specific list of input-validation rules (e.g., explicit strength bounds, exact divisible-by-VAE-scale checks exposed in pipeline source lines). Upstream test fragments reference sample sizes and latent shapes in tests but do not provide a single authoritative Turbo-specific validation contract. Sources: https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/8baca7fb567bd13703049f88c470abeb00b8fba0

### Task-specific formatting

- Evidence gap: The inspected upstream artifacts do not provide a single Turbo-specific prompt template or canonical negative-prompt handling guide in the checkpoint files; the model README and model-index indicate standard generation and editing pipeline roles but do not enumerate a Turbo-specific prompt-formatting contract. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json

## Output interpretation

### Outputs

- Upstream test fragments and model-index entries demonstrate that pipeline variants can return latent tensors when output_type='latent' in tests; decoded-image outputs are the documented generation output in the model family but a Turbo-specific decode-shape table is not present. Sources: https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo

### Interpretation

- Guidance-related behavior is discussed at the family level in README and paper; the Turbo distilled mode is reported in some repository notes as not using classifier-free guidance for its distilled 8-step setting. Upstream artifacts do not provide calibrated probability/confidence outputs for image safety or quality. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://arxiv.org/abs/2511.22699

### Post-inference validation

- Recommended: when using output_type='latent', confirm expected latent tensor shapes before downstream decoding; upstream test fragments reference latent usage but a canonical Turbo-specific latent-shape contract is not present in the inspected artifacts. Sources: https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
- Downstream quality and safety validation are required for safety-critical deployment because upstream artifacts do not document internal NSFW detectors or calibrated safety signals for the checkpoint. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699

## Public benchmarks

### Low-NFE high-speed inference claim

- Dataset/split: not reported / not reported
- Metric/value: Number of Function Evaluations (NFEs) and wall-clock latency claim / 8 NFEs; descriptive claim of sub-second inference on enterprise H800 (`higher-is-better`)
- Model scope: Tongyi-MAI/Z-Image-Turbo (Turbo distilled variant)
- Conditions: Descriptive claim in README/commit entries ties sub-second latency to the distilled Turbo variant and enterprise-grade H800 hardware; no reproducible timing protocol (batch size, resolution, dtype, seed, HW config, measurement methodology) is provided in the inspected upstream artifacts.
- Source: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md
- Locator: README/commit content (model repository)
- Caveat: No numeric reproducible benchmark table or measurement protocol present in the inspected upstream artifacts to support an apples-to-apples latency claim.

### Memory / deployment claim

- Dataset/split: not reported / not reported
- Metric/value: VRAM footprint claim / Descriptive claim that Turbo fits comfortably within 16 GB VRAM (`higher-is-better`)
- Model scope: Tongyi-MAI/Z-Image-Turbo
- Conditions: Upstream README/commit entries describe 16 GB-class consumer compatibility but do not publish a reproducible memory-profiling table or protocol in the inspected artifacts.
- Source: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6
- Locator: Commit/README statements in model repository
- Caveat: No exact protocol (batch size, resolution, dtype, runtime flags) or memory logs found in the inspected upstream artifacts.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Text-to-image generation (throughput/steps/VRAM comparative statements)
- Criteria: No protocol-matched primary-source numeric image-quality or latency benchmarks for both sides are present in the inspected upstream artifacts; external comparative blog material is excluded as non-primary.
- Rationale: Upstream Z-Image artifacts provide descriptive performance claims but lack protocolized numeric tables for head-to-head comparisons with the listed Forge peers.
- Comparison conditions: Absence of protocol-matched numeric benchmarks for the alternatives in the inspected upstream artifacts prevents quantitative comparisons.
- Evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699

## Limitations and safety

### Limitations

- No primary-source numeric image-quality benchmarks (FID, IS, CLIPScore, human evaluation tables with dataset and split) for Tongyi-MAI/Z-Image-Turbo are present in the inspected upstream artifacts. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699
- Latency and VRAM claims for Turbo are descriptive but lack a reproducible measurement protocol in the inspected upstream artifacts. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6
- The checkpoint metadata records diffusers/scheduler/pipeline component versions in model_index.json and commit metadata, indicating runtime-version coupling that can affect reproducible behavior. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/8baca7fb567bd13703049f88c470abeb00b8fba0
- Evidence gap: Turbo-specific pipeline source lines enumerating exact default hyperparameter literals, VAE numeric config fields, and explicit pipeline validation code are not present as a single authoritative Turbo-specific source in the inspected artifacts; where only test fragments or metadata exist, authoritative Turbo-specific implementation detail is absent. Sources: https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo

### Safety

- Evidence gap: The inspected upstream artifacts do not document built-in PHI-handling guidance, clinical validation materials, or regulatory applicability for the Turbo checkpoint; no upstream clinical guidance was found in the model repository or paper. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699
- Evidence gap: The inspected upstream artifacts do not document emitted NSFW scores, internal safety flags, or calibrated probability/confidence outputs for generated images; therefore, safety-/compliance-critical deployments require external safety tooling and human review. Sources: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md
- The Z-Image paper documents substantial training compute at the family level (training GPU-hours and cost figures are described in the paper), which implies reproducibility and environmental/resource considerations for re-training or large-scale experiments. Sources: https://arxiv.org/abs/2511.22699

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model repository: Tongyi-MAI/Z-Image-Turbo

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
- Publisher: Hugging Face (model repository)
- Type: `model-card`
- Primary because: Official Hugging Face model repository landing page for the Z-Image-Turbo checkpoint; provides model README, files index, and basic metadata.
- Scope: Hugging Face model repository: Tongyi-MAI/Z-Image-Turbo (model landing page)
- Supports: model identity and high-level capability statements
- Supports: pipeline tags and usage scope

### Z-Image-Turbo README (blame/main)

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Repository README content as committed in the model repo; includes distilled Turbo claims (8 NFEs, latency/VRAM descriptive claims) and capability statements.
- Scope: Z-Image-Turbo README (blame view)
- Supports: Turbo 8 NFE and sub-second/H800 descriptive claims
- Supports: photorealistic generation and bilingual text-rendering claims
- Supports: pipeline tag declarations

### Z-Image-Turbo README

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md
- Publisher: Hugging Face (model repository)
- Type: `repository`
- Primary because: Primary README in the checkpoint repository describing model family and usage scope.
- Scope: Z-Image-Turbo README (primary README file)
- Supports: family-level capability descriptions and pipeline roles

### Z-Image-Turbo checkpoint commit (Hugging Face commit record)

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/8baca7fb567bd13703049f88c470abeb00b8fba0
- Publisher: Hugging Face (model repository commit)
- Type: `repository`
- Primary because: Checkpoint commit providing upload metadata, component references, and recorded config constants including pipeline and scheduler references.
- Scope: Z-Image-Turbo checkpoint commit record (upload commit and metadata)
- Supports: checkpoint upload record and SHA256 oids
- Supports: pipeline and component entries (text encoder, tokenizer, VAE, scheduler) and recorded diffusers version metadata
- Supports: vocab_size and other checkpoint metadata

### Z-Image-Turbo repository commit f332072aa78be7aecdf3ee76d5c247082da564a6

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6
- Publisher: Hugging Face (model repository commit)
- Type: `repository`
- Primary because: Additional repository commit cited in the findings that includes Turbo descriptive claims and model-zoo table entries.
- Scope: Additional model commit referenced in repository notes
- Supports: Turbo 8 NFE and latency/VRAM descriptive claims as recorded in repo commit history

### Z-Image-Turbo model_index.json (repo file)

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json
- Publisher: Hugging Face (model repository files)
- Type: `repository`
- Primary because: model_index.json in the checkpoint repository listing pipeline class and component names and diffusers version metadata.
- Scope: Model index manifest for Z-Image-Turbo
- Supports: pipeline class = ZImagePipeline
- Supports: component declarations (scheduler, text_encoder, tokenizer, transformer, VAE)
- Supports: diffusers version metadata recorded in the model index

### Z-Image-Turbo text encoder config (repo file)

- URL: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/text_encoder/config.json
- Publisher: Hugging Face (model repository files)
- Type: `repository`
- Primary because: Text encoder config included in the checkpoint repository; records architecture, hidden sizes, and torch_dtype metadata for the text-encoder component.
- Scope: Text encoder configuration file for the checkpoint
- Supports: text encoder architecture and torch_dtype = bfloat16 entry
- Supports: vocabulary and model-architecture metadata

### Z-Image paper (arXiv preprint)

- URL: https://arxiv.org/abs/2511.22699
- Publisher: arXiv (paper)
- Type: `paper`
- Primary because: Canonical research preprint describing the Z-Image architecture (S3-DiT), family-scale, and design goals.
- Scope: Z-Image paper (canonical arXiv preprint)
- Supports: S3-DiT architecture description
- Supports: 6B parameter scale claim for Z-Image family
- Supports: family-level efficiency and latency/VRAM design goals

### Diffusers issue: Z-Image test fragments and notes

- URL: https://github.com/huggingface/diffusers/issues/13583
- Publisher: Hugging Face (Diffusers repository issue)
- Type: `repository`
- Primary because: A first-party Diffusers repository issue contains test fragments and configuration snippets used by the project that reference Z-Image test settings and VAE test config; included as upstream repository evidence in the findings.
- Scope: Diffusers repository issue referencing Z-Image test fragments and VAE/test settings
- Supports: test fragment values for ZImageInpaintPipeline tests (sample_size, latent_channels, guidance_scale, output_type in test context)
- Supports: mention of Z-Image pipeline exports and test coverage notes

### Exact official starting source declared by Forge

- URL: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: tongyi-mai-z-image
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- No primary-source numeric image-quality benchmarks (FID, IS, CLIPScore, or human-eval tables with dataset and split) for Tongyi-MAI/Z-Image-Turbo were found in the inspected upstream artifacts: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md, https://arxiv.org/abs/2511.22699.
- No primary-source, protocol-matched latency or memory benchmarking tables with reproducible measurement protocols (prompt set, seed, batch size, resolution, dtype, HW configuration, exact timing methodology) were present in the inspected upstream artifacts: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/commit/f332072aa78be7aecdf3ee76d5c247082da564a6.
- Evidence gap: Turbo-specific pipeline source-line validation details (exact VAE scale numeric fields, explicit height/width divisibility enforcement code lines, default hyperparameter literal assignments in pipeline source) are not present as a single authoritative Turbo-specific source in the inspected artifacts; only test fragments and metadata exist: https://github.com/huggingface/diffusers/issues/13583, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/9f43c7d3fb4b7ef81cdf8e339bd3aa6c1101f457/model_index.json.
- Evidence gap: No primary-source documentation of emitted NSFW detectors, safety flags, or calibrated confidence/probability outputs for the Turbo checkpoint was found in the inspected upstream artifacts; users must add external safety tooling for safety-critical applications: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blame/main/README.md.
- No primary-source numeric benchmark comparisons directly comparing Tongyi-MAI/Z-Image-Turbo to listed Forge peers (protocol-matched FID/CLIPScore or latency tables) were found in the inspected upstream artifacts; comparative claims in the original draft came from external third-party material excluded from primary evidence: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo, https://arxiv.org/abs/2511.22699.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 28 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11] uses forbidden secondary host docs.vllm.ai: $.sources[11] uses forbidden secondary host docs.vllm.ai Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses unapproved repository owner 'vantagewithai' for this exact model scope: $.sources[12] uses unapproved repository owner 'vantagewithai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14] uses unapproved repository owner 'vllm-project' for this exact model scope: $.sources[14] uses unapproved repository owner 'vllm-project' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary host emergentmind.com: $.sources[15] uses forbidden secondary host emergentmind.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15] uses forbidden secondary URL https: $.sources[15] uses forbidden secondary URL https://emergentmind.com/papers/2511.22699 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16] uses forbidden secondary URL https: $.sources[16] uses forbidden secondary URL https://zimageturbo.com/blog/z-image-turbo-vs-flux-comparison Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[16].primary must be true: $.sources[16].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17] uses forbidden secondary host emergentmind.com: $.sources[17] uses forbidden secondary host emergentmind.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18] uses forbidden secondary URL https: $.sources[18] uses forbidden secondary URL https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions/2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19] uses forbidden secondary URL https: $.sources[19] uses forbidden secondary URL https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions/157 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[19].primary must be true: $.sources[19].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20] uses unapproved repository owner 'jayn7' for this exact model scope: $.sources[20] uses unapproved repository owner 'jayn7' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[20].primary must be true: $.sources[20].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21] uses forbidden secondary URL https: $.sources[21] uses forbidden secondary URL https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/discussions/37 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[21].primary must be true: $.sources[21].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[23].primary must be true: $.sources[23].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[24].primary must be true: $.sources[24].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25] uses unapproved repository owner 'maple-research-lab' for this exact model scope: $.sources[25] uses unapproved repository owner 'maple-research-lab' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[25].primary must be true: $.sources[25].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26] uses forbidden secondary host medium.com: $.sources[26] uses forbidden secondary host medium.com Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[26].primary must be true: $.sources[26].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/z_image: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
