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

- Research key: `huggingface-co-zai-org-cogvideox-2b-ca9a371b9b`
- Independent audit: `revised`
- Researched: `2026-08-06T13:39:24.770357+00:00`

This dossier is checkpoint-scoped to the Hugging Face repository zai-org/CogVideoX-2b and the repository commit snapshot commit/91597cf865135b2e110206c05be3f198b312c43e as identified in the upstream commit page. Primary upstream sources (Hugging Face model card and blobs, THUDM/CogVideo repository, Hugging Face Diffusers documentation, and the canonical arXiv preprint) describe CogVideoX-2B as a ~2B-parameter text-to-video/image-to-video/video-continuation diffusion model using a 3D causal VAE and an expert transformer with a T5 text encoder. Verified checkpoint-scoped facts from the upstream artifacts include: recommended inference precision FP16, tokenizer/prompt length limit 226 tokens (commit), VAE sample height 480 and width 720 with latent_channels = 16 (vae/config.json), common reported output length 6 seconds and frame rate 8 fps (model card and commit), and VideoScore benchmark numeric entries for CogVideoX-2B reported in the canonical paper (arXiv:2412.04814) as 2.86 (VQ), 2.78 (TC), 2.65 (DD), 2.91 (TA), and 2.71 (FC). Several items required by a full operational dossier are not specified in the checked primary sources and are recorded as evidence gaps (notably: no upstream mapping for the Forge suffix "ca9a371b9b" to any commit or tag; missing explicit paper table numbering in available findings for the VideoScore table locator; missing explicit dataset split/protocol for the VideoScore metrics; absence of documented per-sample confidences/logits and concrete output container/codec or tensor layout in the checked sources; and conflicting frame-count conventions between the THUDM repository and some model-card statements). All claims in this dossier are limited to facts supported by the listed primary sources or are explicitly marked as evidence gaps where the findings do not permit a sourced assertion.

## Identity

- Upstream name: CogVideoX-2B
- Checkpoint/version: commit/91597cf865135b2e110206c05be3f198b312c43e
- Immutable revision: not reported
- Parameter scale: 2 B parameters
- Architecture/head: 3D causal variational autoencoder (3D causal VAE) + expert transformer; T5 text encoder; CogVideoXTransformer3DModel diffusion backbone
- License: Apache-2.0
- Evidence: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e, https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json, https://huggingface.co/zai-org/CogVideoX-2b/blob/949aa67efac513c1e769e0f8c6c09f476520e6fc/README.md, https://github.com/THUDM/CogVideo/blob/main/README.md, https://github.com/THUDM/CogVideo/blob/main/sat/README.md, https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox, https://huggingface.co/docs/diffusers/v0.35.0/training/cogvideox, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/cogvideo/pipeline_cogvideox_image2video.py, https://arxiv.org/pdf/2412.04814

## Selection

### Recommended

- **Text-to-video generation (short clips)** — Upstream model repository and Hugging Face model card describe CogVideoX-2B as a text-to-video generative diffusion model and list T2V as a supported inference task; upstream artifacts report common generation outputs at 720×480 and 8 fps and example duration 6 seconds.
  Scope: CogVideoX-2B (zai-org/CogVideoX-2b, commit/91597cf865135b2e110206c05be3f198b312c43e)
  Evidence: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- **Image-to-video generation and video continuation (where supported by the pipeline)** — The Diffusers CogVideoX pipeline documentation and the THUDM project README describe image-to-video and video-to-video (continuation) pipeline variants within the CogVideoX family; these task heads are part of the CogVideoX pipelines and repos.
  Scope: CogVideoX family checkpoints including the 2B variant when used with the corresponding pipeline classes
  Evidence: https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox, https://github.com/THUDM/CogVideo/blob/main/README.md

### Conditional

- **Generation at alternative resolutions, higher frame rates, or longer durations using the 2B checkpoint** — Requires explicit upstream guidance or validated configuration in the checked repository files before deploying; reconcile conflicting frame-count conventions against authoritative repo files and validate memory/precision/runtime constraints prior to use.
  Scope: CogVideoX-2B (zai-org/CogVideoX-2b, commit/91597cf865135b2e110206c05be3f198b312c43e)
  Evidence: https://huggingface.co/zai-org/CogVideoX-2b, https://github.com/THUDM/CogVideo/blob/main/README.md, https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox

### Avoid

