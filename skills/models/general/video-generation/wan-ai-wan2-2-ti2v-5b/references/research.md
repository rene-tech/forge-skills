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

- Research key: `huggingface-co-wan-ai-wan2-2-ti2v-5b-diffusers-a89380e6a9`
- Independent audit: `revised`
- Researched: `2026-08-06T10:08:26.293805+00:00`

Checkpoint-scoped dossier assembled from the official Hugging Face model pages and repository blobs listed in sources. The Wan2.2-TI2V-5B-Diffusers model page and its README/model_index.json assert a TI2V (text-image-video) diffusion model family with a dense 5B variant and an MoE A14B variant described; model_index.json lists pipeline and component classes (WanPipeline, T5TokenizerFast, UMT5EncoderModel, WanTransformer3DModel, AutoencoderKLWan, UniPCMultistepScheduler). config.json (Wan2.2-TI2V-5B repo) provides numeric hyperparameters (dim: 3072; ffn_dim: 14336; num_heads: 24; num_layers: 30; text_len: 512). README blobs assert capability for text-to-video and image-to-video, claim 720P (1280x704 or 704x1280) at 24 FPS and include example generation flags for a 5-second example; README also describes MoE expert parameter counts (~14B per expert, ~27B total for A14B series). The primary blobs do not contain numeric benchmark tables, standardized latency benchmarking methodology, or explicit safety/privacy/dataset-provenance statements for this exact checkpoint; those are recorded as evidence gaps.

## Identity

- Upstream name: Wan2.2 TI2V-5B-Diffusers
- Checkpoint/version: Wan2.2-TI2V-5B-Diffusers
- Immutable revision: not reported
- Parameter scale: Dense 5B; MoE variant described: each MoE expert ~14B parameters; A14B MoE series total ~27B with ~14B active per inference step
- Architecture/head: TI2V (text-image-video) diffusion model family; Mixture-of-Experts (MoE) A14B variant described; 3D transformer and VAE components listed in model_index.json
- License: Apache-2.0 (as stated on Hugging Face model pages and README blobs)
- Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/config.json, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md

## Selection

### Recommended

- **Text-to-video generation (T2V) at 720P/24fps for short outputs (example 5-second clip)** — Model page and README assert T2V capability and include an example 5-second generation at 720P and 24 FPS.
  Scope: Wan2.2 TI2V-5B-Diffusers
  Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers
- **Image-to-video generation (I2V) using reference images** — README and model page describe unified text-image-video (TI2V) support indicating both T2V and I2V workflows.
  Scope: Wan2.2 TI2V-5B-Diffusers
  Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers
- **Integration with Hugging Face Diffusers tooling using the listed pipeline and components** — model_index.json enumerates pipeline and component classes enabling Diffusers-based integration.
  Scope: Wan2.2 TI2V-5B-Diffusers
  Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json

### Conditional

- **Lower-resource deployments using reduced precision or quantized variants** — Evidence gap: Official upstream primary sources do not document validated quantization recipes or reduced-precision runtime guidance for this exact checkpoint; downstream validation and per-device profiling required.
  Scope: Wan2.2 TI2V-5B-Diffusers
  Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json

### Avoid

- **Safety-critical decision-making or clinical/medical diagnostic use** — Evidence gap: Upstream primary sources for this exact checkpoint do not provide safety, privacy, or clinical validation guidance; no suitability claims for safety-critical or clinical tasks are documented.
  Scope: Wan2.2 TI2V-5B-Diffusers
  Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

## Input preparation

### Semantic inputs

- Text prompts (natural language) are the primary conditioning input for text-to-video operation. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers
- Reference image inputs are supported for image-to-video workflows. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json

### Accepted formats

- Text prompts and standard image files are accepted as inputs for T2V and I2V workflows; exact encoding/format conventions are not specified in the primary blobs. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers

### Preprocessing

- Tokenizer and text-encoder classes are listed (T5TokenizerFast and UMT5EncoderModel); model_index.json lists transformer and VAE component classes (WanTransformer3DModel, AutoencoderKLWan) and scheduler (UniPCMultistepScheduler). config.json provides numeric hyperparameters including dim, ffn_dim, num_heads, num_layers, and text_len. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/config.json

### Pre-submit validation

- Evidence gap: Primary sources do not list formal input validation checks, explicit bounds, or ambiguous-case handling for text prompts or reference images; users must implement downstream validation. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

### Task-specific formatting

- README provides example generation flags (e.g., height=704, width=1280, num_frames=121, num_inference_steps=50, guidance_scale=5.0) and example command flags such as --offload_model, --convert_model_dtype, and --t5_cpu; no formal prompt-template schema is published upstream. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

