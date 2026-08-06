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

- Research key: `huggingface-co-stabilityai-stable-diffusion-xl-base-1-0-3c44be280a`
- Independent audit: `revised`
- Researched: `2026-08-06T14:00:50.406989+00:00`

Primary repository manifests and component config files for stabilityai/stable-diffusion-xl-base-1.0 were inspected. The repository model_index.json (checked at refs/pr/246 and main paths) identifies the pipeline class as StableDiffusionXLPipeline, lists UNet as ["diffusers","UNet2DConditionModel"], VAE as ["diffusers","AutoencoderKL"], two text-encoders (["transformers","CLIPTextModel"] and ["transformers","CLIPTextModelWithProjection"]), two CLIPTokenizer entries, scheduler ["diffusers","EulerDiscreteScheduler"], and sets force_zeros_for_empty_prompt = true (model_index.json). UNet numeric configuration keys were inspected in unet/config.json (sample_size = 128; attention_head_dim = [5,10,20]; block_out_channels = [320,640,1280]; transformer_layers_per_block = [1,2,10]; use_linear_projection = true). VAE decoder numeric keys were inspected in vae_decoder/config.json (class AutoencoderKL; sample_size = 1024; latent_channels = 4; scaling_factor = 0.13025; block_out_channels = [128,256,512,512]; out_channels = 3). The repository lists a safetensors weight artifact named sd_xl_base_1.0.safetensors in the model root listing. Diffusers pipeline and image-processor sources were checked for pipeline defaults and preprocessing semantics: the StableDiffusionXLPipeline source documents pipeline defaults including force_zeros_for_empty_prompt behavior and computed vae_scale_factor logic; the Diffusers VaeImageProcessor source documents defaults vae_scale_factor = 8, do_resize = True, resample = "lanczos", do_normalize = True. The repository README lists the license name as "CreativeML Open RAIL++-M License" and the repository LICENSE.md contains patent and copyright license-grant language. The inspected primary sources do not publish a checkpoint-scoped authoritative numeric total parameter count, nor do they publish checkpoint-scoped numeric benchmarks or an explicit canonical table mapping internal tensor names to decoded-image pixel-value ranges; these are reported as evidence gaps below. All factual claims in this dossier cite the exact primary files and paths inspected.

## Identity

- Upstream name: stabilityai/stable-diffusion-xl-base-1.0
- Checkpoint/version: stabilityai/stable-diffusion-xl-base-1.0
- Immutable revision: Commits recorded in the repository commits view: 91704ab, 3941f47, bf71498, d95724c, 4621659, 76d28af, f898a3e, 47cd530, cd44add (as listed on the repository commits page)
- Parameter scale: not reported
- Architecture/head: StableDiffusionXLPipeline (pipeline) wiring: UNet component class UNet2DConditionModel (unet/config.json), VAE decoder class AutoencoderKL (vae_decoder/config.json), two text encoders CLIPTextModel and CLIPTextModelWithProjection and two CLIPTokenizer entries (model_index.json); scheduler listed as EulerDiscreteScheduler (model_index.json); pipeline-level flag force_zeros_for_empty_prompt = true (model_index.json).
- License: CreativeML Open RAIL++-M License (as listed in the repository README) with complementary license-grant language present in LICENSE.md (see LICENSE.md for full text of grants).
- Evidence: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/refs%2Fpr%2F246/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/commits/refs%2Fpr%2F252, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py, https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py, https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl

## Selection

### Recommended

- **High-resolution text-to-image generation using the StableDiffusionXLPipeline with this checkpoint's artifacts** — model_index.json enumerates StableDiffusionXLPipeline as the pipeline class and lists UNet ("diffusers","UNet2DConditionModel") and VAE ("diffusers","AutoencoderKL") components; unet/config.json specifies UNet sample_size = 128 and vae_decoder/config.json specifies VAE sample_size = 1024 and scaling_factor = 0.13025. Diffusers image_processor.py documents VaeImageProcessor defaults including vae_scale_factor = 8 and do_resize = True; the combination of UNet sample_size (unet/config.json) and VAE/image-processor vae_scale_factor (image_processor.py) are the upstream-declared numeric constants relevant to default sample-size/resolution behavior.
  Scope: stabilityai/stable-diffusion-xl-base-1.0
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/refs%2Fpr%2F246/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py, https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl

### Conditional