- **Assuming CogVideoX-2B is equivalent to CogVideoX-5B for generation quality or supported resolutions/durations** — Upstream documentation and the canonical paper distinguish 2B and 5B variants; the paper and repository report different supported resolutions, durations, and numeric benchmark results across the two scales.
  Scope: CogVideoX-2B (zai-org/CogVideoX-2b)
  Evidence: https://arxiv.org/pdf/2412.04814, https://github.com/THUDM/CogVideo/blob/main/README.md, https://huggingface.co/zai-org/CogVideoX-2b
- **Deploying 2B checkpoint for arbitrary resolutions or frame rates without upstream-validated configuration** — The Hugging Face model card and repository commit state specific resolution and frame-rate (720×480, 8 fps) for the 2B variant; using unsupported configurations risks incorrect or unsupported behavior.
  Scope: CogVideoX-2B (zai-org/CogVideoX-2b)
  Evidence: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e

## Input preparation

### Semantic inputs

- Primary input modality: English text prompts for CogVideoX-2B text-to-video generation. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/blob/949aa67efac513c1e769e0f8c6c09f476520e6fc/README.md
- Image inputs and video-continuation inputs are supported by CogVideoX family pipelines (image-to-video and video-to-video pipelines) per upstream pipeline documentation and repository notes; applicability to the 2B checkpoint is conditional on configuration validation. Sources: https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox, https://github.com/THUDM/CogVideo/blob/main/README.md

### Accepted formats

- Upstream model and VAE config list sample height = 480 and sample width = 720 as the model's sample resolution. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json
- Prompt language: English is listed as the supported prompt language in the upstream model card and README. Sources: https://huggingface.co/zai-org/CogVideoX-2b/blob/949aa67efac513c1e769e0f8c6c09f476520e6fc/README.md, https://huggingface.co/zai-org/CogVideoX-2b

### Preprocessing

- Tokenizer/prompt limits: tokenizer maximum prompt length is 226 tokens (as listed on the upstream commit page and corroborated by pipeline max_sequence_length evidence in checked sources). Sources: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/cogvideo/pipeline_cogvideox_image2video.py
- VAE configuration: VAE in_channels = 3, out_channels = 3, latent_channels = 16, sample_height = 480, sample_width = 720, temporal_compression_ratio = 4, and scaling_factor = 1.15258426 per the checkpoint VAE config file. Sources: https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json
- Positional embeddings: upstream commit and pipeline sources document sinusoidal/rotary positional embedding options (sinusoidal positional embeddings are reported for the 2B checkpoint). Sources: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e, https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/cogvideo/pipeline_cogvideox_image2video.py

### Pre-submit validation

- Validate prompt length does not exceed 226 tokens for the 2B checkpoint; upstream commit lists 226-token limit. Sources: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- Validate generation configuration targets the upstream-supported sample resolution (720×480) and commonly-reported frame rate/duration (8 fps, 6 seconds) for the 2B checkpoint; mismatched generation settings may be unsupported. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- Evidence gap: Checked upstream THUDM repository and Hugging Face model card contain conflicting statements about frame-count conventions (see evidenceGaps entry); users must validate exact frame-count rules against authoritative repository files before submission. Sources: https://github.com/THUDM/CogVideo/blob/main/README.md, https://huggingface.co/zai-org/CogVideoX-2b

### Task-specific formatting

- No official structured JSON prompt schema or canonical prompt templates are present in the inspected upstream model card and README; prompts are described as English text inputs. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/blob/949aa67efac513c1e769e0f8c6c09f476520e6fc/README.md

## Output interpretation

### Outputs

- Primary generated output: video frames at resolution 720 × 480 pixels; commonly-documented output duration is 6 seconds and frame rate 8 fps for the 2B checkpoint in the checked upstream sources. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- VAE latent/tensor configuration reported in the checkpoint VAE config: latent_channels = 16, in_channels = 3, out_channels = 3; scaling_factor and temporal_compression_ratio are present in the VAE config. Sources: https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json

### Interpretation

- Interpret generated videos as model samples at the specified resolution and frame rate; upstream sources describe architectural elements (3D causal VAE and expert transformer) that improve temporal consistency, but upstream sources do not provide per-video calibrated confidence or probability outputs. Sources: https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox, https://arxiv.org/pdf/2412.04814

### Post-inference validation

- Validate that generated outputs match the VAE and model resolution/frame-rate expectations (720×480, 8 fps, 6 s) for the 2B checkpoint where those constraints are asserted upstream. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json
- Evidence gap: Upstream sources checked do not document per-sample numeric confidence scores, logits, or the exact tensor layout and container/codec used for exported videos from the standard pipeline; downstream systems must implement and validate their own calibration and containerization. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://arxiv.org/pdf/2412.04814

## Public benchmarks