## Output interpretation

### Outputs

- Primary output is a generated video sequence; README and model page assert operation at 720P resolution and 24 FPS and include an example 5-second generation example. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers
- Evidence gap: Auxiliary outputs (latent tensors, intermediate per-frame model-state dumps, or per-frame confidence scores) are not explicitly documented in the primary blobs for this exact checkpoint. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers

### Interpretation

- Evidence gap: Primary sources do not provide guidance for interpreting numerical confidence scores or per-frame analytic metrics for generated videos; no declared confidence/calibration outputs are documented. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers

### Post-inference validation

- Evidence gap: No post-inference quality calibration, automated sanity checks, or downstream validation steps are described in the primary blobs for this exact checkpoint; downstream users must validate output quality for their application. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

## Public benchmarks

No checkpoint-matched public benchmark row passed the evidence gate.

## Comparisons

### genmo-mochi-1-preview — `insufficient-evidence`

- Task: Video generation
- Criteria: Direct head-to-head comparison on identical prompts, datasets, and metrics
- Rationale: No primary-source head-to-head benchmark or matched protocol for this exact checkpoint was found in the inspected Hugging Face blobs; comparison requires external benchmarking.
- Comparison conditions: Evidence gap: matched prompts/dataset/metric not published upstream for both checkpoints in the checked primary blobs.
- Evidence: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

## Limitations and safety

### Limitations

- Architectural/specification granularity: Primary blobs provide high-level architecture labels and some dimensional hyperparameters but do not publish exhaustive per-layer diagrams or complete training-hyperparameter logs for this exact checkpoint. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/config.json, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md
- Training data and provenance: Evidence gap: Primary blobs include high-level statements about curated data but do not enumerate the training datasets, splits, or detailed data-provenance for this checkpoint. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md
- Evaluation: Evidence gap: No numeric benchmark tables, dataset/split/metric/value triples are published by upstream for this exact checkpoint in the inspected primary blobs. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json
- Operational/latency claims: README asserts generation speed (example: 5-second 720P generation described in examples and a reported timing of a 5-second clip produced in under 9 minutes on a consumer GPU in related README), but primary blobs do not provide a standardized latency/throughput benchmarking methodology or per-device validated numbers for production SLAs. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md
- Licensing: The model weights are recorded as Apache-2.0 in the Hugging Face model pages and README blobs; dataset licensing provenance is not documented in the inspected blobs (Evidence gap). Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B

### Safety

- Evidence gap: No explicit safety, privacy, moderation, or dataset-provenance instructions are documented in the inspected primary blobs for this exact checkpoint; users should apply conservative safety review and content-moderation controls appropriate to their deployment. Sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers, https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Wan2.2 TI2V-5B-Diffusers (Hugging Face model page)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers
- Publisher: Wan AI / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page for the Wan2.2-TI2V-5B-Diffusers checkpoint containing high-level capability claims and links to repository blobs.
- Scope: Wan2.2 TI2V-5B-Diffusers
- Supports: Model hosting and high-level capability claims for the Diffusers-packaged checkpoint
- Supports: Top-level statements about T2V/I2V capability and example generation

### Wan2.2 TI2V-5B-Diffusers README (Hugging Face blob)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md
- Publisher: Wan AI / Hugging Face
- Type: `repository`
- Primary because: README blob in the Wan2.2-TI2V-5B-Diffusers repository containing example prompts, example generation flags, MoE descriptions, and speed/format claims for this checkpoint.
- Scope: Wan2.2 TI2V-5B-Diffusers
- Supports: Example generation flags (height/width/num_frames/steps/guidance)
- Supports: Claims about 720P@24fps operation and example 5-second generation
- Supports: MoE expert descriptions and per-expert parameter claims

### Wan2.2 TI2V-5B-Diffusers model_index.json (Hugging Face blob)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json
- Publisher: Wan AI / Hugging Face
- Type: `repository`
- Primary because: model_index.json blob listing exact pipeline, tokenizer, text-encoder, transformer, VAE, and scheduler classes referenced by the Diffusers packaging of this checkpoint.
- Scope: Wan2.2 TI2V-5B-Diffusers
- Supports: Pipeline class: WanPipeline
- Supports: Tokenizer: T5TokenizerFast
- Supports: Text encoder: UMT5EncoderModel
- Supports: Transformer: WanTransformer3DModel
- Supports: VAE: AutoencoderKLWan
- Supports: Scheduler: UniPCMultistepScheduler

