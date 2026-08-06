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

- Research key: `build-nvidia-com-nvidia-cosmos-reason2-8b-8b6e315315`
- Independent audit: `revised`
- Researched: `2026-07-23T23:19:09.861852+00:00`

Checkpoint-scoped dossier for nvidia/Cosmos-Reason2-8B assembled from inspected first-party artifacts. The upstream checkpoint is hosted on Hugging Face under nvidia/Cosmos-Reason2-8B and is described as an ~8B-parameter multimodal reasoning (vision-language) model for Physical AI and robotics. NVIDIA provides a container/NIM variant (nvcr.io/nim/nvidia/cosmos-reason2-8b) documented in the NGC catalog; container-level packaging, runtime, and serving claims are treated separately from upstream-checkpoint facts in this dossier. The upstream model artifact contains a README benchmark table with numeric rows (e.g., General score 73.73; BlinkDepth 87.90; VideoPhy2 36.80) but the table does not include explicit per-row dataset/split/protocol metadata required for strict protocol-matched comparisons; these numeric rows are recorded with an explicit caveat and evidence gaps. Multiple checkpoint-scoped engineering artifacts required for exact operational reproduction (for example a downloadable checkpoint-scoped tokenizer vocab/token-id mapping file, canonical preprocessing constants such as pixel-normalization and resize dims, and a single consolidated license text covering both model weights and container/code artifacts) were not found in a single authoritative artifact and are recorded as evidence gaps in this dossier. Container/NIM pages and NVIDIA docs provide example API parameters and example default settings (for example video FPS sampling and media IO parameters) and are cited as container/serving-level evidence distinct from upstream-checkpoint evidence.

## Identity

- Upstream name: nvidia/Cosmos-Reason2-8B
- Checkpoint/version: nvidia/Cosmos-Reason2-8B
- Immutable revision: not reported
- Parameter scale: approximately 8 billion parameters
- Architecture/head: not reported
- License: NVIDIA Open Model License (model weights); Apache-2.0 (code/artifacts) where applicable
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://github.com/NVIDIA/Cosmos-Tokenizer, https://docs.nvidia.com/vss/latest/License-Information.html

## Selection

### Recommended

- **Multimodal physical-AI reasoning and explanatory text generation (image/video + text) for research, development, and non-safety-critical prototyping** — The upstream Hugging Face model page and NVIDIA cookbook/repository materials describe the model as an ~8B multimodal reasoning vision-language model intended for Physical AI/robotics reasoning tasks and provide example prompts, recipes, and inference workflows supporting this use.
  Scope: nvidia/Cosmos-Reason2-8B (upstream checkpoint / model card); cookbook and repository examples are supporting artifacts for usage patterns
  Evidence: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://github.com/nvidia-cosmos/cosmos-reason2, https://nvidia-cosmos.github.io/cosmos-cookbook/index.html

### Conditional

- **Very long-context multimodal reasoning (very long videos / extremely long token contexts) — only with integrator validation** — Integrators must validate long-context behavior, exact numeric limits, and serving-image specifics in their deployment environment before relying on very long context; this dossier did not locate a single canonical checkpoint-scoped numeric specification for maximum token/context length.
  Scope: nvidia/Cosmos-Reason2-8B (upstream checkpoint) and nvcr.io/nim/nvidia/cosmos-reason2-8b (container-level serving claims) — treat container/NIM context claims as requiring independent validation
  Evidence: https://docs.nvidia.com/cosmos/latest/reason2/index.html

### Avoid

- **Treating generated text as calibrated probabilities or using raw model text outputs as calibrated confidence scores for direct actuation without external validation** — No publisher-provided checkpoint-scoped calibration semantics or canonical post-inference calibration procedures for textual outputs were found in the inspected upstream artifacts; do not assume generated text corresponds to calibrated probability scores without external calibration/validation.
  Scope: nvidia/Cosmos-Reason2-8B (upstream checkpoint)
  Evidence: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b

## Input preparation

### Semantic inputs

- Text prompts / queries (text modality). Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Images (image modality). Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Videos (video modality). Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B

### Accepted formats

