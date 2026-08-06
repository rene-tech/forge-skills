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

- Research key: `github-com-lightricks-ltx-video-b0012664eb`
- Independent audit: `revised`
- Researched: `2026-07-23T22:29:50.823399+00:00`

This dossier is scoped to the upstream checkpoint ltxv-2b-0.9.6 from the Lightricks LTX-Video project. Upstream primary evidence (model card, README, committed checkpoint uploads, and the arXiv preprint) documents a DiT-based latent diffusion video model architecture with a 3D VAE whose vae/config.json sets latent_channels=128 and block_out_channels [128,256,512,512]. The upstream repos and model card present project-reported runtime/throughput claims (frames-per-second / real-time descriptions) and multiple checkpoint variants (including a named distilled 2B checkpoint); these runtime numbers are reported by the project and are not formal dataset-benchmark results. No formal public dataset-style quality benchmarks (FVD, IS, CLIP-FID, etc.) for the exact checkpoint ltxv-2b-0.9.6 were found in the checked primary sources. The model weights are distributed under upstream RAIL‑M / LTX Video Open Weights License texts that impose use-based restrictions and acceptable-use constraints. Where upstream sources conflict on operational duration limits (arXiv emphasis on shorter focus vs. API docs describing longer caps), the conflict is recorded rather than resolved here.

## Identity

- Upstream name: Lightricks/LTX-Video
- Checkpoint/version: ltxv-2b-0.9.6
- Immutable revision: 0f6a884be0b1adb4782dd289bf5df8deb5d8c533
- Parameter scale: not reported
- Architecture/head: DiT-based (Diffusion Transformer) latent diffusion video model with a 3D VAE; VAE latent_channels = 128 and UNet/score network uses RoPE positional embeddings and RMSNorm per upstream configs and paper.
- License: RAIL‑M / LTX Video Open Weights License 0.X (use-based restrictions; model-weights license distinct from code license)
- Evidence: https://huggingface.co/Lightricks/LTX-Video, https://huggingface.co/Lightricks/LTX-Video/commits/0f6a884be0b1adb4782dd289bf5df8deb5d8c533, https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt, https://static.lightricks.com/legal/LTX-Video-Open-Weights-License-0.X.pdf, https://static.lightricks.com/legal/ltxv-2B-open-railm-license.pdf, https://arxiv.org/abs/2501.00103, https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json, https://huggingface.co/Lightricks/LTX-Video/blob/d61f0026b566c495232a0c112481ca15c96969cb/unet/config.json

## Selection

### Recommended

- **Text-to-video generation of short videos (creative content) using the upstream checkpoint** — Upstream model card and README identify the pipeline and examples as text-to-video and provide prompts and example generation parameters for short video synthesis using the named checkpoint variants.
  Scope: ltxv-2b-0.9.6 (upstream checkpoint evidence)
  Evidence: https://huggingface.co/Lightricks/LTX-Video, https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md
- **Image+text-conditioned video generation (image-to-video / multi-keyframe conditioning) using the upstream trainer/configured pipelines** — Trainer configuration and repository README document an 'images' parameter and image-conditioned generation examples; these are provided as upstream trainer/repo configuration evidence for image+text conditioning with named checkpoints.
  Scope: ltxv-2b-0.9.6 (upstream checkpoint evidence)
  Evidence: https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md, https://github.com/Lightricks/LTX-Video
- **Video extension (forward/backward extension) and video-to-video transformations within documented endpoint limits (upstream API docs describe extend behavior)** — Upstream API documentation for the video-extend endpoint describes using input context frames to generate additional frames and preserving input resolution; it documents parameters and limits for the extend operation.
  Scope: ltxv-2b-0.9.6 (project/endpoint-level feature; verify server-side limits for a deployment)
  Evidence: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend, https://github.com/Lightricks/LTX-Video

### Conditional