### Video generation quality (VideoScore)

- Dataset/split: VideoScore / not reported
- Metric/value: Video Quality (VQ) / 2.86 (`higher-is-better`)
- Model scope: CogVideoX-2B (as reported in arXiv:2412.04814)
- Conditions: Paper reports VideoScore numbers; evaluation prompts were optimized using Qwen2.5-72B-Instruct; training used AdamW with base LR 1e-5 and cosine LR scheduler with warmup ratio 3e-2 on 8 H100 GPUs. The paper does not provide dataset split identifiers in the available findings.
- Source: https://arxiv.org/pdf/2412.04814
- Locator: VideoScore benchmark table in arXiv:2412.04814 (table not numbered in available findings; exact table number/label not provided in the available findings)
- Caveat: Dataset split and exact evaluation protocol (split name, seed, sampling protocol) are not reported in the available findings for the VideoScore entries.

### Temporal consistency (VideoScore)

- Dataset/split: VideoScore / not reported
- Metric/value: Temporal Consistency (TC) / 2.78 (`higher-is-better`)
- Model scope: CogVideoX-2B (as reported in arXiv:2412.04814)
- Conditions: See conditions for VideoScore entries in the canonical paper; dataset split not specified in available findings.
- Source: https://arxiv.org/pdf/2412.04814
- Locator: VideoScore benchmark table in arXiv:2412.04814 (table not numbered in available findings; exact table number/label not provided in the available findings)
- Caveat: Dataset split and exact evaluation protocol are not specified in the available findings for the reported numeric value.

### Dynamic diversity (VideoScore)

- Dataset/split: VideoScore / not reported
- Metric/value: Dynamic Diversity (DD) / 2.65 (`higher-is-better`)
- Model scope: CogVideoX-2B (as reported in arXiv:2412.04814)
- Conditions: See paper; split/protocol not provided in available findings.
- Source: https://arxiv.org/pdf/2412.04814
- Locator: VideoScore benchmark table in arXiv:2412.04814 (table not numbered in available findings; exact table number/label not provided in the available findings)
- Caveat: Dataset split and exact evaluation protocol are not specified in the available findings for the reported numeric value.

### Temporal alignment (VideoScore)

- Dataset/split: VideoScore / not reported
- Metric/value: Temporal Alignment (TA) / 2.91 (`higher-is-better`)
- Model scope: CogVideoX-2B (as reported in arXiv:2412.04814)
- Conditions: See paper; split/protocol not provided in available findings.
- Source: https://arxiv.org/pdf/2412.04814
- Locator: VideoScore benchmark table in arXiv:2412.04814 (table not numbered in available findings; exact table number/label not provided in the available findings)
- Caveat: Dataset split and exact evaluation protocol are not specified in the available findings for the reported numeric value.

### Flicker consistency (VideoScore)

- Dataset/split: VideoScore / not reported
- Metric/value: Flicker Consistency (FC) / 2.71 (`higher-is-better`)
- Model scope: CogVideoX-2B (as reported in arXiv:2412.04814)
- Conditions: See paper; split/protocol not provided in available findings.
- Source: https://arxiv.org/pdf/2412.04814
- Locator: VideoScore benchmark table in arXiv:2412.04814 (table not numbered in available findings; exact table number/label not provided in the available findings)
- Caveat: Dataset split and exact evaluation protocol are not specified in the available findings for the reported numeric value.

## Comparisons

### insufficient-evidence — `insufficient-evidence`

- Task: Direct primary-source numeric comparisons between CogVideoX-2B and external peer models on identical protocols/datasets
- Criteria: No primary-source benchmark tables or numeric comparisons in the checked sources directly compare CogVideoX-2B to the listed external candidate models under identical datasets/splits/protocols.
- Rationale: The inspected upstream CogVideoX paper and repository provide VideoScore results for CogVideoX variants but do not contain direct, protocol-matched primary-source comparison rows against the other named Forge candidates within the available findings.
- Comparison conditions: Comparisons would require identical dataset/split/protocol and primary-source numeric tables for both sides; these are not present in the available findings.
- Evidence: https://arxiv.org/pdf/2412.04814, https://huggingface.co/zai-org/CogVideoX-2b

## Limitations and safety

### Limitations