- Model/serving examples and toolkit docs reference common image and video container formats (examples use JPG/PNG for images and MP4 for video in upstream examples and toolkit docs). Sources: https://docs.nvidia.com/tao/tao-toolkit/latest/text/vlm_finetuning/cosmos_rl.html, https://huggingface.co/nvidia/Cosmos-Reason2-8B

### Preprocessing

- The Cosmos Reason2 API and post-training recipe documents expose video/frame sampling parameters (fps or number-of-frames) and image/video resize/total-pixel configuration knobs (for example keys such as media_io_kwargs.video.fps, media_io_kwargs.video.num_frames, mm_processor_kwargs.size.shortest_edge). Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html, https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/reason2/video_caption_vqa/post_training.html
- Evidence gap: Precise checkpoint-scoped tokenizer artifact (downloadable vocab/token-id mapping file and explicit tokenizer config) and canonical per-checkpoint tokenizer config were not found in the inspected sources; integrators should obtain and lock a tokenizer artifact appropriate to their serving setup. Sources: https://github.com/NVIDIA/Cosmos-Tokenizer
- Evidence gap: Detailed per-modality preprocessing constants (explicit pixel-normalization constants, definitive image resize dimensions, canonical video FPS/codec handling) were not found in a single canonical checkpoint-scoped artifact; integrators must validate preprocessing recipes against their chosen serving configuration. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://github.com/nvidia-cosmos/cosmos-reason2

### Pre-submit validation

- Evidence gap: Explicit input-validation bounds (detailed coordinate conventions beyond high-level examples, explicit per-task coordinate ranges, and exhaustive video frame-count limits) for the named checkpoint were not found in a single canonical artifact; integrators must enforce input bounds appropriate to their deployment. Sources: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html, https://github.com/nvidia-cosmos/cosmos-reason2

### Task-specific formatting

- Example prompt templates and repository-level prompt guidance for common tasks (captioning, temporal localization, embodied reasoning, 2D grounding, Robot COT) are provided in the Cosmos-Reason2 repository prompts area and the cookbook. Sources: https://github.com/nvidia-cosmos/cosmos-reason2/blob/main/prompts/README.md, https://nvidia-cosmos.github.io/cosmos-cookbook/index.html
- Evidence gap: A single authoritative exhaustive paired-input order for all multimodal prompt variants and an authoritative instruction-tuning prompt format for the exact upstream checkpoint were not found in a single canonical artifact. Sources: https://github.com/nvidia-cosmos/cosmos-reason2/blob/main/prompts/README.md

## Output interpretation

### Outputs

- Primary emitted modality reported in inspected artifacts is generated text / textual reasoning as the model's primary response form. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B

### Interpretation

- Evidence gap: The inspected upstream artifacts do not provide publisher-supplied, checkpoint-scoped calibration semantics for textual outputs; do not treat raw generated text as calibrated probability scores without external calibration or validation. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B

### Post-inference validation

- Evidence gap: Checkpoint-scoped post-inference calibration procedures, canonical safety-check scripts, or an exhaustive post-inference validation checklist were not found in the inspected artifacts; integrators should implement task-specific sanity checks and human-in-the-loop gating. Sources: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b, https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html

## Public benchmarks

### Aggregate multimodal benchmark (General score)

- Dataset/split: README benchmark table (dataset/split/protocol not fully specified in artifact) / not reported
- Metric/value: General score (aggregate) / 73.73 (`higher-is-better`)
- Model scope: nvidia/Cosmos-Reason2-8B (upstream README benchmark table)
- Conditions: As presented in the upstream README benchmark table; the artifact does not include explicit per-row dataset/split/protocol metadata required for strict protocol-matched comparisons.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Locator: README.md benchmark table
- Caveat: Missing explicit per-row dataset/split/protocol metadata in the cited README table; cannot assert strict comparability without additional protocol detail.

### BlinkDepth (subscore from README benchmark table)

- Dataset/split: README benchmark table (dataset/split/protocol not fully specified in artifact) / not reported
- Metric/value: BlinkDepth / 87.90 (`higher-is-better`)
- Model scope: nvidia/Cosmos-Reason2-8B (upstream README benchmark table)
- Conditions: As presented in the upstream README benchmark table; protocol details not fully enumerated in the artifact.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Locator: README.md benchmark table
- Caveat: Benchmark table lacks per-row protocol/split metadata required for strict reproducibility.