- **Deployment in public products or services where compliance with repository license terms and any repository-stated requirements is required** — Implementers must inspect and comply with the checkpoint repository LICENSE.md and README-declared license name; legal obligations and allowed/restricted uses must be determined by reviewing the LICENSE.md text and any accompanying repository statements.
  Scope: stabilityai/stable-diffusion-xl-base-1.0
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md

### Avoid

- **Avoid assuming there are no license obligations or usage terms when deploying this checkpoint** — The repository README lists the license name "CreativeML Open RAIL++-M License" and the repository LICENSE.md contains license-grant language (perpetual, worldwide, non-exclusive, royalty-free patent and copyright licenses); implementers must consult LICENSE.md for obligations rather than assuming no restrictions.
  Scope: stabilityai/stable-diffusion-xl-base-1.0
  Evidence: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md

## Input preparation

### Semantic inputs

- Primary runtime input consumed by the pipeline is a natural-language textual prompt; model_index.json lists two text-encoder components (keys: ["transformers","CLIPTextModel"] and ["transformers","CLIPTextModelWithProjection"]) and tokenizers (["transformers","CLIPTokenizer"]). Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json

### Accepted formats

- A safetensors weight artifact named sd_xl_base_1.0.safetensors is present in the model repository listing (artifact listing path in the model root). Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors
- Evidence gap: The inspected repository files do not publish a single canonical upstream enumeration of all officially supported weight packaging formats for this checkpoint; files checked: model_index.json and the repository artifact listing sd_xl_base_1.0.safetensors. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors

### Preprocessing

- Pipeline component wiring and load-time component identifiers are declared in model_index.json (pipeline class name and component list entries) and the StableDiffusionXLPipeline source documents how pipeline components (vae, unet, text_encoders, tokenizers, scheduler) are registered and used. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/refs%2Fpr%2F246/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py
- VAE decoder numeric preprocessing/decoding constant: vae_decoder/config.json key "scaling_factor" = 0.13025 (used in decoding operations as the repository-declared numeric constant). Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json
- Diffusers' VaeImageProcessor defaults used with VAE encoding/decoding are documented in the Diffusers image_processor source: vae_scale_factor = 8, do_resize = True, resample = "lanczos", do_normalize = True. Sources: https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py
- Derived numeric combination present in upstream files: UNet config sample_size = 128 (unet/config.json) and VaeImageProcessor vae_scale_factor default = 8 (image_processor.py) are the upstream-declared numeric constants that combine to relate UNet sample_size to pixel resolution when the pipeline uses the VaeImageProcessor default behavior. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py

### Pre-submit validation

- model_index.json sets the pipeline-level flag force_zeros_for_empty_prompt to true (model_index.json key "force_zeros_for_empty_prompt" = true). Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json
- Evidence gap: The inspected primary files do not publish an authoritative checkpoint-scoped numeric token-length limit or truncation rule. Files checked: model_index.json, StableDiffusionXLPipeline source, and Diffusers image-processor source; none declare a checkpoint-specific token-limit number or truncation key. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py, https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py

### Task-specific formatting

- Diffusers documents and examples for weighted prompts and prompt_embeds usage applicable to SDXL pipelines in the StableDiffusionXLPipeline docs; weighted-prompts documentation demonstrates how to supply weighted text or precomputed prompt_embeds. Sources: https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl
- Evidence gap: The inspected checkpoint repository files do not mandate a single fixed prompt template for use with this checkpoint; prompts are passed as free-form natural language and prompt-weighting is demonstrated in Diffusers docs rather than enforced by the checkpoint manifest. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl

## Output interpretation

### Outputs

- VAE decoder config.json lists latent_channels = 4 and sample_size = 1024 and scaling_factor = 0.13025 (vae_decoder/config.json keys "latent_channels", "sample_size", "scaling_factor"). Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json
- UNet config.json lists sample_size = 128 (unet/config.json key "sample_size"), which the pipeline source documents is used as default_sample_size when available. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py
- Evidence gap: The inspected primary pipeline implementation and model_index.json do not provide a single canonical table enumerating numeric output-tensor shapes for every supported configuration nor an explicit numeric pixel-value output range for decoded images; practitioners should validate decoded-image pixel ranges and file encodings against their application requirements. Files checked: model_index.json, vae_decoder/config.json, unet/config.json, and StableDiffusionXLPipeline source. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py

### Interpretation

- Evidence gap: There is no upstream-declared canonical interpretation table mapping internal tensor names to application-level pixel-value ranges or image file encodings in the inspected primary files; practitioners should validate outputs against application requirements. Files inspected: vae_decoder/config.json, model_index.json, and StableDiffusionXLPipeline source. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py