- Resolution and frame-rate constraints for CogVideoX-2B: upstream model card and VAE config list 720×480 (sample_height=480, sample_width=720) and common model-page statements list 8 fps and 6 s duration for 2B as common configuration. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json
- Compute and memory requirements: upstream commit and diffusers training documentation list GPU/VRAM guidance and inference/fine-tuning memory footprints indicating significant GPU memory requirements for inference and especially fine-tuning. Sources: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e, https://huggingface.co/docs/diffusers/v0.35.0/training/cogvideox
- Checkpoint-scale distinctions: upstream paper and repository distinguish CogVideoX-2B and CogVideoX-5B with different supported resolutions, durations, and numeric benchmark results; do not conflate the variants. Sources: https://arxiv.org/pdf/2412.04814, https://github.com/THUDM/CogVideo/blob/main/README.md
- Evidence gap: Conflicting frame-count conventions are present in the checked upstream sources (THUDM repo states default frame rules that differ from some Hugging Face model-card/common statements); the available findings do not provide a single authoritative reconciliation for the 2B checkpoint. Sources: https://github.com/THUDM/CogVideo/blob/main/README.md, https://huggingface.co/zai-org/CogVideoX-2b
- Upstream documentation does not expose per-sample calibrated confidence scores or logits as structured outputs; no calibration guidance is provided in the inspected primary sources. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://arxiv.org/pdf/2412.04814

### Safety

- License: CogVideoX-2B is released under Apache-2.0 as stated in the upstream Hugging Face repository; license compliance is required for production use. Sources: https://huggingface.co/zai-org/CogVideoX-2b
- Operational constraints: upstream documentation provides compute/VRAM recommendations and fine-tuning memory requirements which are operational constraints for deployment and must be followed. Sources: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e, https://huggingface.co/docs/diffusers/v0.35.0/training/cogvideox
- Evidence gap: The inspected Hugging Face model card and repository files do not contain explicit safety-mitigation guidance (content filters, banned-content lists, or required human-review workflows); implementers must apply their own content-moderation and human-review processes. Sources: https://huggingface.co/zai-org/CogVideoX-2b, https://github.com/THUDM/CogVideo/blob/main/README.md

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### CogVideoX-2b — Hugging Face model repository

- URL: https://huggingface.co/zai-org/CogVideoX-2b
- Publisher: zai-org (Hugging Face)
- Type: `model-card`
- Primary because: Official Hugging Face model card and repository page for the CogVideoX-2B checkpoint; contains model description, usage constraints, and links to components.
- Scope: zai-org/CogVideoX-2b (model card and repository)
- Supports: identity.upstreamName
- Supports: identity.license
- Supports: recommendedUseCases
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.validation
- Supports: outputInterpretation.outputs
- Supports: limitations
- Supports: safety

### Hugging Face repo commit for CogVideoX-2b (commit/91597cf865135b2e110206c05be3f198b312c43e)

- URL: https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- Publisher: zai-org (Hugging Face)
- Type: `repository`
- Primary because: Commit snapshot listing tokenizer limits, memory guidance, and checkpoint-specific runtime notes for the CogVideoX-2B checkpoint.
- Scope: zai-org/CogVideoX-2b (commit snapshot)
- Supports: identity.checkpoint
- Supports: inputPreparation.preprocessing
- Supports: inputPreparation.validation
- Supports: limitations
- Supports: safety

### CogVideoX VAE configuration (vae/config.json)

- URL: https://huggingface.co/zai-org/CogVideoX-2b/blob/main/vae/config.json
- Publisher: zai-org (Hugging Face)
- Type: `repository`
- Primary because: VAE configuration file describing sample resolution, latent channels, in/out channels, and VAE parameters for the checkpoint.
- Scope: zai-org/CogVideoX-2b (VAE config file)
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.outputs
- Supports: limitations

### CogVideoX-2b specific README (blob)

- URL: https://huggingface.co/zai-org/CogVideoX-2b/blob/949aa67efac513c1e769e0f8c6c09f476520e6fc/README.md
- Publisher: zai-org (Hugging Face)
- Type: `model-card`
- Primary because: Detailed README blob in the Hugging Face repository containing configuration, prompt language, and inference-speed notes.
- Scope: zai-org/CogVideoX-2b (README blob)
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.semanticInputs
- Supports: recommendedUseCases
- Supports: limitations

### CogVideo repository (THUDM/CogVideo) — main README

- URL: https://github.com/THUDM/CogVideo/blob/main/README.md
- Publisher: THUDM (GitHub)
- Type: `repository`
- Primary because: Official project repository README describing architecture, variant distinctions (2B vs 5B), and frame-count conventions documented by the project.
- Scope: THUDM/CogVideo (project README)
- Supports: identity.architecture
- Supports: inputPreparation.semanticInputs
- Supports: limitations
- Supports: conditionalUseCases

### CogVideo SAT README (sat/README.md)