### VideoPhy2 (subscore from README benchmark table)

- Dataset/split: README benchmark table (dataset/split/protocol not fully specified in artifact) / not reported
- Metric/value: VideoPhy2 / 36.80 (`higher-is-better`)
- Model scope: nvidia/Cosmos-Reason2-8B (upstream README benchmark table)
- Conditions: As presented in the upstream README benchmark table; protocol details not fully enumerated in the artifact.
- Source: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Locator: README.md benchmark table
- Caveat: Benchmark rows lack dataset/split/protocol detail in the cited artifact; see evidenceGaps for missing protocol metadata.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Multimodal physical-AI / embodied reasoning (as presented in upstream README and cookbook examples)
- Criteria: Upstream README numeric rows exist but lack per-row protocol metadata required for protocol-matched comparisons; cookbook examples provide side-by-side showcase content but do not provide full reproducibility metadata for strict benchmarking.
- Rationale: The inspected primary artifacts (upstream README benchmark table and cookbook showcase) present numeric comparisons and side-by-side examples but do not include per-row protocol metadata required for strict comparability; therefore protocol-matched preference decisions are unsupported by the inspected artifacts.
- Comparison conditions: The README benchmark table and cookbook showcase lack full per-row dataset/split/protocol metadata necessary for direct protocol-matched comparisons.
- Evidence: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://nvidia-cosmos.github.io/cosmos-cookbook/index.html

## Limitations and safety

### Limitations

- Ambiguity and absence of canonical numeric benchmark protocol: the upstream README benchmark table provides numeric scores but does not include explicit per-row dataset/split/protocol metadata required for strict, protocol-matched comparisons. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Evidence gap: Canonical per-checkpoint tokenizer downloads and explicit tokenizer configuration files for the exact upstream checkpoint were not found in the inspected sources; tokenizer code and tooling exist but a packaged checkpoint-scoped tokenizer artifact was not located. Sources: https://github.com/NVIDIA/Cosmos-Tokenizer
- Evidence gap: Detailed preprocessing (explicit pixel-normalization constants, exact image resize dimensions, explicit canonical video fps/codec handling) and exhaustive input-validation bounds for the upstream checkpoint are not specified in the inspected sources. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://github.com/nvidia-cosmos/cosmos-reason2
- Evidence gap: No single consolidated license text enumerating both the model-weights license and all code/container license texts for the exact checkpoint and its container packaging was found in a single canonical artifact. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://docs.nvidia.com/vss/latest/License-Information.html, https://github.com/NVIDIA/Cosmos-Tokenizer

### Safety

- Evidence gap: The inspected artifacts do not include publisher-provided checkpoint-scoped safety validation workflows, human-in-the-loop gating procedures, actuator-safety checklists, or example safety-check scripts tied specifically to this checkpoint; integrators must adopt independent safety validation processes. Sources: https://huggingface.co/nvidia/Cosmos-Reason2-8B, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- Evidence gap: A single canonical documented numeric minimum GPU-memory requirement for the upstream checkpoint (expressed as an absolute single value tied to the named checkpoint) was not found in a single inspected artifact; integrators should consult container/NIM documentation and validate memory requirements in their deployment environment. Sources: https://docs.nvidia.com/cosmos/latest/prerequisites.html, https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Exact official starting source declared by Forge

- URL: https://build.nvidia.com/nvidia/cosmos-reason2-8b
- Publisher: build.nvidia.com
- Type: `official-documentation`
- Primary because: Forge starting URL for the covered checkpoint/serving variant; listed by the user as the canonical Forge entry point for this dossier.
- Scope: forge starting source (serving/packaging identity)
- Supports: researchSummary

### Hugging Face model page: nvidia/Cosmos-Reason2-8B