### Post-inference validation

- Evidence gap: The inspected primary sources do not include a checkpoint-scoped canonical post-inference safety-verification checklist. Files checked: model_index.json, LICENSE.md, and StableDiffusionXLPipeline source. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

No evidence-safe direct comparison is available.

## Limitations and safety

### Limitations

- The repository LICENSE.md file contains license-grant language (perpetual, worldwide, non‑exclusive, royalty‑free patent and copyright licenses) but the inspected primary sources do not publish a named-forum legal interpretation or an enumerated list of prohibited uses; implementers must consult LICENSE.md and the repository README for licensing details. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md
- Evidence gap: An authoritative upstream-declared numeric total parameter count for the exact checkpoint stabilityai/stable-diffusion-xl-base-1.0 was not found in the inspected primary sources. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors
- Evidence gap: The inspected primary files do not publish checkpoint-scoped, exhaustive failure-mode tables, bias analyses, or downstream-evaluation matrices for this exact checkpoint. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py

### Safety

- Compliance with the repository LICENSE.md is required for model-weight use; LICENSE.md contains license-grant language and implementers must consult it for obligations. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md
- Evidence gap: No upstream checkpoint-scoped description of an integrated safety-checker or packaged safety classifier was found in the inspected primary files; files checked: model_index.json, repository artifact listing, and StableDiffusionXLPipeline source. Sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### sd_xl_base_1.0.safetensors (model artifact listing)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: Checkpoint weight artifact file listed in the model repository.
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: artifact presence

### model_index.json for SDXL base 1.0 (main)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: Repository manifest enumerating the pipeline class, components, component identifiers, metadata keys (including force_zeros_for_empty_prompt).
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: pipeline_class
- Supports: component_list
- Supports: force_zeros_for_empty_prompt
- Supports: scheduler
- Supports: text encoder identifiers
- Supports: tokenizer identifiers

### model_index.json for SDXL base 1.0 (refs/pr/246)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/refs%2Fpr%2F246/model_index.json
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: Repository manifest variant at refs/pr/246 used to verify pipeline class name at that commit/ref.
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: pipeline_class

### UNet configuration for stable-diffusion-xl-base-1.0 (config.json)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: UNet model configuration file included in the checkpoint repository providing numeric model hyperparameters (e.g., sample_size).
- Scope: stabilityai/stable-diffusion-xl-base-1.0 (UNet component)
- Supports: unet sample_size
- Supports: UNet numeric configuration keys

### VAE decoder configuration for stable-diffusion-xl-base-1.0 (config.json)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: VAE decoder configuration file included in the checkpoint repository containing numeric scaling_factor and VAE sample_size keys.
- Scope: stabilityai/stable-diffusion-xl-base-1.0 (VAE component)
- Supports: vae scaling_factor
- Supports: vae sample_size
- Supports: vae latent_channels

### Repository README (blame view for commit 91704ab)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: Repository README lists model developer, model type, recommended dependencies, and license name string.
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: developer attribution
- Supports: model description
- Supports: declared license name
- Supports: recommended dependencies and load example

### LICENSE.md (checkpoint repository file)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md
- Publisher: Stability AI / Hugging Face
- Type: `official-documentation`
- Primary because: Authoritative license text published in the checkpoint repository.
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: license grant language
- Supports: legal obligations reference

### Repository commits view (refs/pr/252)

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/commits/refs%2Fpr%2F252
- Publisher: Stability AI / Hugging Face
- Type: `repository`
- Primary because: Repository commits view recording commit hashes related to VAE and artifact changes; used to verify commit hashes present in the repository history.
- Scope: stabilityai/stable-diffusion-xl-base-1.0
- Supports: commit history
- Supports: artifact-related commits

### StableDiffusionXLPipeline implementation (Diffusers)

- URL: https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py
- Publisher: Hugging Face / Diffusers
- Type: `repository`
- Primary because: Official Diffusers pipeline source documenting pipeline component registration, defaults, and behavior (force_zeros_for_empty_prompt, default_sample_size logic, vae_scale_factor computation).
- Scope: StableDiffusionXLPipeline (pipeline source)
- Supports: pipeline defaults
- Supports: force_zeros_for_empty_prompt behavior
- Supports: default_sample_size behavior
- Supports: vae_scale_factor computation

### Diffusers image processor source (VaeImageProcessor defaults)