- URL: https://github.com/THUDM/CogVideo/blob/main/sat/README.md
- Publisher: THUDM (GitHub)
- Type: `repository`
- Primary because: Subdirectory README describing SAT configuration and T5 text-encoder notes referenced by the project.
- Scope: THUDM/CogVideo (sat/ folder)
- Supports: inputPreparation.preprocessing
- Supports: identity.architecture

### Diffusers documentation: CogVideoX pipeline (API)

- URL: https://huggingface.co/docs/diffusers/en/api/pipelines/cogvideox
- Publisher: Hugging Face (diffusers docs)
- Type: `official-documentation`
- Primary because: Official Diffusers pipeline documentation describing CogVideoX pipeline classes, return types, and supported pipeline variants.
- Scope: Diffusers CogVideoX pipeline documentation
- Supports: identity.architecture
- Supports: inputPreparation.semanticInputs
- Supports: recommendedUseCases
- Supports: outputInterpretation

### Diffusers training documentation: CogVideoX (training guidance/VRAM)

- URL: https://huggingface.co/docs/diffusers/v0.35.0/training/cogvideox
- Publisher: Hugging Face (diffusers docs)
- Type: `official-documentation`
- Primary because: Official diffusers training guidance listing VRAM and inference-speed figures referenced by the model maintainers.
- Scope: Diffusers training docs for CogVideoX
- Supports: limitations
- Supports: recommendedUseCases
- Supports: safety

### Diffusers pipeline source: pipeline_cogvideox_image2video.py

- URL: https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/cogvideo/pipeline_cogvideox_image2video.py
- Publisher: Hugging Face (diffusers repository)
- Type: `repository`
- Primary because: Primary pipeline source code in the official diffusers repository documenting positional embedding usage and pipeline output tensor layout semantics.
- Scope: diffusers pipeline source for CogVideoX image2video
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation
- Supports: inputPreparation.validation

### CogVideoX paper (arXiv / canonical paper, PDF)

- URL: https://arxiv.org/pdf/2412.04814
- Publisher: arXiv (preprint)
- Type: `paper`
- Primary because: Canonical paper presenting CogVideoX architecture, training details, and VideoScore benchmark numeric entries for CogVideoX variants.
- Scope: CogVideoX paper-level results (2B and 5B variants)
- Supports: benchmarks
- Supports: identity.architecture
- Supports: limitations

## Evidence gaps

- Evidence gap: No upstream mapping found between the Forge research key suffix 'ca9a371b9b' and any repository commit, tag, or identifier in the checked primary sources. URLs inspected: https://huggingface.co/zai-org/CogVideoX-2b , https://huggingface.co/zai-org/CogVideoX-2b/commit/91597cf865135b2e110206c05be3f198b312c43e
- Evidence gap: The canonical paper (arXiv:2412.04814) is reported in the available findings to contain a VideoScore benchmark table for CogVideoX variants, but the available findings do not provide a specific table number or figure label to serve as a precise locator; table numbering/locator is not available in the checked findings.
- Evidence gap: The VideoScore numeric entries in the paper are reported without explicit dataset split identifiers or full evaluation protocol details in the available findings; the precise dataset split, seed, or sampling protocol for those metrics is not provided in the checked primary sources.
- Evidence gap: The inspected upstream sources do not document per-sample numeric confidence scores, probabilities, or logits exposed by the standard pipeline; no structured per-sample confidence output is documented in the checked primary sources (checked: model card, commit, diffusers docs, paper).
- Evidence gap: The inspected upstream sources do not specify the exact output container/codec or the exact persisted file container format and codec recommended by the standard pipeline; the checked sources describe frames/tensors but not container/codec choices.
- Evidence gap: Conflicting frame-count conventions were found in the checked upstream sources (THUDM repository and Hugging Face model card/commit) with different default frame rules; the available findings do not provide a single authoritative reconciliation for the default frame-count policy for the 2B checkpoint.
- Evidence gap: No official structured prompt templates or canonical JSON prompt schema were found in the checked upstream model card, README blob, or repository files; the checked sources describe English text prompts but do not provide a canonical prompt template.
- Evidence gap: Direct primary-source peer comparisons of CogVideoX-2B to other Forge candidate external models under an identical protocol/dataset are not present in the inspected primary sources; therefore direct numeric comparisons cannot be established from the checked evidence.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 6 deterministic draft defect(s) were supplied to the audit.

- `medium` $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[0].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[1].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[2].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[3].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[4].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading: $.benchmarks[5].sourceLocator for a paper must include a numbered/named table, figure, section, appendix, page, or heading Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