- URL: https://huggingface.co/nvidia/Cosmos-Reason2-8B
- Publisher: Hugging Face (NVIDIA account)
- Type: `model-card`
- Primary because: Upstream model hosting page and README used to verify checkpoint identifier, multimodal capability statements, and the README benchmark numeric rows.
- Scope: nvidia/Cosmos-Reason2-8B (model-card / upstream README)
- Supports: identity.upstreamName
- Supports: identity.parameterScale
- Supports: researchSummary
- Supports: inputPreparation.semanticInputs
- Supports: benchmarks
- Supports: outputInterpretation.outputs
- Supports: limitations

### NVIDIA NGC catalog: nvcr.io/nim/nvidia/cosmos-reason2-8b

- URL: https://catalog.ngc.nvidia.com/orgs/nim/teams/nvidia/containers/cosmos-reason2-8b
- Publisher: NVIDIA NGC
- Type: `official-documentation`
- Primary because: NGC container/registry catalog used to source container-level metadata, packaging identity, and to separate container/NIM claims from upstream-checkpoint facts.
- Scope: nvcr.io/nim/nvidia/cosmos-reason2-8b:1.6.0 (container/NGC catalog listing)
- Supports: researchSummary
- Supports: safety
- Supports: inputPreparation.preprocessin
- Supports: outputInterpretation.validation

### NIM Vision-Language Models examples: Cosmos-Reason2 API (NVIDIA NIM docs)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.6.0/examples/cosmos-reason2/api.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Official NIM/VLM example documentation inspected for API parameters (video fps/num_frames), default sampling behaviors, and mm_processor kwargs.
- Scope: nvcr.io/nim/nvidia/cosmos-reason2-8b:1.6.0 (NIM examples/documentation)
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: conditionalUseCases
- Supports: researchSummary

### NIM Vision-Language Models introduction (1.6.0)

- URL: https://docs.nvidia.com/nim/vision-language-models/1.6.0/introduction.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: NIM introduction and release-level artifacts providing NIM version context and links to release notes; used to separate container/NIM claims from upstream-checkpoint facts.
- Scope: nvcr.io/nim/nvidia/cosmos-reason2-8b:1.6.0 (NIM introduction / 1.6.0 context)
- Supports: researchSummary
- Supports: conditionalUseCases

### Cosmos Reason2 product documentation (reason2 product docs)

- URL: https://docs.nvidia.com/cosmos/latest/reason2/index.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Product-level documentation used to inspect feature claims and to flag long-context and feature-level documentation as container/product-level evidence.
- Scope: Cosmos-Reason2 product documentation
- Supports: conditionalUseCases
- Supports: researchSummary
- Supports: limitations

### Cosmos Reason2 repository (prompts and examples)

- URL: https://github.com/nvidia-cosmos/cosmos-reason2
- Publisher: NVIDIA (GitHub)
- Type: `repository`
- Primary because: Official repository containing prompts, examples, and recipes used to verify availability of prompt templates and usage guidance.
- Scope: nvidia/Cosmos-Reason2-8B (repository examples and prompts)
- Supports: inputPreparation.taskSpecificFormatting
- Supports: researchSummary
- Supports: limitations

### Cosmos Reason2 repository prompts README (file view)

- URL: https://github.com/nvidia-cosmos/cosmos-reason2/blob/main/prompts/README.md
- Publisher: NVIDIA (GitHub)
- Type: `repository`
- Primary because: Repository file with task-specific prompt templates used to support prompt guidance claims.
- Scope: nvidia/Cosmos-Reason2-8B (prompts/examples file)
- Supports: inputPreparation.taskSpecificFormatting
- Supports: researchSummary

### NVIDIA Cosmos Tokenizer repository (tokenizer code/artifacts)

- URL: https://github.com/NVIDIA/Cosmos-Tokenizer
- Publisher: NVIDIA (GitHub)
- Type: `repository`
- Primary because: Official tokenizer repository inspected to search for checkpoint-scoped tokenizer artifacts and to verify tokenizer-related code and licensing.
- Scope: tokenizer tooling and code
- Supports: inputPreparation.preprocessing
- Supports: limitations

### Cosmos cookbook: post-training recipe (video caption VQA)

