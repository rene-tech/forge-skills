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

- Research key: `huggingface-co-docs-diffusers-v0-38-0-en-api-pipelines-pixart-sigma-8e62fb7943`
- Independent audit: `revised`
- Researched: `2026-08-06T11:29:01.655955+00:00`

Checkpoint-scoped summary based only on the provided primary findings: The Hugging Face model page for PixArt-alpha/PixArt-Sigma-XL-2-1024-MS describes PixArt-Σ as a diffusion-transformer text-to-image generative model composed of pure transformer blocks for latent diffusion and states the model can directly generate 1024px, 2K and 4K images from text prompts. The model card/README records required Python packages (transformers, safetensors, sentencepiece, accelerate) and recommends upgrading diffusers to >= 0.28.0. A transformer configuration file and a scheduler configuration file are present in the checkpoint repository. The scheduler_config.json for this checkpoint declares DPMSolverMultistepScheduler, algorithm type "dpmsolver++", prediction type "epsilon", training timesteps = 1000, beta_start = 0.0001, beta_end = 0.02, beta_schedule = "linear", solver_order = 2, solver_type = "midpoint", use_karras_sigmas = false, trained_betas = null, dynamic_thresholding_ratio = 0.995, sample_max_value = 1.0, steps_offset = 0, euler_at_final = false, lower_order_final = true, thresholding = false, timestep_spacing = "linspace", and Diffusers version noted in the scheduler config as "0.22.0.dev0". The transformer/config.json file is present in the repository (location recorded), but the provided findings do not report transformer hyperparameter values inside that file beyond its existence. The supplied primary findings do not report any numeric benchmark scores (e.g., FID, IS, CLIP similarity, human eval) or an explicit parameter count for this exact checkpoint; they also do not provide runtime API I/O shapes, tokenization/maximum-token rules, or checkpoint-scoped safety/mitigation procedures.

## Identity

- Upstream name: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS
- Checkpoint/version: PixArt-Sigma-XL-2-1024-MS
- Immutable revision: 20658be8dd0805c6f7b25b7b2fa252cc9c15b478
- Parameter scale: not reported
- Architecture/head: Diffusion-transformer text-to-image generative model; described in the checkpoint model page as composed of pure transformer blocks for latent diffusion.
- License: openrail
- Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json

## Selection

### Recommended

- **Text-to-image generation at advertised native resolutions (1024 px, 2K, 4K) from text prompts using the PixArt-Sigma-XL-2-1024-MS checkpoint.** — The Hugging Face model page and README for PixArt-alpha/PixArt-Sigma-XL-2-1024-MS state that PixArt-Σ can directly generate 1024px, 2K and 4K images from text prompts and present the model as a diffusion-transformer text-to-image generator.
  Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS (exact checkpoint as hosted on Hugging Face).
  Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

### Conditional

- **Altering or relying on scheduler/sampling behavior (custom sigma schedules, non-default sampler settings) during sampling.** — The scheduler class and many hyperparameters are declared in scheduler_config.json for this checkpoint; however, runtime enforcement and pipeline-level handling of custom sigma schedules or sampler options must be validated in the target pipeline implementation before relying on them.
  Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS (scheduler_config.json present in the checkpoint repository).
  Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json
- **Upgrading or matching Diffusers versions when integrating the checkpoint into a runtime.** — The model README recommends diffusers >= 0.28.0; ensure runtime diffusers version compatibility before deployment, since the checkpoint repository includes a scheduler_config.json that records a diffusers version string "0.22.0.dev0" and runtime integration may require testing.
  Scope: Integration/runtime behavior for PixArt-alpha/PixArt-Sigma-XL-2-1024-MS.
  Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json

### Avoid

- **Assuming the checkpoint provides primary-source numeric benchmark results (e.g., FID, IS, CLIP-similarity, human-eval) for image-generation quality.** — No numeric benchmark scores for this exact checkpoint were reported in the checked primary locations.
  Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS (exact checkpoint).
  Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json
- **Assuming the checkpoint documents exact runtime API input/output shapes, tokenization limits, or explicit safety/mitigation controls.** — The checked primary locations declare input modality and presence of config files but do not specify exact API input types, batching limits, max prompt token length, tokenizer behavior at API boundaries, exact output tensor shapes, or checkpoint-scoped safety mitigations.
  Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS (checkpoint-scoped claims).
  Evidence: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json

## Input preparation

### Semantic inputs

- Primary semantic input is text prompts for text-to-image generation; the Hugging Face model page and README present text prompts as the input modality for this checkpoint. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

### Accepted formats

- The provided primary findings declare text prompts as the input modality but do not document exact runtime input data types (e.g., Python str vs list[str]) or accepted API payload formats for prompts. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

### Preprocessing

- A transformer configuration file and a scheduler configuration file are present in the repository; the primary findings do not specify how these checkpoint config fields map to concrete runtime preprocessing steps or final tensor shapes. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json

### Pre-submit validation

- The checked primary locations do not provide explicit input-validation rules such as maximum prompt token length, batching limits, truncation rules, or tokenization edge-case handling at API boundaries for this checkpoint. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json

### Task-specific formatting

- The checkpoint README and model page do not include official prompt templates, role conventions, paired-input ordering, or other task-specific formatting guidance in the provided primary findings. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

## Output interpretation

### Outputs

- Documented output modality is generated images at native resolutions (1024 px, 2K and 4K) produced from text prompts, as stated in the Hugging Face model page and README in the provided findings. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md
- The checkpoint files in the provided findings do not specify exact runtime output tensor shapes, data types, or serialization formats (e.g., numpy array shape/dtype or specific image file encoding) for generated images. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json