- **Low-latency / real-time interactive generation** — Upstream real-time or large speedup claims are associated with a named distilled/optimized checkpoint variant (e.g., the repository's 'distilled' 2B artifact and its specific pipeline config). Validate you are using the distilled or optimized variant (named in upstream artifacts) and reproduce the pipeline_config settings before assuming real-time behavior.
  Scope: ltxv-2b-0.9.6-distilled (named distilled variant) and other 'distilled' variants as explicitly named in the upstream repo
  Evidence: https://huggingface.co/Lightricks/LTX-Video/commits/0f6a884be0b1adb4782dd289bf5df8deb5d8c533, https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-distilled.yaml, https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-dev.yaml
- **Longer-duration generation beyond short clips** — Upstream sources differ on recommended/advertised duration scope (arXiv emphasizes focus on shorter videos while API docs document caps up to 20 seconds / frame limits). Use longer durations only after checkpoint- and deployment-specific testing to confirm quality, memory, and server-side limits.
  Scope: ltxv-2b-0.9.6 (upstream checkpoint; server/API caps may differ)
  Evidence: https://arxiv.org/abs/2501.00103, https://docs.ltx.video/api-documentation/api-reference/video-generation/extend, https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md

### Avoid

- **Generating harmful or disallowed content (defamation, impersonation, PII misuse, sexual content, child sexual abuse material, trafficking, biometric ID, etc.)** — Upstream RAIL‑M / Open Weights license and acceptable-use policy explicitly prohibit many harmful and disallowed uses and impose distribution/use restrictions.
  Scope: All LTX-Video checkpoints including ltxv-2b-0.9.6 (as governed by upstream license/policy)
  Evidence: https://static.lightricks.com/legal/LTX-Video-Open-Weights-License-0.X.pdf, https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf, https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt
- **Clinical/medical decision-making or other regulated professional applications without expert review** — Upstream acceptable-use guidance and license require disclosure and caution; the model and license do not assert clinical-grade validation.
  Scope: ltxv-2b-0.9.6
  Evidence: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf, https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt
- **Domain-specific tasks (e.g., multi-view synthesis, fine-grained editing) without downstream validation** — Upstream paper and documentation note limited testing/validation for domain-specialized adaptation; such uses require downstream task-specific validation.
  Scope: ltxv-2b-0.9.6
  Evidence: https://arxiv.org/abs/2501.00103

## Input preparation

### Semantic inputs

- Primary semantic inputs are a text prompt (string) plus optional conditioning media such as image(s) or reference video(s); API accepts named fields image_uri, video_uri, audio_uri. Sources: https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md, https://docs.ltx.video/input-formats
- API prompt parameter for the Extend endpoint is optional and limited to 5000 characters per upstream API documentation. Sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend

### Accepted formats

- Supported image MIME types include image/png, image/jpeg, and image/webp as documented by upstream input-format docs. Sources: https://docs.ltx.video/input-formats
- Supported video MIME types include video/mp4 (H.264/H.265), video/quicktime (MOV, H.264/H.265), and video/x-matroska (MKV, H.264/H.265); media can be supplied via Cloud Storage, HTTPS URL, or Data URI with documented size limits. Sources: https://docs.ltx.video/input-formats

### Preprocessing

- Upstream VAE configuration specifies latent_channels = 128, block_out_channels [128,256,512,512], patch_size = 4, and patch_size_t = 1; pipeline implementations use these config values to encode/decode frame latents. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json
- UNet/score network configuration shows RoPE positional embeddings and RMSNorm settings which inform token/position processing inside the denoiser; these are upstream implementation details that affect preprocessing/conditioning semantics. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/d61f0026b566c495232a0c112481ca15c96969cb/unet/config.json
- Upstream config YAMLs list inference/hyperparameter fields such as guidance_scale and num_inference_steps; verify downstream pipeline configs before deploying. Sources: https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-dev.yaml, https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-distilled.yaml
- Evidence gap: The exact pixel-to-latent compression ratio (e.g., a numeric 1:192 claim) is not specified in the upstream VAE/config facts provided in the research findings; do not assume a specific numeric compression ratio without an explicit upstream statement. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json

### Pre-submit validation

- Resolution must be divisible by 32 and frame counts must follow the model's divisibility constraints (frames divisible by 8 + 1) per upstream README and examples; when inputs do not meet these constraints upstream examples show inputs are padded and cropped. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md
- When supplying lists of images or reference_videos for trainer validation, counts must match the expected prompt/image pairing as documented in the trainer configuration reference. Sources: https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md

### Task-specific formatting

- Upstream trainer and README examples use named CLI/config fields such as --prompt, --input_image_path, --height, --width, --num_frames, --seed, and pipeline_config entries; reproduce upstream pipeline_config values for reproducible behavior. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md, https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md
- API/endpoint parameters documented in the Extend endpoint include mode (defaults to 'end'), duration (double between 2 and 20 seconds per upstream docs), and prompt (optional, up to 5000 characters). Sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend

## Output interpretation

### Outputs

- Generated outputs are video frames (height × width pixels × number of frames); upstream VAE latent_channels = 128 informs the latent-channel depth for encoded tensors used internally by the pipeline. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json, https://huggingface.co/Lightricks/LTX-Video
- Project/README examples and API docs describe preserved output resolution for extension operations; treat output resolution and duration as bounded by upstream documented limits and server-side caps. Sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend, https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md

### Interpretation

- Final visual quality depends on the full upstream pipeline (VAE + denoiser + any upscaler stages described in upstream docs); downstream visual inspection and artifact checks are required to assess fidelity for a given use case. Sources: https://huggingface.co/Lightricks/LTX-Video, https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json

### Post-inference validation

- Post-inference checks recommended by upstream documentation: verify resolution divisibility and frame-count constraints, confirm generated duration/aspect ratio against endpoint limits, and visually inspect outputs for artifacts and fidelity. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md, https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md, https://docs.ltx.video/api-documentation/api-reference/video-generation/extend
- When using distilled or optimized variants, validate visual quality against non-distilled checkpoints because upstream configs document different inference step counts and guidance settings for distilled artifacts. Sources: https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-distilled.yaml, https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-dev.yaml

## Public benchmarks

### Inference throughput / runtime claims (project-reported)

- Dataset/split: project documentation / runtime tests (not a public benchmark dataset) / not applicable
- Metric/value: frames per second (fps) and runtime / Project-reported claims in upstream model card and README describe real-time/faster-than-playback behavior and specific FPS examples (e.g., 24–30 FPS statements) and repository examples of example sizes; these are upstream project/runtime claims, not standardized dataset metrics. (`higher-is-better`)
- Model scope: ltxv-2b-0.9.6 and named distilled variants as referenced in upstream commits and README
- Conditions: Reported as project/runtime claims in upstream README and model card; some claims reference specific example sizes and named distilled/optimized variants; these are not formal benchmark protocols on public datasets.
- Source: https://huggingface.co/Lightricks/LTX-Video
- Locator: model card / README and committed README blob
- Caveat: These are project-reported runtime/performance claims rather than formal benchmark results on public datasets with standardized protocols.
- Caveat: Some runtime claims are associated with named distilled or optimized checkpoint variants; verify exact artifact and pipeline config before assuming the same runtime on the base checkpoint.

## Comparisons

### genmo-mochi-1-preview — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No protocol-matched primary-source benchmark or dataset evaluation was found in the provided upstream findings for the alternative; cannot perform head-to-head comparison.
- Rationale: Primary-source benchmark/protocol data for the alternative is not present in the research findings, so direct comparison is not possible.
- Comparison conditions: Protocol-matched dataset/metric/split and measurement conditions required but absent.
- Evidence:

### hunyuanvideo-community-hunyuanvideo-1-5-480p-t2v — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: The research findings do not include the alternative's primary documentation or benchmarks; cannot compare.
- Comparison conditions: Missing primary-source protocol elements for the alternative.
- Evidence:

### lightricks-ltx-2-3-sglang — `insufficient-evidence`

- Task: text-to-video generation / higher-fidelity long-form video
- Criteria: Although LTX-2.3 product docs appear in upstream product documentation, no protocol-matched primary benchmark table comparing ltxv-2b-0.9.6 to LTX-2.3 on the same dataset/metric was found in the research findings.
- Rationale: Different documented scopes (model variants, endpoint defaults) and absence of a shared benchmark in the checked sources prevent a protocol-matched comparison.
- Comparison conditions: Requires a head-to-head protocol using same dataset/metric; absent in findings.
- Evidence: https://docs.ltx.video/input-formats, https://huggingface.co/Lightricks/LTX-Video

### openmoss-team-mova-360p-sglang — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No primary-source protocol data for the alternative is present in the checked findings.
- Rationale: Unable to compare due to lack of the alternative's primary metrics/protocol in findings.
- Comparison conditions: Missing primary-source benchmark/protocol for the alternative.
- Evidence:

### openmoss-team-mova-720p-sglang — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: Insufficient primary-source evidence for the alternative in the findings.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

### skywork-skyreels-v2-df-1-3b-540p — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: No primary-source benchmark data for the alternative in the available findings.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

### stabilityai-stable-video-diffusion-img2vid-xt — `insufficient-evidence`

- Task: image-to-video / img2vid
- Criteria: The checked research findings do not include primary-source protocol comparisons to this alternative.
- Rationale: No matching primary-source benchmarks in the findings to enable a task- and protocol-matched comparison.
- Comparison conditions: Missing alternative primary-source protocols/metrics.
- Evidence:

### wan-ai-wan2-2-t2v-a14b — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: Unable to compare due to lack of the alternative's primary metrics/protocol in findings.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

### wan-ai-wan2-2-ti2v-5b — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: No primary-source benchmarks for the alternative in the available findings.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

### wan-ai-wan2-2-ti2v-5b-sglang — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: Insufficient primary-source evidence for the alternative within the findings.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

### zai-org-cogvideox-2b — `insufficient-evidence`

- Task: text-to-video generation
- Criteria: No comparable primary-source protocol or metric data for the alternative is present in the checked findings.
- Rationale: The alternative's primary documentation or benchmarks are not present in the research findings, preventing a protocol-matched comparison.
- Comparison conditions: Missing primary-source protocol elements.
- Evidence:

## Limitations and safety

### Limitations

- License-based use restrictions: upstream Open Weights License and repo License.txt impose use-based prohibitions and require inclusion of use-based restrictions when redistributing derivatives; licensors may impose restrictions. Sources: https://static.lightricks.com/legal/LTX-Video-Open-Weights-License-0.X.pdf, https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt
- Acceptable Use Policy restricts many harmful outputs and requires disclosure when providing medical/health advice; violations can affect access per upstream policy. Sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf
- Upstream research documentation indicates adaptation to some domain-specific tasks has not been extensively validated; domain adaptation is therefore an evidence gap and requires task-specific validation. Sources: https://arxiv.org/abs/2501.00103
- Operational constraints documented upstream (resolution divisibility, frame-count divisibility, recommended upper bounds for example cases) may limit long-form or very high-resolution uses on specific checkpoints. Sources: https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md, https://github.com/Lightricks/LTX-Video

### Safety

- Users must comply with the upstream RAIL‑M / Open Weights license and Acceptable Use Policy; upstream documentation and license define prohibited categories of outputs and require compliance. Sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf, https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt
- The Open Weights License defines 'Harm' and imposes restrictions to prevent misuse; distribution of derivatives must include use-based restrictions per the license text. Sources: https://static.lightricks.com/legal/LTX-Video-Open-Weights-License-0.X.pdf

## Related upstream agent skills

No exact or related NVIDIA/BioNeMo agent skill is mapped.

## Primary sources

### Lightricks LTX-Video HuggingFace repository (model card & model page)

- URL: https://huggingface.co/Lightricks/LTX-Video
- Publisher: Lightricks (HuggingFace repo)
- Type: `model-card`
- Primary because: Official upstream model card and model page for Lightricks/LTX-Video providing checkpoint names, model card descriptions, and links to committed artifacts.
- Scope: Lightricks/LTX-Video model card and hosted artifacts including named checkpoint variants (ltxv-2b-0.9.6 and distilled variants).
- Supports: identity.checkpoint
- Supports: researchSummary
- Supports: recommendedUseCases
- Supports: benchmarks (project-reported runtime claims)
- Supports: outputInterpretation

### HuggingFace commit showing checkpoint uploads

- URL: https://huggingface.co/Lightricks/LTX-Video/commits/0f6a884be0b1adb4782dd289bf5df8deb5d8c533
- Publisher: Lightricks (HuggingFace repo commits)
- Type: `repository`
- Primary because: Commit history blob demonstrating the presence/upload of the named checkpoint files (ltxv-2b-0.9.6 and distilled artifacts).
- Scope: Committed artifacts for the Lightricks/LTX-Video HuggingFace repository.
- Supports: identity.checkpoint
- Supports: recommendedUseCases
- Supports: conditionalUseCases

### Repository License.txt (RAIL‑M statements)

- URL: https://huggingface.co/Lightricks/LTX-Video/blob/c7c8ad4c2ddba847b94e8bfaefbd30bd8669fafc/License.txt
- Publisher: Lightricks (HuggingFace repo blob)
- Type: `repository`
- Primary because: Repo-hosted license text used by the HuggingFace model distribution describing RAIL‑M terms referenced by the project.
- Scope: HuggingFace repository license blob associated with the model artifacts.
- Supports: identity.license
- Supports: limitations
- Supports: safety

### LTX Video Open Weights License 0.X (official license PDF)

- URL: https://static.lightricks.com/legal/LTX-Video-Open-Weights-License-0.X.pdf
- Publisher: Lightricks (legal)
- Type: `official-documentation`
- Primary because: Official license PDF for model weights distribution and use-restrictions referenced by the project.
- Scope: Open Weights License 0.X governing LTX-Video weight distribution (referenced by project).
- Supports: identity.license
- Supports: limitations
- Supports: safety

### LTXv 2B Open RAIL‑M License PDF

- URL: https://static.lightricks.com/legal/ltxv-2B-open-railm-license.pdf
- Publisher: Lightricks legal
- Type: `official-documentation`
- Primary because: License document specific to the 2B family referenced in upstream findings describing RAIL‑M restrictions for 2B models.
- Scope: Open RAIL‑M License for LTX‑Video 2B family.
- Supports: identity.license
- Supports: limitations
- Supports: safety

### Lightricks Acceptable Use Policy (official PDF)

- URL: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf
- Publisher: Lightricks legal
- Type: `official-documentation`
- Primary because: Official acceptable-use policy referenced by upstream project and license texts describing prohibited categories and disclosure requirements.
- Scope: Acceptable Use Policy governing Lightricks generative products including LTX-Video.
- Supports: limitations
- Supports: safety
- Supports: avoidUseCases

### LTX-Video README blob (specific committed README used for provenance)

- URL: https://huggingface.co/Lightricks/LTX-Video/blob/52609d50c3b6746b508c154b1238a390037d56a3/README.md
- Publisher: Lightricks (HuggingFace repo blob)
- Type: `model-card`
- Primary because: Specific README commit blob used to source operational guidance, divisibility constraints, recommended bounds, and example usage.
- Scope: Committed README content for Lightricks/LTX-Video used as provenance for operational claims.
- Supports: inputPreparation.validation
- Supports: benchmarks (project claims)
- Supports: recommendedUseCases
- Supports: outputInterpretation

### VAE config (repo blob)

- URL: https://huggingface.co/Lightricks/LTX-Video/blob/a6d59ee37c13c58261aa79027d3e41cd41960925/vae/config.json
- Publisher: Lightricks (HuggingFace repo blob)
- Type: `repository`
- Primary because: Upstream committed VAE configuration describing latent_channels, block_out_channels, patch sizes and other VAE internals.
- Scope: VAE configuration for LTX-Video checkpoints.
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.outputs

### UNet/score network config (repo blob)

- URL: https://huggingface.co/Lightricks/LTX-Video/blob/d61f0026b566c495232a0c112481ca15c96969cb/unet/config.json
- Publisher: Lightricks (HuggingFace repo blob)
- Type: `repository`
- Primary because: Upstream committed UNet configuration documenting positional embeddings type (rope) and normalization choices (rms_norm) used by the model.
- Scope: UNet/score network configuration for the upstream model.
- Supports: identity.architecture
- Supports: inputPreparation.preprocessing

### Lightricks GitHub repository (project sources and configs)

- URL: https://github.com/Lightricks/LTX-Video
- Publisher: Lightricks (GitHub)
- Type: `repository`
- Primary because: Official project repository containing pipeline configs, example inference commands, and committed yaml configs naming checkpoint variants.
- Scope: Project repository and configs including ltxv-2b-0.9.6 config YAMLs.
- Supports: conditionalUseCases
- Supports: inputPreparation.taskSpecificFormatting
- Supports: recommendedUseCases
- Supports: benchmarks (project claims)

### Config YAML: ltxv-2b-0.9.6-dev (committed)

- URL: https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-dev.yaml
- Publisher: Lightricks (GitHub repo blob)
- Type: `repository`
- Primary because: Committed config YAML for the dev/dev checkpoint variant documenting inference hyperparameters associated with the named artifact.
- Scope: Configuration for the ltxv-2b-0.9.6-dev artifact.
- Supports: conditionalUseCases
- Supports: inputPreparation.preprocessing
- Supports: outputInterpretation.validation

### Config YAML: ltxv-2b-0.9.6-distilled (committed)

- URL: https://github.com/Lightricks/LTX-Video/blob/main/configs/ltxv-2b-0.9.6-distilled.yaml
- Publisher: Lightricks (GitHub repo blob)
- Type: `repository`
- Primary because: Committed config YAML for the distilled 2B artifact documenting reduced-step/optimized inference settings.
- Scope: Configuration for the ltxv-2b-0.9.6-distilled artifact.
- Supports: conditionalUseCases
- Supports: benchmarks (project claims about speedups)
- Supports: inputPreparation.preprocessing

### LTX-Video Trainer configuration reference

- URL: https://github.com/Lightricks/LTX-Video-Trainer/blob/main/docs/configuration-reference.md
- Publisher: Lightricks (GitHub trainer repo)
- Type: `repository`
- Primary because: Official trainer docs describing CLI/config fields, input semantics, and validation rules used with upstream checkpoints.
- Scope: Trainer/inference configuration and validation guidance for LTX-Video checkpoints.
- Supports: inputPreparation.semanticInputs
- Supports: inputPreparation.validation
- Supports: taskSpecificFormatting

### LTX-Video arXiv preprint (architecture and scope)

- URL: https://arxiv.org/abs/2501.00103
- Publisher: Lightricks (arXiv preprint)
- Type: `paper`
- Primary because: Canonical upstream preprint describing model architecture, intended scope, and documented limitations.
- Scope: Architectural description and research-scope claims for the LTX-Video family.
- Supports: identity.architecture
- Supports: researchSummary
- Supports: limitations

### docs.ltx.video — Extend video-generation API reference

- URL: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend
- Publisher: Lightricks (docs)
- Type: `official-documentation`
- Primary because: API reference documenting the Extend endpoint parameters, response headers, duration limits, and operational semantics.
- Scope: API-level video extension behavior and parameter limits.
- Supports: conditionalUseCases
- Supports: inputPreparation.taskSpecificFormatting
- Supports: outputInterpretation.validation

### docs.ltx.video — Input formats and transport limits

- URL: https://docs.ltx.video/input-formats
- Publisher: Lightricks (docs)
- Type: `official-documentation`
- Primary because: Authoritative upstream documentation on accepted MIME types, upload methods, and per-transport size limits.
- Scope: API input format constraints and transport limits for media inputs.
- Supports: inputPreparation.acceptedFormats
- Supports: inputPreparation.semanticInputs

## Evidence gaps

- No formal public dataset-style quality benchmark tables (FVD, IS, CLIP-FID, etc.) for the exact upstream checkpoint ltxv-2b-0.9.6 were present in the provided primary sources (checked: HuggingFace model page, committed README blob, GitHub configs, and arXiv preprint).
- Where upstream sources conflict on recommended maximum supported durations (arXiv emphasizes focus on short videos while API docs describe caps up to 20 seconds / 480 frames), the research findings document the conflict but do not reconcile it.
- Exact numeric pixel-to-latent compression ratio (a single numeric ratio claim) is not present in the upstream VAE/config facts in the research findings; do not assume a specific numeric compression ratio without an explicit upstream statement.
- No protocol-matched, numeric quality comparisons between ltxv-2b-0.9.6 and the listed Forge peer alternatives were found in the provided primary sources; therefore each peer comparison is recorded as 'insufficient-evidence'.

## Independent audit

Independent primary-source verification returned a complete corrected dossier that passed all local schema, source, and checkpoint-scope gates; 18 deterministic draft defect(s) were supplied to the audit.

- `medium` $.sources[13].primary must be true: $.sources[13].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[14].primary must be true: $.sources[14].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[15].primary must be true: $.sources[15].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[17].primary must be true: $.sources[17].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` $.sources[18].primary must be true: $.sources[18].primary must be true Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-Video/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-Video/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-Video/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-Video/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://docs.ltx.video/api-documentation/api-reference/video-generation/extend Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://huggingface.co/Lightricks/LTX-Video/blame/main/README.md Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
- `medium` evidence URL is absent from $.sources: evidence URL is absent from $.sources: https://static.lightricks.com/legal/ltx-acceptable-use-policy.pdf Resolution: The independently audited dossier corrected or removed the failing draft field and passed the same gate.