- URL: https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/reason2/video_caption_vqa/post_training.html
- Publisher: NVIDIA Cosmos (documentation site)
- Type: `official-documentation`
- Primary because: Post-training recipe used to inspect training/mixing proportions, nframes/fps usage, and pixel-size guidance in recipe examples.
- Scope: post-training recipe guidance for Cosmos-Reason2
- Supports: inputPreparation.preprocessing
- Supports: researchSummary

### Cosmos cookbook index / inference cookbook

- URL: https://nvidia-cosmos.github.io/cosmos-cookbook/index.html
- Publisher: NVIDIA Cosmos (documentation site)
- Type: `official-documentation`
- Primary because: Cookbook site providing prompting guides, inference workflows, and example showcase material.
- Scope: cookbook inference and prompt guidance
- Supports: recommendedUseCases
- Supports: comparisons
- Supports: researchSummary

### Cosmos predict2 reference

- URL: https://docs.nvidia.com/cosmos/latest/predict2/reference.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Reference page consulted for example default resolution/fps configurations and model invocation parameters in product docs.
- Scope: product reference for predict2
- Supports: inputPreparation.preprocessing
- Supports: researchSummary

### TAO Toolkit COSMOS RL (example input field descriptions)

- URL: https://docs.nvidia.com/tao/tao-toolkit/latest/text/vlm_finetuning/cosmos_rl.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: Toolkit docs showing example inference fields (media field, fps defaults) and supported media formats.
- Scope: toolkit example fields and defaults
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.preprocessing

### Deployment/blueprint references and worked examples (video search/summarization blueprint)

- URL: https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/blob/main/skills/vss-deploy-profile/references/base.md
- Publisher: NVIDIA-AI-Blueprints (GitHub)
- Type: `repository`
- Primary because: Blueprint and deployment reference file used to inspect deployment/serve example variables and memory/precision guidance for serving workflows.
- Scope: deployment blueprint references
- Supports: researchSummary
- Supports: limitations
- Supports: safety

### NVIDIA VSS license information (docs)

- URL: https://docs.nvidia.com/vss/latest/License-Information.html
- Publisher: NVIDIA
- Type: `official-documentation`
- Primary because: License information page consulted when assembling license and artifact licensing statements.
- Scope: license and artifact licensing references
- Supports: identity.license
- Supports: limitations

### Cited official first-party source

- URL: https://docs.nvidia.com/cosmos/latest/prerequisites.html
- Publisher: docs.nvidia.com
- Type: `official-documentation`
- Primary because: The independent audit cited this exact URL and its host is narrowly allowlisted as a first-party model or vendor documentation source.
- Scope: nvidia-cosmos-reason2
- Supports: Exact independently audited claim citation

## Evidence gaps

- Evidence gap: No checkpoint-scoped downloadable tokenizer artifact (vocab/token-id mapping file and explicit tokenizer config) for nvidia/Cosmos-Reason2-8B was located in the inspected sources; tokenizer code and tooling exist but a packaged checkpoint-scoped tokenizer file was not found.
- Evidence gap: Precise long-context numeric limits for the upstream checkpoint (a single canonical checkpoint-scoped maximum token/context length) were not found in a single authoritative upstream artifact in the inspected sources; integrators must validate long-context behavior for their serving configuration.
- Evidence gap: Precise per-modality preprocessing constants (explicit pixel-normalization constants, exact image resize dimensions, explicit accepted video fps/codec handling) were not found in a single canonical checkpoint-scoped artifact in the inspected sources.
- Evidence gap: Canonical structured output schemas (exhaustive JSON response contracts) and explicit post-inference calibration procedures tied to the exact upstream checkpoint were not found in the inspected sources.
- Evidence gap: A single consolidated license text enumerating model-weights license and all code/container license texts for the exact checkpoint and its container packaging was not found in a single authoritative inspected artifact.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 2 deterministic draft defect(s) were supplied to the audit.

- `medium` official starting source is absent from $.sources: official starting source is absent from $.sources: https://build.nvidia.com/nvidia/cosmos-reason2-8b Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[12].primary must be true: $.sources[12].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `low` https://docs.nvidia.com/cosmos/latest/prerequisites.html: Audited claim cited a first-party child URL omitted from the source index. Resolution: The runner indexed the exact child URL beneath its already verified first-party parent; no claim content changed.