### Interpretation

- The provided checkpoint documentation does not supply per-image confidence scores, calibration metrics, or probability maps; no checkpoint-scoped guidance on interpreting per-image uncertainty is present in the checked primary locations. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

### Post-inference validation

- The checkpoint files in the provided findings do not include recommended post-inference quality checks, calibration protocols, or downstream validation procedures; users must establish their own validation workflows. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- Model weights license is declared in the checkpoint README/blame view as "openrail"; the provided findings do not reproduce the full license text or enumerate license terms within the checked files. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS
- A transformer configuration file and a scheduler configuration file are present in the repository, but the provided findings do not document exact runtime output tensor shapes or explicit mapping from checkpoint config fields to API shapes. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json
- The scheduler_config.json records a Diffusers version string "0.22.0.dev0" while the README recommends diffusers >= 0.28.0; this indicates a version/compatibility area requiring validation when integrating the checkpoint into a runtime. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json

### Safety

- Evidence gap: no checkpoint-scoped safety mitigations, privacy controls, clinical/biosecurity guidance, or dual-use operational restrictions were documented in the provided checkpoint files. Sources: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Hugging Face model card: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS

- URL: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS
- Publisher: PixArt-alpha (Hugging Face model repository)
- Type: `model-card`
- Primary because: Official upstream model card declaring checkpoint identity, claimed generation resolutions, and model metadata for this exact checkpoint as recorded in the provided findings.
- Scope: Checkpoint: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS
- Supports: Claim: direct generation at 1024 px, 2K and 4K from text prompts within a single sampling process
- Supports: Model type: diffusion-transformer text-to-image generative model (pure transformer blocks)
- Supports: Repository-level usage notes and package recommendations

### Hugging Face README (blame view) for PixArt-Sigma-XL-2-1024-MS (revision 20658be8...)

- URL: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md
- Publisher: PixArt-alpha (Hugging Face model repository)
- Type: `model-card`
- Primary because: Repository README revision containing checkpoint-scoped statements about generation resolutions, architecture, package/runtime recommendations, and license name as recorded in the provided findings.
- Scope: Checkpoint README and repository-level documentation for PixArt-alpha/PixArt-Sigma-XL-2-1024-MS
- Supports: Declaration of model license name (reported as "openrail")
- Supports: Repository-level usage notes and package requirements
- Supports: Claim: generation at 1024px, 2K and 4K

### Transformer configuration for PixArt-Sigma-XL-2-1024-MS (transformer/config.json)

- URL: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json
- Publisher: PixArt-alpha (Hugging Face model repository)
- Type: `model-card`
- Primary because: Checkpoint-scoped transformer configuration file present in the repository (location recorded in the provided findings).
- Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS transformer configuration
- Supports: Presence of a transformer/config.json file for the checkpoint (used to inform architecture/config claims)

### Scheduler configuration file for PixArt-Sigma-XL-2-1024-MS (scheduler_config.json)

- URL: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json
- Publisher: PixArt-alpha (Hugging Face model repository)
- Type: `model-card`
- Primary because: Checkpoint-scoped scheduler configuration file present in the repository and authoritative for declared scheduler class and hyperparameters as recorded in the provided findings.
- Scope: PixArt-alpha/PixArt-Sigma-XL-2-1024-MS scheduler configuration
- Supports: Scheduler declared as DPMSolverMultistepScheduler
- Supports: Scheduler hyperparameter fields recorded in the provided findings (e.g., algorithm type "dpmsolver++", training timesteps = 1000, beta_start = 0.0001, beta_end = 0.02, beta_schedule = "linear", prediction_type = "epsilon", solver_order = 2, solver_type = "midpoint", and other listed fields)

### Exact official starting source declared by Forge

- URL: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: pixart-alpha-pixart-sigma
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- No primary-source numeric benchmark results (e.g., FID, IS, CLIP-similarity, human-eval) for the exact checkpoint PixArt-alpha/PixArt-Sigma-XL-2-1024-MS were found in the checked primary locations: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json.
- No primary-source checkpoint-scoped parameter count for PixArt-alpha/PixArt-Sigma-XL-2-1024-MS was reported in the checked primary locations: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json.
- No primary-source specification of exact runtime input types (e.g., Python str vs list[str] for prompts), batching limits, maximum prompt token length, tokenization behavior at API boundaries, or exact output tensor shapes/data types was found in the checked primary locations: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json.
- No primary-source, checkpoint-scoped safety mitigations, privacy controls, clinical/biosecurity guidance, or dual-use operational restrictions were documented in the checked primary locations: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md.
- VAE provenance: the provided findings do not include a VAE configuration file hosted inside the PixArt-alpha/PixArt-Sigma-XL-2-1024-MS repository in the checked primary locations; no authoritative VAE file within the checkpoint repository was reported in the provided findings, creating an evidence gap for authoritative VAE provenance for this checkpoint. Files checked: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json.
- Before leaving benchmarks empty: checked the following primary locations per the brief and found no numeric benchmarks for this exact checkpoint: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json.
- Before leaving comparisons empty: checked the following primary locations and found no checkpoint-scoped peer-comparison tables or numeric comparisons between PixArt-alpha/PixArt-Sigma-XL-2-1024-MS and alternative models: https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blame/20658be8dd0805c6f7b25b7b2fa252cc9c15b478/README.md, https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/transformer/config.json, and https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS/blob/main/scheduler/scheduler_config.json.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 1 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/pixart_sigma: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