### Wan2.2 TI2V-5B config.json (Hugging Face blob)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/config.json
- Publisher: Wan AI / Hugging Face
- Type: `repository`
- Primary because: config.json blob in the Wan2.2-TI2V-5B repository containing numeric model hyperparameters for the Wan2.2 family checkpoint.
- Scope: Wan2.2 TI2V-5B (config for Wan2.2 family checkpoint)
- Supports: Numeric hyperparameters: dim, ffn_dim, num_heads, num_layers, text_len
- Supports: Model type: "ti2v" and class name declarations

### Wan2.2 TI2V-5B README (Hugging Face blob)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md
- Publisher: Wan AI / Hugging Face
- Type: `repository`
- Primary because: README blob associated with the Wan2.2-TI2V-5B config that asserts capability claims and reported generation timing for the Wan2.2 family checkpoint.
- Scope: Wan2.2 TI2V-5B
- Supports: Claims about 720P@24fps operation and reported example generation timing (e.g., 5-second clip in under 9 minutes on a consumer GPU)
- Supports: VAE compression ratio statements and training-data summary claims

### Wan2.2 TI2V-5B model page (Hugging Face)

- URL: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B
- Publisher: Wan AI / Hugging Face
- Type: `model-card`
- Primary because: Official Hugging Face model page for the Wan2.2-TI2V-5B checkpoint referenced by the config and README blobs; contains license metadata and high-level statements.
- Scope: Wan2.2 TI2V-5B
- Supports: License declaration for Wan2.2 family checkpoint
- Supports: High-level capability and dataset/training summary claims (as presented)

## Evidence gaps

- Evidence gap: No numeric benchmark tables (dataset/split/metric/value) found in README.md (checked top-level sections and example blocks) and model_index.json (checked metadata entries) at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md
- Evidence gap: Primary blobs do not publish a formal prompt-template schema for the exact checkpoint beyond illustrative example prompts in README.md at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md
- Evidence gap: No primary-source head-to-head benchmark tables or unified evaluation protocol comparing this exact checkpoint to named alternatives were found in README.md or model_index.json at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md and https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json
- Evidence gap: Primary blobs do not provide validated quantization recipes or supported reduced-precision runtime guidance for this exact checkpoint (checked README.md and model_index.json at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md and https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/model_index.json)
- Evidence gap: No standardized latency/throughput benchmarking methodology or per-device validated numbers are published in the inspected primary blobs for this exact checkpoint (checked README.md and Wan2.2 README at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md and https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md)
- Evidence gap: Dataset licensing and detailed data-provenance statements are not enumerated in the inspected primary blobs for this exact checkpoint (checked README.md and model pages at https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers and https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 43 deterministic draft defect(s) were supplied to the audit.

- `medium` $.inputPreparation.semanticInputs[0]: $.inputPreparation.semanticInputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1]: $.inputPreparation.semanticInputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0]: $.inputPreparation.acceptedFormats[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0]: $.inputPreparation.preprocessing[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0]: $.inputPreparation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.taskSpecificFormatting[0]: $.inputPreparation.taskSpecificFormatting[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0]: $.outputInterpretation.outputs[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1]: $.outputInterpretation.outputs[1]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0]: $.outputInterpretation.interpretation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0]: $.outputInterpretation.validation[0]: missing required property evidenceUrls Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5]: $.sources[5]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6]: $.sources[6]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7]: $.sources[7]: missing required property supports Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[1].primary must be true: $.sources[1].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[2].primary must be true: $.sources[2].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[3].primary must be true: $.sources[3].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[5].primary must be true: $.sources[5].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6] uses unapproved repository owner 'wan-video' for this exact model scope: $.sources[6] uses unapproved repository owner 'wan-video' for this exact model scope Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[6].primary must be true: $.sources[6].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[7].primary must be true: $.sources[7].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/modelscope.cn/models/Wan-AI/Wan2.2-TI2V-5B-Diffusers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/blob/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/genmoai/mochi Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-2.3 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://github.com/Lightricks/LTX-Video Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/OpenMOSS-Team/MOVA-360p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/OpenMOSS-Team/MOVA-720p Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.37.1/en/api/pipelines/skyreels_v2 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers/commit/4b2672c6ea255d3258fd9f9f04c85780b02ae2bf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/docs/diffusers/v0.38.0/en/api/pipelines/hunyuan_video15 Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.avoidUseCases must contain at least one scoped item: $.avoidUseCases must contain at least one scoped item Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.semanticInputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.acceptedFormats[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.preprocessing[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.inputPreparation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.outputs[1] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.interpretation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap: $.outputInterpretation.validation[0] without evidence must be labeled as a Forge policy or evidence gap Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` discarded:$.benchmarks[0]: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