- URL: https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py
- Publisher: Hugging Face / Diffusers
- Type: `repository`
- Primary because: Diffusers source code declaring VaeImageProcessor defaults and resizing/normalization behavior.
- Scope: Diffusers VaeImageProcessor (implementation)
- Supports: vae_scale_factor default
- Supports: do_resize behavior
- Supports: resample default
- Supports: do_normalize behavior

### Diffusers StableDiffusionXL pipeline API docs

- URL: https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl
- Publisher: Hugging Face / Diffusers
- Type: `official-documentation`
- Primary because: Official API documentation describing required pipeline components and pipeline-level flags.
- Scope: StableDiffusionXLPipeline (documentation)
- Supports: pipeline component types
- Supports: force_zeros_for_empty_prompt default
- Supports: pipeline API semantics

### Exact official starting source declared by Forge

- URL: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- Publisher: huggingface.co
- Type: `official-documentation`
- Primary because: The Forge exact-version catalog declares this first-party URL as the official source for the covered serving variant.
- Scope: stabilityai-stable-diffusion-xl
- Supports: Forge-to-upstream exact-version identity

## Evidence gaps

- Evidence gap: No upstream-declared authoritative numeric total parameter count for stabilityai/stable-diffusion-xl-base-1.0 was found in the inspected primary sources. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors.
- Evidence gap: No checkpoint-scoped numeric benchmarks (dataset/split/metric/value) naming stabilityai/stable-diffusion-xl-base-1.0 were found in the inspected primary sources. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blame/91704abbae38a0e1f60d433fb08d7f7d99081d21/README.md, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json.
- Evidence gap: No upstream-declared, checkpoint-scoped canonical enumeration of accepted weight packaging formats was found in the inspected primary files. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json and https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors.
- Evidence gap: The inspected primary pipeline implementation and model_index.json do not include a canonical, checkpoint-scoped table enumerating numeric output-tensor shapes and explicit decoded-image pixel-value ranges for every supported configuration. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json.
- Evidence gap: No checkpoint-scoped integrated safety-checker or packaged safety classifier description was found in the inspected primary files. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/sd_xl_base_1.0.safetensors, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py.
- Evidence gap: No checkpoint-scoped token-length limit or truncation rule was declared in the inspected primary files. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/stable_diffusion_xl/pipeline_stable_diffusion_xl.py, https://github.com/huggingface/diffusers/blob/main/src/diffusers/image_processor.py, https://huggingface.co/docs/diffusers/en/api/pipelines/stable_diffusion/stable_diffusion_xl.
- Evidence gap: No checkpoint-scoped comparisons to other named checkpoints were located in the inspected primary sources. Files checked: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/model_index.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/vae_decoder/config.json, https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/unet/config.json.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 18 deterministic draft defect(s) were supplied to the audit.

- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[11].sourceType: $.sources[11].sourceType: 'issue-discussion' is not in ['paper', 'model-card', 'repository', 'official-documentation', 'technical-report'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].sourceType: $.sources[12].sourceType: 'discussion' is not in ['paper', 'model-card', 'repository', 'official-documentation', 'technical-report'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13].sourceType: $.sources[13].sourceType: 'discussion' is not in ['paper', 'model-card', 'repository', 'official-documentation', 'technical-report'] Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources must not contain duplicate URLs: $.sources must not contain duplicate URLs Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[10] uses unapproved repository owner 'stability-ai' for this exact model scope: $.sources[10] uses unapproved repository owner 'stability-ai' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12] uses forbidden secondary URL https: $.sources[12] uses forbidden secondary URL https://github.com/huggingface/diffusers/discussions/8944 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[13] uses forbidden secondary URL https: $.sources[13] uses forbidden secondary URL https://github.com/huggingface/diffusers/discussions/6836 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/stabilityai-stable-diffusion-xl-base-1-0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://ai.azure.com/catalog/models/stabilityai-stable-diffusion-xl-base-1-0 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://content.linkedin.com/content/dam/help/tns/en/CreativeM-L-Open-R-22-08-22.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface/docs/diffusers/v0.38.0/en/api/pipelines/stable_diffusion/stable_diffusion_xl Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/diffusers/main/examples/community/lpw_stable_diffusion_xl.py Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/huggingface/diffusers/discussions/3654 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/6bae04ca53ecd34a73d41aba23b01719b1f4a94e Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://content.linkedin.com/content/dam/help/tns/en/CreativeM-L-Open-R-22-08-22.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path: $.benchmarks[0].sourceLocator must identify the exact table, figure, section, appendix, page, heading, or repository path Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
